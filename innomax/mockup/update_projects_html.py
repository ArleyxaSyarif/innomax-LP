
import os

html_path = r'c:/projek/HtmlProjek/innomax-technology-it-startup-template-2024-12-26-16-25-57-utc/innomax-html-package/innomax/mockup/mockup1.html'

start_marker = '<!-- testimonial section start  -->'
end_marker = '<!-- testimonial section end  -->'

# Using existing imagery to populate the slider
# Images: 
# ../assets/img/blog/da-img01.jpg
# ../assets/img/project/pro_img01.jpg (assuming exists or use generic)
# for safety I will reuse known images or similar naming conventions from previous files if I recall, 
# but looking at file structure: ../assets/img/blog/da-img01.jpg exists.
# I'll use placeholders that likely exist or just the same image for demo if I can't verify others,
# but usually templates have portfolio/project images. 
# I will use da-img01.jpg and maybe others if I saw them. 
# Previous view showed ../assets/img/bg/da-service_bg.jpg etc.
# I'll stick to a safe image I know exists: ../assets/img/blog/da-img01.jpg and maybe ../assets/img/shape/perusahaan.jpg used earlier.

# Actually better to use placeholders if I'm not sure, but user wants "Selected Projects".
# I'll use:
# 1. ../assets/img/shape/perusahaan.jpg
# 2. ../assets/img/blog/da-img01.jpg
# 3. ../assets/img/bg/da-service_bg.jpg
# 4. ../assets/img/bg/da-footer.jpg

new_project_block = """            <!-- testimonial section start  -->
            <section id="casestudy" class="project-section pt-120 pb-120">
                <div class="container">
                    <!-- Section Header -->
                    <div class="project-header mb-60">
                        <div class="header-left">
                             <h2 class="title">Selected Projects</h2>
                             <p>Explore our portfolio of strategic transformations and digital innovations. We partner with industry leaders to deliver measurable impact.</p>
                        </div>
                        <div class="header-right">
                            <div class="project-arrows">
                                <div class="project-arrow project-prev"><i class="far fa-angle-left"></i></div>
                                <div class="project-arrow project-next"><i class="far fa-angle-right"></i></div>
                            </div>
                        </div>
                    </div>

                    <!-- Slider -->
                    <div class="project-slider swiper-container">
                        <div class="swiper-wrapper">
                            <!-- Slide 1 -->
                            <div class="swiper-slide">
                                <div class="project-card">
                                    <img src="../assets/img/shape/perusahaan.jpg" alt="Project 1">
                                </div>
                            </div>
                            <!-- Slide 2 -->
                            <div class="swiper-slide">
                                <div class="project-card">
                                    <img src="../assets/img/blog/da-img01.jpg" alt="Project 2">
                                </div>
                            </div>
                            <!-- Slide 3 -->
                            <div class="swiper-slide">
                                <div class="project-card">
                                    <img src="../assets/img/bg/da-service_bg.jpg" alt="Project 3">
                                </div>
                            </div>
                             <!-- Slide 4 -->
                            <div class="swiper-slide">
                                <div class="project-card">
                                    <img src="../assets/img/bg/da-footer.jpg" alt="Project 4">
                                </div>
                            </div>
                        </div>
                        <!-- Pagination -->
                        <div class="project-pagination"></div>
                    </div>
                </div>
            </section>
            <!-- testimonial section end  -->"""

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_project_block + content[end_idx + len(end_marker):]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Successfully replaced Case Study section with Selected Projects slider.')
else:
    print('Could not find Case Study section markers.')
