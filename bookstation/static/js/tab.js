const tabLinks = document.querySelectorAll('.tab-link');
const contents = document.querySelectorAll('.content');

  tabLinks.forEach(link => {
    link.addEventListener('click', () => {
      tabLinks.forEach(btn => btn.classList.remove('active'));
      link.classList.add('active');

      contents.forEach(content => content.classList.remove('active'));
      document.getElementById(link.dataset.tab).classList.add('active');
    });
  });
  
  
  

  const deleteButtons = document.querySelectorAll('.delete');
  deleteButtons.forEach(btn => {
    btn.addEventListener('click', (event) => {
      event.target.closest('tr').remove();
    });
  });