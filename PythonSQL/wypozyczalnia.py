import sqlite3

def create_film_table():
	with sqlite3.connect('wypozyczalnia.db') as db:
		c=db.cursor()	#tworzenie tablicy
		c.execute("""
			CREATE TABLE Film(
			FilmID integer,
			Tytul text,
			Typ real,
			Rok integer,
			Primary Key(FilmID)
			) """)
		db.commit() #zmiany
#create_film_table()

def insert_records(values):
	with sqlite3.connect('wypozyczalnia.db') as db:
		c=db.cursor()
		sql = """INSERT INTO Film (Tytul, Typ, Rok)
		          VALUES(?,?,?)"""
		c.execute(sql,values)
		db.commit()
		
def delete_record(tytul):
	with sqlite3.connect('wypozyczalnia.db') as db:
		c=db.cursor()
		sql="DELETE FROM Film WHERE tytul = ?"
		c.execute(sql,(tytul,))
		db.commit()

def select_all_films():
	with sqlite3.connect('wypozyczalnia.db') as db:
		c=db.cursor()
		sql="Select * from Film"
		c.execute(sql)
		wynik=c.fetchall()
		print(wynik)

def select_one_film():
	with sqlite3.connect('wypozyczalnia.db') as db:
		c=db.cursor()
		sql="Select * from Film where FilmID = 1"
		c.execute(sql)
		wynik=c.fetchone()
		print(wynik)

def select_genre(typ):
	with sqlite3.connect("wypozyczalnia.db") as db:
		cursor = db.cursor()
		sql = "Select * from Film where typ = ?"
		cursor.execute(sql,(typ,))
		result = cursor.fetchall()
		return result

def select_year(rok):
	with sqlite3.connect("wypozyczalnia.db") as db:
		cursor = db.cursor()
		sql = "Select * from Film where rok = ?"
		cursor.execute(sql,(rok,))
		result = cursor.fetchall()
		return result
		
#wybor = input("Podaj typ: ")
#films = select_genre(wybor)
#print(films)

while 1:
	print ("WYPOZYCZALNIA FILMOW")
	print ("====================")
	print ("1 - Dodaj film")
	print ("2 - Usun film")
	print ("3 - Pokaz wszystkie filmy")
	print ("4 - Znajdz filmy w zadanych latach")
	print ("5 - Wyjscie")
	x = int(input())
	if x == 1:
		tytul = input ("Podaj tytul: ")
		typ = input ("Podaj typ: ")
		print ("Podaj rok: ", end='')
		rok = int(input())
		nastepny_film = (tytul,typ,rok)
		insert_records(nastepny_film)
	elif x == 2:
		tytul = input ("Podaj tytul filmu ktory chcesz usunac: ")
		delete_record(tytul)
	elif x == 3:
		select_all_films()
	elif x == 4:
		print ("Podaj rok")
		rok = int(input())
		filmy = select_year(rok)
		print (filmy)
	elif x == 5:
		break
	else:
		print ("Podaj prawidlowa liczbe!")
		