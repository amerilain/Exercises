import mariadb

connection = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game2',
         user='root',
         password='root123',
         autocommit=True
         )

icao = input("Enter IACO: ")
sql = "SELECT name, municipality FROM airport WHERE ident = '"+icao+"'"
cursor = connection.cursor()
cursor.execute(sql)
response = cursor.fetchall()

print(response)