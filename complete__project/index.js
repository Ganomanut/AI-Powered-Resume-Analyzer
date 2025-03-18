
function toggleMenu() {
    const sidebar = document.querySelector('.sidebar');
    const container = document.querySelector('.container');
    const hamburger = document.querySelector('.hamburger-menu');
    
    hamburger.classList.toggle('active'); // Toggle the hamburger icon to X
    sidebar.classList.toggle('active');
    container.style.marginLeft = sidebar.classList.contains('active') ? '0' : '250px';
}