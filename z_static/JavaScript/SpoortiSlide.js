let slideIndex = 0;

function showSlides() {
  let i;
  const slides = document.getElementsByClassName("slide");

  // Hide all slides
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }

  // Increment index and reset if out of bounds
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }

  // Display the current slide
  slides[slideIndex - 1].style.display = "block";

  // Change slide every 2 seconds (2000 milliseconds)
  setTimeout(showSlides, 2000);
}

// Navigate to the previous or next slide
function plusSlides(n) {
  showSlide(slideIndex += n);
}

// Show a specific slide
function currentSlide(n) {
  showSlide(slideIndex = n);
}

// Initialize the slideshow when the page loads
window.onload = showSlides;
