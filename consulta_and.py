from sqlalchemy import and_
from configuracion import session
from crear_base_entidades import Profesor


def consulta_and():
    print("Consulta _and: Profesores por id_carrera y especialidad")
    profesores = (
        session.query(Profesor)
        .filter(
            and_(Profesor.id_carrera == 1, Profesor.especialidad.like("%Software%"))
        )
        .all()
    )

    for p in profesores:
        print(p)
    if not profesores:
        print(
            "Ningún profesor en la carrera id=1 coincidió con la Especialidad Arquitectura de Software"
        )


if __name__ == "__main__":
    consulta_and()
    session.close()
