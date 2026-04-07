class PersonajeControlador:

    def __init__(self, servicio, vista):
        self.servicio = servicio
        self.vista = vista
        self.opciones = {
            "1": self.op_crear,
            "2": self.op_listar,
            "3": self.op_buscar,
            "4": self.op_salir
        }
        self.ejecutando = True

    def ejecutar(self):
        while self.ejecutando:
            self.vista.mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")

            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("Opción inválida.")

    def op_crear(self):
        # TODO: conectar con servicio
        pass

    def op_listar(self):
        # TODO: conectar con servicio
        pass

    def op_buscar(self):
        # TODO: conectar con servicio
        pass

    def op_salir(self):
        print("Saliendo...")
        self.ejecutando = False