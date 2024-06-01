document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("qualityForm");

    // Load saved values from local storage
    Array.from(form.elements).forEach(element => {
        if (element.type === "checkbox") {
            element.checked = localStorage.getItem(element.id) === "true";
        } else if (element.type === "range" || element.type === "select-one" || element.tagName.toLowerCase() === "textarea") {
            element.value = localStorage.getItem(element.id) || element.value;
            if (element.type === "range") {
                updateValue(element.id + '-value', element.value); // Update the display for range inputs
            }
        }
    });

    // Save form values to local storage on change
    form.addEventListener("input", (event) => {
        const element = event.target;
        if (element.type === "checkbox") {
            localStorage.setItem(element.id, element.checked);
        } else {
            localStorage.setItem(element.id, element.value);
        }
    });
});

function updateValue(id, value) {
    document.getElementById(id).innerText = value;
}

function submitForm() {
    const form = document.getElementById('qualityForm');
    const formData = new FormData(form);
    const selectedOptions = Array.from(document.querySelectorAll('input[id="positive"]:checked'))
    
    .map(option => option.value)
    .concat(document.querySelector('textarea#positive').value)
    .join(', ');
    const negativeElements = document.querySelectorAll('input[name="negetive"]:checked');
    const negatives = Array.from(negativeElements).map(el => el.value).join(", ")
    .concat(document.querySelector('textarea#negetive').value);
    console.log(negatives);

 

    const data = {
        prompt: selectedOptions,
        negetive: negatives,
        cfg: formData.get('cfg'),
        steps: formData.get('steps'),
        batch: formData.get('batch'),
        aspect: formData.get('aspect')
    };

    const spinner = document.getElementById('loading-spinner');
    const imageContainer = document.getElementById('image-container');
    imageContainer.innerHTML = ''; // Clear previous images
    spinner.style.display = 'block'; // Show loading spinner

    fetch(form.action, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log('Success:', result);
        displayImages(result);
        spinner.style.display = 'none'; // Hide loading spinner
    })
    .catch(error => {
        console.error('Error:', error);
        spinner.style.display = 'none'; // Hide loading spinner
    });
}
function displayImages(urls) {
    const imageContainer = document.getElementById('image-container');
    imageContainer.innerHTML = ''; // Clear previous images
    urls.forEach(url => {
        const img = document.createElement('img');
        img.src = url;
        imageContainer.appendChild(img);
    });
}
function toggleTextAreas() {
    const advancedOptions = document.getElementById('advanced-options');
    if (document.getElementById('advanced').checked) {
        advancedOptions.style.display = 'block';
    } else {
        advancedOptions.style.display = 'none';
    }
}