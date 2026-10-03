document.addEventListener("DOMContentLoaded", function() {
    const prevBtn = document.getElementById('prev');
    const nextBtn = document.getElementById('next');
    const carouselWindow = document.querySelector('.carousel-window');

    function updateButtons() {
        if (carouselWindow.scrollLeft <= 0) {
            prevBtn.style.display = 'none';
        } else {
            prevBtn.style.display = 'flex';
        }
        if (carouselWindow.scrollLeft + carouselWindow.clientWidth >= carouselWindow.scrollWidth - 5) {
            nextBtn.style.display = 'none';
        } else {
            nextBtn.style.display = 'flex';
        }
    }

    carouselWindow.addEventListener('scroll', updateButtons);
    window.addEventListener('resize', updateButtons);
    setTimeout(updateButtons, 100);

    prevBtn.addEventListener('click', function(e) {
        e.preventDefault();
        carouselWindow.scrollBy({ left: -carouselWindow.clientWidth, behavior: 'smooth' });
    });

    nextBtn.addEventListener('click', function(e) {
        e.preventDefault();
        carouselWindow.scrollBy({ left: carouselWindow.clientWidth, behavior: 'smooth' });
    });
});