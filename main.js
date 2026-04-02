// Initialize Lucide icons
lucide.createIcons();

// Smooth reveal animation on scroll
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

document.querySelectorAll('.reveal, .glass-card, .service-card').forEach(el => {
    // Check if already in viewport
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight) {
        el.classList.add('visible');
    }
    observer.observe(el);
});

// Force visibility fallback after 2 seconds (safeguard)
setTimeout(() => {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
}, 2000);

// Cursor Glow Effect
const cursorGlow = document.querySelector('.cursor-glow');
document.addEventListener('mousemove', (e) => {
    if (cursorGlow) {
        cursorGlow.style.left = e.clientX + 'px';
        cursorGlow.style.top = e.clientY + 'px';
    }
});

// Mobile Menu Toggle
const menuToggle = document.querySelector('.mobile-menu-toggle');
const navLinksContainer = document.querySelector('.nav-links');
const menuIcon = menuToggle ? menuToggle.querySelector('i') : null;

if (menuToggle && navLinksContainer) {
    menuToggle.addEventListener('click', () => {
        navLinksContainer.classList.toggle('nav-active');
        
        // Toggle icon
        if (menuIcon) {
            const isOpened = navLinksContainer.classList.contains('nav-active');
            menuIcon.setAttribute('data-lucide', isOpened ? 'x' : 'menu');
            lucide.createIcons();
        }
    });

    // Close menu when clicking a link
    navLinksContainer.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            navLinksContainer.classList.remove('nav-active');
            if (menuIcon) {
                menuIcon.setAttribute('data-lucide', 'menu');
                lucide.createIcons();
            }
        });
    });
}

// Parallax Watermarks & Header Scroll
window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;
    
    // Header
    const header = document.querySelector('header');
    if (header) {
        if (scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }

    // Watermark Parallax
    document.querySelectorAll('.watermark').forEach(el => {
        const speed = 0.1;
        el.style.transform = `translateY(${scrollY * speed}px)`;
    });
});

// Smooth scroll for nav links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            window.scrollTo({
                top: target.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });
});
// Expandable cards logic
document.querySelectorAll('.problem-item.expandable').forEach(card => {
    card.addEventListener('click', () => {
        const isActive = card.classList.contains('active');
        
        // Optional: Close other cards (uncomment if you want accordion style)
        /*
        document.querySelectorAll('.problem-item.expandable').forEach(other => {
            other.classList.remove('active');
        });
        */
        
        if (!isActive) {
            card.classList.add('active');
        } else {
            card.classList.remove('active');
        }
    });
});
