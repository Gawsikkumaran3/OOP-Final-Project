from hr import get_policy
from productivity import get_role
from contacts import get_employee_address

class Employee_Database:
    """
    Employee Database has the details of the employee's name and role based on employee's id. It has a property
    'employees' which collects the employee's id,name,role details.

    It has one more function called 'get_employee_info' which returns the name and role of the employee with
    the use of Employee ID.
    
    """
    def __init__(self):

        self._employees = {
            1: {
                'name': 'Mary Poppins',
                'role': 'manager'
            },
            2: {
                'name': 'John Smith',
                'role': 'secretary'
            },
            3: {
                'name': 'Kevin Bacon',
                'role': 'sales'
            },
            4: {
                'name': 'Jane Doe',
                'role': 'factory'
            },
            5: {
                'name': 'Robin Williams',
                'role': 'secretary'
            }
        }

    @property
    def employees(self):
        return [Employee(id_) for id_ in sorted(self._employees)]

    def get_employee_info(self,employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError(employee_id)
        return info



class Employee:
    """
    Employee class initializes employee's details of id,name,address,role and payroll. 
    
    It has a function called 'work' which collects the string value of the duties performed by the individual employee, and tracks the 
    number of working hours of each employee's based on the payroll method.

    It also has a calculate payroll function, which calls the calculate_payroll function and calculates the
    payroll for each employees.
    
    """
    def __init__(self,id):
        self.id = id
        info = employee_database.get_employee_info(self.id)
        self.name = info.get('name')
        self.address = get_employee_address(self.id)
        self._role = get_role(info.get('role'))
        self._payroll = get_policy(self.id)

    def work(self,hours):
        duties = self._role.perform_duties(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}')
        print('')
        self._payroll.track_work(hours)
    
    def calculate_payroll(self):
        return self._payroll.calculate_payroll()

#instance of the Employee_Database class
employee_database = Employee_Database()

