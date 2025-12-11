// Tüm sosyal medya linklerini nesne olarak tanımla
const socialLinks = {
    'side-image-2': 'https://www.linkedin.com/in/ya%C4%9F%C4%B1z-enes-do%C4%9Fan-1b0731295/',
    'side-image-3': 'https://github.com/YENESDGN',
    'side-image-4': 'https://www.instagram.com/yagizz_eness?igsh=MTQybTM5ZGhkaTQ4aA%3D%3D&utm_source=qr',
    'side-image-5': 'mailto:yenesdogan@outlook.com.tr'
};

// Event delegation - tek listener
document.querySelector('.side-images').addEventListener('click', (e) => {
    const clickedClass = Array.from(e.target.classList).find(cls => cls.startsWith('side-image-'));
    
    if (clickedClass && socialLinks[clickedClass]) {
        const url = socialLinks[clickedClass];
        
        if (url.startsWith('mailto:')) {
            window.location.href = url;
        } else {
            window.open(url, '_blank', 'noopener,noreferrer');
        }
    }
});

const selectors = [
    '.welcome-text',
    '.images_description',
    '.tech-images', 
    '.about_me',
    '.about-me-content-grid',
    '.projects-section',
    '.projects-grid',
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