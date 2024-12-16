// Generate Summary
function generateSummary() {
    const inputText = document.getElementById('input-text').value;
    const summaryType = document.querySelector('input[name="summary-type"]:checked');
    const summarySize = summarySizeSlider.value;
    const summaryOutput = document.getElementById('summary-output');

    if (!inputText) {
        alert('Please enter text to summarize');
        return;
    }

    if (!summaryType) {
        alert('Please select a summary type');
        return;
    }

    // Simulated summary generation
    const words = inputText.split(' ');
    const summaryLength = Math.floor(words.length * (summarySize / 100));
    const summary = words.slice(0, summaryLength).join(' ') + '...';
    
    summaryOutput.textContent = summary;
}