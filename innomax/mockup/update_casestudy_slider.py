
import os

html_path = r'c:/projek/HtmlProjek/innomax-technology-it-startup-template-2024-12-26-16-25-57-utc/innomax-html-package/innomax/mockup/mockup1.html'

# HTML for the Slider with 2 Slides, each having a Grid of 6 items (2 rows x 3 cols)
# We reuse the existing images and duplicate them for demo purposes.
slider_html = """
                    <!-- Case Study Slider (Swiper) -->
                    <div class="cs-grid-slider swiper-container">
                        <div class="swiper-wrapper">
                            
                            <!-- Slide 1 -->
                            <div class="swiper-slide">
                                <div class="cs-grid-container">
                                    <div class="cs-grid">
                                        <!-- Item 1 -->
                                        <div class="cs-grid-item">
                                            <img src="../assets/img/shape/perusahaan.jpg" alt="Project 1" class="cs-grid-img">
                                            <div class="cs-grid-overlay">
                                                <div class="cs-grid-content">
                                                    <h3>Digital Transformation</h3>
                                                    <p>FinTech</p>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- Item 2 -->
                                        <div class="cs-grid-item">
                                            <img src="../assets/img/blog/da-img01.jpg" alt="Project 2" class="cs-grid-img">
                                            <div class="cs-grid-overlay">
                                                <div class="cs-grid-content">
                                                    <h3>Data Analytics</h3>
                                                    <p>Healthcare</p>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- Item 3 -->
                                        <div class="cs-grid-item">
                                            <img src="../assets/img/bg/da-service_bg.jpg" alt="Project 3" class="cs-grid-img">
                                            <div class="cs-grid-overlay">
                                                <div class="cs-grid-content">
                                                    <h3>Cloud Migration</h3>
                                                    <p>E-commerce</p>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- Item 4 -->
                                        <div class="cs-grid-item">
                                            <img src="../assets/img/bg/da-footer.jpg" alt="Project 4" class="cs-grid-img">
                                            <div class="cs-grid-overlay">
                                                <div class="cs-grid-content">
                                                    <h3>AI Integration</h3>
                                                    <p>Retail</p>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- Item 5 -->
                                        <div class="cs-grid-item">
                                            <img src="../assets/img/testimonial/da-img.png" alt="Project 5" class="cs-grid-img">
                                            <div class="cs-grid-overlay">
                                                <div class="cs-grid-content">
                                                    <h3>Cyber Security</h3>
                                                    <p>Banking</p>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- Item 6 -->
                                        <div class="cs-grid-item">
                                            <img src="../assets/img/shape/perusahaan.jpg" alt="Project 6" class="cs-grid-img">
                                            <div class="cs-grid-overlay">
                                                <div class="cs-grid-content">
                                                    <h3>Mobile App</h3>
                                                    <p>Logistics</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- End Slide 1 -->

                            <!-- Slide 2 -->
                            <div class="swiper-slide">
                                <div class="cs-grid-container">
                                    <div class="cs-grid">
                                         <!-- Item 7 -->
                                        <div class="cs-grid-item">
                                            <img src="../assets/img/bg/da-service_bg.jpg" alt="Project 7" class="cs-grid-img">
                                            <div class="cs-grid-overlay">
                                                <div class="cs-grid-content">
                                                    <h3>Blockchain</h3>
                                                    <p>Finance</p>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- Item 8 -->
                                        <div class="cs-grid-item">
                                            <img src="../assets/img/blog/da-img01.jpg" alt="Project 8" class="cs-grid-img">
                                            <div class="cs-grid-overlay">
                                                <div class="cs-grid-content">
                                                    <h3>IoT Solutions</h3>
                                                    <p>Industrial</p>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- Item 9 -->
                                        <div class="cs-grid-item">
                                            <img src="../assets/img/shape/perusahaan.jpg" alt="Project 9" class="cs-grid-img">
                                            <div class="cs-grid-overlay">
                                                <div class="cs-grid-content">
                                                    <h3>DevOps</h3>
                                                    <p>Tech</p>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- Item 10 -->
                                        <div class="cs-grid-item">
                                            <img src="../assets/img/bg/da-footer.jpg" alt="Project 10" class="cs-grid-img">
                                            <div class="cs-grid-overlay">
                                                <div class="cs-grid-content">
                                                    <h3>SaaS Platform</h3>
                                                    <p>Education</p>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- Item 11 -->
                                        <div class="cs-grid-item">
                                            <img src="../assets/img/testimonial/da-img.png" alt="Project 11" class="cs-grid-img">
                                            <div class="cs-grid-overlay">
                                                <div class="cs-grid-content">
                                                    <h3>UX Design</h3>
                                                    <p>Creative</p>
                                                </div>
                                            </div>
                                        </div>
                                        <!-- Item 12 -->
                                        <div class="cs-grid-item">
                                            <img src="../assets/img/blog/da-img01.jpg" alt="Project 12" class="cs-grid-img">
                                            <div class="cs-grid-overlay">
                                                <div class="cs-grid-content">
                                                    <h3>Marketing API</h3>
                                                    <p>Sales</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- End Slide 2 -->
                            
                        </div>
                    </div>
"""

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the *previous* grid insert.
# The previous insert started with: <!-- 3-Column Grid --> (maybe, if I successfully wrote it? Wait, I saw "replaced slider with grid" output success in Step 676/677)
# But wait, in Step 677 verify, it printed "replaced slider with grid" and exit code 0.
# So the mockup1.html SHOULD ALREADY HAVE the 3-column grid I inserted.

# I need to find that grid and replace it.
# The previous insertion used text: 
# <div class="cs-grid-container"> ... </div>
# And I think I missed adding the "<!-- 3-Column Grid -->" comment in the *final write* of Step 676? 
# Ah, looking at Step 676 code: `grid_html = ... <!-- 3-Column Grid --> ...`
# Yes, it included the comment.

# So I can assume the content is wrapped or identified by:
# <!-- 3-Column Grid -->
# ... content ...
# </div> (closing cs-grid-container)
# </div> (closing cs-grid-container parent if mistaken? No just cs-grid-container)

start_marker = '<!-- 3-Column Grid -->'
start_idx = content.find(start_marker)

if start_idx == -1:
    # Try finding the div class directly if comment missing
    start_marker = '<div class="cs-grid-container">'
    start_idx = content.find(start_marker)

if start_idx != -1:
    # We need to find the end of this block.
    # The block ends before the closing of the section or before the next section.
    # The NEXT section starts with: <!-- quote&cta section start  --> (based on file view)
    # OR <!-- testimonial section end  -->
    
    # Let's find the next comment marker.
    next_marker = '<!-- testimonial section end  -->'
    end_idx = content.find(next_marker, start_idx)
    
    if end_idx == -1:
        # Fallback
        end_idx = content.find('</section>', start_idx)
    
    if end_idx != -1:
        # We replace everything from start_idx up to (but not including) end_idx's previous line end?
        # Let's look at the structure.
        # <section id="casestudy" ...>
        #    ... HEADER ...
        #    [GRID BLOCK]
        # </section>
        
        # We want to keep </section>. We want to replace [GRID BLOCK].
        # [GRID BLOCK] ends with a closing </div> for .cs-grid-container.
        
        # Since I am replacing with a slider that wraps everything, I can just replace the whole chunk.
        
        # Verify if I need to delete any trailing </div>s that might be left over from bad replaces?
        # The previous replace was: new_content = content[:start_idx] + grid_html + content[end_idx:]
        # So it should be clean.
        
        # Precise replacement: find the last </div> before the end_idx.
        # That closes the container.
        
        # Actually, let's just replace from start_idx to the last closing div of the container.
        # It's <div class="cs-grid-container"> ... </div>
        
        # But wait, Swiper setup often needs the container to have overflow hidden? 
        # .swiper-container usually has it.
        
        # Let's just do a big swap.
        
        # Locate the header end
        header_end = content.find('<div class="project-header mb-60">')
        if header_end != -1:
             # Find close div of header
             # <div class="project-header ..."> ... </div>
             header_close = content.find('</div>', header_end + 30) 
             # header has children divs (left, right). So we need to skip them.
             # Easier: find the start of the grid.
             pass
        
        # Okay, using start_marker is best.
        # And finding the next section marker to clamp the end.
        
        # Let's check what came before the grid.
        # The header ends. Then the grid starts.
        # The grid needs to be replaced by `slider_html`.
        
        # Identify the content to cut.
        # From `start_idx`
        # To `end_idx` (which is <!-- testimonial section end -->)
        # But we need to keep the closing `</div>` of the `<div class="container">`?
        # The structure is:
        # <section>
        #   <div class="container">
        #       <header>...</header>
        #       [GRID WAS HERE]
        #   </div>
        # </section>
        
        # So `end_idx` points to `<!-- testimonial section end -->`.
        # Before that, there is `</section>`.
        # Before that, there is `</div>` (container).
        # Before that, there is [GRID].
        
        # So I should find the `</div>` that closes `.container` and stop before it.
        container_close = content.rfind('</div>', start_idx, end_idx)
        
        # If I replace from start_idx to container_close, I am good.
        
        new_content = content[:start_idx] + slider_html + content[container_close:]
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Success: Replaced grid with 6-item slider.")
        
    else:
        print("Error: Could not find end marker.")
else:
    print("Error: Could not find start marker (Grid).")
