
import os

html_path = r'c:/projek/HtmlProjek/innomax-technology-it-startup-template-2024-12-26-16-25-57-utc/innomax-html-package/innomax/mockup/mockup1.html'

# Distinctive markers for the Case Study section
start_marker = '<!-- testimonial section start  -->'
end_marker = '<!-- testimonial section end  -->'

# New content block
new_cs_block = """            <!-- testimonial section start  -->
            <section id="casestudy" class="casestudy-section pt-120 pb-120" style="background-color: #fff;">
                <div class="container">
                    <div class="row align-items-center">
                        <!-- Content Side (Left) -->
                        <div class="col-lg-6">
                            <div class="casestudy-content wow fadeInLeft" data-wow-delay="0.2s">
                                <div class="sec-title mb-30">
                                    <span class="sub-title" style="color: #036AAD; text-transform: uppercase; font-weight: 600; letter-spacing: 2px;">Success Stories</span>
                                    <h2 class="title" style="font-size: 36px; font-weight: 800; line-height: 1.3;">Transforming Medical Imaging with <span style="color: #036AAD;">Microsoft Cloud</span></h2>
                                </div>
                                <p class="mb-40" style="color: #555; font-size: 17px; line-height: 1.7;">With the ambition to scale and further develop its AI-imaging biomarker service offering to the global clinical trial market, IXICO partnered with us for a secure and seamless cloud transformation.</p>

                                <!-- Metrics/Stats Row -->
                                <div class="cs-metrics-wrap d-flex mb-40">
                                    <div class="cs-metric-item">
                                        <h3 style="color: #036AAD; font-size: 32px; font-weight: 800;">$3M+</h3>
                                        <p>Annual Cost Savings</p>
                                    </div>
                                    <div class="cs-metric-item">
                                        <h3 style="color: #036AAD; font-size: 32px; font-weight: 800;">200+</h3>
                                        <p>Clinical Trials Supported</p>
                                    </div>
                                </div>

                                <a href="#!" class="thm-btn thm-btn--about">
                                    <span>View Case Study</span>
                                    <i class="far fa-long-arrow-right"></i>
                                </a>
                            </div>
                        </div>

                        <!-- Image Side (Right) -->
                        <div class="col-lg-6">
                            <div class="casestudy-img-wrap wow fadeInRight" data-wow-delay="0.2s">
                                <!-- decorative shape -->
                                <div class="cs-shape"></div>
                                <img src="../assets/img/blog/da-img01.jpg" alt="Case Study" class="cs-main-img">
                                <div class="cs-overlay-info">
                                    <span class="cs-tag">Medical / Cloud</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <!-- testimonial section end  -->"""

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_cs_block + content[end_idx + len(end_marker):]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Successfully replaced Case Study section HTML.')
else:
    print('Could not find Case Study section markers.')
