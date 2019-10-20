import sqlite3
import random
import string


#initialization
DATABASE_NAME = 'GS_MotorVehicle'
# random the amount of entries
CAR_AMOUNT = random.choice(list(range(10, 20)))

class FakeMotorData():
    def __init__(self,DATABASE_NAME):
        # connect to database.
        self.DBNAME = '%s.db' % (DATABASE_NAME)
        self.conn = sqlite3.connect(self.DBNAME)
        self.cur = self.conn.cursor()

    def insert_car_data(self):
        """
        insert random generated car info into database.
        :return:
        """
        tuple_transformed = self.random_car()
        # print(tuple_transformed)
        statement = '''insert into Motors Values (Null,?,?,?,?,?,?,?)'''

        self.cur.execute(statement, tuple_transformed)
        self.conn.commit()

    def random_car(self):
        """generate random car information.
        Call by self.insert_car_data().
        :return: a tuple of car info.
        """
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
        call by self.random_car()
        :return: a random ID
        """
        vin_length = 17
        random_char = string.ascii_uppercase + string.ascii_lowercase + string.digits

        return ''.join(random.choice(random_char) for _ in range(vin_length))

    def check_unique_ID(self):
        #TODO: Call by self.create_fake_VIN(). check if the VIN is already exists. If yes, regenerate VIN number.
        pass



    def insert_claims_data(self,list_of_columns):
        """

        :param list_of_columns:
        :return:
        """
        tuple_transformed = tuple(list_of_columns)
        statement = '''insert into Claims Values (Null,?,?,?,?,?,?,?,?,?)'''
        self.conn.commit()
        self.cur.execute(statement, tuple_transformed)

    def get_motors_data(self, VIN ):
        """ Print vehicle info based on VIN number

        :param VIN: String. VIN number
        """

        statement = '''select * from Motors WHERE VIN = ?'''

        result_cn = self.cur.execute(statement,(VIN,))

        self.conn.commit()
        for row in result_cn:
            print('ID:%s \nYear:%s\nMake:%s\nModel:%s\nPrice:%s\nVIN:%s\nState:%s\nPlateNumber:%s'%row)



    def get_claims_data(self):
        pass


class MotorVehicleDB():
    def __init__(self,db_name):
        self.DBNAME = '%s.db' % (db_name)
        try:

            self.conn = sqlite3.connect(self.DBNAME)
            self.cur = self.conn.cursor()
            print('successfully connnect to database %s' % (db_name))
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

        statement1 = '''select count(*),sum(PurchaseValue) from Motors'''


        summary_info = list(self.cur.execute(statement1,()))[0]

        self.conn.commit()
        print('There are %s cars in record, the total purchase price is $%s'%summary_info)

        statement2 = '''select YEAR , count(*) from Motors 
                        group by YEAR order by year desc'''

        result_cn = self.cur.execute(statement2, ())

        self.conn.commit()
        print('the number of motor vehicles for each year:')
        for row in result_cn:
            print('Year %s: %s vehicle(s)'%row)

    def get_VINs(self,):
        statement = '''select VIN from Motors'''

        result_cn = self.cur.execute(statement, ())

        self.conn.commit()

        print('VIN numbers:')
        for row in result_cn:
            print(row[0])

if __name__ == '__main__':


    #create database
    testdb = MotorVehicleDB(DATABASE_NAME)
    testdb.create_table()


    # randomly create data entries
    testcar = FakeMotorData(DATABASE_NAME)

    for _ in range(CAR_AMOUNT):
        testcar.insert_car_data()


    #standard output as requested.
    testdb.get_summary()
    #print out list of VIN numbers for the search in the interactive mode.
    testdb.get_VINs()
    #get requested VIN
    input_VIN = input('Please Type in VIN number to search a vehicle:')
    #output VIN related car information
    testcar.get_motors_data(input_VIN)