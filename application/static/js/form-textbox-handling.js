document.addEventListener("DOMContentLoaded", function() {
  const inputs = document.querySelectorAll(".form-control");
  
  inputs.forEach(input => {
      const label = input.nextElementSibling;
      
      input.addEventListener("input", function() {
          if (this.value.trim() !== "") {
              label.classList.add("active");
          } else {
              label.classList.remove("active");
          }
      });
  });
});