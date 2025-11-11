from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class WireVariable(BaseModel):
    definition: str
    id: str = ""
    value: Optional[Any] = None
    value2: Optional[Any] = None
    model_config = {"extra": "allow"}

class WireProps(BaseModel):
    active: str = "true"
    name: str

class WirePayload(BaseModel):
    template: str
    variables: List[WireVariable]
    rights: Dict[str, Any] = Field(default_factory=lambda: {"owner": ""})
    priority: str = "Normal"
    props: WireProps
    skip: str = "false"
    folder: str
