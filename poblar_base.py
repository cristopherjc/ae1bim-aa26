import random
from faker import Faker
from configuracion import session
from crear_base_entidades import Facultad, Carrera, Profesor, RecursoAcademico

fake = Faker("es_ES")


def poblar_base():
    if session.query(Facultad).count() > 0:
        print("La base de datos ya tiene registros.")
        return

    print("Generando datos con Faker")

    nombres_facultades = [
        ("Facultad de Ingenierias y Arquitectura", "Bloque A"),
        ("Facultad de Ciencias Economicas y Empresariales", "Bloque B"),
        ("Facultad de Ciencias Exactas y Naturales", "Bloque C"),
    ]

    facultades_db = []
    for nombre, ubicacion in nombres_facultades:
        facultad = Facultad(
            nombre=nombre,
            ubicacion=ubicacion,
            decano=f"Mgtr. {fake.first_name()} {fake.last_name()}",
        )
        session.add(facultad)
        facultades_db.append(facultad)

    session.flush()

    carreras_facultad = {
        "Facultad de Ingenierias y Arquitectura": [
            "Computacion",
            "Arquitectura",
            "Telecomunicaciones",
        ],
        "Facultad de Ciencias Economicas y Empresariales": [
            "Administracion de Empresas",
            "Economia",
            "Finanzas",
        ],
        "Facultad de Ciencias Exactas y Naturales": [
            "Biologia",
            "Alimentos",
            "Ingenieria Quimica",
        ],
    }

    carreras_db = []
    for facultad in facultades_db:
        listado = carreras_facultad.get(facultad.nombre, [])
        for nombre_carrera in listado:
            carrera = Carrera(
                nombre=nombre_carrera,
                codigo=f"{facultad.nombre[:3].upper()}-{fake.unique.bothify(text='####')}",
                id_facultad=facultad.id,
            )
            session.add(carrera)
            carreras_db.append(carrera)

    session.flush()

    profesores_db = []
    especialidades = [
        "Sistemas Distribuidos",
        "Arquitectura de Software",
        "Ciberseguridad",
        "Estructura de Datos",
        "Macroeconomia",
        "Finanzas Internacionales",
        "Diseño Urbano",
        "Biologia Celular",
        "Quimica Organica",
        "Biotecnologia",
    ]

    cuenta_profesor = 1

    for carrera in carreras_db:
        for _ in range(3):
            nombre = fake.first_name()
            apellido = fake.last_name()
            correo_utpl = (
                f"{nombre.lower()[0]}{apellido.lower()}{cuenta_profesor}@utpl.edu.ec"
            )

            profesor = Profesor(
                nombre=nombre,
                apellido=apellido,
                correo=correo_utpl,
                especialidad=random.choice(especialidades),
                id_carrera=carrera.id,
            )
            session.add(profesor)
            profesores_db.append(profesor)
            cuenta_profesor += 1
        cuenta_profesor = 1
    session.flush()

    tipos_recursos = ["Libro", "Video", "Guia de estudio"]

    for profesor in profesores_db:
        for _ in range(random.randint(1, 2)):
            recurso = RecursoAcademico(
                titulo=fake.sentence(nb_words=4).replace(".", ""),
                fecha_publicacion=fake.date_between(start_date="-2y", end_date="today"),
                tipo=random.choice(tipos_recursos),
                url=fake.url(),
                id_profesor=profesor.id,
            )
            session.add(recurso)

            session.commit()
    print("Base de datos poblada correctamente")


if __name__ == "__main__":
    poblar_base()
