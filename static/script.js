const themeButton = document.getElementById('theme-button');
let isDarkMode = false;

themeButton.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    document.body.classList.toggle('light-theme');
    isDarkMode = !isDarkMode;
    
    // Mettre à jour l'icône en fonction du thème actuel
    themeButton.innerHTML = isDarkMode 
        ? '<i class="fas fa-moon"></i>' 
        : '<i class="fas fa-sun"></i>';
});

// Initialisation au démarrage
themeButton.innerHTML = '<i class="fas fa-sun"></i>';
