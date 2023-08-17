document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-button');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const itemId = button.getAttribute('data-item-id');
            const confirmDelete = confirm('Are you sure you want to delete this Task?');

            if (confirmDelete) {
                // Redirect to the delete view or perform deletion logic here
                // For testing, let's just display a message in the console
                console.log(`Item with ID ${itemId} will be deleted.`);
            }
        });
    });
});
