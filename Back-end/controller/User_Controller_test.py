
from User_Controller import User_Controller
from model.User import User

    # ------------------
    # ----- PRUEBAS-----
    # ------------------

if __name__ == "__main__":


    # Crear usuarios falsos para poblar la lista
    user1 = User_Controller.register("pete_the_great@gmail.com", "sqllover123", "Pete")
    user1.portfolio_id = 1
    user2 = User_Controller.register("jdoe89@hotmail.com", "27051989", "John Doe")
    user2.portfolio_id = 2
    user3 = User_Controller.register("casandrawilliams@gmail.com", "cswl897", "Caswill")
    user3.portfolio_id = 3


 # Caso de uso 1: Usuario erróneo

    print("#"*5,"\n","Caso de uso 1: Mail erróneo. Se espera una excepción por mail/usuario inválido")

    try:
        User_Controller.login("matew@gmail.com", "sqllover123")
        print("\n", "#"*5, "Fallo comprobación!!!", "#" * 5, sep="\n", end="\n")
    except Exception as e:
        print(
            "#"*5, f"Efectivamente dio error: {e}", "#" * 5, sep="\n", end="\n")

    # Caso de uso 2: Contraseña errónea
    print("Caso de uso 2: Password errónea. Se espera una excepción por mail/usuario inválido")

    try:
        User_Controller.login("pete_the_great@gmail.com", "sqlover123")
        print("\n", "#"*5, "Fallo comprobación!!!", "#" * 5, sep="\n", end="\n")
    except Exception as e:
        print(
            "#"*5, f"Efectivamente dio error: {e}", "#" * 5, sep="\n", end="\n")

    # Caso de uso 3: Usuario y contraseña correctos
    print("Caso de uso 3: Usuario y contraseña correctos. Se espera loguearse exitosamente")

    try:
        test_user = User_Controller.login("casandrawilliams@gmail.com", "cswl897")
        print(
            "#"*5, f"Usuario logueado: {test_user}", "#" * 5, sep="\n", end="\n")
    except Exception as e:
        print("#"*5, f"Fallo comprobación!!! {e}", "#" * 5, sep="\n", end="\n")

   
