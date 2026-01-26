
import os

html_path = r'c:/projek/HtmlProjek/innomax-technology-it-startup-template-2024-12-26-16-25-57-utc/innomax-html-package/innomax/mockup/mockup1.html'

# Distinctive markers for the Feature section
start_marker = '<!-- feature section start  -->'
end_marker = '<!-- feature section end  -->'

# New content block
# Note using the icons from user request image: Oil Can, Cogs, Flask, Drafting Compass roughly match the themes.
# I will use FontAwesome 5 icons available in the template.
new_feature_block = """            <!-- feature section start  -->
            <section id="feature" class="feature pt-120 pb-120" style="background-color: #f9f9f9;">
                <div class="container">
                    <div class="row justify-content-center">
                        <div class="col-lg-8">
                            <div class="sec-title text-center mb-60">
                                <h2 class="title" style="font-size: 36px; font-weight: 800; color: #111;">We Provide <span style="color: #036AAD;">Best Service</span></h2>
                            </div>
                        </div>
                    </div>

                    <div class="row mt-none-30">
                        <!-- Item 1: Petroleum & Gas Energy -->
                        <div class="col-lg-3 col-md-6 mt-30">
                            <div class="feature-card-item wow fadeInUp" data-wow-delay="0ms">
                                <div class="icon">
                                    <i class="fal fa-gas-pump"></i>
                                </div>
                                <h3 class="title">Petroleum & Gas Energy</h3>
                                <p>Delivering long-term principles centered processes world.</p>
                                <a href="#!" class="read-more">Read More <i class="far fa-long-arrow-right"></i></a>
                            </div>
                        </div>
                        
                        <!-- Item 2: Mechanical & Engineering -->
                        <div class="col-lg-3 col-md-6 mt-30">
                            <div class="feature-card-item wow fadeInUp" data-wow-delay="100ms">
                                <div class="icon">
                                    <i class="fal fa-cogs"></i>
                                </div>
                                <h3 class="title">Mechanical & Engineering</h3>
                                <p>Starts with engineers principle centered processes centering.</p>
                                <a href="#!" class="read-more">Read More <i class="far fa-long-arrow-right"></i></a>
                            </div>
                        </div>

                        <!-- Item 3: Basic Industrial Chemicals -->
                        <div class="col-lg-3 col-md-6 mt-30">
                            <div class="feature-card-item wow fadeInUp" data-wow-delay="200ms">
                                <div class="icon">
                                    <i class="fal fa-flask"></i>
                                </div>
                                <h3 class="title">Basic Industrial Chemicals</h3>
                                <p>Our service engineers principle centered processes market.</p>
                                <a href="#!" class="read-more">Read More <i class="far fa-long-arrow-right"></i></a>
                            </div>
                        </div>

                        <!-- Item 4: Development & Engineering -->
                        <div class="col-lg-3 col-md-6 mt-30">
                            <div class="feature-card-item wow fadeInUp" data-wow-delay="300ms">
                                <div class="icon">
                                    <i class="fal fa-drafting-compass"></i>
                                </div>
                                <h3 class="title">Development & Engineering</h3>
                                <p>Services get engineers principle centered processes forward.</p>
                                <a href="#!" class="read-more">Read More <i class="far fa-long-arrow-right"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <!-- feature section end  -->"""

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # Replace content between markers including the markers themselves (since my new block includes them)
    # Actually wait, my new block INCLUDES markers.
    # content[:start_idx] includes everything before start_marker.
    # content[end_idx + len(end_marker):] includes everything after end_marker.
    
    new_content = content[:start_idx] + new_feature_block + content[end_idx + len(end_marker):]
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Successfully replaced Feature section HTML.')
else:
    print('Could not find Feature section markers.')
