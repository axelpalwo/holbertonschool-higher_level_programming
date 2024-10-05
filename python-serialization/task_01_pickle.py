#!/usr/bin/python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)


    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except EOFError:
            print("El archivo que se desea abrir está vacío o corrupto.")
            return None
        except pickle.UnpicklingError:
            print("Hubo un error con la deserealización.")
            return None
