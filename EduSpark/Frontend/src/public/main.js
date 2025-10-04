// This is a simple JavaScript file.
// It can handle user interactions, form submissions, and dynamic content updates.

// A function to handle the "Get Started" button click
function handleGetStartedClick() {
    console.log("Get Started button was clicked!");
    // You could add more complex logic here, like redirecting to a login page.
    window.location.href = "login.html"; // Example of a redirect
}

// Attach the function to the button.
// This is a more robust way than using inline `onclick` in HTML.
document.addEventListener('DOMContentLoaded', () => {
    const getStartedButton = document.querySelector('button');
    if (getStartedButton) {
        getStartedButton.addEventListener('click', handleGetStartedClick);
    }
});