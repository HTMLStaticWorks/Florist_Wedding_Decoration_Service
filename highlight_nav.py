import os
import re

directory = r"d:\project 2\Florist & Wedding Decoration Service"

# Base classes
default_class = "text-on-surface-variant dark:text-surface-variant hover:text-primary dark:hover:text-primary-fixed transition-colors hover:opacity-80 duration-300"
active_class = "text-primary dark:text-primary-fixed border-b border-primary dark:border-primary-fixed pb-1 font-bold hover:opacity-80 transition-all duration-300 scale-95"

links_data = [
    ("index.html", "Home"),
    ("home2.html", "Alternative Home"),
    ("services.html", "Services"),
    ("gallery.html", "Gallery"),
    ("blog.html", "Blog"),
    ("booking.html", "Booking")
]

# Regex to find the desktop nav links container
# It looks for <div class="hidden md:flex space-x-8 items-center"> ... </div>
nav_pattern = re.compile(r'(<div class="hidden md:flex space-x-8 items-center">)(.*?)(</div>\s*<!-- Trailing)', re.IGNORECASE | re.DOTALL)

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Build the new nav HTML for this specific file
        new_nav_html = "\n"
        for href, text in links_data:
            # If the link matches the current file, it's active. 
            # Note: For home2.html we can let it match home2.html.
            is_active = (href == filename)
            cls = active_class if is_active else default_class
            new_nav_html += f'    <a class="{cls}" href="{href}">{text}</a>\n'
            
        # Replace the contents of the nav div
        # Using a replacement function to substitute the inner HTML
        def replace_nav(match):
            return match.group(1) + new_nav_html + match.group(3)
            
        new_content = nav_pattern.sub(replace_nav, content)
        
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)

print("Menu highlights updated across all HTML pages.")
