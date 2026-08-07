import os
import re

directory = r"d:\project 2\Florist & Wedding Decoration Service"

# The new Sign Up button HTML
sign_up_btn = """<a class="hidden md:inline-block border border-primary text-primary dark:border-primary-fixed dark:text-primary-fixed px-6 py-3 uppercase tracking-wider hover:bg-primary hover:text-on-primary dark:hover:bg-primary-fixed dark:hover:text-on-primary-fixed transition-colors duration-300" href="register.html">
        Sign Up
    </a>\n    """

# We look for the "Enquire Now" button which is uniquely in the nav
pattern = re.compile(r'(<a class="hidden md:inline-block bg-primary-container[^>]*href="booking\.html"[^>]*>\s*Enquire Now\s*</a>)', re.IGNORECASE)

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Only inject if not already present
        if 'href="register.html"' not in content or 'Sign Up' not in content:
            new_content = pattern.sub(sign_up_btn + r'\1', content)
            
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)

print("Sign Up button added to the navigation menu on all pages.")
