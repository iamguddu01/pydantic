from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pincode : str

class Patient(BaseModel):
    name:str
    gender : str = 'Male'
    age : int
    address : Address
    
address_dict = {'city':'Noida', 'state':'Uttar Pradesh', 'pincode':'201310'}
address1 = Address(**address_dict)

patient_dict = {'name':'Govind', 'age':22, 'address':address1}
patient1 = Patient(**patient_dict)

# print(patient1)
# print(patient1.name)
# print(patient1.address.city)
# print(patient1.address.pincode)

# Export methods
print(patient1.model_dump()) # The type of model_dump is dict
print(patient1.model_dump_json())  # The type of model_dump is str
print(patient1.model_dump(include=['name', 'gender'])) # It will print name and gender only
print(patient1.model_dump(exclude=['name', 'gender'])) # It will print everything except name and gender
print(patient1.model_dump(exclude={'address':['state']})) # Chain

print(patient1.model_dump(exclude_unset=True)) # Exclude unset fields, it will exclude the fields which are not set by user and have default values