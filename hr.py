class PayrollPolicy:

    def __init__(self):
        self.hours_worked = 0

    def track_work(self,hours):
        self.hours_worked = self.hours_worked + hours

class SalaryPolicy(PayrollPolicy):

    def __init__(self,weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyPolicy(PayrollPolicy):

    def __init__(self,hour_rate):
        super().__init__()
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hour_rate * self.hours_worked


class CommissionPolicy(SalaryPolicy):

    def __init__(self, weekly_salary , commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    @property
    def commission(self):
        sale = self.hours_worked/5
        return sale * self.commission_per_sale
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


class PayrollSystem:

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

