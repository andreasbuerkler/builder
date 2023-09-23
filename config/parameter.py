from dataclasses import dataclass, field

@dataclass
class Parameter:
    name: str = ""
    example: str = ""
    description: str = ""
    children: list["Parameter"] = field(default_factory=list)

