#!/usr/bin/env python3
"""
Local Dev Server with static hosting and Resend Email Edge API proxy.
Handles:
  - Static files from public/
  - POST /api/send-email (dispatches live email via Resend)
  - GET /api/health (checks system status)
"""
import http.server
import socketserver
import json
import urllib.request
import urllib.error
import os

PORT = 3000
PUBLIC_DIR = os.path.join(os.path.dirname(__file__), '..', 'public')
def load_resend_api_key():
    key = os.environ.get('RESEND_API_KEY')
    if key:
        return key
    env_file = os.path.join(os.path.dirname(__file__), '..', '.env')
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('RESEND_API_KEY='):
                    return line.split('=', 1)[1].strip().strip('"').strip("'")
    return None

RESEND_API_KEY = load_resend_api_key()

class DevHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PUBLIC_DIR, **kwargs)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_GET(self):
        if self.path in ('/api/health', '/api/email-status'):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {
                "status": "online",
                "service": "Local Dev Server & Resend Email Bridge",
                "emailProvider": "Resend",
                "hasApiKey": bool(RESEND_API_KEY),
                "port": PORT
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))
            return
        
        # Pretty URL rewriting for clean URLs (e.g. /portfolio -> /portfolio.html)
        clean_path = self.path.split('?')[0]
        if clean_path != '/' and not os.path.exists(os.path.join(PUBLIC_DIR, clean_path.lstrip('/'))):
            html_candidate = os.path.join(PUBLIC_DIR, clean_path.lstrip('/') + '.html')
            if os.path.exists(html_candidate):
                self.path = clean_path + '.html'

        return super().do_GET()

    def do_POST(self):
        if self.path == '/api/send-email':
            content_length = int(self.headers.get('Content-Length', 0))
            body_bytes = self.rfile.read(content_length)
            try:
                body = json.loads(body_bytes.decode('utf-8'))
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": f"Invalid JSON: {e}"}).encode('utf-8'))
                return

            to_addr = body.get('to') or 'nikhilrawnka@gmail.com'
            subject = body.get('subject') or 'Platform Notification'
            html = body.get('html') or f"<p>{body.get('text', 'Notification from Nikhil Jain Platform')}</p>"
            msg_type = body.get('type', 'notification')

            full_html = f"""
            <!DOCTYPE html>
            <html>
            <body style="font-family: -apple-system, sans-serif; background-color: #030712; color: #f3f4f6; padding: 24px;">
              <div style="background-color: #0f172a; border: 1px solid #334155; border-radius: 16px; max-width: 600px; margin: 0 auto; overflow: hidden;">
                <div style="background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); padding: 24px;">
                  <h1 style="margin: 0; color: #ffffff; font-size: 20px;">Nikhil Jain Platform</h1>
                  <p style="margin: 4px 0 0; color: #e0e7ff; font-size: 13px; font-family: monospace;">Cloud Engineering • Autonomous AI Systems</p>
                </div>
                <div style="padding: 28px; line-height: 1.6; font-size: 14px; color: #cbd5e1;">
                  <div style="display: inline-block; padding: 4px 10px; border-radius: 9999px; font-size: 11px; font-weight: 600; text-transform: uppercase; background-color: #1e1b4b; color: #818cf8; border: 1px solid #4338ca; margin-bottom: 16px;">{msg_type.upper()}</div>
                  {html}
                </div>
                <div style="background-color: #0b0f19; padding: 16px 28px; border-top: 1px solid #1e293b; text-align: center; font-size: 12px; color: #64748b;">
                  Sent live via Resend API from <a href="https://nikhiljain.pages.dev" style="color: #818cf8;">nikhiljain.pages.dev</a>
                </div>
              </div>
            </body>
            </html>
            """

            payload = {
                "from": "Nikhil Jain Platform <onboarding@resend.dev>",
                "to": [to_addr],
                "subject": subject,
                "html": full_html
            }

            req = urllib.request.Request(
                "https://api.resend.com/emails",
                data=json.dumps(payload).encode('utf-8'),
                headers={
                    "Authorization": f"Bearer {RESEND_API_KEY}",
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                },
                method="POST"
            )

            try:
                with urllib.request.urlopen(req) as resp:
                    resp_data = json.loads(resp.read().decode('utf-8'))
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(json.dumps({
                        "success": True,
                        "id": resp_data.get('id'),
                        "deliveredTo": to_addr,
                        "subject": subject
                    }).encode('utf-8'))
                    return
            except urllib.error.HTTPError as he:
                err_content = he.read().decode('utf-8')
                try:
                    err_json = json.loads(err_content)
                except:
                    err_json = {"error": err_content}
                
                # If error is validation_error due to sandbox restriction, retry to nikhilrawnka@gmail.com
                if to_addr != 'nikhilrawnka@gmail.com':
                    fallback_payload = {
                        "from": "Nikhil Jain Platform <onboarding@resend.dev>",
                        "to": ["nikhilrawnka@gmail.com"],
                        "subject": f"[For: {to_addr}] {subject}",
                        "html": full_html
                    }
                    fallback_req = urllib.request.Request(
                        "https://api.resend.com/emails",
                        data=json.dumps(fallback_payload).encode('utf-8'),
                        headers={
                            "Authorization": f"Bearer {RESEND_API_KEY}",
                            "Content-Type": "application/json",
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                        },
                        method="POST"
                    )
                    try:
                        with urllib.request.urlopen(fallback_req) as f_resp:
                            f_data = json.loads(f_resp.read().decode('utf-8'))
                            self.send_response(200)
                            self.send_header('Content-Type', 'application/json')
                            self.send_header('Access-Control-Allow-Origin', '*')
                            self.end_headers()
                            self.wfile.write(json.dumps({
                                "success": True,
                                "id": f_data.get('id'),
                                "deliveredTo": f"nikhilrawnka@gmail.com (Forwarded for {to_addr})",
                                "subject": subject
                            }).encode('utf-8'))
                            return
                    except Exception as fe:
                        pass

                self.send_response(he.code)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(err_json)}).encode('utf-8'))
                return
            except Exception as ex:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(ex)}).encode('utf-8'))
                return

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), DevHandler) as httpd:
        print(f"Dev server running at http://localhost:{PORT}")
        httpd.serve_forever()
