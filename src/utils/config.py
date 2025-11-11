import os

API_CONFIG = {
    "api_base_url": os.getenv("API_BASE_URL", "https://172.16.22.13:8084/job/save"),
    "query_api_base_url": os.getenv("QUERY_API_BASE_URL", "https://172.16.22.13:8084/utility/query"),
    "job_search_url": os.getenv("JOB_SEARCH_URL", "https://172.16.22.13:8084/search"),
    "timeout": 30.0,
}