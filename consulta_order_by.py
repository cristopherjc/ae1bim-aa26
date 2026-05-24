from configuracion import session
from crear_base_entidades import Carrera


def consulta_order_by():
    print("Consultar order_by: Carreras ordenadas en orden alfabetico")
    carreras = session.query(Carrera).order_by(Carrera.nombre.asc()).all()
    for carrera in carreras:
        print(carrera)


if __name__ == "__main__":
    consulta_order_by()
    session.close()
