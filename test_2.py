from sqlalchemy import create_engine,text,select,Column, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

host="localhost"
database = "postgres"
user="postgres"
password="postgres"
connection_string =f"postgresql://{user}:{password}@{host}/{database}"
engine=create_engine(connection_string)

class siswa(Base):
    __tablename__= "siswa"
    nis = Column(String, primary_key=True)
    nama = Column(String)
    alamat = Column(String)

sqlnya=select(siswa)
with Session(engine) as session:
    result = session.execute(sqlnya)
    for row in result.scalars():
        print(row.nis, row.nama,row.alamat)

