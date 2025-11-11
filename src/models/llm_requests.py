import uuid
from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field, EmailStr


class Rights(BaseModel):
    owner: str = "184431757886694"

class Props(BaseModel):
    active: str = "true"
    name: str
    description: Optional[str] = ""
class BaseLLMRequest(BaseModel):
    id: Optional[str] = None
    rights: Rights
    priority: str = "Normal"
    props: Props
    skip: str = "false"

    def ensure_id(self):
        if not self.id:
            self.id = str(uuid.uuid4())

    def template_key(self) -> str:
        raise NotImplementedError

    def to_field_values(self) -> Dict[str, Any]:
        raise NotImplementedError


class SendEmailVariables(BaseModel):
    sql_query: str
    to: EmailStr
    cc: Optional[str] = ""
    subject: str
    text: str
    attachment: bool = True
    extra_id: str = "110673709476681"
class SendEmailLLMRequest(BaseLLMRequest):
    template: str = "110673709194435"
    variables: List[SendEmailVariables]

    def template_key(self) -> str:
        return "SENDEMAIL"

    def to_field_values(self) -> Dict[str, Any]:
        return {
            "template": self.template,
            "extra_id": self.variables.extra_id,
            "sql_query": self.variables.sql_query,
            "to": self.variables.to,
            "cc": self.variables.cc or "",
            "subject": self.variables.subject,
            "text": self.variables.text,
            "attachment": "true" if self.variables.attachment else "false",
        }


class SelectedColumn(BaseModel):
    columnName: str

class ReadSqlLLMRequest(BaseLLMRequest):
    customer_id: str
    sql: str
    columns: List[SelectedColumn] = Field(default_factory=list)
    paginate: bool = False
    limit: Optional[int] = None
    output_name: str = ""
    output_path: str = ""
    overwrite: bool = False
    return_json: bool = True
    return_csv: bool = False
    opt_a: str = ""
    opt_b: str = ""

    def template_key(self) -> str:
        return "READSQL"

    def to_field_values(self) -> Dict[str, Any]:
        return {
            "customer_id": self.customer_id,
            "sql": self.sql,
            "columns_json": [c.model_dump() for c in self.columns],
            "paginate": "true" if self.paginate else "false",
            "limit": None if self.limit is None else self.limit,
            "output_name": self.output_name,
            "output_path": self.output_path,
            "overwrite": "true" if self.overwrite else "false",
            "opt_a": self.opt_a,
            "opt_b": self.opt_b,
            "return_json": "true" if self.return_json else "false",
            "return_csv": "true" if self.return_csv else "false",
        }


class ColumnSchema(BaseModel):
    columnName: str
    columnType: Optional[str] = None
    columnLength: Optional[int] = 2000
    alias: str = ""

class WriteDataLLMRequest(BaseLLMRequest):

    source_job_id: str
    job_name: str
    folder: str = "3023602439587835"

    columns_schema: List[ColumnSchema]
    job_id: Optional[str] = ""
    customer_id: str
    database: str
    table: str
    write_mode: str = "DROP"
    use_temp: bool = False
    create_if_missing: bool = False
    partitioned: bool = False
    batch_size: Optional[int] = None
    note: str = ""
    tags: str = ""

    def template_key(self) -> str:
        return "WRITEDATA"

    def to_field_values(self) -> Dict[str, Any]:
        return {
            # Mixed variable (value + jobName + folder)
            "job_context": {
                "value": self.source_job_id,
                "jobName": self.job_name,
                "folder": self.folder,
            },
            "columns_schema_json": [c.model_dump() for c in self.columns_schema],
            "job_id": self.job_id or "",
            "customer_id": self.customer_id,
            "database": self.database,
            "table": self.table,
            "write_mode": self.write_mode,
            "use_temp": "true" if self.use_temp else "false",
            "create_if_missing": "true" if self.create_if_missing else "false",
            "partitioned": "true" if self.partitioned else "false",
            "batch_size": self.batch_size,
            "note": self.note,
            "tags": self.tags,
        }
