'''
  Mysql Connector
'''
import sys
import datetime
import logging
import mysql.connector
logging.basicConfig(filename='applog.log',level=logging.DEBUG,format='%(asctime)s:%(message)s')
myDB=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='ADF'
)
mycursor = myDB.cursor()
# mycursor.execute('create table request_info
# (Req_id int auto_increment primary key,FirstName varchar(20),'
#                    'MiddleName varchar(20),LastName varchar(20),dob varchar(10),gender
#                    varchar(10),nationality varchar(15),'
#                    'city varchar(20),state varchar(20),pin int(6),qual varchar(20),
#                    salary int(15),pan int(10),Req_date varchar(10),age int(3))')
# mycursor.execute('create table `response_info`
# (Res_id int auto_increment primary key,Req_id int(100),Response varchar(10),reason varchar(100))')
# pylint: disable=broad-except
# pylint: disable=too-many-statements
class New: # pylint: disable=too-many-instance-attributes
    '''
    create a class
    '''
    def __init__(self):
        self.firstname = None
        self.middlename = None
        self.lastname = None
        self.dob = None
        self.gender = None
        self.nat = None
        self.city = None
        self.state = None
        self.pin = None
        self.qual = None
        self.salary = None
        self.pan = None
        self.age=None
        self.test_str = 'Eligible'
    def get_first_name(self,value):
        '''
            Get First Name
        '''
        self.firstname=value
        logging.debug("first name received: {value}")

    def get_middle_name(self,value):
        '''
            Get Middle Name
        '''
        if value!='*':
            self.middlename=value
            logging.debug("middle name received: {value}")
        else:
            self.middlename=' '

    def get_last_name(self,value):
        '''
            Get Last Name
        '''
        self.lastname=value
        logging.debug("last name received: {value}")

    def get_dob(self,value):
        '''
            Get DOB as (YYYY-MM-DD)
        '''
        self.dob=value
        logging.debug("DOB received: {value}")
    def get_gender(self,value):
        '''
            Get Gender as (Male/Female/others)
        '''
        self.gender=value
        logging.debug("gender received: {value}")
    def get_nationality(self,value):
        '''
            Get Nationality ex,Indian , American
        '''
        self.nat=value
        logging.debug("nationality received: {value}")
    def get_current_city(self,value):
        '''
            Get Current City
        '''
        self.city=value
        logging.debug("current city received: {value}")
    def get_state(self,value):
        '''
            Get State
        '''
        self.state=value
        logging.debug("state received: {value}")

    def get_pin_code(self,value):
        '''
            Get Pin-code ex,(635521)
        '''
        self.pin=value
        logging.debug("pin-code received: {value}")

    def get_qualification(self,value):
        '''
            Get Qualification ex,B.Tech ,B.E
        '''
        self.qual=value
        logging.debug("qualification received: {value}")

    def get_salary(self,value):
        '''
            Get Salary ex,50000
        '''
        self.salary=value
        logging.debug("salary received: {value}")

    def get_pan_number(self,value):
        '''
            Get Pan Number ex,NUM2345671
        '''
        self.pan=value
        logging.debug("Pan Number received: {value}")
    def add_request(self):
        '''
            Add a table Named Request
        '''
        try:
            stmt="""insert into `request_info`
            (`FirstName`,`MiddleName`,`LastName`,`dob`,`gender`,`nationality`,
            `city`,`state`,`pin`,`qual`,`salary`,`pan`,`Req_date`) 
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            val=(self.firstname,self.middlename,self.lastname,self.dob,self.gender,
                 self.nat,self.city,self.state,self.pin,self.qual,self.salary,self.pan,
                 str(datetime.date.today()))

            mycursor.execute(stmt,val)
            myDB.commit()
            logging.debug("User's details are inserted to the DB")
            print('Request added successfully')
        except Exception:
            print(Exception)
            sys.exit()
    def valid_val(self):
        '''
            Validate all Values
        '''
        stmt = """select `Req_id` from
        `request_info` where `pan`=%(pan_number)s"""
        mycursor.execute(stmt, {'pan_number': self.pan})
        rows = mycursor.fetchall()
        row = list(rows[len(rows) - 1])
        if len(self.firstname) < 3 :
            mycursor.execute('insert into `response_info` '
                             '(`Req_id`,`Response`,`reason`) '
                             'values (%s,%s,%s)',
                             (row[0], 'Failed', 'Invalid first name'))
            myDB.commit()
            logging.debug("Invalid firstname detected")
            sys.exit()
        if self.middlename!=' ' and len(self.middlename)<3 :
            mycursor.execute('insert into `response_info` '
                             '(`Req_id`,`Response`,`reason`) '
                             'values (%s,%s,%s)',
                             (row[0], 'Failed', 'Invalid middle name'))
            myDB.commit()
            logging.debug("Invalid middlename detected")
            sys.exit()
        if len(self.lastname) < 1 :
            mycursor.execute('insert into `response_info` '
                             '(`Req_id`,`Response`,`reason`) '
                             'values (%s,%s,%s)',
                             (row[0], 'Failed', 'Invalid last name'))
            myDB.commit()
            logging.debug("Invalid lastname detected")
            sys.exit()
        try:
            birth_date = datetime.datetime.strptime(self.dob, '%Y-%m-%d')
            logging.debug("Valid DOB detected")
            end_date = datetime.datetime.today()
            time_difference = end_date - birth_date
            self.age = int(int(time_difference.days) / 365)
            if self.age>-1 and self.age<101 :
                mycursor.execute('update `request_info` set '
                                 '`age`=%(ageFound)s where '
                                 '`Req_id`=%(ri)s',
                                 {'ageFound':self.age,'ri':row[0]})
                logging.debug("User's age is calculated")
                myDB.commit()
            else:
                raise ValueError
        except ValueError:
            mycursor.execute('insert into `response_info` '
                             '(`Req_id`,`Response`,`reason`) '
                             'values (%s,%s,%s)',
                             (row[0], 'Failed', 'Invalid input for DOB'))
            myDB.commit()
            logging.debug("Invalid DOB detected")
            sys.exit()
        if not(self.gender.lower() == 'male' or self.gender.lower() == 'female'
               or self.gender.lower() == 'others'):
            mycursor.execute('insert into `response_info` '
                             '(`Req_id`,`Response`,`reason`) '
                             'values (%s,%s,%s)',
                             (row[0], 'Failed', 'Given gender is invalid'))
            myDB.commit()
            logging.debug("Invalid gender detected")
            sys.exit()

        if not(len(str(self.pin)) == 6 and str(self.pin).isdigit()):
            mycursor.execute('insert into `response_info` '
                             '(`Req_id`,`Response`,`reason`) '
                             'values (%s,%s,%s)',
                             (row[0], 'Failed', 'Given PIN number is invalid'))
            myDB.commit()
            logging.debug("Invalid PIN code detected")
            sys.exit()

        if not str(self.salary).isdigit():
            mycursor.execute('insert into `response_info` '
                             '(`Req_id`,`Response`,`reason`) '
                             'values (%s,%s,%s)',
                             (row[0], 'Failed', 'Given salary is invalid'))
            myDB.commit()
            logging.debug("Invalid salary detected")
            sys.exit()

        if not(len(str(self.pan)) == 10 and self.pan.isalnum()):
            mycursor.execute('insert into `response_info` '
                             '(`Req_id`,`Response`,`reason`) values (%s,%s,%s)',
                             (row[0], 'Failed', 'Given PAN ID is invalid'))
            myDB.commit()
            logging.debug("Invalid PAN ID detected")
            sys.exit()

    def validate(self):
        '''
            Validate
        '''
        stmt="""select `age`,`gender`,`Req_date`,`nationality`,`state`,
        `salary`,`Req_id` from `request_info` where `pan`=%(pan_number)s"""
        mycursor.execute(stmt,{'pan_number': self.pan})
        rows=mycursor.fetchall()
        logging.debug("Values fetched from DB")
        row=list(rows[len(rows)-1])
        if (not(((str(row[1]).lower()=='male' or str(row[1]).lower()=='others')
                 and row[0]>21) or (str(row[1]).lower()=='female' and row[0]>18))):
            mycursor.execute('insert into `response_info` '
                             '(`Req_id`,`Response`,`reason`) values (%s,%s,%s)',
                             (row[6],'Failed','Age is less than expected.'))
            myDB.commit()
            logging.debug("Given age is out of range for eligibility")
            sys.exit()
        if (row[3]!='Indian' and row[3]!='American'):
            mycursor.execute('insert into `response_info` '
                             '(`Req_id`,`Response`,`reason`) values (%s,%s,%s)',
                             (row[6],'Failed', 'Enterd nationality is not eligible'))
            myDB.commit()
            logging.debug("Given nationality is not eligible")
            sys.exit()
        if (row[4]  not in ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
                            'Chattisgarh',  'Karnataka',  'Madhya Pradesh',  'Odisha',
                            'Tamil Nadu',  'Telangana', 'West Bengal']):
            mycursor.execute('insert into `response_info` '
                             '(`Req_id`,`Response`,`reason`) values (%s,%s,%s)',
                             (row[6],'Failed', 'Entered state is not eligible'))
            myDB.commit()
            logging.debug("Given state is not eligible")
            sys.exit()
        if row[5]<10000 or row[5]>90000:
            mycursor.execute('insert into `response_info` '
                             '(`Req_id`,`Response`,`reason`) values (%s,%s,%s)',
                             (row[6], 'Failed', 'Salary is not equal to expected value.'))
            myDB.commit()
            logging.debug("Provided salary is out of range for eligibility")
            sys.exit()
        j=1
        for get in rows:
            get=list(get)
            if j!=len(rows):
                prev_date=datetime.datetime.strptime(get[2],'%Y-%m-%d')
                cur_date=datetime.datetime.strptime(row[2],'%Y-%m-%d')
                if(cur_date-prev_date).days<6:
                    mycursor.execute('insert into `response_info` '
                                     '(`Req_id`,`Response`,`reason`) values (%s,%s,%s)',
                                     (row[6], 'Failed',
                                      'Recently request received in last 5 days'))
                    myDB.commit()
                    logging.debug("Not eligible-recently request received in last 5 days")
                    sys.exit()
            j+=1
        mycursor.execute('insert into `response_info` '
                         '(`Req_id`,`Response`,`reason`) values (%s,%s,%s)',
                         (row[6], 'Success', 'Eligible'))
        myDB.commit()

# obj=New()
# obj.get_first_name(input('Enter the First Name : '))
# obj.get_middle_name(input('Enter the Middle Name or to skip press "*": '))
# obj.get_last_name(input('Enter the Last Name : '))
# obj.get_dob(input('Enter the DOB : '))
# obj.get_gender(input('Enter the Gender : '))
# obj.get_nationality(input('Enter the Nationality :'))
# obj.get_current_city(input('Enter the Current City : '))
# obj.get_state(input('Enter the State : '))
# obj.get_pin_code(int(input('Enter the Pin-Code : ')))
# obj.get_qualification(input('Enter the Qualification : '))
# obj.get_salary(int(input('Enter the Salary: ')))
# obj.get_pan_number(input('Enter the Pan Number : '))
#
# obj.add_request()
# obj.valid_val()
# obj.validate()
# logging.debug('Eligible user')
# mycursor.close()
# logging.debug('Mysql cursor closed')
# myDB.close()
# logging.debug('Mysql connection closed')
