from rpg_manager.vista.personaje_vista import PersonajeVista
from personaje_ctrl import PersonajeControlador
from personaje_servicio import PersonajeServicio
def main():
    servicio = PersonajeServicio()
    vista = PersonajeVista()

    controlador = PersonajeControlador(servicio, vista)
    controlador.ejecutar()
if __name__ == "__main__":
    main()