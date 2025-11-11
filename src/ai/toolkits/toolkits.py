from src.ai.toolkits.icc_toolkit import ICCToolkit
from src.ai.toolkits.example_toolkit import ExampleToolkit

class Toolkits:
    icc_toolkit = ICCToolkit.get_tools()
    example_toolkit = ExampleToolkit.get_tools()