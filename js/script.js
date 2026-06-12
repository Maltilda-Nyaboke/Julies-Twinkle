

let menuToggle = document.querySelector('.menuToggle');
let header = document.querySelector('header');
let section = document.querySelector('section');
// let section = document.getElementsByTagName('*');


menuToggle.onclick = function () {
    header.classList.toggle('active')
    section.classList.toggle('active')
}

const slides = document.querySelectorAll('.slide');

// console.log(slides)

let counter = 0;
// console.log(i)



slides.forEach((slide, index) => {
    slide.style.left = `${index * 100}%`

});

const goPrev = () => {
    counter--
    slideImg()
}
const goNext = () => {
    counter++ 
    slideImg()
}


const slideImg = () => {
    for (let i = 0; i < slides.length; i++) {
        if (counter >= slides.length) {
            slides.forEach(slide => {
                slide.style.transform = `translateX(-${counter * 0}%)`
            });
        } else {
            slides.forEach(slide => {
                slide.style.transform = `translateX(-${counter * 100}%)`
            });
        }
    }
}
// const slideImg = () => {
//     for (let i = 0; i < slides.length; i++) {
//         if (counter >= slides.length) {
//             slides.forEach(slide => {
//                 slide.style.transform = `translateX(-${counter * 0}%)`
//             });
//         } else {
//             slides.forEach(slide => {
//                 slide.style.transform = `translateX(-${counter * 100}%)`
//             });
//         }
//     }
// }


// setInterval(() => {
    // if (counter < 2) {
    //     console.log(counter++)
    //     slides.forEach((slide, index) => {
    //         slide.style.left = `${index * 100}%`
    //         slide.style.transform = `translateX(-${counter * 100}%)`
    //     });
    // } 
    
    // else {
    //     console.log(counter--)
    //     slides.forEach((slide, index) => {
    //         slide.style.left = `${index * 100}%`
    //         slide.style.transform = `translateX(-${counter * 100}%)`
    //     }); 
    // }
// }, 2000);



document.addEventListener("DOMContentLoaded", function() {
    const text = "Welcome to my website!";
    const typewriterElement = document.getElementById("typewriter");
    let index = 0;

    function type() {
        if (index < text.length) {
            typewriterElement.textContent += text.charAt(index);
            index++;
            setTimeout(type, 100);
        }
    }

    type();
});


ocument.addEventListener("DOMContentLoaded", () => {
    const background = document.querySelector('.background');
    const images = [
        '../img/home-model3.jpg',
        '../img/home-model4.jpg',
        '../img/backgroundimg.jpg', // Add more images here
        
    ];
    let currentIndex = 0;

    setInterval(() => {
        background.classList.add('fade-out');

        setTimeout(() => {
            currentIndex = (currentIndex + 1) % images.length;
            background.style.backgroundImage = `url(${images[currentIndex]})`;

            background.classList.remove('fade-out');
        }, 500); // Fade out duration
       
    }, 10000); // Change image every 10 seconds

});

const carousel = document.querySelector('.carousel');
const items = document.querySelectorAll('.carousel-item');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');

let currentIndex = 0;
let autoSlideTimeout;

// Function to show a specific slide
function showSlide(index) {
  items.forEach((item, i) => {
    item.classList.toggle('active', i === index);
  });
  carousel.style.transform = `translateX(-${index * 100}%)`;
}

// Function to go to the next slide
function nextSlide() {
  currentIndex = (currentIndex + 1) % items.length;
  showSlide(currentIndex);
  // resetAutoSlide();
}

// Function to go to the previous slide
function prevSlide() {
  currentIndex = (currentIndex - 1 + items.length) % items.length;
  showSlide(currentIndex);
  resetAutoSlide();
}

// Automatically slide every 5 seconds
function autoSlide() {
  autoSlideTimeout = setTimeout(() => {
    nextSlide();
    autoSlide();
  }, 3000);
}

// Reset auto-slide timer
function resetAutoSlide() {
  clearTimeout(autoSlideTimeout);
  autoSlide();
}

// Event listeners for buttons
prevBtn.addEventListener('click', prevSlide);
nextBtn.addEventListener('click', nextSlide);

// Initialize the carousel
showSlide(currentIndex);
autoSlide();

// Hide carousel after 15 seconds
etTimeout(() => {
  document.querySelector('.carousel-section').style.display = 'none';
}, 15000);



// Show the button when the user scrolls down
const backToTopButton = document.getElementById("backToTop");

window.onscroll = function () {
  if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
    backToTopButton.style.display = "block"; // Show the button
  } else {
    backToTopButton.style.display = "none"; // Hide the button
  }
};

// Scroll back to the top when the button is clicked
backToTopButton.addEventListener("click", function () {
  window.scrollTo({ top: 0, behavior: "smooth" });
});




