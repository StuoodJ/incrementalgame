// server.js
const express = require('express');
const app = express();
const path = require('path');

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Endpoint to get initial game state
app.get('/game-state', (req, res) => {
    const initialState = {
        points: 0,
        pointsPerClick: 1,
        upgrades: [
            { id: 1, name: 'Double Points', cost: 10, multiplier: 2 },
            { id: 2, name: 'Triple Points', cost: 50, multiplier: 3 }
        ]
    };
    res.json(initialState);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
