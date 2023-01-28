import mariadb
import dbcreds

# connecting to mariadb DB
# got this info from dbcreds.py file
conn = mariadb.connect(
                        user = dbcreds.user,
                        password = dbcreds.password,
                        host = dbcreds.host,
                        port = dbcreds.port,
                        database = dbcreds.database
                        )
cursor = conn.cursor()
print("Please select from the following:\
    \n1.Add new user\
    \n2.See all users")
selection = input("Enter your option")
if selection == '1':
    username = input("Please provide a username:")
    dob = input("Please provide your date of birth (yyyy-mm-dd)")
    cursor.execute("CALL add_user(?, ?)",[username, dob])
    conn.commit()
if selection == '2':
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    print(result)
cursor.close()
conn.close()



# !Notes
# you need to run this to commit to push the above code your Database! 
# conn.commit()
# after commiting, you can check the data tab in your table and should be able to see it on there

# (?) a special thing for mariadb to understand to push the next code in []
# even if you use one variale when you're executing, it still needs to be in a list form []
