"""
webes nagyon elterjedt
ORM - Object Relation Mapping

python objektumon keresztüli sql használat

"""

from sqlalchemy import create_engine, delete, select, update
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///test.db")

base = declarative_base()

# model-nek nevezzük az ORM tábla definíciót
class FilmTable(base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)

Session = sessionmaker(engine)
session = Session()


base.metadata.drop_all(engine)
base.metadata.create_all(engine)


# insert  - serializáció

alien = FilmTable(id=1, title="Alien", director="Ridley Scott")
star_wars = FilmTable(id=2, title="Star Wars", director="George Lucas")

session.add_all([alien, star_wars])
session.commit()

#############################
# select - serializácó - deserializáció:
# a python és az adatbázis között történik

movies = session.query(FilmTable).filter(FilmTable.id==2)

for movie in movies:
    print(movie.title, movie.id)

    # update

    movie.title = "Star Wars: Return of Jedi"

    session.commit()


# update

session.execute(update(FilmTable)
            .where(FilmTable.id==1)
            .values(title='Alien: A nyolcadik utas a halál'))

session.commit()


# delete

session.query(FilmTable).filter(FilmTable.id==2).delete()
# delete from movies where id = (select id from movies where id = 1)

session.commit()


session.execute(delete(FilmTable).where(FilmTable.id == 1))
## delete from movies where id = 1

session.commit()