import io
from datetime import datetime
import psycopg2
import io
from psycopg2 import Error



try:
    f = open('tuples.txt', "r")
    s = f.readline()
    print(str(s))
    count1=0
    count2=0
    times = []
    emotions = []
    time = ""
    emotion = ""
    for i in s:
        print(str(i))
        print(str(count2))
        print(time)
        time = ""
        if i == "]":
            count1=count1+1
            print("HERE")
            times.append(time)
            emotions.append(emotion)
            time=""
            emotion=""
        if (count2-(38*count1) > 1 and count2-(38*count1) < 21):
            time=time+i
        if (count2-(38*count1) > 30 and count2-(38*count1) < 34):
            emotion=emotion+i           
        count2=count2+1
        
except:
    print("fail")


try:
    connection = psycopg2.connect(user = "fizzhazlt", password = "Admin@123", host = "127.0.0.1", port = "5432", database = "test")
        
    cursor = connection.cursor()
                                  
    create_table_query = '''CREATE TABLE test (TIME TEXT PRIMARY KEY     NOT NULL, EMOTION           TEXT    NOT NULL); '''
                                  
    #cursor.execute(create_table_query)
    for i in range(len(times)):
        #cursor.execute("INSERT INTO test (TIME, EMOTION) VALUES (%s, %s, %s)", (times[i-1], emotions[i-1]))
        1+1
    
    connection.commit()
    print("Table created successfully in PostgreSQL ")





except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
