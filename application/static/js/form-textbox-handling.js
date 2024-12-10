document.addEventListener("DOMContentLoaded", function() {
    const inputs = document.querySelectorAll(".form-control");
    
    function handleInputChange(event) {
        const input = event.target.value;
        const label = event.target.nextElementSibling;
        
        if (input.trim() !== "") {
            label.classList.add("active");
        } else {
            label.classList.remove("active");
        }
    }

    inputs.forEach(input => {
        handleInputChange({ target: input });
        input.addEventListener("input", handleInputChange);
    });
});