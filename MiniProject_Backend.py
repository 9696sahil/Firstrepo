import sqlite3

def MovieData():
    con = sqlite3.connect("movie1.db") 
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY,
            Movie_ID TEXT,
            Movie_Name TEXT,
            Date TEXT,
            Time TEXT,
            Hall_Name TEXT,
            Seat_no REAL,
            Booking_id REAL,
            Total_amount REAL
        )
    """)
    con.commit()
    con.close()

def AddMovieRec(Movie_ID, Movie_Name, Date, Time, Hall_Name, Seat_no, Booking_id, Total_amount):
    con = sqlite3.connect("movie1.db")    
    cur = con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?,?,?,?,?)", 
                (Movie_ID, Movie_Name, Date, Time, Hall_Name, Seat_no, Booking_id, Total_amount))
    con.commit()
    con.close()

def ViewMovieData():
    con = sqlite3.connect("movie1.db")    
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    con.close()    
    return rows

def DeleteMovieRec(id):    
    con = sqlite3.connect("movie1.db")    
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    con.commit()
    con.close()  


def UpdateMovieData(id, Movie_ID="", Movie_Name="", Date="", Time="", Hall_Name="", Seat_no="", Booking_id="", Total_amount=""):
    con = sqlite3.connect("movie1.db")    
    cur = con.cursor()
    cur.execute("UPDATE book SET Movie_ID=?, Movie_Name=?, Release_Date=?, Director=?, Cast=?, Budget=?, Duration=?, Rating=? WHERE id=?", 
                (Movie_ID, Movie_Name, Date, Time, Hall_Name, Seat_no, Booking_id, Total_amount, id))
    con.commit()
    con.close()

# Initialize the database
MovieData()
