class Employee_Database:
    
    def __init__(self,func=None):
        import functools
        functools.wraps(self,func)
        self.func = func
        self._employees = [
            {
                'id': 1,
                'name': 'Mary Poppins',
                'role': 'manager'
            },
            {
                'id': 2,
                'name': 'John Smith',
                'role': 'secretary'
            },
            {
                'id': 3,
                'name': 'Kevin Bacon',
                'role': 'sales'
            },
            {
                'id': 4,
                'name': 'Jane Doe',
                'role': 'factory'
            },
            {
                'id': 5,
                'name': 'Robin Williams',
                'role': 'secretary'
            },
        ]
        from productivity import ProductivitySystem
        from hr import PayrollSystem
        from contacts import Address_Book
        self.productivity_system = ProductivitySystem()
        self.payroll_system = PayrollSystem()
        self.address = Address_Book()

    @property
    def employees(self):
        return [create_employees(**data) for data in self._employees]

    def __call__(self,*args,**kwargs):
        return self.func(self,*args,**kwargs)
    

@Employee_Database
def create_employees(obj,id,name,role):
    from productivity import get_role
    from hr import get_policy
    from contacts import get_employee_address
    address = get_employee_address(id)
    job_role = get_role(obj.productivity_system,role)
    payroll_policy = get_policy(obj.payroll_system,id)
    return Employee(id=id,name=name,address=address,role=job_role,payroll_policy=payroll_policy)
    

class Employee:

    def __init__(self,func=None,id=None,name=None,address=None,role=None,payroll_policy=None):
        import functools
        functools.wraps(self,func)
        self.id = id
        self.name = name
        self.address = address
        self.role = role
        self.payroll_policy = payroll_policy
        self.func = func
    
    def __call__(self,*args,**kwargs):
        return self.func(*args,**kwargs)

@Employee
def work(obj,hours):
    from productivity import perform_duties
    duties = perform_duties(obj.role,hours)
    print(f'Employee {obj.id} - {obj.name} : ')
    print(f'- {duties}')
    print('')
    obj.payroll_policy.track_work(hours)

@Employee
def calculate_payroll(obj):
    return obj.payroll_policy.calculate_payroll()