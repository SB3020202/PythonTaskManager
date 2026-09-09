""" FR1 """
from datetime import date, datetime, timedelta


# date      -> ano, mes. dia
# datetime  -> ano, mes, dia, hora
# timedelta -> intervalo de tempo

"""------------------------------------------- FR1 ----------------------------------------------""" 
class Car:
    def __init__(self, plate: str, model: str, fuel: str, status: str, inspection_date: date):
        self.plate = plate                 
        self.model = model                 
        self.fuel = fuel                   
        self.status = status               
        self.inspection_date = inspection_date

