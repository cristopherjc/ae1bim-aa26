from configuracion import session
from crear_base_entidades import Facultad


def consulta_all():
    print("Consulta .all: Listar todas las facultades")
    facultades = session.query(Facultad).all()
    for f in facultades:
        print(f)


if __name__ == "__main__":
    consulta_all()
    session.close()
