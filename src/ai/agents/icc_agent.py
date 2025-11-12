"""Workflow for running a LangGraph ReAct agent with a weather tool and a chat model."""

import json
from langgraph.prebuilt import create_react_agent
import logging
from src.ai.configs.configs import AgentConfigs

logging.basicConfig(level=logging.INFO)


# ===================== CREATE AGENT USING CONFIG ===========================
icc_agent = create_react_agent(**AgentConfigs.icc_config)


# ====================== RUN
response = icc_agent.invoke({"messages": [{"role": "user", "content": "Can you read following sql? SELECT * FROM customers WHERE country = 'USA';"}]})
logging.info(json.dumps(response, indent=2, default=str))
# logging.info(response["messages"][-1].content)
