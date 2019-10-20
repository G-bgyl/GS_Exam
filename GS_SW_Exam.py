import sqlite3
import random
import string

class FakeMotorData():
    def __init__(self,DataBase_Name):
        self.DBNAME = DataBase_Name
        self.conn = sqlite3.connect(self.DBNAME)
        self.cur = self.conn.cursor()
    def create_fake_VIN(self):
        """ creat fake VIN number.
        :return: a rondom ID
        """
        vin_length = 17
        random_char = string.ascii_uppercase + string.ascii_lowercase + string.digits

        return ''.join(random.choice(random_char) for _ in range(vin_length))
    def check_unique_ID(self):
        pass
    def insert_car_data(self,  list_of_columns):
        tuple_transformed = tuple(list_of_columns)
        statement = '''insert into Motors Values (Null,?,?,?,?,?,?,?,?)'''
        self.cur.execute(statement, tuple_transformed)

    def insert_claims_data(self,list_of_columns):
        tuple_transformed = tuple(list_of_columns)
        statement = '''insert into Claims Values (Null,?,?,?,?,?,?,?,?,?)'''
        self.cur.execute(statement, tuple_transformed)
    def get_motors_data(self,list_of_columns):
        tuple_transformed = tuple(list_of_columns)
        statement = '''select * from Motors'''
        '''select c.EnglishName, c.Region, count(b.SpecificBeanBarName) 
                                                        from Countries as c
                                                        join Bars as b on b.? = c.Id
                                                        where c.Region = ?
                                                        group by c.EnglishName
                                                        having count(b.SpecificBeanBarName) >4
                                                        order by count(b.SpecificBeanBarName)  desc'''
        result_cn = self.cur.execute(statement, tuple_transformed)

        self.conn.commit()
        for row in result_cn:
            print(row)
    def get_claims_data(self):
        pass


class MotorVehicleDB():
    def __init__(self,db_name):
        self.DBNAME = '%s.db' % (db_name)
        try:

            self.conn = sqlite3.connect(self.DBNAME)
            self.cur = self.conn.cursor()
            print('successfully create database %s' % (db_name))
        except:
            print('there\'s an error when creating an database')
    def create_table(self):

        statement = '''
                DROP TABLE IF EXISTS 'Motors';
            '''
        self.cur.execute(statement)
        statement = '''
                        DROP TABLE IF EXISTS 'Claims';
                    '''
        self.cur.execute(statement)


        statement = '''create table 'Motors'(
                            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
                            'Year' INTEGER ,
                            'Make' TEXT ,
                            'Model' TEXT ,
                            'PurchaseValue' TEXT ,
                            'VIN' TEXT,
                            'PlateState' INTEGER ,
                            'number' REAL
                            )
                            '''

        self.cur.execute(statement)
        self.conn.commit()
        statement = '''create table 'Claims'(
                                    'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
                                    'LOSSYEAR' INTEGER ,
                                    'DESCRIPTION' TEXT ,
                                    'TOTALPAID' REAL ,
                                    'VIN' TEXT,
                                    'LossState' INTEGER ,
                                    'MotorID' INTERGER ,
                                    'VINNUMBER' INTERGER NOT NULL,
                                    'OTHERINFO' TEXT,
                                    FOREIGN KEY('VINNUMBER') REFERENCES Motors(VIN)
                                    )
                                    '''

        self.cur.execute(statement)
        self.conn.commit()

    def get_summary(self):
        '''select c.EnglishName, c.Region, count(b.SpecificBeanBarName)
                                                from Countries as c
                                                join Bars as b on b.? = c.Id
                                                where c.Region = ?
                                                group by c.EnglishName
                                                having count(b.SpecificBeanBarName) >4
                                                order by count(b.SpecificBeanBarName)  desc'''
        pass


if __name__ == '__main__':

    DataBase_Name = 'GS_MotorVehicle'
    #create database
    testdb = MotorVehicleDB(DataBase_Name)
    testdb.create_table()
    # create data

    testcar = FakeMotorData(DataBase_Name)
    testcar.insert_car_data(list_of_columns=("NULL",'1','2','3','4',testcar.create_fake_VIN(),'6','7'))

