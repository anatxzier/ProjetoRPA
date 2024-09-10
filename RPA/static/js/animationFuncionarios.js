document.querySelector('.user-header').addEventListener('click', toggleDetails);

function toggleDetails() {
    const details = document.getElementById('user-details');
    details.style.display = details.style.display === 'none' || details.style.display === '' ? 'block' : 'none';
}
