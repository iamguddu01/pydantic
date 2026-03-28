from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pincode : str

class Patient(BaseModel):
    name:str
    gender : str
    age : int
    address : Address
    
address_dict = {'city':'Noida', 'state':'Uttar Pradesh', 'pincode':'201310'}
address1 = Address(**address_dict)

patient_dict = {'name':'Govind', 'gender':'male', 'age':22, 'address':address1}
patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pincode)