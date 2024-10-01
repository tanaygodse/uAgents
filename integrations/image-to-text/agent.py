from uagents import Agent, Model, Context
from uagents.setup import fund_agent_if_low

import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"


def query(filename, key):
    with open(filename, "rb") as f:
        data = f.read()
    print(data)
    headers = {"Authorization": f"Bearer {key}"}
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


class Request(Model):
    key: str
    path: str


class Response(Model):
    caption: str


# Agent Configuration
SEED_PHRASE = "image to text agent opaksdngj"

# Define the agent
agent = Agent(
    name="imagetotext",
    seed=SEED_PHRASE,
    endpoint=['http://localhost:8000/submit']
)

fund_agent_if_low(agent.wallet.address())

print(agent.address)


@agent.on_rest_post("/imagetotext", Request, Response)
async def handle_get(ctx: Context, req: Request) -> Response:
    image_path = req.path
    key = req.key
    response = query(image_path, key)
    caption = response[0]['generated_text']
    return Response(caption=caption)

if __name__ == "__main__":
    agent.run()
