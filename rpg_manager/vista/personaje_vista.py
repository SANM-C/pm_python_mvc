class PersonajeVista:

    def mostrar_menu_principal(self):
        print("=== MENÚ PRINCIPAL ===")
        print("1. Crear personaje")
        print("2. Listar personajes")
        print("3. Buscar personaje")
        print("4. Salir")

    def mostrar_personaje(self, personaje):
        if personaje:
            print("=== PERSONAJE ===")
            print(personaje)
        else:
            print("Personaje no encontrado.")

    def pedir_nombre_personaje(self) -> str:
        return input("Ingrese el nombre del personaje: ")

    def mostrar_lista(self, lista: list):
        print("=== LISTA DE PERSONAJES ===")
        if not lista:
            print("No hay personajes.")
        else:
            for personaje in lista:
                print(personaje)