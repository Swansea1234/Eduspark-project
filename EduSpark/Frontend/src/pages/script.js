// A. Event Handling for Buttons and Links
// This section handles clicks on the two main interactive buttons.

// 1. Color Changer Button
// Get the button and the section it will affect.
const colorChangeBtn = document.getElementById('color-change-btn');
const colorChangerSection = document.getElementById('color-changer-section');

// Array of colors for the background.
const colors = ['#f8c5c5', '#c5f8e0', '#c5d8f8', '#f8f1c5', '#e0c5f8'];

// Add a click event listener to the button.
colorChangeBtn.addEventListener('click', () => {
    // Generate a random index to pick a color from the array.
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    // Change the background color of the section.
    colorChangerSection.style.backgroundColor = randomColor;
});

// 2. Content Toggle Button
// Get the button and the hidden content div.
const toggleContentBtn = document.getElementById('toggle-content-btn');
const hiddenContent = document.getElementById('hidden-content');

// Add a click event listener to the button.
toggleContentBtn.addEventListener('click', () => {
    // Toggle the 'hidden' class on the content div.
    // This will show or hide the content based on the CSS class.
    hiddenContent.classList.toggle('hidden');
    // Change the button text based on the state.
    if (hiddenContent.classList.contains('hidden')) {
        toggleContentBtn.textContent = 'Show Message';
    } else {
        toggleContentBtn.textContent = 'Hide Message';
    }
});

// B. Custom Form Validation
// This section handles the form submission and provides custom validation.

// Get the form and all its input fields.
const contactForm = document.getElementById('contact-form');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const messageInput = document.getElementById('message');

// Add a submit event listener to the form.
contactForm.addEventListener('submit', (event) => {
    // Prevent the default form submission behavior.
    event.preventDefault();

    // Call the custom validation function.
    if (validateForm()) {
        // If the form is valid, you can process the data here.
        alert('Form submitted successfully!');
        // Reset the form after successful submission.
        contactForm.reset();
    }
});

// The custom validation function.
function validateForm() {
    let isValid = true;
    
    // Clear previous error messages.
    clearErrors();

    // 1. Validate the Name field.
    if (nameInput.value.trim() === '') {
        showError('name-error', 'Name is required.');
        isValid = false;
    }

    // 2. Validate the Email field.
    if (emailInput.value.trim() === '') {
        showError('email-error', 'Email is required.');
        isValid = false;
    } else if (!isValidEmail(emailInput.value.trim())) {
        showError('email-error', 'Please enter a valid email address.');
        isValid = false;
    }

    // 3. Validate the Message field.
    if (messageInput.value.trim() === '') {
        showError('message-error', 'Message is required.');
        isValid = false;
    }

    return isValid;
}

// Helper function to display error messages.
function showError(elementId, message) {
    const errorElement = document.getElementById(elementId);
    errorElement.textContent = message;
}

// Helper function to clear all error messages.
function clearErrors() {
    document.querySelectorAll('.error-message').forEach(element => {
        element.textContent = '';
    });
}

// Helper function to validate email format using a simple regex.
function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}