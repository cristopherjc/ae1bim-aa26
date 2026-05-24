from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import Relationship, relationship
from configuracion import Base, engine


class Facultad(Base):
    __tablename__ = "facultades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    ubicacion = Column(String, nullable=False)
    decano = Column(String, nullable=False)

    carreras = Relationship(
        "Carrera", back_populates="facultad", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Facultad(id={self.id}, nombre='{self.nombre}', ubicacion='{self.ubicacion}', decano='{self.decano}')"


class Carrera(Base):
    __tablename__ = "carreras"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    codigo = Column(String, unique=True, nullable=False)
    id_facultad = Column(Integer, ForeignKey("facultades.id"), nullable=False)

    facultad = relationship("Facultad", back_populates="carreras")
    profesores = relationship(
        "Profesor", back_populates="carrera", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Carrera(if={self.id}, nombre='{self.nombre}', codigo='{self.codigo}')"


class Profesor(Base):
    __tablename__ = "profesores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    correo = Column(String, nullable=False)
    especialidad = Column(String, nullable=False)
    id_carrera = Column(Integer, ForeignKey("carreras.id"), nullable=False)

    carrera = relationship("Carrera", back_populates="profesores")
    recursos = relationship(
        "RecursoAcademico", back_populates="profesor", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Profesor(id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}'. correo='{self.correo}', especialidad='{self.especialidad}')"


class RecursoAcademico(Base):
    __tablename__ = "recursos_academicos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    fecha_publicacion = Column(Date, nullable=False)
    tipo = Column(String, nullable=False)
    url = Column(String, nullable=False)
    id_profesor = Column(Integer, ForeignKey("profesores.id"), nullable=False)

    profesor = relationship("Profesor", back_populates="recursos")

    def __repr__(self):
        return f"Recurso Academico(id={self.id}, titulo='{self.titulo}', fecha_publicacion={self.fecha_publicacion}, tipo='{self.tipo}', url={self.url})"


def inicializar_base():
    Base.metadata.create_all(engine)
    print("Tablas creadas en 'database.db'")


if __name__ == "__main__":
    inicializar_base()
