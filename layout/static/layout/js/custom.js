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