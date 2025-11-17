"""ICC Agent - Main agent module for data operations and workflow automation."""

import json
from langchain.agents import create_agent
import logging
from src.ai.configs.configs import AgentConfigs

logging.basicConfig(level=logging.INFO)


# Create ICC agent with configuration
icc_agent = create_agent(**AgentConfigs.icc_config)


# Example usage
if __name__ == "__main__":
    response = icc_agent.invoke({
        "messages": [{
            "role": "user", 
            "content": "Can you read following sql? SELECT * FROM customers WHERE country = 'USA';"
        }]
    })
    logging.info(json.dumps(response, indent=2, default=str))
