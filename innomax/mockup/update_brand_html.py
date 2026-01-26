
import os

html_path = r'c:/projek/HtmlProjek/innomax-technology-it-startup-template-2024-12-26-16-25-57-utc/innomax-html-package/innomax/mockup/mockup1.html'

# Update markers based on view_file result
start_marker = '<!-- brand section start  -->'
# Will find end marker dynamically or assume it closes the section

# New Brand Section HTML
# 2 Rows:
# Row 1: cs-brd01 to cs-brd09
# Row 2: cs-brd10 to cs-brd18
# Duplicated 4 times each for infinite looped feel.

list_1 = [f'cs-brd{i:02d}.png' for i in range(1, 10)]
list_2 = [f'cs-brd{i:02d}.png' for i in range(10, 19)]

def generate_row_html(image_list, direction_class):
    # Repeat list 4 times
    full_list = image_list * 4
    cards_html = ""
    for img in full_list:
        cards_html += f"""
                            <div class="brand-card">
                                <img src="../assets/img/brand/{img}" alt="Brand Logo">
                            </div>"""
    
    return f"""
                    <div class="brand-marquee-row {direction_class}">
                        <div class="brand-track">
                            {cards_html}
                        </div>
                    </div>"""

row1_html = generate_row_html(list_1, 'scroll-left')
row2_html = generate_row_html(list_2, 'scroll-right')

new_brand_html = f"""<!-- brand section start  -->
            <section class="brand-section">
                <div class="container">
                    <div class="brand-title-wrap">
                        <h2 class="xb-item--title" style="font-size: 36px; font-weight: 800; margin-bottom: 20px;">
                            Trusted by <span style="color: #036AAD;">Global Innovators</span>
                        </h2>
                        <p style="max-width: 600px; margin: 0 auto; color: #555;">
                            Join over 25,000+ companies that rely on Innomax for their digital transformation.
                        </p>
                    </div>
                </div>
                
                <div class="brand-marquee-wrapper">
                    {row1_html}
                    {row2_html}
                </div>
            </section>
            <!-- brand section end  -->"""

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the section
start_idx = content.find(start_marker)
# Finding the end marker. Usually it's <!-- brand section end  --> or similar.
# Inspecting file content from tool output:
# 452:             <!-- brand section start  -->
# ...
# I will assume the section closes before the next comment or footer.
# Let's search for the end marker if I can see it in previous outputs, otherwise search for </section> + comment.

# Looking at previous context, it likely ends with <!-- brand section end -->
end_marker = '<!-- brand section end  -->'
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_brand_html + content[end_idx + len(end_marker):]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Successfully replaced Brand section.')
else:
    print(f'Could not find markers. Start: {start_idx}, End: {end_idx}')
    # If end marker not found, try finding the next section start or footer
    if start_idx != -1:
         # Try finding next section
         next_section = content.find('<!--', start_idx + len(start_marker))
         if next_section != -1:
             new_content = content[:start_idx] + new_brand_html + '\n            ' + content[next_section:]
             with open(html_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
             print('Successfully replaced Brand section (using next marker fallback).')

