document.addEventListener('DOMContentLoaded', () => {
    let points = 0;
    let pointsPerClick = 1;
    const pointsDisplay = document.getElementById('points');
    const clickButton = document.getElementById('clickButton');
    const upgradesDiv = document.getElementById('upgrades');

    // Fetch initial game state from the server
    fetch('/game-state')
        .then(response => response.json())
        .then(data => {
            points = data.points;
            pointsPerClick = data.pointsPerClick;
            renderUpgrades(data.upgrades);
            updatePointsDisplay();
        });

    // Update points display
    function updatePointsDisplay() {
        pointsDisplay.textContent = points;
    }

    // Handle click button
    clickButton.addEventListener('click', () => {
        points += pointsPerClick;
        updatePointsDisplay();
    });

    // Render upgrades
    function renderUpgrades(upgrades) {
        upgradesDiv.innerHTML = '';
        upgrades.forEach(upgrade => {
            const upgradeButton = document.createElement('button');
            upgradeButton.textContent = `${upgrade.name} (Cost: ${upgrade.cost})`;
            upgradeButton.addEventListener('click', () => purchaseUpgrade(upgrade));
            upgradesDiv.appendChild(upgradeButton);
        });
    }

    // Handle purchasing upgrades
    function purchaseUpgrade(upgrade) {
        if (points >= upgrade.cost) {
            points -= upgrade.cost;
            pointsPerClick *= upgrade.multiplier;
            updatePointsDisplay();
        } else {
            alert('Not enough points!');
        }
    }
});
