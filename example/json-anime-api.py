from typing import Any
import asyncio
from quickspirit import HttpAsyncClient
from dataclasses import dataclass
from json import loads


@dataclass()
class AnimeQuote:
    anime: str
    character: str
    quote: str

    def serialize(self):
        return {
            "anime": self.anime,
            "character": self.character,
            "quote": self.quote,
        }


async def main():
    result = await HttpAsyncClient().get("https://animechan.io/api/v1/quotes/random")

    if result.Error:
        raise result.Error

    data: dict[str, Any] = loads(result.Data)

    x = AnimeQuote(
        anime=data["data"]["anime"]["name"],
        character=data["data"]["character"]["name"],
        quote=data["data"]["content"],
    )

    print(f"{x!r}")


asyncio.run(main())
