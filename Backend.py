#backend
import sqlite3

def MovieData():
    con=sqlite3.connect("movie1.db") 
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (Movie_ID VARCHAR(50) PRIMARY KEY,Movie_Name VARCHAR(50),Release_Date VARCHAR(50),Director VARCHAR(50),Cast VARCHAR(50),Budget VARCHAR(50),Duration VARCHAR(50),Rating VARCHAR(50))")
    con.commit()
    con.close()
    
def AddMovieRec(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating):
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("INSERT INTO book VALUES (?,?,?,?,?,?,?,?)", (Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    con.commit()
    con.close()

def ViewMovieData():
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    con.close()    
    return rows

def DeleteMovieRec(id):    
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("DELETE FROM book WHERE Movie_ID=?", (id,))

    con.commit()
    con.close()  

def SearchMovieData(Movie_ID="",Movie_Name="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):  
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    # cur.execute("SELECT * FROM book WHERE Movie_ID=? OR Movie_Name=? OR Release_Date=? OR Director=? OR Cast=? OR Budget=? OR Duration=? OR Rating=?",(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    cur.execute("SELECT * FROM book WHERE Movie_ID=? OR Movie_Name=? OR Release_Date=? OR Director=? OR Cast=? OR Budget=? OR Duration=? OR Rating=?", (Movie_ID, Movie_Name, Release_Date, Director, Cast, Budget, Duration, Rating))

    rows=cur.fetchall()
    con.close()    
    return rows

def UpdateMovieData(id,Movie_ID="",Movie_Name="",Release_Date="",Director="",Cast="",Budget="",Duration="",Rating=""):
    con=sqlite3.connect("movie1.db")    
    cur=con.cursor()
    cur.execute("UPDATE book SET Movie_ID=?,Movie_Name=?,Release_Date=?,Director=?,Cast=?,Budget=?,Duration=?,Rating=?, WHERE id=?",(Movie_ID,Movie_Name,Release_Date,Director,Cast,Budget,Duration,Rating))
    con.commit()
    con.close()

