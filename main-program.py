from productivity import ProductivitySystem , track
from hr import PayrollSystem , calculate_payroll
from employee import Employee_Database

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = Employee_Database()
employees = employee_database.employees
track(productivity_system,employees,9)
calculate_payroll(payroll_system,employees)