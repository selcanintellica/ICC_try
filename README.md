# ICC_try

## Overview

ICC_try is an AI-driven project structured for modular agent development, configuration management, and toolkit integration. It is organized to support flexible agent workflows, prompt engineering, and model interactions.

## Folder Structure

```
src/
  ai/
    agents/         # Agent implementations
    configs/        # Configuration files and classes
    prompts/        # Prompt templates and logic
    toolkits/       # Toolkits for agent capabilities
    models/         # Model definitions and requests
    repositories/   # Data access and repository logic
    utils/          # Utility functions and builders
```

## Setup

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd ICC_try
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   Or use Poetry:
   ```sh
   poetry install
   ```

## Usage

- Main scripts and modules are located in `src/ai/`.
- Agents can be configured via the `configs` module.
- Prompts and toolkits are customizable for different agent tasks.

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.

## License

See the `LICENSE` file for details.

