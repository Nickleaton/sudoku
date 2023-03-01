from enum import Enum
from typing import Optional


class VariableType(Enum):
    INT = 'int'
    FLOAT = 'float'
    LOGINT = 'logint'
    LOGFLOAT = 'logfloat'

    def format(self, value: Optional[float]) -> str:
        if value is None:
            return " None"
        if self == VariableType.INT:
            return f"{value:5.0f}"
        if self == VariableType.FLOAT:
            return f"{value:5.3f}"
        if self == VariableType.LOGINT:
            return f"{pow(10, value):5.0f}"
        if self == VariableType.LOGFLOAT:
            return f"{pow(10, value):5.3f}"
        return 'Unknown'

    def __repr__(self) -> str:
        return f"VariableType.{self.name}"
