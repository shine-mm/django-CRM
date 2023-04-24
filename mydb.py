import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '58966985'
    
)

#prepare a cursor obejct 

cursorObject = dataBase.cursor()

# Create a database 
cursorObject.execute('CREATE DATABASE elderco')

print('all done!')