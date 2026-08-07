import os
import re

directory = r"d:\project 2\Florist & Wedding Decoration Service"

link_map = {
    "Home": "index.html",
    "Alternative Home": "home2.html",
    "Services": "services.html",
    "Gallery": "gallery.html",
    "Blog": "blog.html",
    "Booking": "booking.html",
    "Enquire Now": "booking.html",
    "Log In": "login.html",
    "Create one": "register.html",
    "Back to Home": "index.html"
}

# Add some other common links we saw
link_map_exact = {
    'href="#">Home</a>': 'href="index.html">Home</a>',
    'href="#">Alternative Home</a>': 'href="home2.html">Alternative Home</a>',
    'href="#">Services</a>': 'href="services.html">Services</a>',
    'href="#">Gallery</a>': 'href="gallery.html">Gallery</a>',
    'href="#">Blog</a>': 'href="blog.html">Blog</a>',
    'href="#">Booking</a>': 'href="booking.html">Booking</a>',
    'href="#">Log In</a>': 'href="login.html">Log In</a>',
    'href="#">Create one</a>': 'href="register.html">Create one</a>',
    'href="#">Back to Home</a>': 'href="index.html">Back to Home</a>',
    'href="#">Aurelia Floral</a>': 'href="index.html">Aurelia Floral</a>'
}

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        for old, new in link_map_exact.items():
            content = content.replace(old, new)
            
        # Regex for Enquire Now (spans multiple lines)
        content = re.sub(
            r'href="#"([^>]*)>(\s*)Enquire Now(\s*)</a>',
            r'href="booking.html"\1>\2Enquire Now\3</a>',
            content
        )
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

print("Links replaced.")
