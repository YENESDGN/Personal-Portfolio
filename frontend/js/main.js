document.querySelector('.footer-image-4').addEventListener('click', function() {
    window.open('https://instagram.com/yourpage', '_blank');
});

document.querySelector('.footer-image-2').addEventListener('click', function() {
    window.open('https://www.linkedin.com/in/ya%C4%9F%C4%B1z-enes-do%C4%9Fan-1b0731295/', '_blank');
});

document.querySelector('.footer-image-3').addEventListener('click', function() {
    window.open('https://github.com/YENESDGN', '_blank');
});


// İstediğin elementleri seç
// Animasyon istediğin elementleri buraya yaz
const selectors = [
    '.welcome-text',
    '.images_description',
    '.tech-images', 
    '.about_me',
    '.about-me-content-grid',
    '.projects-section',
    '.projects-grid',
    '.deco-block-1',
    '.deco-block-2',
];

const elements = document.querySelectorAll(selectors.join(', '));

elements.forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(50px)';
    el.style.transition = 'all 0.8s ease';
});

function checkScroll() {
    elements.forEach(el => {
        if (el.getBoundingClientRect().top < window.innerHeight - 100) {
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }
    });
}

window.addEventListener('scroll', checkScroll);
window.addEventListener('load', checkScroll);