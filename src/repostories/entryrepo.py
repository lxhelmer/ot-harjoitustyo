from services.tables import setup

class EntryRepo:
    def __init__(self,table_name):
        self.table=table_name
        self.cursor = setup()
        self.offset = 0 
        
    def get_csize(self):
        self.cursor.execute('''select count(*) from pragma_table_info(\''''+ self.table +'''\');''')
        columncount = self.cursor.fetchall()
        return columncount[0][0]
    
    def get_colnames(self):
        self.cursor.execute('''select name from pragma_table_info(\''''+ self.table + '''\');''')
        cols = self.cursor.fetchall()
        return cols
    def ret_rows(self,rows):
        retrows = []
        for row in rows:
            aprow = []
            for indx in range(self.get_csize()):
                aprow.append(row[indx])
            retrows.append(aprow)
        print (retrows)
        return retrows
        
    def get_first(self):
        self.cursor.execute('''select * from ''' + self.table + ''' limit 30''')
        rows = self.cursor.fetchall()
        return self.ret_rows(rows)

    def get_next(self):
        self.offset += 30
        self.cursor.execute('''select * from ''' + self.table + ''' limit 30 offset ''' + str(self.offset))
        rows = self.cursor.fetchall()
        return self.ret_rows(rows)

    def get_last(self):
        if self.offset >= 30:
            self.offset -= 30
            self.cursor.execute('''select * from ''' + self.table + ''' limit 30 offset ''' + str(self.offset))
        rows = self.cursor.fetchall()
        return self.ret_rows(rows)

    def insert_entry(self,valuesin):
        values = valuesin.split(", ")
        query = ('''insert into '''+ self.table + '''(''')
        for indx in range(self.get_csize()):
            cols = self.get_colnames()
            query += cols[indx][0]
            if indx < self.get_csize()-1:
                query += ''', '''

        query += ''')\nvalues ('''
        
        for indx in range(self.get_csize()):
            query += '''\''''+values[indx]+'''\''''
            if indx < self.get_csize()-1:
                query += ''', '''
        query += ''');'''
        print (query)
        self.cursor.execute(query)
    def delete_entry(self,name):
        priocol = self.get_colnames()[0][0]
        print (priocol)
        query = ('''delete from '''  + self.table + ''' where ''' + priocol + ''' = \'''' + name + '''\'''')
        print (query)
        self.cursor.execute(query)
