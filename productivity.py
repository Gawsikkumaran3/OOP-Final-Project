class ProductivitySystem:

    def __init__(self,func=None):

        self._roles = {
            'manager': 'ManagerRole',
            'secretary': 'SecretaryRole',
            'sales': 'SalesRole',
            'factory': 'FactoryRole',
        }
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args,**kwargs)


@ProductivitySystem
def get_role(obj,role_id):

        role = obj._roles.get(role_id)
        if not role:
            raise ValueError(role_id)
        else:
            return role

@ProductivitySystem
def track(obj,employees,hours):
        from employee import work
        print('Tracking Employee Productivity')
        print('==============================')

        for employee in employees:
            work(employee,hours)

        print('')

@ProductivitySystem
def perform_duties(obj,hours):

    if str(obj) == 'ManagerRole':
        return f'screams and yells for {hours} hours.'
    
    elif str(obj) == 'SecretaryRole':
        return f'does paperwork for {hours} hours.'

    elif str(obj) == 'SalesRole':
        return f'expends {hours} hours on the phone.'
    
    elif str(obj) == 'FactoryRole':
        return f'manufactures gadgets for {hours} hours.'
        



