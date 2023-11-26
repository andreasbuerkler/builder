from dataclasses import dataclass, field

@dataclass
class Parameter:
    name: str = ""
    example: str = ""
    description: str = ""
    value: str = ""
    isOptional: bool = False
    optionalCondition: list[str] = field(default_factory=list)
    requires: list[str] = field(default_factory=list)
    parent: str = ""


@dataclass
class ParameterTree:
    parameter: Parameter
    children: list["ParameterTree"] = field(default_factory=list)

