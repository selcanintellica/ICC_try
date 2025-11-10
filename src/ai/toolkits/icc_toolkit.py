from typing import List
from langchain_core.tools import tool
from src.repositories.job_repository import JobRepository
from src.models.jobs import WriteDataPayload, ReadSqlPayload, SendEmailPayload, APIResponse

import uuid



async def write_data_job(data: WriteDataPayload) -> dict:
    """
    Create a job to write data using the JobRepository.
    Use this to initiate data writing tasks.
    Args:
        data (WriteDataPayload): Payload containing data to be written.
    Returns:
        dict: Confirmation message and job details.

    """
    if not data.id:
        data.id = str(uuid.uuid4())
    await JobRepository.write_data_job(data)
    return {"message": "Success", "data": data.model_dump()}


@tool
async def read_sql_job(data: ReadSqlPayload) -> dict:
    """
    Create a job to read SQL data using the JobRepository.
    Use this to initiate SQL data reading tasks.
    Args:
        data (ReadSqlPayload): Payload containing SQL read parameters.
    Returns:
        dict: Confirmation message and job details.

    """
    if not data.id:
        data.id = str(uuid.uuid4())
    await JobRepository.read_sql_job(data)
    return {"message": "Success", "data": data.model_dump()}


@tool
async def send_email_job(data: SendEmailPayload) -> dict:
    """
    Create a job to send an email using the JobRepository.
    Use this to initiate email sending tasks.
    Args:
        data (SendEmailPayload): Payload containing email parameters.
    Returns:
        dict: Confirmation message and job details.
    """
    if not data.id:
        data.id = str(uuid.uuid4())
    await JobRepository.send_email_job(data)
    return {"message": "Success", "data": data.model_dump()}


class ICCToolkit:
    @staticmethod
    def get_tools() -> List:
        """
        Get the list of tools provided by the ICC Toolkit.
        Returns:
            List: A list of tool functions available in the ICC Toolkit.

        """
        return [
            write_data_job,
            read_sql_job,
            send_email_job,
        ]
