document.addEventListener('DOMContentLoaded', function () {
    // Get the current URL
    const currentUrl = window.location.href;

    // Check if the URL is the login page
    if (currentUrl.includes('/login/')) {
        // Toggle the login
        document.getElementById('chk').checked = true;
    }
});