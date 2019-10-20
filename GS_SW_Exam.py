import sqlite3
import random
import string

class FakeMotorData():
    def __init__(self):
        pass
    def create_fake_VIN(self):
        """ creat fake VIN number.
        :return: a rondom ID
        """
        vin_length = 17
        random_char = string.ascii_uppercase + string.digits

        return ''.join(random.choice(random_char) for _ in range(vin_length))
    def check_unique_ID(self):
        pass
    def insert_data(self):
        tuple_transformed = tuple(list_of_columns)
        statement = '''insert into Countries Values (Null,?,?,?,?,?,?,?)'''
        cur.execute(statement, tuple_transformed)
    def get_data(self):
        pass


class MotorVehicleDB():
    def __init__(self):
        pass
    def create_db(self,db_name,table_list):
        DBNAME = '%s.db'%(db_name)
        try :

            conn = sqlite3.connect(DBNAME)
            cur = conn.cursor()
            print('successfully create database %s'%(db_name))
        except:
            print('there\'s an error when creating an database')
        for table_name in table_list:
            statement = '''
                    DROP TABLE IF EXISTS 'Bars';
                '''
            cur.execute(statement)


            statement = '''create table 'Countries'(
                            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
                            'Alpha2' TEXT ,
                            'Alpha3' TEXT ,
                            'EnglishName' TEXT ,
                            'Region' TEXT ,
                            'Subregion' TEXT,
                            'Population' INTEGER ,
                            'Area' REAL
                            )
                            '''

        cur.execute(statement)
        conn.commit()

    def get_summary(self):
        pass


