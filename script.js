// Get the fetch button element
const fetchButton = document.getElementById('fetchButton');

// Add click event listener to the fetch button
fetchButton.addEventListener('click', () => {
    // Fetch the text file containing the URLs
    fetch('https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/game.txt')
        .then(response => response.text())
        .then(data => {
            // Split the text into an array of URLs
            const urls = data.trim().split('\n');

            // Create buttons for each URL
            urls.forEach(url => {
                const button = document.createElement('button');
                button.textContent = url;
                button.addEventListener('click', () => {
                    window.open(url, '_blank');
                });
                document.body.appendChild(button);
            });
        })
        .catch(error => {
            console.error('Failed to fetch URLs:', error);
        });
});
