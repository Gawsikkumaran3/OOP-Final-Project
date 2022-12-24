class ManagerRole:
    """
    ManagerRole class has a function 'perform_duties' to return a string details of the employee's duty
    along with the number of working hours.
    
    """

    def perform_duties(hours):
        return f'screams and yells for {hours} hours'

class SecretaryRole:
    """
    SecretaryRole class has a function 'perform_duties' to return a string details of the employee's duty
    along with the number of working hours.
    
    """
    def perform_duties(hours):
        return f'expends {hours} hours for doing paperworks'

class SalesRole:
    """
    SalesRole class has a function 'perform_duties' to return a string details of the employee's duty
    along with the number of working hours.
    
    """

    def perform_duties(hours):
        return f'expends {hours} hours in phone calls'

class FactoryRole:
    """
    FactoryRole class has a function 'perform_duties' to return a string details of the employee's duty
    along with the number of working hours.
    
    """

    def perform_duties(hours):
        return f'spends {hours} hours in manufacturing gadgets'


class ProductivitySystem:
    """
    ProductivitySystem class stores the roles class details based on the role assigned to the employee, it has
    'get_role' function to get the role_type of the employee based on the assigned role id, and 'track' function
    to track the Employee's productivity.
    
    """

    def __init__(self):
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole,
        }

    def get_role(self,role_id):
        
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError(role_id)
        return role_type

    def track(self,employees,hours):

        print("Tracking Employee's productivity")
        print("================================")
        for employee in employees:
            employee.work(hours)
        print(" ")

productivity_system = ProductivitySystem()

#get_role function calls the get_role function of the ProductivitySystem class
def get_role(role_id):

    return productivity_system.get_role(role_id)

#track_employees function calls the track function of the ProductivitySystem class
def track_employees(employees,hours):

    return productivity_system.track(employees,hours)




    