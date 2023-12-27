from dataclasses import dataclass, field

@dataclass
class Parameter:
    name: str = ""
    example: str = ""
    description: str = ""
    value: str = ""
    isOptional: bool = False
    optionalCondition: list["Parameter"] = field(default_factory=list)
    requires: list["Parameter"] = field(default_factory=list)
    parent: list[str] = field(default_factory=list)


@dataclass
class ParameterTree:
    parameter: Parameter
    children: list["ParameterTree"] = field(default_factory=list)

