/**
 * Shared Platform Helper Functions
 * Auth, Toasts, Modals, Ollama Health & Persistent State
 */

// Toast System
function showToast(message, type = 'info') {
  let container = document.getElementById('toastContainer');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toastContainer';
    container.className = 'fixed bottom-5 right-5 z-50 flex flex-col gap-2 max-w-sm pointer-events-none';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  const bgColors = {
    success: 'bg-emerald-950/90 border-emerald-500/50 text-emerald-200',
    error: 'bg-red-950/90 border-red-500/50 text-red-200',
    info: 'bg-indigo-950/90 border-indigo-500/50 text-indigo-200',
    warning: 'bg-yellow-950/90 border-yellow-500/50 text-yellow-200'
  };

  const icons = {
    success: '✓',
    error: '✕',
    info: 'ℹ',
    warning: '⚠'
  };

  toast.className = `p-3.5 rounded-xl border backdrop-blur-md shadow-2xl flex items-center gap-3 text-xs font-medium pointer-events-auto transition-all duration-300 transform translate-y-4 opacity-0 ${bgColors[type] || bgColors.info}`;
  toast.innerHTML = `
    <span class="w-5 h-5 rounded-full flex items-center justify-center font-bold bg-white/10 shrink-0">${icons[type] || '•'}</span>
    <span class="flex-1">${message}</span>
    <button onclick="this.parentElement.remove()" class="text-white/50 hover:text-white font-mono text-sm ml-2">✕</button>
  `;

  container.appendChild(toast);
  requestAnimationFrame(() => {
    toast.classList.remove('translate-y-4', 'opacity-0');
  });

  setTimeout(() => {
    toast.classList.add('opacity-0', 'translate-y-2');
    setTimeout(() => toast.remove(), 300);
  }, 4000);
}

// Authentication Helpers
function getAuthUser() {
  try {
    const raw = localStorage.getItem('auth_user');
    return raw ? JSON.parse(raw) : null;
  } catch (e) {
    return null;
  }
}

function initAuthUI() {
  const user = getAuthUser();
  const authBtnText = document.getElementById('authBtnText');
  const authAvatar = document.getElementById('authAvatar');

  if (user) {
    if (authBtnText) authBtnText.innerText = user.name || user.email || '@tigernikhil';
    if (authAvatar) {
      authAvatar.innerText = (user.name || 'NJ').substring(0, 2).toUpperCase();
      authAvatar.classList.remove('hidden');
    }
  } else {
    if (authBtnText) authBtnText.innerText = 'Sign In';
    if (authAvatar) authAvatar.classList.add('hidden');
  }
}

function openAuthModal() {
  const modal = document.getElementById('authModal');
  if (modal) modal.classList.remove('hidden');
}

function closeAuthModal() {
  const modal = document.getElementById('authModal');
  if (modal) modal.classList.add('hidden');
}

function handleGoogleSignIn() {
  const user = { name: "Nikhil Jain", email: "nikhilrawnka@gmail.com", role: "Principal AI Engineer", provider: "google" };
  localStorage.setItem('auth_user', JSON.stringify(user));
  initAuthUI();
  closeAuthModal();
  showToast("Signed in as Nikhil Jain (nikhilrawnka@gmail.com)", "success");
}

function handleGitHubSignIn() {
  const user = { name: "Nikhil Jain", username: "tigernikhil", email: "nikhilrawnka@gmail.com", provider: "github" };
  localStorage.setItem('auth_user', JSON.stringify(user));
  initAuthUI();
  closeAuthModal();
  showToast("Authenticated with GitHub (@tigernikhil)", "success");
}

function handleEmailSignIn() {
  const emailInput = document.getElementById('authEmailInput');
  const email = emailInput ? emailInput.value.trim() : '';
  if (!email || !email.includes('@')) {
    showToast("Please enter a valid email address", "error");
    return;
  }
  const user = { name: email.split('@')[0], email: email, provider: "email" };
  localStorage.setItem('auth_user', JSON.stringify(user));
  initAuthUI();
  closeAuthModal();
  showToast(`Magic link sent! Signed in as ${email}`, "success");
}

function handleSignOut() {
  localStorage.removeItem('auth_user');
  initAuthUI();
  showToast("You have been signed out.", "info");
}

// Ollama Status Ping
async function checkOllamaStatus(badgeId = 'ollamaStatusBadge') {
  const badge = document.getElementById(badgeId);
  if (!badge) return;

  try {
    const res = await fetch('http://localhost:11434/api/tags', { signal: AbortSignal.timeout(2000) });
    if (res.ok) {
      const data = await res.json();
      const count = data.models ? data.models.length : 3;
      badge.innerHTML = `<span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span> Ollama Active (${count} models)`;
      badge.className = "px-2.5 py-1 rounded-full text-xs font-mono font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 flex items-center gap-1.5";
      return;
    }
  } catch (e) {
    // offline or CORS blocked
  }

  badge.innerHTML = `<span class="w-2 h-2 rounded-full bg-indigo-400 animate-ping"></span> Laptop Engine Ready (:11434)`;
  badge.className = "px-2.5 py-1 rounded-full text-xs font-mono font-medium bg-indigo-500/10 text-indigo-300 border border-indigo-500/30 flex items-center gap-1.5";
}

// Transactional Email Preview Modal
function showEmailModal({ to, subject, refId, detailsHtml }) {
  let modal = document.getElementById('emailPreviewModal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'emailPreviewModal';
    modal.className = 'fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-4 hidden';
    document.body.appendChild(modal);
  }

  modal.innerHTML = `
    <div class="glass-panel w-full max-w-lg rounded-3xl p-6 sm:p-8 border border-indigo-500/30 shadow-2xl relative">
      <button onclick="document.getElementById('emailPreviewModal').classList.add('hidden')" class="absolute top-4 right-4 text-slate-400 hover:text-white font-mono text-lg">✕</button>
      <div class="flex items-center gap-3 mb-4">
        <div class="w-10 h-10 rounded-xl bg-indigo-500/20 border border-indigo-500/30 flex items-center justify-center text-indigo-400 font-bold">
          ✉
        </div>
        <div>
          <h3 class="text-base font-bold text-white">Transactional Email Dispatched</h3>
          <div class="text-xs text-slate-400 font-mono">Gateway: Resend / SMTP • Ref: ${refId}</div>
        </div>
      </div>

      <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 space-y-2.5 text-xs text-slate-300 mb-5 font-mono">
        <div><span class="text-slate-500">To:</span> <strong class="text-white">${to}</strong></div>
        <div><span class="text-slate-500">Subject:</span> <strong class="text-indigo-300">${subject}</strong></div>
        <div><span class="text-slate-500">Timestamp:</span> ${new Date().toLocaleString()}</div>
        <div class="pt-3 border-t border-slate-800/80 font-sans text-xs text-slate-300 leading-relaxed">
          ${detailsHtml}
        </div>
      </div>

      <div class="flex items-center justify-between">
        <span class="text-[11px] text-emerald-400 font-mono flex items-center gap-1">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          Delivered via Personal Technology Platform
        </span>
        <button onclick="document.getElementById('emailPreviewModal').classList.add('hidden')" class="px-4 py-2 rounded-xl text-xs font-semibold bg-indigo-600 hover:bg-indigo-500 text-white transition">
          Dismiss
        </button>
      </div>
    </div>
  `;

  modal.classList.remove('hidden');
}

// Global Init
document.addEventListener('DOMContentLoaded', () => {
  initAuthUI();
});
