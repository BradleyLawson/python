import csv
import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "0987^%poIU",
  database = "python"
)
myCursor = mydb.cursor()

table = """
    CREATE TABLE IF NOT EXISTS people (
    firstname varchar(45),
    lastname varchar(45),
    age int,
    address varchar(45)
    ); 
      """
myCursor.execute(table)


with open('file.csv') as csvfile:
  reader = csv.DictReader(csvfile)

  for row in reader:
    firstname = row['FirstName']
    lastname = row['LastName']
    age = row['Age']
    address = row['Address']
    value = (firstname, lastname, age, address)
    sql = "INSERT INTO people (firstname, lastname, age, address) VALUES (%s,%s,%s,%s)"
    myCursor.execute(sql, value)
    mydb.commit()
    print(myCursor.rowcount,"record inserted.")