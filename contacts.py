class Address:
    """
    Address class initializes the address details of each employees and structure the output of the address
    detail in a more readable format.
    
    """

    def __init__(self,street,city,state,zipcode,street2 = ''):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.street2 = street2
    

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city} , {self.state}-{self.zipcode}')
        return '\n'.join(lines)


class _AddressBook:
    """
    Address book is a private class which contains the address of each employees , and has a function which 
    helps to get the employee address of all the employees by his/her employee id.
    
    """
    def __init__(self):

        self._employee_addresses = {

            1: Address('121 Admin Rd.', 'Concord', 'NH', '03301'),
            2: Address('67 Paperwork Ave', 'Manchester', 'NH', '03101'),
            3: Address('15 Rose St', 'Concord', 'NH', '03301', 'Apt. B-1'),
            4: Address('39 Sole St.', 'Concord', 'NH', '03301'),
            5: Address('99 Mountain Rd.', 'Concord', 'NH', '03301'),

        }

 
    def get_employee_address(self,employee_id):

        employee__address = self._employee_addresses.get(employee_id)
        if not employee__address:
            raise ValueError(employee_id)
        return employee__address
        
_address_book = _AddressBook()

#get_employee_address function calls the get_employee_address function inside the _AddressBook class
def get_employee_address(employee_id):

    return _address_book.get_employee_address(employee_id)