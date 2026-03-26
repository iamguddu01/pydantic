from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("DATA INSERTED")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age+5)
    print("DATA UPDATED")

patient_info = {'name':'Govind', 'age':22}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)
update_patient_data(patient1)