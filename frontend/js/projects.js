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


// Proje verilerini backend'den çekme
document.addEventListener('DOMContentLoaded', async () => {
    //URL'den proje ID'sini alma
    const urlParams = new URLSearchParams(window.location.search);
    const projectId = urlParams.get('id');
    
    if (projectId) {
        try {
            const response = await fetch(`/api/projects/${projectId}`);

            if (!response.ok) {
                throw new Error('Proje verisi bulunamadı.');
            }

            const project = await response.json();

            //Proje bilgilerini sayfaya yerleştirme
            updateProjectContent(project);
        } catch (error) {
            console.error('Hata:', error);
            alert('Proje verisi yüklenirken bir hata oluştu.');
        }
    }
});

function updateProjectContent(project) {
    const titleElement = document.querySelector('.image-desc-1 h3');
    if (titleElement) {
        titleElement.textContent = project.title;
    }
    
    const desc1Element = document.querySelector('.image-desc-1 p');
    if (desc1Element) {
        desc1Element.textContent = project.description;  // 'description1' değil 'description'
    }
    
    const desc2Elements = document.querySelectorAll('.image-desc-1 p');
    if (desc2Elements.length > 1) {
        desc2Elements[1].textContent = project.description2;
    }
    
    const imageElement = document.querySelector('.bottom-bar-image img');
    if (imageElement) {
        imageElement.src = project.image_url;
        imageElement.alt = project.title;
    }
}