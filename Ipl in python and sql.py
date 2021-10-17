import csv
import mysql.connector
IPL = open('most_runs_average_strikerate.csv')
IPLString = IPL.read()

IPLList = []
for line in IPLString.split('\n'):
    IPLList.append(line.split(','))

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='******',
    #database='IPL_average_runs__db'
)
print(mydb)


cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IPL_average_runs_db")
cursor.execute('SHOW DATABASES')


#total_runs	out	average	average

batsman = IPLList[0][0]
total_runs = IPLList[0][1]
out = IPLList[0][2]
numberofballs = IPLList[0][3]
average = IPLList[0][4]
strikerate = IPLList[0][5]

queryCreateTable = """CREATE TABLE FOOTBALL(
                    {} varchar(255) not null,
                    {} int(10) not null,
                    {} int(10) not null,
                    {} int(10) not null,
                    {} float(9,6) not null,
                    {} float(9,6) not null,
                    )""".format(batsman, total_runs, out, numberofballs, average, strikerate)

cursor.execute(queryCreateTable)

del IPLList[0]

rows = ''

for i in range(len(IPLList)-1):
     rows += "('{}','{}','{}','{}','{}','{}')"\
         .format(IPLList[i][0], IPLList[i][1], IPLList[i][2], IPLList[i][3], IPLList[i][4],
                 IPLList[i][5])

     if i != len(IPLList)-2:
         rows += ','

print(rows)
queryInsert = "INSERT INTO BATTING PERFORMANCE STATS" + rows

cursor.execute(queryInsert)
mydb.commit()



