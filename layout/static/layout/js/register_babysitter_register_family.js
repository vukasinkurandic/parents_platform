
//Input with dynamic ID, depends on the language
let hidden = document.getElementById('input-sr')

/*register family and babysiter error if language is Serbian*/
if (hidden != null) {
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

