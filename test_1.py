from sqlalchemy import create_engine,text,select

host="localhost"
database = "postgres"
user="postgres"
password="postgres"
connection_string =f"postgresql://{user}:{password}@{host}/{database}"
engine=create_engine(connection_string)

conn=engine.connect()

sqlnya=text("select * from siswa")
results=conn.execute(sqlnya).fetchall()
print(results)


