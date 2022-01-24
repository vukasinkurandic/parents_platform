// ovo ide u family/edit_profil
// babisitter/edit_profil/


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
