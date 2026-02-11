// Tüm sosyal medya linklerini nesne olarak tanımla
const socialLinks = {
    'side-image-2': 'https://www.linkedin.com/in/ya%C4%9F%C4%B1z-enes-do%C4%9Fan-1b0731295/',
    'side-image-3': 'https://github.com/YENESDGN',
    'side-image-4': 'https://www.instagram.com/yagizz_eness?igsh=MTQybTM5ZGhkaTQ4aA%3D%3D&utm_source=qr',
};

// Event delegation - tek listener
document.querySelector('.side-images').addEventListener('click', (event) => {
    const clickedClassId = Array.from(event.target.classList).find(cls => cls.startsWith('side-image-'));

    if (!clickedClassId) return;

    if (clickedClassId == 'side-image-5') {
        decryptAndOpenEmail();
    }

    else if (socialLinks[clickedClassId]) {
        window.open(socialLinks[clickedClassId], '_blank', 'noopener,noreferrer');
    }
})

const decryptAndOpenEmail = () => {
    if(!window.serverData || !window.serverData.code) {
        console.error("Mail verisi bulunamadı.");
    }

    try {
        const encryptedStr = atob(window.serverData.code);
        
        let decryptedEmail = "";
        for (let i = 0; i < encryptedStr.length; i++) {
            decryptedEmail += String.fromCharCode(encryptedStr.charCodeAt(i) ^ window.serverData.key)
        };
        window.location.href = decryptedEmail;
    }
    catch (error) {
        console.error("Mail deşifreleme hatası:", error);
    }
}

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

let ticking = false;

function checkScroll() {
    if (!ticking) {
        window.requestAnimationFrame(() => {
            elements.forEach(el => {
                // Element ekrana girdiğinde 'reveal' sınıfını ekle
                if (el.getBoundingClientRect().top < window.innerHeight - 100) {
                    el.classList.add('reveal');
                }
            });
            ticking = false;
        });
        ticking = true;
    }
}

window.addEventListener('scroll', checkScroll);
window.addEventListener('load', checkScroll);

window.onbeforeunload = function() {
    window.scrollTo(0, 0);
};

//Backend Verileri Çekme ve Sayfaya Yerleştirme
document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('/api/projects/');
        const projects = await response.json();
        
        // Tüm proje kartlarını bul
        const projectCards = document.querySelectorAll('.project-card');
        
        // Her kart için backend'den gelen title'ı uygula
        projectCards.forEach((card, index) => {
            if (projects[index]) {
                const project = projects[index];
                
                // Sadece başlığı güncelle
                const h3 = card.querySelector('.card-info h3');
                if (h3) h3.textContent = project.title;
                
                // Tıklanınca detay sayfasına git
                card.onclick = () => window.location.href = `/projects?id=${project.id}`;
            }
        });
        
    } catch (error) {
        console.error('Projeler Title Yüklenemedi:', error);
    }
});

function updateProjectTitle(project) {
    const titleElement = document.querySelector('.card-info h3');
    if (titleElement) {
        titleElement.textContent = project.title;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const languageToggle = document.getElementById('language-toggle');
    
    let currentLanguage = localStorage.getItem('selectedLanguage') || 'tr';
    updateLanguageDisplay(currentLanguage);
    
    languageToggle.addEventListener('click', function() {
        currentLanguage = currentLanguage === 'tr' ? 'en' : 'tr';
        localStorage.setItem('selectedLanguage', currentLanguage);
        updateLanguageDisplay(currentLanguage);
    });
    
    function updateLanguageDisplay(language) {
        languageToggle.textContent = language.toUpperCase();
        languageToggle.setAttribute('data-lang', language);
        
        // Tüm `data-tr` ve `data-en` içerikleri güncelle
        updatePageContent(language);
    }
    
    function updatePageContent(language) {
        // Başlık
        updateElement('.about_me_title', language);
        updateElement('.about_me_context', language);
        updateElement('.images_description h3', language);
        updateElement('.card-info h3', language);
        
        // Nav linklerini güncelle
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            const text = link.getAttribute(`data-${language}`);
            if (text) link.textContent = text;
        });
    }
    
    function updateElement(selector, language) {
        const element = document.querySelector(selector);
        if (element) {
            const content = element.getAttribute(`data-${language}`);
            if (content) element.innerHTML = content;
        }
    }
});

window.addEventListener('load', function() {
    const currentLanguage = localStorage.getItem('selectedLanguage') || 'tr';
    // Gerekli yerlerde dili uygula
    document.documentElement.setAttribute('lang', currentLanguage);
});
