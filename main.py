from parser import parser
from models import Products
from db_config import create_table,insert_into_db
from lxml import html
import time
from utils import load


file="bata.html"
table_name="shoes_urls"

def main():
    create_table(table_name)
    html_content = load(file)
    result=parser(html_content)
    validated=[]
    for prod in result:
        try:
            validated.append(Products(**prod))
        except Exception as e:
            print("Validation Error: ",e)
    if validated:
        insert_into_db(table_name,validated)

if __name__=="__main__":
    st=time.time()
    main()
    et=time.time()
    print(et-st)