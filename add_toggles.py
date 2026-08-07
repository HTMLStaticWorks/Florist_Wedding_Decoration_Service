import os
import re

directory = r"d:\project 2\Florist & Wedding Decoration Service"

trailing_action_replacement = """<!-- Trailing Actions & Toggles -->
<div class="hidden md:flex items-center space-x-4">
    <button id="theme-toggle" class="text-primary dark:text-primary-fixed hover:opacity-80 transition-opacity flex items-center justify-center p-2 rounded-full border border-primary/20" title="Toggle Dark/Light Mode">
        <span class="material-symbols-outlined text-xl dark:hidden">dark_mode</span>
        <span class="material-symbols-outlined text-xl hidden dark:block">light_mode</span>
    </button>
    <button id="rtl-toggle" class="text-primary dark:text-primary-fixed hover:opacity-80 transition-opacity font-label-sm uppercase tracking-widest border border-primary/20 px-3 py-1.5 rounded-full text-xs" title="Toggle RTL/LTR">
        RTL
    </button>
    <a class="hidden md:inline-block bg-primary-container text-on-primary-container px-6 py-3 uppercase tracking-wider hover:bg-inverse-primary transition-colors duration-300" href="booking.html">
        Enquire Now
    </a>
</div>"""

pattern = re.compile(r"<!--\s*Trailing Action\s*-->\s*<a[^>]*>.*?Enquire Now\s*</a>", re.IGNORECASE | re.DOTALL)

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace trailing action
        content = pattern.sub(trailing_action_replacement, content)
        
        # Append script if needed
        if 'theme-toggles.js' not in content:
            content = content.replace("</body>", '<script src="theme-toggles.js"></script>\n</body>')
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

print("Nav toggles and script added to all HTML pages.")
