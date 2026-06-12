class AudioPlayerManager {
    constructor() {
        this.players = [];
        this.init();
    }

    init() {
        this.players = Array.from(document.querySelectorAll('audio'));
        this.setupEventListeners();
    }

    setupEventListeners() {
        this.players.forEach(player => {
            player.addEventListener('play', () => this.pauseOtherPlayers(player));
        });
    }

    pauseOtherPlayers(currentPlayer) {
        this.players.forEach(player => {
            if (player !== currentPlayer && !player.paused) {
                player.pause();
            }
        });
    }
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
    new AudioPlayerManager();
});