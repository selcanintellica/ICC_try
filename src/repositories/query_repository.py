from src.utils.config import API_CONFIG
from src.models.query import QueryPayload, QueryResponse
from src.repositories.base_repository import BaseRepository


class QueryRepository(BaseRepository):

    # Although this method called get, it actually sends a POST request with the query payload
    @staticmethod
    async def get_column_names(self, data: QueryPayload):
        endpoint = f"{API_CONFIG['query_api_base_url']}"
        response = await self.post_request(endpoint, data, QueryResponse)
        return response

