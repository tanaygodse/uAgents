# UAgent Spotify Integration

## Overview
This integration makes use of blip-image-captioning-large model for image captioning using the HuggingFace Inference API.

## Setup

### 1. Set Up the Environment

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fetchai/uAgents.git
   cd uAgents/integrations/image-to-text
   ```

2. **Create and activate a virtual environment:**

    ```bash
    poetry env use python3
    poetry shell
    ```

3. **Install Dependencies**

    ```bash
    poetry install
    ```

### 2. Run the Script

Execute the script to get the agent's address and create a mailbox:

    ```bash
    python3 agent.py
    ```

Get the agent mailbox key from [Local Agent ↗️](https://agentverse.ai/agents/local) and for more reference please visit [Mailbox Guide ↗️](https://fetch.ai/docs/guides/agents/intermediate/mailbox#agent-mailboxes)
## Expected Output
Passing an URL for the image gives a caption explaining what is seen in the image.
