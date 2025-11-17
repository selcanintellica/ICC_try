"""Connection mapping for ICC database connections."""

from typing import Dict, Any, Optional


CONNECTIONS: Dict[str, Dict[str, Any]] = {
    "Cassandra": {
        "id": "5861393593217446",
        "db_type": "Cassandra",
        "url": "jdbc:cassandra://172.16.44.17:9042;AuthMech=1",
        "user": "cassandra",
    },
    "HANA": {
        "id": "8448800292564427",
        "db_type": "SAP HANA",
        "url": "jdbc:sap://172.16.44.15:39015",
        "user": "SYSTEM",
    },
    "Hive": {
        "id": "8453303386327603",
        "db_type": "Hive",
        "url": "jdbc:hive2://172.16.44.17:10000/default",
        "user": "hive",
    },
    "MSSQL": {
        "id": "8449030761986558",
        "db_type": "SQL Server",
        "url": "jdbc:sqlserver://172.16.44.11:1433;databaseName=master",
        "user": "sa",
    },
    "Mongo": {
        "id": "2929902649070900",
        "db_type": "MongoDB",
        "url": "mongodb://172.16.44.11:27017/testdb",
        "user": "testuser",
    },
    "NETEZZA": {
        "id": "1829742320324078",
        "db_type": "Netezza",
        "url": "jdbc:netezza://172.16.44.13:5480/SYSTEM",
        "user": "admin",
    },
    "ORACLE_10": {
        "id": "955448816772621",
        "db_type": "Oracle",
        "url": "jdbc:oracle:thin:@172.16.44.10:1521:ORCL19C",
        "user": "icc_test",
    },
    "ORACLE_11": {
        "id": "9592123237737",
        "db_type": "Oracle",
        "url": "jdbc:oracle:thin:@172.16.44.11:1521:ORCL19C",
        "user": "ICC_META",
    },
    "oracle_18": {
        "id": "23061586410134803",
        "db_type": "Oracle",
        "url": "jdbc:oracle:thin:@172.16.44.18:1521:ORCL19C",
        "user": "ICC_DEV_META",
    },
    "POSTGRE_11": {
        "id": "955225233921727",
        "db_type": "PostgreSQL",
        "url": "jdbc:postgresql://172.16.44.11:5432/postgres",
        "user": "postgres",
    },
    "POSTGRE_14": {
        "id": "2433676967192755",
        "db_type": "PostgreSQL",
        "url": "jdbc:postgresql://172.16.44.14:5432/postgres",
        "user": "icc_test",
    },
    "POSTGRE_DEMO": {
        "id": "3134782933199896",
        "db_type": "PostgreSQL",
        "url": "jdbc:postgresql://172.16.44.21:5432/postgres",
        "user": "postgres",
    },
    "Postgresql": {
        "id": "8449161086856529",
        "db_type": "PostgreSQL",
        "url": "jdbc:postgresql://172.16.44.11:5432/postgres",
        "user": "icc",
    },
    "VFPT_POSTGRESQL": {
        "id": "31817712937260880",
        "db_type": "PostgreSQL",
        "url": "jdbc:postgresql://172.16.44.21:5432/postgres",
        "user": "postgres",
    },
    "SFTP_SERVER": {
        "id": "32050305818626884",
        "db_type": "SFTP",
        "url": "ftp://172.16.22.10:22",
        "user": "sftpuser",
    },
    "ozlem_908": {
        "id": "13926603303722332",
        "db_type": "Azure Data Lake",
        "url": None,
        "user": None,
    },
    "piateam_azure_data_lake": {
        "id": "13924989252846968",
        "db_type": "Azure Data Lake",
        "url": "https://storagepiateam.blob.core.windows.net",
        "user": "icc-no-reply@intellica.net",
    },
}


# Reverse lookup: ID to connection name
CONNECTION_ID_MAP: Dict[str, str] = {
    conn_data["id"]: conn_name for conn_name, conn_data in CONNECTIONS.items()
}


def get_connection_by_name(name: str) -> Optional[Dict[str, Any]]:
    """
    Get connection data by name.
    
    Args:
        name: Connection name
        
    Returns:
        Connection data dictionary or None if not found
        
    Example:
        >>> conn = get_connection_by_name("ORACLE_10")
        >>> print(conn["id"])
        955448816772621
    """
    return CONNECTIONS.get(name)


def get_connection_by_id(connection_id: str) -> Optional[Dict[str, Any]]:
    """
    Get connection data by ID.
    
    Args:
        connection_id: Connection ID string
        
    Returns:
        Connection data dictionary or None if not found
        
    Example:
        >>> conn = get_connection_by_id("955448816772621")
        >>> print(conn["db_type"])
        Oracle
    """
    name = CONNECTION_ID_MAP.get(connection_id)
    if name:
        return CONNECTIONS.get(name)
    return None


def get_connection_id(name: str) -> Optional[str]:
    """
    Get connection ID by name.
    
    Args:
        name: Connection name
        
    Returns:
        Connection ID string or None if not found
        
    Example:
        >>> conn_id = get_connection_id("ORACLE_10")
        >>> print(conn_id)
        955448816772621
    """
    conn = CONNECTIONS.get(name)
    return conn["id"] if conn else None


def get_connection_name_by_id(connection_id: str) -> Optional[str]:
    """
    Get connection name by ID.
    
    Args:
        connection_id: Connection ID string
        
    Returns:
        Connection name or None if not found
        
    Example:
        >>> name = get_connection_name_by_id("955448816772621")
        >>> print(name)
        ORACLE_10
    """
    return CONNECTION_ID_MAP.get(connection_id)


def list_all_connections() -> Dict[str, Dict[str, Any]]:
    """
    Get all connections.
    
    Returns:
        Dictionary of all connections
    """
    return CONNECTIONS.copy()

