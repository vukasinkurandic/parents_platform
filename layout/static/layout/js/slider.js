var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 5,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    breakpoints: {
      640: {
        slidesPerView: 1,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 1,
        spaceBetween: 40,
      },
      1024: {
        slidesPerView: 2,
        spaceBetween: 40,
      },
    },
       autoplay: {
      delay: 3000,
      disableOnInteraction: false,
    }
  });
  
  
  document.getElementsByClassName("swiper-wrapper")[0].addEventListener("mouseover", function( ) {
  swiper.autoplay.stop();
  });
  
  document.getElementsByClassName("swiper-wrapper")[0].addEventListener("mouseout", function( ) {
  swiper.autoplay.start();
  });
  