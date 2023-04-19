
function validarCorreo(){
    var emailus = document.getElementById("emailusuario");
    var emailRegex = /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;
    if(emailRegex.test(emailus.value)){
        alert("correo enviado");
        return true;
    }
    else{
        alert("formato invalido o campo vacio");
        return false;
    }
 }