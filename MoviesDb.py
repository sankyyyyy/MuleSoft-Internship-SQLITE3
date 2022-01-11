import sqlite3
con= sqlite3.connect('Movies.db')
print(con) 

con.cursor()

#Insert values into table
con.execute("INSERT INTO MoviesINFO VALUES('Endgame ','Tony stark        ','2020','Marval')")
con.execute("INSERT INTO MoviesINFO VALUES('ABCD    ','PrabhuDeva       ','2018','Karan johar')")
con.execute("INSERT INTO MoviesINFO VALUES('14 phere','kriti kharbanda  ','2021','Devanshu singh')")
con.execute("INSERT INTO MoviesINFO VALUES('October ','varun dhvan       ','2018','sujjit sarkar')")
print("Data added!")

#commit changes
con.commit()
con.close()