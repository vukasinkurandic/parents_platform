// ovo ide u babysitter/edit_calendar 
// family/edit_calendar
  
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
