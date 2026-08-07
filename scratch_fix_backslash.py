with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('flex flex-col h-full\\"', 'flex flex-col h-full"')
with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(content)
