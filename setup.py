import sqlite3

conn = sqlite3.connect('reviewData.db')

conn.execute("CREATE TABLE Reviews (Username VARCHAR(40), Movie text, ReviewTime VARCHAR(16),"
             "Rating REAL, Review VARCHAR(500))")
print("Table Reviews Created Successfully")
conn.execute("CREATE TABLE Ratings (Movie text, Acting REAL, Image REAL, Story REAL,"
             " BoxOffice REAL, Overall REAL)")
print("Table Ratings Created Successfully")
conn.commit()
conn.close()


