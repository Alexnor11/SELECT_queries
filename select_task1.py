# SELECT-запросы
import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://alexnor1104:alexnor123@localhost:5432/db_demo1109')
connection = engine.connect()

print('Название и год выхода альбомов, вышедших в 2016 году:')
album = connection.execute("SELECT album_name, album_year  FROM album "
                           "WHERE album_year = 2016;").fetchall()
print(album)
print('\nНазвание и продолжительность самого длительного трека:')
track = connection.execute("""SELECT track_name, track_duration FROM track 
                           ORDER BY track_duration DESC;""").fetchmany(1)
print(track)

print('\nНазвание треков, продолжительность которых не менее 3,5 (210сек.) минуты:')
track_duration = connection.execute("""SELECT track_name, track_duration FROM track
    WHERE track_duration > 210;""").fetchall()
pprint(track_duration)

print('\nНазвания сборников, вышедших в период с 2018 по 2020 год включительно:')
collection = connection.execute("""SELECT collection_name, collection_year FROM collection
    WHERE collection_year BETWEEN 2018 AND 2020""").fetchall()
pprint(collection)

print('\nИсполнители, чье имя состоит из 1 слова:')
artist = connection.execute("""SELECT name FROM artist WHERE name NOT LIKE '%% %%';""").fetchall()
pprint(artist)

print('\nНазвание треков, которые содержат слово "мой"/"my"')
track_name = connection.execute("""SELECT track_name FROM track WHERE track_name iLIKE '%%my%%';""").fetchall()
print(track_name)
