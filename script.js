// Fetch the text file containing the URLs
fetch('https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/game.txt')
    .then(response => response.text())
    .then(data => {
        // Split the text into an array of URLs
        const urls = data.trim().split('\n');

        // Get the button container element
        const buttonContainer = document.getElementById('buttonContainer');

        // Create buttons for each URL
        urls.forEach(url => {
            // Extract the name from the URL and replace underscores with spaces
            const name = url.split('/').pop().replace(/_/g, ' ').replace(/\.(?:html?|php)$/i, '');

            const button = document.createElement('button');
            button.textContent = name;
            button.addEventListener('click', () => {
                window.open(url, '_blank');
            });
            buttonContainer.appendChild(button);
        });
    })
    .catch(error => {
        console.error('Failed to fetch URLs:', error);
    });
