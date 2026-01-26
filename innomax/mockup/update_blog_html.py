
import os

html_path = r'c:/projek/HtmlProjek/innomax-technology-it-startup-template-2024-12-26-16-25-57-utc/innomax-html-package/innomax/mockup/mockup1.html'

# New Editorial Blog HTML
# Using project images:
# Featured: ../assets/img/blog/da-img01.jpg (as logic placeholder, or use snippet URL if user prefers. I will use a mix or just URLs for now to match design exactly first, then maybe swap).
# User provided snippet uses external URLs. I will stick to external URLs for the "look" as requested, but maybe add a comment to swap them.
# Actually, better to use local images if possible.
# da-img01.jpg exists. I will use it for featured.
# da-img02.jpg, da-img03.jpg for sidebars.

new_blog_html = """<!-- blog section start -->
            <section id="blog" class="blog-editorial-section">
                <div class="container">
                    <!-- Section Header -->
                    <div class="be-header">
                        <div class="be-header-top">
                            <h2 class="be-title">From the Journal</h2>
                            <a class="be-view-all" href="#">
                                View all posts 
                                <span class="material-symbols-outlined" style="font-size: 20px;">arrow_forward</span>
                            </a>
                        </div>
                        <p class="be-subtitle">
                            Insights on design, productivity, and the future of work from our creative team.
                        </p>
                    </div>

                    <!-- Editorial Grid Layout -->
                    <div class="be-grid">
                        <!-- Featured Post (Left, 2/3 width) -->
                        <div class="be-featured-col">
                            <div class="be-featured-card">
                                <!-- Background Image (Using placeholder or local if available) -->
                                <div class="be-featured-bg" style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuCJ_2Y-YJw3rwjm-_HixWTk09JBvYlYWOlH791yuHJKlSagqyXzAJQ2JHhfcoauLRY9kK3fsYkjlU93tJe4NEoVMpGM3yKhPGZ6vJrmmdfbGLHQmcCU8yP2sEo5sjaOyzzoHq_AbrMDiGni8exHFrNlGIjMKi4uw0jZuD7CD-bOYsg8k42V20w1W76FppIflxLADWr3_Mefbp52_SCCSaGAur4yqLMz4SG0vzls7YVKRyaexanuGQiSH72j-xlZORdmcGZBDTXaLZq3");'></div>
                                
                                <!-- Gradient Overlay -->
                                <div class="be-overlay"></div>
                                
                                <!-- Content Overlay -->
                                <div class="be-content">
                                    <div class="be-meta">
                                        <span class="be-badge">Featured</span>
                                        <span class="be-read-time">
                                            <span class="material-symbols-outlined" style="font-size: 16px;">schedule</span> 5 min read
                                        </span>
                                    </div>
                                    <h3 class="be-featured-title">
                                        The Future of Asynchronous Work in Creative Agencies
                                    </h3>
                                    <p class="be-desc">
                                        Discover how modern teams are reshaping productivity through asynchronous communication models and abandoning the 9-to-5 meeting marathon.
                                    </p>
                                    <div class="be-btn-wrap">
                                        <button class="be-btn-primary">
                                            <span>Read Full Story</span>
                                            <span class="material-symbols-outlined" style="font-size: 18px;">arrow_outward</span>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Sidebar List (Right, 1/3 width) -->
                        <div class="be-sidebar-col">
                            <!-- List Item 1 -->
                            <article class="be-article-item">
                                <div class="be-img-wrapper">
                                    <div class="be-img-bg" style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuDjuMIH0AiFJ1WIKYuaK6rP_wslZveNANojwQetFhxd0vZJF_wh6-uTPFJTPtnF7fO3c2AIkwVFb21S-jsr_7HzXyvwDfTvQ0zitrMwdXYIY1GTkuwfZokyIxhFvNLHcVs8M6uX_pZMuQueDTQWiqnJIdJ1Rso4R7JzYnwObNWnpZKbWVRRSk6cSM2yN-EPsyt60H4WlziPdAJwj4krvTrttYrdJkijHwUVqEeiEJUrI5mmLUXd5iwKI-0CVLdS0HWjbnwu3rOGh6N4");'></div>
                                </div>
                                <div class="be-article-content">
                                    <div class="be-article-meta">
                                        <span class="be-cat">Design</span>
                                        <span class="be-date">Oct 12, 2023</span>
                                    </div>
                                    <h4 class="be-article-title">
                                        Why Typography Matters More Than You Think
                                    </h4>
                                    <p class="be-article-desc">
                                        Typography is about more than just choosing a font; it defines the voice of your brand and shapes user perception.
                                    </p>
                                    <a class="be-read-more" href="#">
                                        Read article <span class="material-symbols-outlined" style="font-size: 16px;">chevron_right</span>
                                    </a>
                                </div>
                            </article>

                            <!-- List Item 2 -->
                            <article class="be-article-item">
                                <div class="be-img-wrapper">
                                    <div class="be-img-bg" style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuBKdJ7hm9jmgAAztGROqHEdmWY6Yd0yL0WOtIAIAFxZwFfpwx2qYClZqPrvYM5weJPxLbcHgB2S05I3Dkb0TtAUUeR9-W_luLRp82zx1eNVIamGuyzNLNN8--MQ1GS-oz4auuuit5fM678yNRp71Xpou4Gz5wZLGjG9GQPq2QAQvlKlLp57tkbtBkWB_7kZ_gnzuKaN4YNDFUUOK1nya2-D_5gU1fvWPVwIlRuG7z6GybfqTqXhM_vlRBdryHZeYuzYDvoN2DBegRN-");'></div>
                                </div>
                                <div class="be-article-content">
                                    <div class="be-article-meta">
                                        <span class="be-cat">Freelance</span>
                                        <span class="be-date">Sep 28, 2023</span>
                                    </div>
                                    <h4 class="be-article-title">
                                        5 Tools Every Freelancer Should Be Using
                                    </h4>
                                    <p class="be-article-desc">
                                        Maximize your efficiency with this curated list of essential software designed specifically for independent workers.
                                    </p>
                                    <a class="be-read-more" href="#">
                                        Read article <span class="material-symbols-outlined" style="font-size: 16px;">chevron_right</span>
                                    </a>
                                </div>
                            </article>
                        </div>
                    </div>
                </div>
            </section>
            <!-- blog section end -->"""

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the blog section
start_marker = '<!-- blog section start  -->'
# Note: In previous file View, the marker was <!-- blog section start  --> (with two spaces at end maybe, or one).
# Actually line 473: <!-- blog section start  -->
# And earlier logging showed it.

# Fallback search if exact string fails
start_idx = content.find(start_marker)
if start_idx == -1:
    start_marker = '<!-- blog section start -->' # try single space
    start_idx = content.find(start_marker)

end_marker = '<!-- blog section end  -->' # Try matching what we think it is
end_idx = content.find(end_marker)

# If end marker failing, search for next section or footer
if start_idx != -1:
    if end_idx == -1:
        # Check for footer start or just next section
        next_sec = content.find('<!-- footer', start_idx + 100)
        if next_sec != -1:
             # assume it ends before footer
             end_idx = next_sec
        else:
             # simple search for </section> after start
             end_idx = content.find('</section>', start_idx) + 10 # approximate
             # Better to find next comment
             
    if end_idx != -1:
        # We want to replace from start_marker to the end of the section closure.
        # But wait, if I use my new_blog_html, it includes the markers.
        # So I should cut OUT the old markers and content.
        
        # If end_idx implies specific position
        # Let's just find the closing tag corresponding to the section if possible, or just hack it by markers.
        # content[:start_idx] + new_blog_html + content[end_idx + len(end_marker):] ??
        
        # To be safe, let's use the exact range if markers found.
        # If I found '<!-- blog section end  -->', I can replace everything between.
        
        # Let's inspect content around end_idx to see if we consume the marker or not.
        # I will replace the defined block with my new block (which has its own markers).
        
        # If end_idx points to start of '<!-- blog section end  -->', then:
        replace_end = end_idx + len(end_marker)
        if content[end_idx:end_idx+4] != '<!--': 
             # If I found footer or something else, I should be careful not to delete it.
             replace_end = end_idx
             
        new_content = content[:start_idx] + new_blog_html + content[replace_end:]
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully replaced Blog section.")
    else:
        print("Could not find end of blog section.")
else:
    print("Could not find start of blog section.")
