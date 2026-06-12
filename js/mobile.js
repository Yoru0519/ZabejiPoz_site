// Обработка касаний
document.addEventListener('DOMContentLoaded', () => {
    // Улучшенная обработка кликов для мобильных
    const buttons = document.querySelectorAll('button, a.btn');
    buttons.forEach(btn => {
        btn.addEventListener('touchstart', () => {
            btn.classList.add('active');
        });
        btn.addEventListener('touchend', () => {
            btn.classList.remove('active');
        });
    });
    
    // Оптимизация видео
    const videos = document.querySelectorAll('video');
    videos.forEach(video => {
        video.setAttribute('playsinline', '');
        video.setAttribute('preload', 'metadata');
    });
});