from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel
import logging
import json
import subprocess

class MachineSpecs(BaseModel)
    name: str
    os: Literal("centos", "redhat", "ubuntu")
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
    def log_creation(self):
        print(f"Provisioning machine: {self.name}, with {self.os} OS, {self.cpu} core CPU, {self.ram}GB RAM and {self.storage}GB of storage")
        
