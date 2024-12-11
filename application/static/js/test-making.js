let optionCount = 1;

document.addEventListener('DOMContentLoaded', function() {
    // Set up event listeners
    const questionTypeSelect = document.getElementById("question-type");
    if (questionTypeSelect) {
        questionTypeSelect.addEventListener('change', toggleQuestionType);
    }
    toggleQuestionType();
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


function toggleOtherTypeInput() {
    var testTypeSelect = document.getElementById('test-type');
    var otherTypeGroup = document.getElementById('other-type-group');
    if (testTypeSelect.value === 'other') {
        otherTypeGroup.style.display = 'block';
    } else {
        otherTypeGroup.style.display = 'none';
    }
}


$(document).ready(function() {
    $('#categories').select2({
        tags: true,
        tokenSeparators: [',', ' '],
        width: '100%'  // Ensure the select2 input takes the full width
    });
});