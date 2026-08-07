import glob

select_fix = """  html.dark select {
    background-color: #1a231e !important;
    color: #fbf9f4 !important;
    color-scheme: dark;
  }
  html.dark select option {
    background-color: #1a231e !important;
    color: #fbf9f4 !important;
  }
  html.dark input, html.dark textarea {
    color-scheme: dark;
  }
"""

# Insert before the closing of the dark-theme-overrides block
marker = '  html.dark .organic-shadow {'
updated = 0
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if marker in content and 'html.dark select {' not in content:
        new_content = content.replace(marker, select_fix + marker)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file}')
        updated += 1
    elif 'html.dark select {' in content:
        print(f'Already fixed: {file}')
    else:
        print(f'Marker not found in: {file}')

print(f'Done! Updated {updated} files.')
