import os

directory = r"d:\project 2\Florist & Wedding Decoration Service"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # The footer copyright might look like "&copy; 2024"
        if "&copy; 2024" in content:
            content = content.replace("&copy; 2024", "&copy; 2026")
            
        if "© 2024" in content:
            content = content.replace("© 2024", "© 2026")
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

print("Updated footer copyright year from 2024 to 2026.")
