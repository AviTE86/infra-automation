from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, Field, field_validator
import logger
class MachineSpecs(BaseModel):
    name: str = Field(
        min_length=3,  # Minimum length of 3 characters
        max_length=20, # Maximum length of 20 characters
        pattern=r"^[a-zA-Z0-9_]*$" # Only alphanumeric and underscore characters allowed
    )
    os: Literal["centos", "redhat", "ubuntu"]
    cpu: int = Field(gt=0)
    ram: int = Field(gt=0)
    storage: int = Field(gt=0)

    @field_validator("name")
    def normalize_name(cls, value: str) -> str:
        return value.lower()

    def dictionary(self):
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram,
            "storage": self.storage
        }
    def log_creation(self):
        logger.logger.info(
            f"Provisioning machine: {self.name}, " 
            f"with {self.os} OS, {self.cpu} core CPU, "
            f"{self.ram}GB RAM and {self.storage}GB of storage."
        )
