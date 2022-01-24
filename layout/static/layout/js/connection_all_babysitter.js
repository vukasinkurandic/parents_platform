// ovo ide u connection/all_babysitters
// JAVASCRIPT FOR PRICE FILTER

  window.onload = function () {
    slideOne();
    slideTwo();
  }

  let sliderOne = document.getElementById("price_range_min");
  let sliderTwo = document.getElementById("price_range_max");
  let displayValOne = document.getElementById("range1");
  let displayValTwo = document.getElementById("range2");
  let minGap = 0;
  let sliderTrack = document.querySelector(".slider-track");
  let sliderMaxValue = document.getElementById("price_range_min").max;

  function slideOne() {
    if (parseInt(sliderTwo.value) - parseInt(sliderOne.value) <= minGap) {
      sliderOne.value = parseInt(sliderTwo.value) - minGap;
    }
    displayValOne.textContent = sliderOne.value;
    fillColor();
  }
  function slideTwo() {
    if (parseInt(sliderTwo.value) - parseInt(sliderOne.value) <= minGap) {
      sliderTwo.value = parseInt(sliderOne.value) + minGap;
    }
    displayValTwo.textContent = sliderTwo.value;
    fillColor();
  }
  function fillColor() {
    percent1 = (sliderOne.value / sliderMaxValue) * 100;
    percent2 = (sliderTwo.value / sliderMaxValue) * 100;
    sliderTrack.style.background = `linear-gradient(to right, #dadae5 ${percent1}% , #73c4f4 ${percent1}% , #73c4f4 ${percent2}%, #dadae5 ${percent2}%)`;
  }




// samo za filter stranu

let inerWidBraust2 = window.innerWidth;  
let remodiv = document.querySelectorAll(".add-fluid-div2");
if (inerWidBraust2 < 1400) {
remodiv.forEach(function (e) {
e.classList.remove("container");
e.classList.add("container-fluid");
});
}
