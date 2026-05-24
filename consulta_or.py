from sqlalchemy import or_
from configuracion import session
from crear_base_entidades import RecursoAcademico


def consulta_or():
    print("Consulta _or: Filtrar por tipo de Recurso")
    recursos = (
        session.query(RecursoAcademico)
        .filter(
            or_(
                RecursoAcademico.tipo == "Libro",
                RecursoAcademico.tipo == "Guia de estudio",
            )
        )
        .all()
    )

    for recurso in recursos:
        print(recurso)


if __name__ == "__main__":
    consulta_or()
    session.close()
