import glob

old_rule = '  html.dark .bg-surface-container, html.dark .bg-surface-container-low, html.dark .bg-surface-container-lowest, html.dark .bg-surface, html.dark .bg-white {'
new_rule = '''  html.dark .bg-surface-container, html.dark .bg-surface-container-low, html.dark .bg-surface-container-lowest, html.dark .bg-surface, html.dark .bg-white, html.dark .bg-surface-container-high, html.dark .bg-surface-container-highest, html.dark .bg-surface-dim, html.dark .bg-surface-bright {'''

updated = 0
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_rule in content:
        new_content = content.replace(old_rule, new_rule)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file}')
        updated += 1
    else:
        print(f'No match in {file}')

print(f'Done! Updated {updated} files.')
