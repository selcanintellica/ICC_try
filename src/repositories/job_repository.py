from src.models.wire import WirePayload
from src.utils.config import API_CONFIG
from base_repository import BaseRepository
from loguru import logger



class JobRepository(BaseRepository):
    """Repository for handling job-related API operations"""

    @staticmethod
    async def write_data_job(self, data: WirePayload) -> APIResponse[WriteDataDTO]:
        logger.info(f"Creating write data job: {data.name if hasattr(data, 'name') else 'unknown'}")
        endpoint = f"{API_CONFIG['write_data_endpoint']}/WriteData"
        response = await self.create_job(endpoint, data, WriteDataDTO)
        return response

    @staticmethod
    async def read_sql_job(self, data: WirePayload) -> APIResponse[ReadSQLDTO]:
        logger.info(f"Creating read SQL job: {data.template}")
        endpoint = f"{API_CONFIG['read_sql_endpoint']}/ReadSql"
        response = await self.create_job(endpoint, data, ReadSQLDTO)
        return response

    @staticmethod
    async def send_email_job(self, data: WirePayload) -> APIResponse[SendEmailDTO]:
        logger.info(f"Creating send email job: {data.template}")
        endpoint = f"{API_CONFIG['send_email_endpoint']}/SendEmail"
        response = await self.create_job(endpoint, data, SendEmailDTO)
        return response

