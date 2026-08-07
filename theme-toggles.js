document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle
    const themeBtn = document.getElementById('theme-toggle');
    const html = document.documentElement;

    // Initialize theme from localStorage or OS preference
    if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        html.classList.add('dark');
    }

    if (themeBtn) {
        themeBtn.addEventListener('click', () => {
            html.classList.toggle('dark');
            if (html.classList.contains('dark')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
    }

    // RTL Toggle
    const rtlBtn = document.getElementById('rtl-toggle');
    
    // Initialize RTL from localStorage
    if (localStorage.getItem('dir') === 'rtl') {
        html.setAttribute('dir', 'rtl');
    }

    if (rtlBtn) {
        rtlBtn.addEventListener('click', () => {
            if (html.getAttribute('dir') === 'rtl') {
                html.setAttribute('dir', 'ltr');
                localStorage.setItem('dir', 'ltr');
            } else {
                html.setAttribute('dir', 'rtl');
                localStorage.setItem('dir', 'rtl');
            }
        });
    }
});
