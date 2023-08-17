document.addEventListener('DOMContentLoaded', function() {
    const addTaskLink = document.getElementById('addTaskLink');
    const addTaskForm = document.getElementById('addTaskForm');

    addTaskLink.addEventListener('click', function(event) {
        event.preventDefault();
        addTaskForm.style.display = 'block';
    });
});

// delete_confirmation.js
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-button');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const itemId = button.getAttribute('data-item-id');
            const confirmDelete = confirm('Are you sure you want to delete this item?');

            if (confirmDelete) {
                // Redirect to the delete view
                window.location.href = `/delete/${itemId}/`; // Update the URL as needed
            }
        });
    });
});


