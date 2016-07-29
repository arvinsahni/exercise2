import psycopg2
import sys

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()
numb_list=sys.argv
if (len(sys.argv)<=2):
        print "check the parameters passed"
else:
     	cur.execute("SELECT word, count from tweetwordcount WHERE (count>=%s AND count <=%s)",(numb_list[1],numb_list[2]))
        records = cur.fetchall()
        if not(records):
                print "not found in the table"
        else:
             	for rec in records:
                        print "word = ", rec[0]
                        print "count = ", rec[1], "\n"

conn.commit()

conn.close()
