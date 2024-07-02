document.addEventListener('DOMContentLoaded', () => {
    const menuItems = document.querySelectorAll('.menu-item');
    menuItems.forEach(item => {
        item.addEventListener('click', () => {
            // Remove active class from all items
            menuItems.forEach(el => el.classList.remove('active'));
            // Add active class to clicked item
            item.classList.add('active');
            // Update main content based on the selected menu item
            const headerTitle = document.querySelector('.header h1');
            headerTitle.textContent = item.textContent;
            // Add your own logic to update the content area based on the selected menu item
        });
    });

    const submenus = document.querySelectorAll('.submenu');
    submenus.forEach(submenu => {
        submenu.addEventListener('click', (event) => {
            event.stopPropagation(); // Prevent parent menu item click event
            submenu.classList.toggle('active');
        });
    });
});




function updateGroup() {
    var selectedGroup = document.getElementById("group-select").value;
    var url = new URL(window.location.href);
    url.searchParams.set('group', selectedGroup);
    window.location.href = url.toString();
    console.log("hello world")
}

function enviarSolicitacao(nome) {
    // Implemente a lógica para enviar a solicitação com o nome do integrante
    console.log('Solicitação enviada para: ' + nome);
    // Aqui você pode enviar uma requisição AJAX para o backend, por exemplo
}

function updateRole() {
    var userRole = document.getElementById('user-role').value;
    var adminItems = document.querySelectorAll('.admin-only');
    
    if (userRole === 'Integrante') {
        adminItems.forEach(function(item) {
            item.style.display = 'none';
        });
    } else {
        adminItems.forEach(function(item) {
            item.style.display = 'block';
        });
    }
}

// Inicializa a visibilidade com base no papel selecionado ao carregar a página
document.addEventListener('DOMContentLoaded', function() {
    updateRole();
});