document.addEventListener('DOMContentLoaded', function() {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // Back to top button
    const backToTop = document.getElementById('back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTop.style.display = 'flex';
            } else {
                backToTop.style.display = 'none';
            }
        });
        backToTop.addEventListener('click', function() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Auto dismiss flash messages
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Stats counter animation
    const counters = document.querySelectorAll('.counter');
    const speed = 200;

    const animateCounters = () => {
        counters.forEach(counter => {
            const updateCount = () => {
                const target = +counter.getAttribute('data-target');
                const count = +counter.innerText;
                const inc = target / speed;

                if (count < target) {
                    counter.innerText = Math.ceil(count + inc);
                    setTimeout(updateCount, 1);
                } else {
                    counter.innerText = target;
                }
            };
            updateCount();
        });
    }

    // Intersection Observer for counters
    if (counters.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                animateCounters();
                observer.disconnect();
            }
        });
        observer.observe(counters[0]);
    }

    // Intersection Observer for Fade-In animations
    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                fadeObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.fade-in-section').forEach(el => {
        fadeObserver.observe(el);
    });

    // SPA Navigation Logic
    const links = document.querySelectorAll('a.spa-link');
    const loader = document.getElementById('spa-loader');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const url = this.getAttribute('href');
            
            if (loader) loader.style.transform = 'scaleX(1)';
            
            fetch(url)
                .then(response => response.text())
                .then(html => {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(html, 'text/html');
                    
                    // Replace main content
                    const newContent = doc.querySelector('main');
                    const oldContent = document.querySelector('main');
                    if(newContent && oldContent) {
                        oldContent.innerHTML = newContent.innerHTML;
                        
                        // Re-initialize animations for new content
                        document.querySelectorAll('main .fade-in-section').forEach(el => {
                            fadeObserver.observe(el);
                        });
                        if(typeof feather !== 'undefined') feather.replace();
                    }
                    
                    // Update title
                    document.title = doc.title;
                    
                    // Push state
                    history.pushState(null, doc.title, url);
                    
                    if (loader) loader.style.transform = 'scaleX(0)';
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                })
                .catch(err => {
                    console.error('Failed to fetch page: ', err);
                    window.location.href = url; // Fallback
                });
        });
    });
});

// Admin Sidebar Toggle
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const content = document.getElementById('content');
    if (window.innerWidth > 768) {
        sidebar.classList.toggle('collapsed');
        content.classList.toggle('expanded');
    } else {
        sidebar.classList.toggle('show');
    }
}
