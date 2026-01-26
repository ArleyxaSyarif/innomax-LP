
import os

html_path = r'c:/projek/HtmlProjek/innomax-technology-it-startup-template-2024-12-26-16-25-57-utc/innomax-html-package/innomax/mockup/mockup1.html'

details_block = """            <!-- about section start  -->
            <section id="about" class="about pos-rel pt-120 pb-120">
                <div class="container">
                    <div class="row align-items-center">
                        <div class="col-lg-6">
                            <div class="da-about-img-wrap wow fadeInLeft" data-wow-duration="600ms">
                                <div class="img-shape"></div>
                                <img src="../assets/img/shape/about-glassisom.png" alt="" class="main-img">
                            </div>
                        </div>
                        <div class="col-lg-6">
                            <div class="da-about-content wow fadeInRight" data-wow-duration="600ms">
                                <div class="sec-title mb-30">
                                    <span class="sub-title">About Innomax</span>
                                    <h2 class="title">Harness Data to Drive <span>Business Success</span></h2>
                                </div>
                                <p>In an increasingly data-driven world, maximizing your data's potential is key. Our AI and Analytics solutions transform dispersed inputs into actionable intelligence, empowering you with insights that revolutionize your business.</p>
                                
                                <ul class="about-feature-list list-unstyled mb-40">
                                    <li><i class="far fa-check-circle"></i> Comprehensive Data Integration</li>
                                    <li><i class="far fa-check-circle"></i> Advanced AI-Powered Insights</li>
                                    <li><i class="far fa-check-circle"></i> Operational Efficiency & Innovation</li>
                                </ul>

                                <a href="../contact.html" class="thm-btn thm-btn--about">
                                    <span>Get Started Now</span>
                                    <i class="far fa-long-arrow-right"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <!-- about section end  -->"""

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<!-- about section start  -->'
end_marker = '<!-- about section end  -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + details_block + content[end_idx + len(end_marker):]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Successfully replaced About section HTML.')
else:
    print('Could not find About section markers.')
