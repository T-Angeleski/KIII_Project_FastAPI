async function fetchGames() {
    const response = await fetch('/games');
    const games = await response.json();

    const contentDiv = document.getElementById('content');
    contentDiv.innerHTML = '';


    games.forEach(game => {
        const cardDiv = document.createElement('div');
        cardDiv.classList.add('game-card');

        const title = document.createElement('h3');
        title.textContent = game.name;

        const platform = document.createElement('p');
        platform.textContent = `Platform: ${game.platform}`;

        const price = document.createElement('p');
        price.textContent = `Price: $${game.price}`;

        const genre = document.createElement('p');
        genre.textContent = `Genre: ${game.genre}`;

        const description = document.createElement('p');
        description.textContent = `Description: ${game.description}`;

        const imageLink = document.createElement('img');
        imageLink.src = game.image_url
        imageLink.alt = game.name


        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', async () => {
            await deleteGame(game.id);
            fetchGames();
        })

        const editButton = document.createElement('button');
        editButton.textContent = 'Edit';
        editButton.classList.add('edit-button');
        editButton.addEventListener('click', () => {
            window.location.href = `/static/create_game.html?id=${game.id}`;
        });

        cardDiv.appendChild(title);
        cardDiv.appendChild(imageLink);
        cardDiv.appendChild(platform);
        cardDiv.appendChild(price);
        cardDiv.appendChild(genre);
        cardDiv.appendChild(description);
        cardDiv.appendChild(deleteButton);
        cardDiv.appendChild(editButton);

        contentDiv.appendChild(cardDiv);

    });
}

async function deleteGame(gameId) {
    await fetch(`/games/${gameId}`, {method: 'DELETE'});
}

async function fetchGameById(gameId) {
    const resp = await fetch(`/games/${gameId}`);
    return resp.json();
}

async function handleFormSubmit(event) {
    event.preventDefault();

    const gameId = document.getElementById('gameId').value;
    const game = {
        name: document.getElementById('name').value,
        price: parseFloat(document.getElementById('price').value),
        platform: document.getElementById('platform').value,
        genre: document.getElementById('genre').value,
        description: document.getElementById('description').value,
        image_url: document.getElementById('image_url').value,
    }


    // Check if exists for edit or create
    if (gameId) {
        // Edit
        await fetch(`/games/${gameId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(game)
        });
    } else {
        await fetch('/create', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(game),
        });
    }

    window.location.href = '/';
}

document.addEventListener('DOMContentLoaded', () => {
    console.log("DOM loaded", window.location.pathname)
    if (window.location.pathname === '/') {
        fetchGames();
    } else if (window.location.pathname === '/static/create_game.html') {
        const urlParams = new URLSearchParams(window.location.search);
        const gameId = urlParams.get('id');
        console.log(gameId)
        if (gameId) {
            fetchGameById(gameId).then(game => {
                document.getElementById('gameId').value = game.id;
                document.getElementById('name').value = game.name;
                document.getElementById('price').value = game.price;
                document.getElementById('platform').value = game.platform;
                document.getElementById('genre').value = game.genre;
                document.getElementById('description').value = game.description;
                document.getElementById('image_url').value = game.image_url;
            });
        }

        const form = document.getElementById('gameForm');
        form.addEventListener('submit', handleFormSubmit);
        form.classList.add('game-form');
    }
});