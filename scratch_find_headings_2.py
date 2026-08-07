import os, glob, re

html_files = glob.glob('*.html')
custom_fonts = [
    'font-headline-md', 'font-label-sm', 'font-body-md', 
    'font-body-lg', 'font-headline-lg', 'font-headline-lg-mobile', 'font-display-lg'
]

class_pattern = re.compile(r'class="([^"]+)"')
size_pattern = re.compile(r'text-(xs|sm|base|lg|xl|2xl|3xl|4xl|5xl|6xl|7xl|8xl|9xl|headline-md|headline-lg|headline-lg-mobile|display-lg|body-md|body-lg|label-sm|\[\d+px\])')

found_any = False
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        matches = class_pattern.finditer(line)
        for m in matches:
            cls = m.group(1).split()
            has_custom_font = any(f in cls for f in custom_fonts)
            if has_custom_font:
                has_size = any(size_pattern.search(c) for c in cls)
                if not has_size:
                    print(f'{file}: line {i+1} - {" ".join(cls)}')
                    found_any = True

if not found_any:
    print("All good!")
