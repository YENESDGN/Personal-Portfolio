// Scroll animasyonu için elemanlar
const animatedElements = document.querySelectorAll('.bottom-bar-image, .image-desc-1, .toGitHub-content, .github-link');
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


document.addEventListener('DOMContentLoaded', async () => {
    console.log('projects.js yüklendi');
    
    try {
        const urlParams = new URLSearchParams(window.location.search);
        const projectId = urlParams.get('id');
        
        console.log('Proje ID:', projectId);
        
        if (!projectId) {
            console.error('Proje ID bulunamadı');
            return;
        }
        
        const response = await fetch(`/api/projects/${projectId}`);
        console.log('Response status:', response.status);
        
        if (!response.ok) throw new Error('Proje bulunamadı');
        
        const project = await response.json();
        console.log('Proje verisi:', project);
        
        // Description 1
        const desc1Element = document.querySelector('.image-desc');
        console.log('desc1Element:', desc1Element);
        if (desc1Element) {
            desc1Element.textContent = project.description;
        }
        
        // Description 2
        const desc2Element = document.querySelector('.image-desc-1');
        console.log('desc2Element:', desc2Element);
        if (desc2Element) {
            desc2Element.textContent = project.description2;
        }
        
        // Image 1
        const image1Element = document.querySelector('.top-bar-image img');
        console.log('image1Element:', image1Element);
        if (image1Element) {
            image1Element.src = project.image_url;
            image1Element.alt = project.title;
        }
        
        // Image 2
        const image2Element = document.querySelector('.bottom-bar-image img');
        console.log('image2Element:', image2Element);
        if (image2Element) {
            image2Element.src = project.image_url2;
            image2Element.alt = project.title;
        }
        
        //GitHub Link
        document.querySelectorAll('.github-link a, .toGitHub-content a').forEach(link => {
            if (project.github_url) {
                link.href = project.github_url;
            }
        });


    } catch (error) {
        console.error('Proje detayları yüklenemedi:', error);
    }
});