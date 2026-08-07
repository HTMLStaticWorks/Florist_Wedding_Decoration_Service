import glob

# The key dark mode fix to add - this is the complete set of dark mode fixes
dark_fix_addition = """  html.dark .text-primary {
    color: #e9c349 !important;
  }
  html.dark .border-primary {
    border-color: #e9c349 !important;
  }
  html.dark .border-primary\\/20 {
    border-color: rgba(233, 195, 73, 0.2) !important;
  }
  html.dark .border-primary\\/10 {
    border-color: rgba(233, 195, 73, 0.1) !important;
  }
  html.dark .text-primary\\/60 {
    color: rgba(233, 195, 73, 0.6) !important;
  }
  html.dark .text-primary\\/80 {
    color: rgba(233, 195, 73, 0.8) !important;
  }
  html.dark .bg-primary {
    background-color: #e9c349 !important;
    color: #1b1c19 !important;
  }
  html.dark .bg-primary-container {
    background-color: #4d3d00 !important;
    color: #ffe088 !important;
  }
  html.dark .text-on-primary-container {
    color: #ffe088 !important;
  }
  html.dark .hover\\:text-primary:hover {
    color: #e9c349 !important;
  }
  html.dark .hover\\:bg-primary:hover {
    background-color: #e9c349 !important;
    color: #1b1c19 !important;
  }
"""

marker = '  html.dark .organic-shadow {'

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if marker in content and 'html.dark .text-primary {' not in content:
        new_content = content.replace(marker, dark_fix_addition + marker)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file}')
    elif 'html.dark .text-primary {' in content:
        print(f'Already has fix: {file}')
    else:
        print(f'Marker not found: {file}')

print('Done!')
