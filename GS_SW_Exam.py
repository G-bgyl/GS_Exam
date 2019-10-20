import sqlite3
import random
import string

class FakeMotorData():
    def __init__(self,DataBase_Name):
        self.DBNAME = '%s.db' % (DataBase_Name)
        self.conn = sqlite3.connect(self.DBNAME)
        self.cur = self.conn.cursor()

    def random_car(self):
        random_year=random.choice(list(range(1998,2020)))
        random_make=random.choice(['Honda','GMC','Ford','Toyota'])
        random_model = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
        random_purchase_value = round(random.uniform(5000,40000),2)
        random_VIN = self.create_fake_VIN()
        states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                  "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                  "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                  "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                  "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        random_state = random.choice(states)
        random_number =  ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        return (random_year,random_make,random_model,random_purchase_value,random_VIN,random_state,random_number)
    def create_fake_VIN(self):
        """ creat fake VIN number.
        :return: a rondom ID
        """
        vin_length = 17
        random_char = string.ascii_uppercase + string.ascii_lowercase + string.digits

        return ''.join(random.choice(random_char) for _ in range(vin_length))
    def check_unique_ID(self):
        pass
    def insert_car_data(self):

        tuple_transformed = self.random_car()
        print(tuple_transformed)
        statement = '''insert into Motors Values (Null,?,?,?,?,?,?,?)'''

        self.cur.execute(statement, tuple_transformed)
        self.conn.commit()

    def insert_claims_data(self,list_of_columns):
        tuple_transformed = tuple(list_of_columns)
        statement = '''insert into Claims Values (Null,?,?,?,?,?,?,?,?,?)'''
        self.conn.commit()
        self.cur.execute(statement, tuple_transformed)
    def get_motors_data(self):
        # tuple_transformed = tuple(list_of_columns)
        statement = '''select * from Motors'''

        '''select c.EnglishName, c.Region, count(b.SpecificBeanBarName) 
                                                        from Countries as c
                                                        join Bars as b on b.? = c.Id
                                                        where c.Region = ?
                                                        group by c.EnglishName
                                                        having count(b.SpecificBeanBarName) >4
                                                        order by count(b.SpecificBeanBarName)  desc'''
        result_cn = self.cur.execute(statement,())

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

        statement1 = '''select count(*),sum(PurchaseValue) from Motors'''


        result_cn = self.cur.execute(statement1,())

        self.conn.commit()
        print('test db:')
        for row in result_cn:
            print(row)
        statement2 = '''select YEAR , count(*) from Motors 
                        group by YEAR'''

        result_cn = self.cur.execute(statement2, ())

        self.conn.commit()
        print('test db:')
        for row in result_cn:
            print(row)


if __name__ == '__main__':

    DataBase_Name = 'GS_MotorVehicle'
    #create database
    testdb = MotorVehicleDB(DataBase_Name)
    testdb.create_table()
    # create data

    testcar = FakeMotorData(DataBase_Name)
    for _ in range(10):
        testcar.insert_car_data()

    # testcar.get_motors_data()

    testdb.get_summary()
