create table if not exists Artist(
	id serial primary key,
	name varchar(40) not null
);

create table if not exists Album(
	id serial primary key,
	album_name varchar(50) not null,
	album_year integer check(album_year >= 0)
);

create table if not exists Track (
	id serial primary key,
	track_name varchar(60) not null,
	track_duration integer check(track_duration >= 0),
	album_id integer not null references Album(id)	
);

create table if not exists Genre (
	id serial primary key,
	genre_name varchar(50) not null
	
);

create table if not exists Collection (
	id serial primary key,
	collection_name varchar(70) not null,
	collection_year integer not null
);

create table if not exists ArtistGenre(
	autor_id integer not null references Artist(id),
	genre_id integer not null references Genre(id)
);

create table if not exists ArtistAlbum(
	album_id integer not null references Album(id),
	artist_id integer not null references Artist(id)
);

create table if not exists Unification(
	track_id integer not null references Track(id),
	collection_id integer not null references Collection(id) 
);
