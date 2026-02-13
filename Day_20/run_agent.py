import asyncio
from browser_use import Agent, ChatGoogle
from dotenv import load_dotenv

load_dotenv()

async def main():
    llm = ChatGoogle(model="gemini-2.5-flash")

    agent = Agent(
        task="Open https://news.ycombinator.com and find the #1 post under Show HN",
        llm=llm
    )

    result = await agent.run()
    print(result)

asyncio.run(main())
