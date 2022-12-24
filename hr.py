class PayrollPolicy:
    """
    PayrollPolicy class initializes hours_worked , and has a function 'track_work' to track the
    number of working hours of each employee based on payroll policy.
    
    """

    def __init__(self):
        self.hours_worked = 0

    def track_work(self,hours):
        self.hours_worked = self.hours_worked + hours

class HourlyPolicy(PayrollPolicy):
    """
    HourlyPolicy class is a child class of PayrollPolicy which initializes hours_rate , and has a function 
    'calculate_payroll' to track the number of working hours of each employee based on payroll policy.
    
    """

    def __init__(self,hour_rate):
        super().__init__()
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class SalaryPolicy(PayrollPolicy):
    """
    SalaryPolicy class is a child class of PayrollPolicy which initializes weekly_salary , and has a function 
    'calculate_payroll' to track the number of working hours of each employee based on payroll policy.
    
    """

    def __init__(self,weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class CommissionPolicy(SalaryPolicy):
    """
    CommissionPolicy class is a child class of SalaryPolicy which initializes weekly_salary and 
    commission_per_sale , and has a function 'calculate_payroll' to track the number of working hours of 
    each employee based on payroll policy.
    
    """

    def __init__(self,weekly_salary,commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    @property
    def commission(self):
        sales =  self.hours_worked/5
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        fixed =  self.weekly_salary
        return fixed + self.commission


class PayrollSystem:
    """
    PayrollSystem class stores the salary policy data of the employee's based on the employee ID,
    and has two functions 'get_policy' to get the policy details of the employee based on emplpoyee ID input,
    and 'calculate_payroll' to calculate the employee's payroll and prints the details.
    
    """

    def __init__(self):

        self._employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(1500),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9)
        }

    def get_policy(self,employee_id):

        policy = self._employee_policies.get(employee_id)
        if not policy:
            raise ValueError(policy)
        return policy

    def calculate_payroll(self,employees):
        print("Calculating Payroll")
        print("===================")
        for employee in employees:
            print(f'Payroll for : {employee.id} - {employee.name}')
            print(f'- Check amount : {employee.calculate_payroll()}')
            if employee.address:
                print(f'- Sent to : {employee.address}')
            print(" ")

payroll_system = PayrollSystem()

#get_policy function calls the get_policy function of the PayrollSystem class
def get_policy(employee_id):

    return payroll_system.get_policy(employee_id)

#calculate_payroll function calls the calculate_payroll function of the PayrollSystem class
def calculate_payroll(employees):

    return payroll_system.calculate_payroll(employees)




