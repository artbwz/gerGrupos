
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

function updateRole() {
    const role = document.getElementById('user-role').value;
    console.log(`Role selected: ${role}`);
    // Update the content or menu based on the selected role if needed
}



function enviarSolicitacao(nome) {
    // Implemente a lógica para enviar a solicitação com o nome do integrante
    console.log('Solicitação enviada para: ' + nome);
    // Aqui você pode enviar uma requisição AJAX para o backend, por exemplo
}

function updateGroup() {
    var selectedGroup = document.getElementById("group-select").value;
    var url = new URL(window.location.href);
    url.searchParams.set('group', selectedGroup);
    window.location.href = url.toString();
    console.log("hello world")
}