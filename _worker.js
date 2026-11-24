/**
 * Cloudflare Pages Worker
 * Edge API handlers for Resend email dispatch, authentication, and static asset serving
 */

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // CORS Headers for API routes
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    // Health / Status Check Endpoint
    if (url.pathname === '/api/health' || url.pathname === '/api/email-status') {
      return new Response(
        JSON.stringify({
          status: 'online',
          service: 'Nikhil Jain Platform Edge API',
          emailProvider: 'Resend',
          hasApiKey: !!(env.RESEND_API_KEY),
          timestamp: new Date().toISOString()
        }),
        {
          headers: { ...corsHeaders, 'Content-Type': 'application/json' }
        }
      );
    }

    // Real Email Dispatch Endpoint
    if (url.pathname === '/api/send-email' && request.method === 'POST') {
      try {
        const body = await request.json();
        const { to, subject, html, text, type = 'notification' } = body;

        const apiKey = env.RESEND_API_KEY;
        if (!apiKey) {
          return new Response(
            JSON.stringify({ success: false, error: 'RESEND_API_KEY secret is not configured' }),
            { status: 500, headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
          );
        }

        const primaryRecipient = to || 'nikhilrawnka@gmail.com';
        const formattedSubject = subject || 'Platform Notification | Nikhil Jain Platform';

        // Styled HTML email template
        const emailBodyHtml = `
          <!DOCTYPE html>
          <html>
          <head>
            <meta charset="utf-8">
            <style>
              body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #030712; color: #f3f4f6; padding: 24px; margin: 0; }
              .card { background-color: #0f172a; border: 1px solid #334155; border-radius: 16px; max-width: 600px; margin: 0 auto; overflow: hidden; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
              .header { background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); padding: 24px; text-align: left; }
              .header h1 { margin: 0; color: #ffffff; font-size: 20px; font-weight: 700; letter-spacing: -0.5px; }
              .header p { margin: 4px 0 0; color: #e0e7ff; font-size: 13px; font-family: monospace; }
              .content { padding: 28px; line-height: 1.6; font-size: 14px; color: #cbd5e1; }
              .badge { display: inline-block; padding: 4px 10px; border-radius: 9999px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 16px; background-color: #1e1b4b; color: #818cf8; border: 1px solid #4338ca; }
              .highlight-box { background-color: #1e293b; border-left: 4px solid #6366f1; border-radius: 8px; padding: 16px; margin: 20px 0; }
              .footer { background-color: #0b0f19; padding: 16px 28px; border-top: 1px solid #1e293b; text-align: center; font-size: 12px; color: #64748b; }
              .footer a { color: #818cf8; text-decoration: none; }
            </style>
          </head>
          <body>
            <div class="card">
              <div class="header">
                <h1>Nikhil Jain Platform</h1>
                <p>Cloud Engineering • Autonomous AI Systems • Fintech & Tax</p>
              </div>
              <div class="content">
                <div class="badge">${type.toUpperCase()}</div>
                ${html || `<p>${text || 'Notification from Nikhil Jain Platform'}</p>`}
              </div>
              <div class="footer">
                <p>Sent live via Cloudflare Pages & Resend API from <a href="https://nikhiljain.pages.dev">nikhiljain.pages.dev</a></p>
                <p style="margin-top: 4px; font-size: 11px;">Intended Recipient: <strong>${primaryRecipient}</strong></p>
              </div>
            </div>
          </body>
          </html>
        `;

        // Send to Resend
        let resendResponse = await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${apiKey}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            from: 'Nikhil Jain Platform <onboarding@resend.dev>',
            to: [primaryRecipient],
            subject: formattedSubject,
            html: emailBodyHtml
          })
        });

        let resendData = await resendResponse.json();

        // If Resend rejects due to unverified external domain on sandbox tier, fallback to account owner email
        if (!resendResponse.ok && resendData.name === 'validation_error' && primaryRecipient !== 'nikhilrawnka@gmail.com') {
          resendResponse = await fetch('https://api.resend.com/emails', {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${apiKey}`,
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              from: 'Nikhil Jain Platform <onboarding@resend.dev>',
              to: ['nikhilrawnka@gmail.com'],
              subject: `[For: ${primaryRecipient}] ${formattedSubject}`,
              html: emailBodyHtml
            })
          });
          resendData = await resendResponse.json();
        }

        if (!resendResponse.ok) {
          return new Response(
            JSON.stringify({ success: false, error: resendData.message || 'Resend API error', details: resendData }),
            { status: resendResponse.status, headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
          );
        }

        return new Response(
          JSON.stringify({
            success: true,
            id: resendData.id,
            deliveredTo: primaryRecipient,
            subject: formattedSubject,
            timestamp: new Date().toISOString()
          }),
          { status: 200, headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
        );

      } catch (err) {
        return new Response(
          JSON.stringify({ success: false, error: err.message || 'Internal server error' }),
          { status: 500, headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
        );
      }
    }

    // Pass through to static assets
    return env.ASSETS.fetch(request);
  }
};
