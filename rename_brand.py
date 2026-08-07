import os
import re

directory = r"d:\project 2\Florist & Wedding Decoration Service"

# We will replace both the standard version and the line-break version found in the footer
replacements = {
    "Aurelia Floral": "Floréa",
    "Aurelia <br/> Floral": "Floréa",
    "Aurelia <br> Floral": "Floréa"
}

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        modified = False
        for old_text, new_text in replacements.items():
            if old_text in content:
                content = content.replace(old_text, new_text)
                modified = True
                
        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

print("Brand name updated to Floréa across all HTML pages.")
