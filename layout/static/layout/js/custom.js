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
