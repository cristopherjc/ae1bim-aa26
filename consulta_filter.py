from configuracion import session
from crear_base_entidades import Carrera


def consulta_filter():
    print("Consulta filter: Buscar Carrera por Codigo")
    consulta = session.query(Carrera).first()
    print(f"Codigo a buscar: {consulta.codigo}")
    if consulta:
        carrera = (
            session.query(Carrera).filter(Carrera.codigo == consulta.codigo).first()
        )
        print(carrera)
    else:
        print("No hay carreras en la base de datos")


if __name__ == "__main__":
    consulta_filter()
    session.close()

