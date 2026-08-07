document.addEventListener('DOMContentLoaded', () => {
    const html = document.documentElement;

    // Theme Toggle Logic
    const themeBtn = document.getElementById('theme-toggle');
    const initTheme = () => {
        if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            html.classList.add('dark');
        } else {
            html.classList.remove('dark');
        }
    };
    initTheme();

    const toggleTheme = () => {
        html.classList.toggle('dark');
        localStorage.setItem('theme', html.classList.contains('dark') ? 'dark' : 'light');
    };

    if (themeBtn) {
        themeBtn.addEventListener('click', toggleTheme);
    }

    // RTL Toggle Logic
    const rtlBtn = document.getElementById('rtl-toggle');
    if (localStorage.getItem('dir') === 'rtl') {
        html.setAttribute('dir', 'rtl');
    }

    const toggleRTL = () => {
        const currentDir = html.getAttribute('dir');
        const newDir = currentDir === 'rtl' ? 'ltr' : 'rtl';
        html.setAttribute('dir', newDir);
        localStorage.setItem('dir', newDir);
    };

    if (rtlBtn) {
        rtlBtn.addEventListener('click', toggleRTL);
    }

    // Mobile & Tablet Menu Drawer Management
    let mobileMenu = document.getElementById('mobile-menu');
    if (!mobileMenu) {
        mobileMenu = document.createElement('div');
        mobileMenu.id = 'mobile-menu';
        mobileMenu.className = 'fixed inset-0 z-[100] bg-[#0c1a11]/95 dark:bg-[#060e08]/98 backdrop-blur-2xl flex flex-col justify-between p-8 text-white transition-all duration-300 transform -translate-y-full opacity-0 pointer-events-none';
        
        const rawPath = window.location.pathname.split('/').pop() || 'index.html';
        const path = rawPath === '' ? 'index.html' : rawPath;

        mobileMenu.innerHTML = `
            <div class="flex items-center justify-between border-b border-[#d4af37]/30 pb-6">
                <a href="index.html" class="font-display-lg text-2xl text-[#d4af37] tracking-widest uppercase">Floréa</a>
                <button id="close-mobile-menu" class="text-white hover:text-[#d4af37] p-2 focus:outline-none transition-colors" aria-label="Close Navigation Menu">
                    <span class="material-symbols-outlined text-3xl">close</span>
                </button>
            </div>
            
            <nav class="flex flex-col space-y-6 my-auto text-center font-serif text-2xl">
                <a href="index.html" class="transition-all duration-300 ${path === 'index.html' ? 'text-[#d4af37] font-bold underline underline-offset-8 scale-105' : 'text-white/90 hover:text-[#d4af37]'}">Home</a>
                <a href="home2.html" class="transition-all duration-300 ${path === 'home2.html' ? 'text-[#d4af37] font-bold underline underline-offset-8 scale-105' : 'text-white/90 hover:text-[#d4af37]'}">Alternative Home</a>
                <a href="services.html" class="transition-all duration-300 ${path === 'services.html' ? 'text-[#d4af37] font-bold underline underline-offset-8 scale-105' : 'text-white/90 hover:text-[#d4af37]'}">Services</a>
                <a href="gallery.html" class="transition-all duration-300 ${path === 'gallery.html' ? 'text-[#d4af37] font-bold underline underline-offset-8 scale-105' : 'text-white/90 hover:text-[#d4af37]'}">Gallery</a>
                <a href="blog.html" class="transition-all duration-300 ${path === 'blog.html' ? 'text-[#d4af37] font-bold underline underline-offset-8 scale-105' : 'text-white/90 hover:text-[#d4af37]'}">Blog</a>
            </nav>

            <div class="flex flex-col gap-4 border-t border-[#d4af37]/30 pt-6">
                <div class="flex justify-center space-x-4 mb-2">
                    <button id="mobile-theme-btn" class="px-4 py-2 text-xs font-label-sm uppercase tracking-widest border border-[#d4af37]/40 text-[#d4af37] hover:bg-[#d4af37]/10 rounded-full flex items-center gap-2">
                        <span class="material-symbols-outlined text-sm">dark_mode</span> Toggle Theme
                    </button>
                    <button id="mobile-rtl-btn" class="px-4 py-2 text-xs font-label-sm uppercase tracking-widest border border-[#d4af37]/40 text-[#d4af37] hover:bg-[#d4af37]/10 rounded-full">
                        Toggle RTL
                    </button>
                </div>
                <a href="register.html" class="w-full text-center border border-[#d4af37] text-[#d4af37] py-3.5 font-label-sm uppercase tracking-wider hover:bg-[#d4af37] hover:text-black transition-colors rounded-sm">Sign Up</a>
                <a href="booking.html" class="w-full text-center bg-[#d4af37] text-black py-3.5 font-label-sm uppercase tracking-wider hover:bg-white transition-colors shadow-lg font-semibold rounded-sm">Enquire Now</a>
            </div>
        `;
        document.body.appendChild(mobileMenu);

        // Bind mobile inner theme/RTL toggles
        document.getElementById('mobile-theme-btn')?.addEventListener('click', toggleTheme);
        document.getElementById('mobile-rtl-btn')?.addEventListener('click', toggleRTL);
    }

    const openMenu = () => {
        mobileMenu.classList.remove('-translate-y-full', 'opacity-0', 'pointer-events-none');
        mobileMenu.classList.add('translate-y-0', 'opacity-100', 'pointer-events-auto');
        document.body.style.overflow = 'hidden';
    };

    const closeMenu = () => {
        mobileMenu.classList.remove('translate-y-0', 'opacity-100', 'pointer-events-auto');
        mobileMenu.classList.add('-translate-y-full', 'opacity-0', 'pointer-events-none');
        document.body.style.overflow = '';
    };

    // Attach listeners to open / close buttons
    const closeBtn = document.getElementById('close-mobile-menu');
    if (closeBtn) closeBtn.addEventListener('click', closeMenu);

    // Attach click listener to any mobile menu trigger button
    const menuTriggers = document.querySelectorAll('#mobile-menu-btn, button.md\\:hidden, button.lg\\:hidden, button.xl\\:hidden');
    menuTriggers.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            openMenu();
        });
    });

    // Close mobile menu on nav link click
    mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', closeMenu);
    });
});
