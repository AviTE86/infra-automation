from datetime import datetime
from typing import Optional
from pydantic import BaseModel
import logging

class machine:

    def __init__(self, name: str, os: Literal["centos", "redhat", "ubuntu"], cpu: int, ram: int, storage: int):
        self.name = name
        self.os = os.lower()
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        
class Machine(BaseModel):
    name: str
    os: Literal["centos", "redhat", "ubuntu"]
    cpu: int
    ram: int
    storage: int

    
    def dictionary(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram,
            "storage": self.storage
        }
