const login = document.getElementById("form-login");

login.addEventListener("submit", (e) => {
  console.log("Ingreso exitoso");
  e.preventDefault();

  Swal.fire({
    icon: "success",
    title: "BIENVENIDO!",
  });
});
