let ja = document.querySelector("nav");
let mob_menu = document.querySelector(".menu");
mob_menu.addEventListener("click", function () {
  ja.classList.toggle("add_men");
  this.classList.toggle("active-nav");
});

// skidanje kontejnere umeniju
let inerWidBraus = window.innerWidth;
if (inerWidBraus < 767) {
  let remove = document.querySelector(".rem-onmobile");
  remove.classList.remove("container");
}

// skidanje kontejnere i dodavanje fluid kontejnera u profil wraper divu i u njegovom kontejneru
let inerWidBraust = window.innerWidth;
let removee = document.querySelectorAll(".add-fluid-div");
if (inerWidBraust < 992) {
  removee.forEach(function (e) {
    e.classList.remove("container");
    e.classList.add("container-fluid");
  });
}

const host = "http://127.0.0.1:8000/";
// JAVASCRIPT FOR INDEX PAGE
if (
  window.location.href == host + "babysitter/edit_calendar" ||
  window.location.href == host + "family/edit_calendar"
) {
  let selektuj = document.querySelector(".select_all");
  selektuj.addEventListener("click", function () {
    selects();
  });
  function selects() {
    let ele = document.querySelectorAll(".chk");
    for (let i = 0; i < ele.length; i++) {
      if (ele[i].type == "checkbox") ele[i].checked = true;
    }
  }

  let deselect = document.querySelector(".deselect_all");
  deselect.addEventListener("click", function () {
    deselectcheck();
  });
  function deselectcheck() {
    let ele = document.querySelectorAll(".chk");
    for (let i = 0; i < ele.length; i++) {
      if (ele[i].type == "checkbox") ele[i].checked = false;
    }
  }
}


if (window.location.href == host + "password-reset-confirm/MTU/set-password") {
  let passinfo = document.querySelector('#hint_id_new_password1');
  passinfo.innerHTML = "";

  let error1 = document.querySelector('#error_1_id_new_password2');
  let error2 = document.querySelector('#error_2_id_new_password2');
  let error3 = document.querySelector('#error_3_id_new_password2');

  error1.innerHTML = 'Lozinke se ne poklapaju ili su slične sa email adresom/Passwords must match or is too similar to the email address.'
  error2.innerHTML = 'Lozinka mora sadržati min 8 karaktera/Password must contain at least 8 characters';
  error3.innerHTML = "Lozinka ne sme biti sastavljena samo od brojeva/Password can't be entirely numeric ";
}
if (window.location.href == host + "family/edit_profil/" ||
  window.location.href == host + "babisitter/edit_profil/") {
  /*Clear chack box and label for edit family and babysitter profil form*/
  let clear_check = document.querySelector('#picture-clear_id');
  clear_check.remove()
  var labels = document.getElementsByTagName('label');
  for (var i = 0; i < labels.length; i++)
    if (labels[i].htmlFor == 'picture-clear_id') {
      label = labels[i];
      break;
    }
  label.remove()
}

if (window.location.href == host + 'register_babysitter/' ||
  window.location.href == host + 'register_family/') {
  /*register family and babysiter error*/
  let error66 = document.getElementById('66')
  let error28 = document.getElementById('28')
  let error34 = document.getElementById('34')
  let error49 = document.getElementById('49')
  if (error66) {
    error66.innerHTML = '<strong>Vaša lozinka mora da sadrži najmanje 8 karaktera</strong>';
  }
  if (error28) {
    error28.innerHTML = '<strong>Lozinka ne sme biti među najčešće korišćenim lozinkama</strong>';
  }
  if (error34) {
    error34.innerHTML = '<strong>Lozinka ne može da sadrži samo cifre</strong>';
  }
  if (error49) {
    error49.innerHTML = '<strong>Lozinka ne sme biti slična email adresi</strong>';
  }
}

// JAVASCRIPT FOR PRICE FILTER
const price_range_slid = "http://127.0.0.1:8000/";

if (window.location.href == price_range_slid + "connection/all_babysitters") {

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
}

