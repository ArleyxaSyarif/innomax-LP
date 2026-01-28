
import re
import os

source_path = r'c:/projek/HtmlProjek/innomax-technology-it-startup-template-2024-12-26-16-25-57-utc/innomax-html-package/innomax/home-3.html'
target_path = r'c:/projek/HtmlProjek/innomax-technology-it-startup-template-2024-12-26-16-25-57-utc/innomax-html-package/innomax/sinekra/sinekra.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Asset Paths (img, css, js)
# matches src="assets/..." or href="assets/..."
content = re.sub(r'(src|href)=([\"\'])assets/', r'\1=\2../assets/', content)

# 2. Update HTML Link Paths (sibling pages)
# We want to catch href="about.html", href="index.html" etc.
# avoiding http, #, mailto, and already relative paths starting with ..
# Regex explanation:
# href=         matches "href="
# ([\"\'])      matches the quote (group 1)
# (?!           negative lookahead start
#  http|        no http
#  \#|          no #
#  mailto|      no mailto
#  \.\./        no ../
# )             end negative lookahead
# ([^\"\']+\.html) matches the filename ending in .html (group 2)
# \1            matches the closing quote

pattern = r'href=([\"\'])(?!http|#|mailto|\.\./)([^\"\']+\.html)\1'

def replace_html_link(match):
    quote = match.group(1)
    link = match.group(2)
    new_link = f'../{link}'
    print(f'Replacing {link} with {new_link}')
    return f'href={quote}{new_link}{quote}'

content = re.sub(pattern, replace_html_link, content)

# 3. Inject sinekra.css link before </head>
custom_css_link = '    <link rel="stylesheet" href="sinekra.css">\n'
if '</head>' in content:
    content = content.replace('</head>', f'{custom_css_link}</head>')
else:
    print("Warning: </head> tag not found, appending CSS link to end.")
    content += custom_css_link

# Ensure target directory exists
os.makedirs(os.path.dirname(target_path), exist_ok=True)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully created sinekra.html with corrected paths.')
