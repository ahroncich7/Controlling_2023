function chng__pass() {
  let htmlChngPass =
    '<h2 class="form__h2">Cambio de contraseña</h2><form class="form__user" action=""><fieldset><legend class="form__legend">Ingresa los siguientes datos:</legend><br /><label class="form__label" for="password">Contraseña actual:<br /><input class="form__input"  type="password" name="password" id="password" required /></label> <br /> <br /> <label class="form__label" for="new_password" >Nueva contraseña: <br /> <input class="form__input" type="password" name="new_password" id="new_password" required /> </label> <br /> <br /> <label class="form__label" for="confirm_pass">Confirma nueva contraseña: <br /> <input class="form__input" type="password" name="confirm_pass" id="confirm_pass" required/> </label><br /><br /><button type="reset" class="btn btn-primary btn-sm" style="padding-left: 1.5rem; padding-right: 1.5rem; margin: 0.5rem">Restablecer</button> <button type="button" class="btn btn-primary btn-sm" style="padding-left: 1.5rem; padding-right: 1.5rem; margin: 0.5rem" onclick="pass__compare()">Guardar cambios</button> <br /> <button type="button" class="btn btn-primary btn-sm" style="padding-left: 1.5rem; padding-right: 1.5rem; margin: 0.5rem" onclick="cancel__chng()">Cancelar Cambio</button>';

  document.getElementById("chng__pass").innerHTML = htmlChngPass;
  document.getElementById("btn__chng--pass").innerHTML = "";

  let password = document.getElementById("password").value;
  let email = document.getElementById("email").value;
}

function pass__compare() {
  let password = document.getElementById("password").value;
  let new_password = document.getElementById("new_password").value;
  let confirm_pass = document.getElementById("confirm_pass").value;

  if (password != "" && new_password != "" && confirm_pass != "") {
    if (new_password == confirm_pass) {
      window.alert("La contraseña se cambio correctamente");
    } else {
      window.alert("Las nueva contraseña y su confirmacion no coinciden");
    }
  } else {
    window.alert(
      "Los siguientes campos son obligatorios: \n Contraseña actual \n Nueva Contraseña \n Confirma nueva Contraseña"
    );
  }
}

function cancel__chng() {
  let htmlBtnChngPass =
    '<button id="btn__chng" type="button" class="btn btn-primary btn-md" style=" padding-left: 1.5rem; padding-right: 1.5rem; margin: 0.5rem;" onclick="chng__pass()" >Cambiar contraseña</button>';
  document.getElementById("chng__pass").innerHTML = "";
  document.getElementById("btn__chng--pass").innerHTML = htmlBtnChngPass;
}
