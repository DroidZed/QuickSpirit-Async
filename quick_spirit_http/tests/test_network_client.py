import pytest
from typing import Any
from dataclasses import dataclass
from json import loads

from ..http import HttpAsyncClient


@dataclass
class CharacterData:
    id: int
    name: str

    def __init__(self, json: dict[str, Any]):
        self.id = json["id"]
        self.name = json["name"]


@dataclass
class AnimeData:
    id: int
    name: str
    altName: str

    def __init__(self, json: dict[str, Any]):
        self.id = json["id"]
        self.name = json["name"]
        self.altName = json["altName"]


@dataclass
class QuoteData:
    content: str
    anime: AnimeData
    character: CharacterData

    def __init__(self, json: dict[str, Any]):
        self.content = json["content"]
        self.anime = AnimeData(json["anime"])
        self.character = CharacterData(json["character"])


@dataclass
class Quote:
    status: str
    data: QuoteData

    def __init__(self, json: dict[str, Any]):
        self.status = json["status"]
        self.data = QuoteData(json["data"])


class TestNetworkClient:
    @pytest.mark.asyncio
    async def test_should_get_a_random_anime_quote(self):
        client = HttpAsyncClient()
        data = await client.get("https://animechan.io/api/v1/quotes/random")

        assert data.Error is None

        content: Quote = Quote(loads(data.Data))

        assert content.status == "success"

        print(content)
