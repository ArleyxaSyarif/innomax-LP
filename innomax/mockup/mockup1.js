
// Mockup 1 JS

// Project Slider Initialization
$(document).ready(function () {
    if ($('.project-slider').length) {
        var projectSwiper = new Swiper('.project-slider', {
            slidesPerView: 3,
            spaceBetween: 30,
            loop: true,
            pagination: {
                el: '.project-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.project-next',
                prevEl: '.project-prev',
            },
            allowTouchMove: false, // Disables dragging/swiping. Only scrolls on click.
            breakpoints: {
                320: {
                    slidesPerView: 1,
                    spaceBetween: 20
                },
                768: {
                    slidesPerView: 2,
                    spaceBetween: 30
                },
                1024: {
                    slidesPerView: 3,
                    spaceBetween: 30
                }
            }
        });
    }
});
