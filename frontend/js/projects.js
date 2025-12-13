// Scroll animasyonu için elemanlar
const animatedElements = document.querySelectorAll('.bottom-bar-image, .image-desc-1');
let ticking = false;

// Intersection Observer API kullanarak performanslı scroll animasyonu
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            // Bir kez görünür olduktan sonra gözlemlemeyi durdur
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Tüm animasyonlu elemanları gözlemle
animatedElements.forEach(element => {
    observer.observe(element);
});

// Fallback: Eski tarayıcılar için scroll event listener
if (!('IntersectionObserver' in window)) {
    function checkScroll() {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                animatedElements.forEach(el => {
                    const rect = el.getBoundingClientRect();
                    const isVisible = rect.top < window.innerHeight - 100;
                    
                    if (isVisible && !el.classList.contains('visible')) {
                        el.classList.add('visible');
                    }
                });
                ticking = false;
            });
            ticking = true;
        }
    }
    
    window.addEventListener('scroll', checkScroll, { passive: true });
    window.addEventListener('load', checkScroll);
}

// Sayfa yeniden yüklendiğinde en üste scroll
if ('scrollRestoration' in history) {
    history.scrollRestoration = 'manual';
}

window.addEventListener('beforeunload', () => {
    window.scrollTo(0, 0);
});