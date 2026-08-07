import glob

theme_old = '<button id="theme-toggle" class="text-primary dark:text-primary-fixed hover:opacity-80 transition-opacity flex items-center justify-center p-2 rounded-full border border-primary/20" title="Toggle Dark/Light Mode">'
theme_new = '<button id="theme-toggle" class="text-primary dark:text-primary-fixed hover:opacity-80 transition-opacity flex items-center justify-center w-10 h-10 rounded-full border border-primary/20" title="Toggle Dark/Light Mode">'

rtl_old = '<button id="rtl-toggle" class="text-primary dark:text-primary-fixed hover:opacity-80 transition-opacity font-label-sm uppercase tracking-widest border border-primary/20 px-3 py-1.5 rounded-full text-xs" title="Toggle RTL/LTR">'
rtl_new = '<button id="rtl-toggle" class="text-primary dark:text-primary-fixed hover:opacity-80 transition-opacity font-label-sm uppercase tracking-widest flex items-center justify-center w-10 h-10 rounded-full border border-primary/20 text-[11px]" title="Toggle RTL/LTR">'

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace(theme_old, theme_new)
    new_content = new_content.replace(rtl_old, rtl_new)
    
    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {file}')
print('Done!')
