function updateValue(id, value) {
    document.getElementById(id).innerText = value;
}

function submitForm() {
    const form = document.getElementById('qualityForm');
    const formData = new FormData(form);
    const selectedOptions = Array.from(document.querySelectorAll('input[name="option"]:checked'))
                               .map(option => option.value).join(', ');

    const data = {
        prompt: selectedOptions,
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