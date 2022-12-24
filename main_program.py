from hr import PayrollSystem, HourlyPolicy
from productivity import ProductivitySystem
from employee import Employee_Database

productivity_system = ProductivitySystem()  #instance of the ProductivitySystem
payroll_system = PayrollSystem()            #instance of the PayrollSystem   
employee_database = Employee_Database()     #instance of the Employee_Database   
employees = employee_database.employees     #collecting employee details from Employee_Database
manager = employees[0]                      #assigning the first employee details
manager.payroll = HourlyPolicy(55)          #assigning the policy and the number of working hours

productivity_system.track(employees, 40)    #tracking and printing the productivity of the employees based on number of working hours
payroll_system.calculate_payroll(employees) #calculating and printing the payroll details   