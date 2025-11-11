import os

API_CONFIG = {
    "api_base_url": os.getenv("API_BASE_URL", "https://api.example.com"),
    "read_sql_endpoint": os.getenv("Read", "/data/v2/sql"),
    "send_email_endpoint": os.getenv("Send", "/notifications/v1/email"),
    "write_data_endpoint": os.getenv("Write", "/data/v1/write"),

    "timeout": 30.0,
}