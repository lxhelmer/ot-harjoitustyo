from services.connection import get_connection

def setup():
    connection = get_connection()
    cursor = connection.cursor()
    return cursor

def get_tables():
    cursor = setup()
    
    cursor.execute('''select name from sqlite_master where type='table' order by name''')
    
    tables = cursor.fetchall()
    ret = []
    for row in tables:
        ret.append(row[0])
    return ret

def delete_table(name):
    cursor = setup()
    
    cursor.execute('''drop table ''' + name)
    

def create_table(name, columns):
    connection = get_connection()

    cursor = connection.cursor()
    command = '''create table ''' + name + ''' (\n '''
    testc = '''
        create table users (
            username text primary key,
            password text
        );
    '''

    for columnindx in range(len(columns)):
        if columnindx == 0:
            command += columns[columnindx] + ''' unique'''
        else:
            command = command + columns[columnindx]
        if columnindx < len(columns)-1:
            command += ''',\n'''

    command += '''\n); '''
    
    cursor.execute(command)
def make_columns(colstring):
    return colstring.split(", ")
