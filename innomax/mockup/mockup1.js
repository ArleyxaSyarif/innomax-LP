
/* --- Enhanced Smooth Accordion Logic --- */
function toggleFaq(button) {
    const item = button.parentElement;
    const content = item.querySelector('.faq-answer');
    const allItems = document.querySelectorAll('.faq-item');
    
    // Close all other items
    allItems.forEach(otherItem => {
        if (otherItem !== item) {
            otherItem.classList.remove('active');
            const otherContent = otherItem.querySelector('.faq-answer');
            if (otherContent) otherContent.style.maxHeight = null;
        }
    });
    
    // Toggle current
    item.classList.toggle('active');
    
    if (item.classList.contains('active')) {
        content.style.maxHeight = content.scrollHeight + 'px';
    } else {
        content.style.maxHeight = null;
    }
}
