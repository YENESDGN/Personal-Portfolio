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
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

animatedElements.forEach(element => {
    if (element) observer.observe(element);
});

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

if ('scrollRestoration' in history) {
    history.scrollRestoration = 'manual';
}

window.addEventListener('beforeunload', () => {
    window.scrollTo(0, 0);
});

// Global değişken - project verilerini sakla
let currentProject = null;

// Dil değiştirme fonksiyonları
function updateProjectLanguage(language) {
    if (!currentProject) return;
    
    const desc1Element = document.querySelector('.image-desc');
    const desc2Element = document.querySelector('.image-desc-1');
    
    if (desc1Element) {
        if (language === 'en' && currentProject.description_en) {
            desc1Element.textContent = currentProject.description_en;
        } else {
            desc1Element.textContent = currentProject.description;
        }
    }
    
    if (desc2Element) {
        if (language === 'en' && currentProject.description2_en) {
            desc2Element.textContent = currentProject.description2_en;
        } else {
            desc2Element.textContent = currentProject.description2;
        }
    }
    
    // Başlık ve "Geri Dön" butonunu güncelle
    updatePageText(language);
}

function updatePageText(language) {
    const goBackButton = document.querySelector('.go-back p');
    if (goBackButton) {
        goBackButton.textContent = language === 'en' ? 'Go Back' : 'Geri Dön';
    }
    
    const githubLinkText = document.querySelector('.github-link p');
    if (githubLinkText) {
        githubLinkText.textContent = language === 'en' ? 'View on GitHub' : 'GitHub\'da Görüntüle';
    }
}

// Dil seçimini dinle ve sayfayı güncelle
function listenToLanguageChanges() {
    // LocalStorage'u düzenli olarak kontrol et
    const checkLanguage = setInterval(() => {
        const savedLanguage = localStorage.getItem('selectedLanguage') || 'tr';
        const currentLangAttr = document.documentElement.getAttribute('data-language') || 'tr';
        
        if (savedLanguage !== currentLangAttr) {
            document.documentElement.setAttribute('data-language', savedLanguage);
            updateProjectLanguage(savedLanguage);
        }
    }, 500);
}

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
        
        // Proje verilerini sakla
        currentProject = project;
        
        // Başlığı ayarla
        document.title = project.title + ' - Portföy';
        document.documentElement.setAttribute('lang', 'tr');
        
        // Mevcut dili al
        const currentLanguage = localStorage.getItem('selectedLanguage') || 'tr';
        
        // Description 1
        const desc1Element = document.querySelector('.image-desc');
        if (desc1Element) {
            if (currentLanguage === 'en' && project.description_en) {
                desc1Element.textContent = project.description_en;
            } else {
                desc1Element.textContent = project.description;
            }
        }
        
        // Description 2
        const desc2Element = document.querySelector('.image-desc-1');
        if (desc2Element) {
            if (currentLanguage === 'en' && project.description2_en) {
                desc2Element.textContent = project.description2_en;
            } else {
                desc2Element.textContent = project.description2;
            }
        }
        
        // Image 1
        const image1Element = document.querySelector('.top-bar-image img');
        if (image1Element) {
            image1Element.src = project.image_url;
            image1Element.alt = project.title;
        }
        
        // Image 2
        const image2Element = document.querySelector('.bottom-bar-image img');
        if (image2Element) {
            image2Element.src = project.image_url2;
            image2Element.alt = project.title;
        }
        
        // GitHub Link
        const githubLinkElement = document.querySelectorAll('.github-link a, .toGitHub-content a');
        githubLinkElement.forEach(link => {
            if (link) {
                link.href = project.github_url;
                link.target = '_blank';
            }
        });
        
        // Sayfa metnini güncelle
        updatePageText(currentLanguage);
        
        // Dil değişikliklerini dinle
        listenToLanguageChanges();

    } catch (error) {
        console.error('Proje detayları yüklenemedi:', error);
    }
});