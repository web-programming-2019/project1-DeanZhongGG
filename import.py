import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
	#建表
	db.execute("DROP TABLE IF EXIST Books;")
	db.execute("create table Books(
						isbn varchar(100) primary key,
						title varchar(100),
						author varchar(100),
						year varchar(100)
						);")
	#插入数据
  b = open("books.csv")
  reader = csv.reader(b)
  for isbn,title,author,year in reader:
   db.execute("Insert into Books (isbn,title,author,year) Values (:isbn, :title, :author, :year)",
         {"isbn":isbn, 
         	"title":title, 
         	"author" :author,
          "year":year})
  db.commit()

if __name__ == "__main__":
	main()