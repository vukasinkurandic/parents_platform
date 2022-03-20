// ovo ide na sve strane
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


let inerWidBraust = window.innerWidth;
let removee = document.querySelectorAll(".add-fluid-div");
if (inerWidBraust < 992) {
  removee.forEach(function (e) {
    e.classList.remove("container");
    e.classList.add("container-fluid");
  });
}

let hostimgmobile = "https://parentstime.rs";

let index_mob = window.innerWidth;
 if (index_mob < 656) {
let slid = document.querySelectorAll('.slid img' );
slid.forEach(function(n){
  n.src= hostimgmobile + "/static/layout/img/for_mob.webp";
})
 }



let fot_mob2 = window.innerWidth;
if (fot_mob2 < 656) {
  fot = document.querySelector(".footer-wrapper-main");
  fot.style.backgroundImage = "url("+hostimgmobile+"/static/layout/img/for_mob_footer.webp)";
}




// popup

const popup = document.querySelector(".popup");
const close = document.querySelector(".close");
setTimeout(function () {
  let visited = sessionStorage.getItem("visited");
  if (!visited) {
    popup.style.display = "block";
    sessionStorage.setItem("visited", true);
  }
}, 500);

close.addEventListener("click", function () {
  document.querySelector(".popup").style.display = "none";
});



