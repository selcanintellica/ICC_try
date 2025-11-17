"""Helper functions for invoking ICC agents with optional database context."""

from src.ai.agents.icc_agent import icc_agent
from src.ai.utils.context_builder import build_enhanced_message
from typing import List, Dict


def invoke_agent(
    user_message: str,
    connection_name: str = None,
    schema: str = None,
    table: str = None,
    columns: List[Dict] = None,
):
    """
    Invoke ICC agent with optional database context.
    
    This function uses the existing ICC agent instance and invokes it with the user message.
    If database context is provided, it will be prepended to the user message
    in a readable format.
    
    Args:
        user_message: The user's message/query
        connection_name: Name of the database connection (optional)
        schema: Schema name (optional)
        table: Table name (optional)
        columns: List of column dictionaries (optional). Each dict should have:
            - columnName (str): Name of the column
            - columnType (str): Data type of the column
            - columnLength (str/int, optional): Length/precision of the column
    
    Returns:
        Agent response dictionary
    
    Example without context:
        >>> response = invoke_agent(
        ...     user_message="Can you help me with a SQL query?"
        ... )
    
    Example with context:
        >>> columns = [
        ...     {"columnName": "CUSTOMER_ID", "columnType": "NUMBER", "columnLength": 39},
        ...     {"columnName": "NAME", "columnType": "VARCHAR2", "columnLength": 100}
        ... ]
        >>> response = invoke_agent(
        ...     user_message="Show me all customers from USA",
        ...     connection_name="ORACLE_10",
        ...     schema="ICC_TEST",
        ...     table="CUSTOMER",
        ...     columns=columns
        ... )
    """
    # Build enhanced message with context if provided
    enhanced_message = build_enhanced_message(
        user_message=user_message,
        connection_name=connection_name,
        schema=schema,
        table=table,
        columns=columns
    )
    
    # Use the existing ICC agent instance (efficient - no recreation)
    response = icc_agent.invoke({
        "messages": [
            {"role": "user", "content": enhanced_message}
        ]
    })
    
    return response

