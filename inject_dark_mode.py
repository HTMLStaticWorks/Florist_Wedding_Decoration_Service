import os

directory = r"d:\project 2\Florist & Wedding Decoration Service"

dark_mode_styles = """
<!-- Dark Mode CSS Overrides -->
<style id="dark-theme-overrides">
  html.dark body, html.dark .bg-background {
    background-color: #1b1c19 !important;
    color: #fbf9f4 !important;
  }
  html.dark .text-on-surface, html.dark .text-on-background {
    color: #fbf9f4 !important;
  }
  html.dark .bg-surface-container, html.dark .bg-surface-container-low, html.dark .bg-surface-container-lowest, html.dark .bg-surface, html.dark .bg-white {
    background-color: #1a231e !important;
    color: #fbf9f4 !important;
  }
  html.dark .bg-white\/70, html.dark .bg-surface-container-lowest\/90 {
    background-color: rgba(26, 35, 30, 0.9) !important;
  }
  html.dark .text-secondary {
    color: #d0e9d4 !important;
  }
  html.dark .text-on-surface-variant {
    color: #b4cdb8 !important;
  }
  html.dark .border-primary\/30, html.dark .border-primary-container\/30 {
    border-color: rgba(212, 175, 55, 0.2) !important;
  }
  html.dark .organic-shadow {
    box-shadow: 0 10px 40px -10px rgba(0,0,0,0.5);
  }
</style>
</head>"""

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        if '<style id="dark-theme-overrides">' not in content:
            content = content.replace("</head>", dark_mode_styles)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)

print("Dark mode CSS overrides injected to all HTML pages.")
