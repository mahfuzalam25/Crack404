// nav bar icons
const menu = document.querySelector(".nav_menu");
const menuBtn = document.querySelector("#open-menu-btn");
const closeBtn = document.querySelector("#close-menu-btn");

menuBtn.addEventListener('click', () => {
    menu.style.display = "flex";
    closeBtn.style.display = "inline-block";
    menuBtn.style.display = "none";
});

const closeNav = () => {
    menu.style.display = "none";
    closeBtn.style.display = 'none';
    menuBtn.style.display = "inline-block";
};

menuBtn.addEventListener('click', () => {
    menu.style.display = "flex";
});

closeBtn.addEventListener('click', closeNav)


//  for swiping header and web

var swiper = new Swiper(".mySwiper", {
    spaceBetween: 30,
    centeredSlides: true,
    speed: 1000,
    autoplay: {
        delay: 7500,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});


// for swiping project and team


var swiper = new Swiper(".swiper",{
    slidesPerView:1,
    spaceBetween:10,
    speed:400,
    preventClicks:true,
    noSwiping: true,
    freeMode: false,
    nevigation:{
        nextEl: ".next",
        prevEl: ".prev",
    },
    breakpoints:{
        550:{
            slidesPerView:2,
            spaceBetween:20,
        },
        950:{
            slidesPerView:3,
            spaceBetween:30,
        },
        1200:{
            slidesPerView:4,
            spaceBetween:30,
        },
    },
})



// swiper of review  
  
var swiper = new Swiper(".swiper-container", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
      rotate: 50,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows: true,
    },
    pagination: {
      el: ".swiper-pagination",
    },
});


const contact = document.getElementById('contact');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    contact.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    contact.classList.remove("active");
});
