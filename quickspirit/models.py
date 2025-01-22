from dataclasses import dataclass
from typing import Optional

from .http_errors import RequestError


@dataclass
class Result:
    Error: Optional[RequestError]
    Data: bytes
