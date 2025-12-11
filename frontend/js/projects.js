const selectors = [
    '.bottom-bar-image',
    '.image-desc-1'
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

let ticking = false;

function checkScroll() {
    if (!ticking) {
        window.requestAnimationFrame(() => {
            elements.forEach(el => {
                if (el.getBoundingClientRect().top < window.innerHeight - 100) {
                    el.style.opacity = '1';
                    el.style.transform = 'translateY(0)';
                }
            });
            ticking = false;
        });
        ticking = true;
    }
}

window.onbeforeunload = function() {
    window.scrollTo(0, 0);
};