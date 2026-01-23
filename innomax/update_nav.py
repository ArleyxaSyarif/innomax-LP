
import os

file_path = r"c:/projek/HtmlProjek/innomax-technology-it-startup-template-2024-12-26-16-25-57-utc/innomax-html-package/innomax/home-5.html"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
desktop_replaced = False
mobile_replaced = False

desktop_nav_replacement = """                                <nav class="main-menu collapse navbar-collapse">
                                    <ul>
                                        <li class="active"><a href="#hero"><span>Home</span></a></li>
                                        <li><a href="#about"><span>About</span></a></li>
                                        <li><a href="#service"><span>Services</span></a></li>
                                        <li><a href="#process"><span>Process</span></a></li>
                                        <li><a href="#tech"><span>Tech Stack</span></a></li>
                                        <li><a href="#feature"><span>Features</span></a></li>
                                        <li><a href="#blog"><span>Blog</span></a></li>
                                        <li><a href="contact.html"><span>Contact</span></a></li>
                                    </ul>
                                </nav>
"""

mobile_nav_replacement = """                                    <nav class="xb-header-nav">
                                        <ul class="xb-menu-primary clearfix">
                                            <li class="active"><a href="#hero"><span>Home</span></a></li>
                                            <li><a href="#about"><span>About</span></a></li>
                                            <li><a href="#service"><span>Services</span></a></li>
                                            <li><a href="#process"><span>Process</span></a></li>
                                            <li><a href="#tech"><span>Tech Stack</span></a></li>
                                            <li><a href="#feature"><span>Features</span></a></li>
                                            <li><a href="#blog"><span>Blog</span></a></li>
                                            <li><a href="contact.html"><span>Contact</span></a></li>
                                        </ul>
                                    </nav>
"""

i = 0
while i < len(lines):
    line = lines[i]
    stripped = line.strip()
    
    # Desktop Nav Detection
    if 'class="main-menu collapse navbar-collapse"' in line and not desktop_replaced:
        new_lines.append(desktop_nav_replacement)
        desktop_replaced = True
        # Skip until </nav>
        
        # Find the closing nav tag. Since it's nested structure, we need to be careful.
        # But in this specific file, the <nav> starts, contains <ul> and mega menus.
        # We can just skip lines until we find a line that is EXACTLY `</nav>` or contains `</nav>` at a matching indentation level?
        # Actually, let's just count open/close tags or just look for the </nav> that closes this.
        # Given the previous reads, it seems the </nav> is on its own line or with whitespace.
        
        # Simple Logic: Iterate forward until we find `</nav>` that seems to close this one. 
        # Since looking at file content, there are SUBMENUS but they are <ul> inside <li>. 
        # There are NO nested <nav> tags inside the main menu.
        
        j = i + 1
        while j < len(lines):
            if '</nav>' in lines[j]:
                i = j + 1 # Continue after this line
                break
            j += 1
        continue

    # Mobile Nav Detection
    if 'class="xb-header-nav"' in line and not mobile_replaced:
        new_lines.append(mobile_nav_replacement)
        mobile_replaced = True
        j = i + 1
        while j < len(lines):
            if '</nav>' in lines[j]:
                i = j + 1
                break
            j += 1
        continue
        
    new_lines.append(line)
    i += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Successfully updated home-5.html")
