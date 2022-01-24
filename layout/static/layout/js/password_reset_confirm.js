// ovo ide u password-reset-confirm/MTU/set-password

let passinfo = document.querySelector('#hint_id_new_password1');
passinfo.innerHTML = "";

let error1 = document.querySelector('#error_1_id_new_password2');
let error2 = document.querySelector('#error_2_id_new_password2');
let error3 = document.querySelector('#error_3_id_new_password2');

error1.innerHTML = 'Lozinke se ne poklapaju ili su slične sa email adresom/Passwords must match or is too similar to the email address.'
error2.innerHTML = 'Lozinka mora sadržati min 8 karaktera/Password must contain at least 8 characters';
error3.innerHTML = "Lozinka ne sme biti sastavljena samo od brojeva/Password can't be entirely numeric ";
