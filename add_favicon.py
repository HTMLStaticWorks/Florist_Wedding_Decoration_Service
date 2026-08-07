import os

directory = r"d:\project 2\Florist & Wedding Decoration Service"

favicon_tag = '\n<link rel="icon" href="favicon.svg" type="image/svg+xml" />\n</head>'

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        if 'rel="icon"' not in content:
            # We insert it right before the closing </head> tag
            content = content.replace("</head>", favicon_tag)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

print("Favicon tag added to all HTML pages.")
