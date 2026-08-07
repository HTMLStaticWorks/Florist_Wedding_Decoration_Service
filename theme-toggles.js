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

    // Mobile Menu Management & Dynamic Drawer Injection
    let mobileMenu = document.getElementById('mobile-menu');
    if (!mobileMenu) {
        mobileMenu = document.createElement('div');
        mobileMenu.id = 'mobile-menu';
        mobileMenu.className = 'fixed inset-0 z-[100] bg-background/95 dark:bg-[#121c15]/98 backdrop-blur-2xl flex flex-col justify-between p-8 transition-all duration-300 transform -translate-y-full opacity-0 pointer-events-none';
        
        const rawPath = window.location.pathname.split('/').pop() || 'index.html';
        const path = rawPath === '' ? 'index.html' : rawPath;

        mobileMenu.innerHTML = `
            <div class="flex items-center justify-between border-b border-primary/20 pb-6">
                <a href="index.html" class="font-display-lg text-2xl text-primary dark:text-primary-fixed tracking-widest uppercase">Floréa</a>
                <button id="close-mobile-menu" class="text-primary dark:text-primary-fixed p-2 focus:outline-none hover:opacity-80 transition-opacity">
                    <span class="material-symbols-outlined text-3xl">close</span>
                </button>
            </div>
            
            <nav class="flex flex-col space-y-6 my-auto text-center font-serif text-2xl">
                <a href="index.html" class="hover:text-primary transition-colors ${path === 'index.html' ? 'text-primary font-bold underline underline-offset-8' : 'text-on-surface'}">Home</a>
                <a href="home2.html" class="hover:text-primary transition-colors ${path === 'home2.html' ? 'text-primary font-bold underline underline-offset-8' : 'text-on-surface'}">Alternative Home</a>
                <a href="services.html" class="hover:text-primary transition-colors ${path === 'services.html' ? 'text-primary font-bold underline underline-offset-8' : 'text-on-surface'}">Services</a>
                <a href="gallery.html" class="hover:text-primary transition-colors ${path === 'gallery.html' ? 'text-primary font-bold underline underline-offset-8' : 'text-on-surface'}">Gallery</a>
                <a href="blog.html" class="hover:text-primary transition-colors ${path === 'blog.html' ? 'text-primary font-bold underline underline-offset-8' : 'text-on-surface'}">Blog</a>
            </nav>

            <div class="flex flex-col gap-4 border-t border-primary/20 pt-6">
                <div class="flex justify-center space-x-4 mb-2">
                    <button id="mobile-theme-btn" class="px-4 py-2 text-xs font-label-sm uppercase tracking-widest border border-primary/30 rounded-full flex items-center gap-2 text-primary">
                        <span class="material-symbols-outlined text-sm">dark_mode</span> Toggle Theme
                    </button>
                    <button id="mobile-rtl-btn" class="px-4 py-2 text-xs font-label-sm uppercase tracking-widest border border-primary/30 rounded-full text-primary">
                        Toggle RTL
                    </button>
                </div>
                <a href="register.html" class="w-full text-center border border-primary text-primary py-3.5 font-label-sm uppercase tracking-wider hover:bg-primary hover:text-on-primary transition-colors">Sign Up</a>
                <a href="booking.html" class="w-full text-center bg-primary text-on-primary py-3.5 font-label-sm uppercase tracking-wider hover:bg-inverse-primary transition-colors shadow-lg">Enquire Now</a>
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
    const menuTriggers = document.querySelectorAll('#mobile-menu-btn, button.md\\:hidden');
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
