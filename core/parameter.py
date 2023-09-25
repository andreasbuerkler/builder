from dataclasses import dataclass, field

@dataclass
class Parameter:
    name: str = ""
    example: str = ""
    description: str = ""
    value: str = ""
    parent: str = ""

@dataclass
class ParameterTree:
    parameter: Parameter
    children: list["ParameterTree"] = field(default_factory=list)

