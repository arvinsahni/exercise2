import psycopg2
import plotly.plotly as pl
import plotly.graph_objs as gobjs

#pl.tools.set_credentials_file(username='arvinsahni', api_key='ufgr1voq80')

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()
cur.execute("SELECT word, count from tweetwordcount ORDER BY count DESC LIMIT 20")
records = dict(cur.fetchall())

x_sql=list(records.viewkeys())
y_sql=list(records.viewvalues())

data =[gobjs.Bar(x=x_sql,y=y_sql)]
pl.iplot(data,filename='basic-bar')

conn.commit()
conn.close()
