class Address:
    """
    Address class initializes the address details of each employees and structure the output of the address
    detail in a more readable format.
    
    """

    def __init__(self,street1,city,state,zipcode,street2=''):
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street1]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city} {self.state} {self.zipcode}')
        return '\n'.join(lines)


class Address_Book:
    """
    Address book is a private class which contains the address of each employees , and it wraps a function 
    which helps to get the employee address of all the employees by his/her employee id.
    
    """

    def __init__(self,func=None):
        import functools
        functools.wraps(self,func)
        self.func = func
        self._employee_address = {

        1: Address('121 Admin Rd.', 'Concord', 'NH', '03301'),
        2: Address('67 Paperwork Ave', 'Manchester', 'NH', '03101'),
        3: Address('15 Rose St', 'Concord', 'NH', '03301', 'Apt. B-1'),
        4: Address('39 Sole St.', 'Concord', 'NH', '03301'),
        5: Address('99 Mountain Rd.', 'Concord', 'NH', '03301'),
    }

    def __call__(self,*args,**kwargs):
        return self.func(self,*args,**kwargs)
    

@Address_Book
def get_employee_address(obj,employee_id):
    address  = obj._employee_address.get(employee_id)
    if not address:
        raise ValueError(address)
    else:
        return address

    



    