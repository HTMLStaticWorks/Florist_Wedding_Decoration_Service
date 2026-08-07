import os
import re

directory = r"d:\project 2\Florist & Wedding Decoration Service"

grand_footer = """<!-- Footer -->
<footer class="relative w-full overflow-hidden mt-20">
    <!-- Background Image with Overlay -->
    <div class="absolute inset-0 z-0">
        <div class="w-full h-full bg-cover bg-center bg-fixed" style="background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuAESXC4SMK2VFhKELf6SmkJiZU4ZJ_yjgDjLZlA34N84BxSn99_luzZltUUTWlrxFH8jRJTwdR4A-mabLU017uZUXg4EEhejxfnPeK_XFEfxSokTLiKVZ3pt3hFfiA9-Gi2cM32Zb8FfaVNBo6tsRe2vLPwU4yKAjw0Cp3FHqOYwTQIdz9NTvJMdKOa1kdk7WuDLSyiR8MQ_K1LDLKm9Z-76QiHw5M_Lzt76exSzpwLgeSYdJchZnIL');"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-[#0b2013] via-[#0b2013]/95 to-[#0b2013]/70 mix-blend-multiply"></div>
        <!-- Extra dark gradient for readability -->
        <div class="absolute inset-0 bg-[#0b2013]/80"></div>
    </div>
    
    <div class="relative z-10 max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop pt-24 pb-12">

        <div class="grid grid-cols-1 md:grid-cols-12 gap-12 mb-16">
            <!-- Brand Section -->
            <div class="md:col-span-4 flex flex-col items-start">
                <a href="index.html" class="font-display-lg text-[48px] text-[#d4af37] mb-6 hover:opacity-80 transition-opacity leading-none">Aurelia <br/> Floral</a>
                <p class="font-body-sm text-[#b4cdb8] max-w-xs font-light leading-relaxed">
                    A boutique floral design studio specializing in editorial, romantically undone aesthetics for weddings of distinction.
                </p>
            </div>
            
            <!-- Quick Links -->
            <div class="md:col-span-2 md:col-start-6 flex flex-col">
                <h4 class="font-label-sm text-[11px] text-[#fbf9f4] uppercase tracking-[0.25em] mb-8">Navigation</h4>
                <div class="flex flex-col space-y-5">
                    <a href="index.html" class="font-label-sm text-[12px] text-[#b4cdb8] hover:text-[#d4af37] hover:translate-x-2 transition-all duration-300 uppercase tracking-widest w-fit">Home</a>
                    <a href="services.html" class="font-label-sm text-[12px] text-[#b4cdb8] hover:text-[#d4af37] hover:translate-x-2 transition-all duration-300 uppercase tracking-widest w-fit">Services</a>
                    <a href="gallery.html" class="font-label-sm text-[12px] text-[#b4cdb8] hover:text-[#d4af37] hover:translate-x-2 transition-all duration-300 uppercase tracking-widest w-fit">Gallery</a>
                    <a href="blog.html" class="font-label-sm text-[12px] text-[#b4cdb8] hover:text-[#d4af37] hover:translate-x-2 transition-all duration-300 uppercase tracking-widest w-fit">Journal</a>
                </div>
            </div>
            
            <!-- Studio Details -->
            <div class="md:col-span-3 flex flex-col">
                <h4 class="font-label-sm text-[11px] text-[#fbf9f4] uppercase tracking-[0.25em] mb-8">The Studio</h4>
                <div class="font-body-md text-[#b4cdb8] space-y-5 font-light">
                    <p>
                        <span class="block text-[#fbf9f4] font-medium mb-1 text-sm">Location</span>
                        128 Floral Avenue, Suite 4<br/>
                        Botanica District, NY 10012
                    </p>
                    <p>
                        <span class="block text-[#fbf9f4] font-medium mb-1 text-sm">Hours</span>
                        Tuesday – Saturday<br/>
                        10:00 AM – 6:00 PM<br/>
                        <span class="text-[11px] italic text-[#d4af37] mt-1 block">By appointment only</span>
                    </p>
                </div>
            </div>
            
            <!-- Contact & Social -->
            <div class="md:col-span-2 flex flex-col">
                <h4 class="font-label-sm text-[11px] text-[#fbf9f4] uppercase tracking-[0.25em] mb-8">Connect</h4>
                <div class="font-body-md text-[#b4cdb8] space-y-5 font-light mb-8">
                    <p>
                        <a href="mailto:hello@aureliafloral.com" class="hover:text-[#d4af37] transition-colors border-b border-[#b4cdb8]/30 pb-1">hello@aureliafloral.com</a>
                    </p>
                    <p>
                        <a href="tel:+12125550198" class="hover:text-[#d4af37] transition-colors">212.555.0198</a>
                    </p>
                </div>
                
                <div class="flex space-x-4">
                    <a href="#" class="w-10 h-10 rounded-full border border-[#d4af37]/30 flex items-center justify-center text-[#d4af37] hover:bg-[#d4af37] hover:text-[#0b2013] transition-all duration-300" aria-label="Instagram">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                            <path fill-rule="evenodd" d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z" clip-rule="evenodd" />
                        </svg>
                    </a>
                    <a href="#" class="w-10 h-10 rounded-full border border-[#d4af37]/30 flex items-center justify-center text-[#d4af37] hover:bg-[#d4af37] hover:text-[#0b2013] transition-all duration-300" aria-label="Pinterest">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                            <path fill-rule="evenodd" d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10c5.51 0 10-4.48 10-10S17.51 2 12 2zm6.605 4.61a8.502 8.502 0 011.93 5.314c-.281-.054-3.101-.629-5.943-.271-.065-.141-.12-.293-.184-.445a25.416 25.416 0 00-.564-1.236c3.145-1.28 4.577-3.124 4.761-3.362zM12 3.475c2.17 0 4.154.813 5.662 2.148-.152.216-1.443 1.941-4.48 3.08-1.399-2.57-2.95-4.675-3.189-5A8.687 8.687 0 0112 3.475zm-3.633.803a53.896 53.896 0 013.167 4.935c-3.992 1.063-7.517 1.04-7.896 1.04a8.581 8.581 0 014.729-5.975zM3.453 12.01v-.26c.37.01 4.512.065 8.775-1.215.166.329.332.682.479 1.05-4.092 1.439-8.563 2.15-8.98 2.22-.057-.597-.09-1.201-.09-1.815a8.59 8.59 0 01.077-1.025zM12 20.518c-2.22 0-4.22-.857-5.733-2.261.428-.088 4.397-.935 8.016-2.613a26.046 26.046 0 01-1.353 3.966c-.302.046-.61.083-.92.115a8.487 8.487 0 01-1.357.108zm2.63-1.745c.08-.226.155-.453.226-.684.81-2.628 1.107-4.887 1.144-5.201 3.232.88 5.485 2.122 5.568 2.17A8.528 8.528 0 0114.63 18.773z" clip-rule="evenodd" />
                        </svg>
                    </a>
                </div>
            </div>
        </div>
        
        <!-- Bottom Bar -->
        <div class="flex flex-col md:flex-row justify-between items-center border-t border-[#d4af37]/20 pt-8 mt-8">
            <p class="font-label-sm text-[10px] text-[#b4cdb8]/60 tracking-[0.2em] uppercase mb-4 md:mb-0">
                &copy; 2024 Aurelia Floral. All rights reserved.
            </p>
            <div class="flex space-x-6 text-[10px] text-[#b4cdb8]/60 tracking-[0.2em] uppercase font-label-sm">
                <a href="#" class="hover:text-[#d4af37] transition-colors">Privacy Policy</a>
                <a href="#" class="hover:text-[#d4af37] transition-colors">Terms of Service</a>
                <span>Designed with Elegance</span>
            </div>
        </div>
    </div>
</footer>"""

pattern = re.compile(r"(<!--\s*Footer\s*-->\s*)?<footer[\s\S]*?</footer>", re.IGNORECASE)

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        content = pattern.sub(grand_footer, content)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

print("Redesigned grand footer applied to all pages.")
