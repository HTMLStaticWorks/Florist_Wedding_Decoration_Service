import os, glob, re

html_files = glob.glob('*.html')
pattern = re.compile(r'<h[1-6][^>]*class="([^"]*font-headline-[^"]*)"[^>]*>')
size_pattern = re.compile(r'text-(xs|sm|base|lg|xl|2xl|3xl|4xl|5xl|6xl|7xl|8xl|9xl|headline-md|headline-lg|headline-lg-mobile|display-lg|body-md|body-lg|label-sm|\[\d+px\])')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = pattern.finditer(content)
    for m in matches:
        cls = m.group(1)
        if not size_pattern.search(cls):
            print(f'{file}: {m.group(0)}')
