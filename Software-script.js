// Fetch the text file containing the URLs
fetch('https://raw.githubusercontent.com/HttpAnimation/SteamFree/main/software.api')
    .then(response => response.text())
    .then(data => {
        // Split the text into an array of URLs
        const urls = data.trim().split('\n');

        // Get the button container element
        const buttonContainer = document.getElementById('buttonContainer');

        // Create buttons for each URL
        urls.forEach(url => {
            const button = document.createElement('button');
            button.textContent = url;
            button.addEventListener('click', () => {
                window.open(url, '_blank');
            });
            buttonContainer.appendChild(button);
        });
    })
    .catch(error => {
        console.error('Failed to fetch URLs:', error);
    });
