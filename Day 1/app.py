class employee:

    def Declare_employee(self,name,age,gender,salary,state,city):
        self.name=name
        self.age=age
        self.gender=gender
        self.salary=salary
        self.state=state
        self.city=city

    def Print_employee(self):
        print('Name :',self.name)
        print('Age :',self.age)
        print('Gender :',self.gender)
        print('Salary :', self.salary)
        print('State :',self.state)
        print('City :',self.city)


name=input('Enter the name: ')
age=int(input('Enter the age: '))
gender=input('Enter the gender: ')
salary=int(input('Enter the salary: '))
state=input('Enter the state: ')
city=input('Enter the city: ')
sum=employee()
sum.Declare_employee(name,age,gender,salary,state,city)
sum.Print_employee()