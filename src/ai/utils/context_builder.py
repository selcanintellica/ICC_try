"""Context builder for formatting database context in user messages."""

from typing import List, Dict, Optional
from src.models.connection_map import get_connection_by_name


def build_database_context(
    connection_name: str = None,
    schema: str = None,
    table: str = None,
    columns: List[Dict] = None,
) -> str:
    """
    Build a formatted database context string to prepend to user messages.
    
    Args:
        connection_name: Name of the database connection
        schema: Schema name
        table: Table name
        columns: List of column dictionaries with keys: columnName, columnType, columnLength (optional)
    
    Returns:
        Formatted context string, or empty string if no context provided
        
    Example:
        >>> columns = [
        ...     {"columnName": "ID", "columnType": "NUMBER", "columnLength": 39},
        ...     {"columnName": "NAME", "columnType": "VARCHAR2", "columnLength": 100}
        ... ]
        >>> context = build_database_context("ORACLE_10", "ICC_TEST", "CUSTOMER", columns)
        >>> print(context)
        [Database Context]
        Connection: ORACLE_10 (Oracle)
        Schema: ICC_TEST
        Table: CUSTOMER
        Columns:
          - ID (NUMBER, length: 39)
          - NAME (VARCHAR2, length: 100)
    """
    # If no table context, return empty string
    if not table or not columns or len(columns) == 0:
        return ""
    
    context_parts = ["[Database Context]"]
    
    # Add connection info
    if connection_name:
        conn_data = get_connection_by_name(connection_name)
        if conn_data:
            db_type = conn_data.get("db_type", "Unknown")
            context_parts.append(f"Connection: {connection_name} ({db_type})")
        else:
            context_parts.append(f"Connection: {connection_name}")
    
    # Add schema
    if schema:
        context_parts.append(f"Schema: {schema}")
    
    # Add table
    if table:
        context_parts.append(f"Table: {table}")
    
    # Add columns
    if columns and len(columns) > 0:
        context_parts.append("Columns:")
        for col in columns:
            col_name = col.get("columnName", "unknown")
            col_type = col.get("columnType", "unknown")
            col_length = col.get("columnLength")
            
            if col_length:
                context_parts.append(f"  - {col_name} ({col_type}, length: {col_length})")
            else:
                context_parts.append(f"  - {col_name} ({col_type})")
    
    return "\n".join(context_parts)


def build_enhanced_message(
    user_message: str,
    connection_name: str = None,
    schema: str = None,
    table: str = None,
    columns: List[Dict] = None,
) -> str:
    """
    Build an enhanced user message with database context prepended.
    
    Args:
        user_message: The original user message
        connection_name: Name of the database connection
        schema: Schema name
        table: Table name
        columns: List of column dictionaries
    
    Returns:
        Enhanced message with context prepended if context is provided,
        otherwise returns the original message
        
    Example:
        >>> columns = [{"columnName": "ID", "columnType": "NUMBER"}]
        >>> msg = build_enhanced_message(
        ...     "Show me all customers",
        ...     connection_name="ORACLE_10",
        ...     schema="ICC_TEST",
        ...     table="CUSTOMER",
        ...     columns=columns
        ... )
        >>> print(msg)
        [Database Context]
        Connection: ORACLE_10 (Oracle)
        Schema: ICC_TEST
        Table: CUSTOMER
        Columns:
          - ID (NUMBER)
        
        [User Query]
        Show me all customers
    """
    context = build_database_context(
        connection_name=connection_name,
        schema=schema,
        table=table,
        columns=columns
    )
    
    if context:
        return f"{context}\n\n[User Query]\n{user_message}"
    else:
        return user_message

