// File Upload Handler
function handleFileUpload(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('input-text').value = e.target.result;
        };
        reader.readAsText(file);
    }
}

// Summary Size Slider
const summarySizeSlider = document.getElementById('summary-size');
const summarySizeDisplay = document.getElementById('summary-size-display');

summarySizeSlider.addEventListener('input', function() {
    summarySizeDisplay.textContent = `${this.value}%`;
});