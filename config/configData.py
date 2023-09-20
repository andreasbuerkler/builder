from dataclasses import dataclass

@dataclass
class ConfigData:
    parent: str
    name: str
    example: str
    description: str

