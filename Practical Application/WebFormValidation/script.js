document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission (So we can do additional checks here!)

    // This grabs all he details from the "input" tagged items on the webpage by their ids.
    // then it saves them to a constant variable.

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const dob = document.getElementById('dob').value;
    const password = document.getElementById('password').value; 
    // Password really *shouldnt* be parsed in plain text for security reasons
    // Should be atleast MD5 hashed but the task specifies it gets set to the next page

    // Store data in sessionStorage to pass to the next page (Different variable for each item)
    sessionStorage.setItem('userName', name);
    sessionStorage.setItem('userEmail', email);
    sessionStorage.setItem('userDob', dob);
    sessionStorage.setItem('userPassword', password);

    // Redirect to a new page to display details (This could be done through the submit in html)
    window.location.href = 'details.html';
});

// This is further date validation
// The goal is to not allow the user to set their date of birth to be a future date.
document.addEventListener('DOMContentLoaded', function() {
    // Gets the date today and converts it into different string formats (yyyy, mm, then dd)
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0');
    var yyyy = today.getFullYear()

    // Parses todays format into the "dob" input field (that has type of date).
    // and makes its max variable (setting the max selectable date) to be today :)
    var maxDate = yyyy + '-' + mm + '-' + dd;
    document.getElementById('dob').setAttribute('max', maxDate);
});