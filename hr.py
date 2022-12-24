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
    and wraps two functions 'get_policy' to get the policy details of the employee based on emplpoyee ID input,
    and 'calculate_payroll' to calculate the employee's payroll and prints the details.
    
    """

    def __init__(self,func=None):

        self._employee_policies = {

            1: SalaryPolicy(3000),
            2: SalaryPolicy(1500),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9)
        }
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args,**kwargs)

@PayrollSystem
def get_policy(obj,employee_id):
    policy = obj._employee_policies.get(employee_id)
    if not policy:
        raise ValueError(employee_id)
    else:
        return policy

@PayrollSystem
def calculate_payroll(obj,employees):
    from employee import calculate_payroll
    print("Calculating payroll of the employees")
    print('==============================')

    for employee in employees:
        print("")
        print(f"Payroll for {employee.id} - {employee.name}")
        print(f"Check of : {calculate_payroll(employee)}")
        if employee.address:
            print("Sent to")
            print(f"- {employee.address}")
            print("")

