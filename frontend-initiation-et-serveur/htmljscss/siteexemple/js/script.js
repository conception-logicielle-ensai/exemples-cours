// Attendre que le DOM soit complètement chargé
document.addEventListener('DOMContentLoaded', function() {
    
    // Bouton retour
    const btnRetour = document.getElementById('btnRetour');
    if (btnRetour) {
        btnRetour.addEventListener('click', function() {
            window.history.back();
        });
    }

    // Gestion du formulaire
    const formulaire = document.getElementById('monFormulaire');
    if (formulaire) {
        formulaire.addEventListener('submit', function(event) {
            event.preventDefault(); // Empêche le rechargement de la page
            
            const nom = document.getElementById('inputNom').value;
            const age = document.getElementById('inputAge').value;
            
            if (nom && age) {
                alert(`Formulaire soumis !\nNom : ${nom}\nÂge : ${age}`);
                // Réinitialiser le formulaire
                formulaire.reset();
            } else {
                alert('Veuillez remplir tous les champs');
            }
        });
    }

    // Animation au scroll pour les sections
    const sections = document.querySelectorAll('section');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observerCallback = function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '0';
                entry.target.style.transform = 'translateY(20px)';
                
                setTimeout(() => {
                    entry.target.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, 100);
            }
        });
    };

    const observer = new IntersectionObserver(observerCallback, observerOptions);
    
    sections.forEach(section => {
        observer.observe(section);
    });

    // Smooth scroll pour les liens de navigation
    const navLinks = document.querySelectorAll('nav a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Log de bienvenue dans la console
    console.log('✅ JavaScript chargé avec succès !');
    console.log('📄 Page : Exemple de balises HTML');
    console.log('🎓 © Conception Logicielle ENSAI');
});