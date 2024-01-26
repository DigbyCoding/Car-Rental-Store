import CTkMessagebox
import customtkinter as ctk 
import pyodbc 

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Tres\Documents\Car-Rental-Store\Car_Rental.accdb;')




#def main():
#    runSQL("SELECT * FROM Login",True)



def runSQL(strSQL, results):
    global conn 

    cursor = conn.cursor()
    cursor.execute(strSQL)

    fetched_values = []

    if results:
        print('\n')

        columns = [column[0] for column in cursor.description]
        for c in columns:
            print(c, end = ",")
        print("")


        for row in cursor.fetchall():
            for c in row:
                print(c, end = "\t")
                fetched_values.append(row)
        print("")

    else:
        conn.commit()
        print("\n", strSQL, ": Run - ", cursor.rowcount, "record(s) affected")
    
    cursor.close()

    return fetched_values

