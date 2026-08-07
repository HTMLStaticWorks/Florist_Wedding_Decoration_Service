import re
with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

count2 = len(re.findall(r'</p>\s*</article>', content))
print(f'Matches for closing tags with \s*: {count2}')

count3 = len(re.findall(r'</p>[\s\S]*?</article>', content))
print(f'Matches for closing tags with [\s\S]*?: {count3}')
