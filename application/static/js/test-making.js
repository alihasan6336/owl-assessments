let optionCount = 1;

document.addEventListener('DOMContentLoaded', function() {
    // Set up event listeners
    const questionTypeSelect = document.getElementById("question-type");
    if (questionTypeSelect) {
        questionTypeSelect.addEventListener('change', toggleQuestionType);
    }

    // Ensure the initial display state is correct // here
    toggleQuestionType();

    // // Add event listener for form submission // here
    // const form = document.querySelector("form");
    // if (form) {
    //     form.addEventListener('submit', getCorrectMCQOption);
    // }
});

function toggleQuestionType() {
    const questionType = document.getElementById("question-type").value;
    const mcqSection = document.getElementById("mcq-section");

    const mcqInputs = mcqSection.querySelectorAll('textarea');

    if (questionType === "mcq") {
        mcqSection.style.display = "block";
        mcqInputs.forEach(input => {
            input.setAttribute('required', 'true');
        });

    } else if (questionType === "esa") {
        mcqSection.style.display = "none";

        mcqInputs.forEach(input => {
            input.removeAttribute('required');
        });

    } else {
        mcqSection.style.display = "none";

        mcqInputs.forEach(input => {
            input.removeAttribute('required');
        });
    }
}

function addOption() {
    optionCount++;
    const mcqOptions = document.getElementById("mcq-options");

    const newOptionDiv = document.getElementById('option-template-1').cloneNode(true);
    console.log(newOptionDiv);
    newOptionDiv.id = `option-template-${optionCount}`;
    newOptionDiv.querySelector('label').innerText = `Option ${optionCount}`;
    newOptionDiv.querySelector('label').setAttribute('for', `option-${optionCount}`);

    newOptionDiv.querySelector('textarea').setAttribute('id', `option-${optionCount}`);
    mcqOptions.appendChild(newOptionDiv);
}

function removeOption() {
    if (optionCount > 1) {
        const mcqOptions = document.getElementById("mcq-options");
        mcqOptions.removeChild(mcqOptions.lastElementChild);
        optionCount--;
    } else {
        alert('At least 1 options are required.');
    }
}

