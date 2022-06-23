import sqlite3
con= sqlite3.connect('mvs.db')
print(con) 

con.cursor()

#Insert values into table
con.execute("INSERT INTO MoviesINFO VALUES('Endgame ','Tony stark        ','2020','Marval')")
con.execute("INSERT INTO MoviesINFO VALUES('KGF 2    ','Yash       ','2022','Prashanth Neel')")
con.execute("INSERT INTO MoviesINFO VALUES('RRR','NTR   ','2022','SSR')")
con.execute("INSERT INTO MoviesINFO VALUES('KGF 1 ','Sri nidhi       ','2018','Prashanth Neel')")
print("Data added!")

#commit changes
con.commit()
con.close()
