from productivity import ProductivitySystem , track
from hr import PayrollSystem , calculate_payroll
from employee import Employee_Database

productivity_system = ProductivitySystem()  #instance of the ProductivitySystem
payroll_system = PayrollSystem()            #instance of the PayrollSystem   
employee_database = Employee_Database()     #instance of the Employee_Database   
employees = employee_database.employees     #collecting employee details from Employee_Database
track(productivity_system,employees,9)      #tracking and printing the productivity of the employees based on number of working hours
calculate_payroll(payroll_system,employees) #calculating and printing the payroll details