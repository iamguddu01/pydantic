# Computed Fields is pydantic field whose value does not provided by user, in this field we get values by calculating other fields
from pydantic import BaseModel, EmailStr, computed_field


class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float #kg
    height : float #meter
    married : bool = False
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
def data(patient : Patient):
    print(patient.model_dump())
    print('BMI', patient.bmi)
    
patient_info = {'name':'Govind', 'email':'abc@hdfc.com','weight':55.3,'height':2.5,'age':70, 'married':False}
patient1 = Patient(**patient_info)
data(patient1)