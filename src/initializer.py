from services.connection import get_connection
from services.tables import get_tables

def drop_tables(connection):
    cursor = connection.cursor()
    tables = get_tables()
    
    for i in tables: 
        cursor.execute('''drop table if exists  '''+i)
    
    connection.commit()

def initialize_tables():
    connection = get_connection()
    drop_tables(connection)


if __name__ == "__main__":
    initialize_tables()
