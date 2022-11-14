function comprobarClave(){
    clave1 = document.f1.password1.value
    clave2 = document.f1.password2.value

    if (clave1 == clave2)
       alert("Las dos claves son iguales")
    else
       alert("Las dos claves son distintas")
}
