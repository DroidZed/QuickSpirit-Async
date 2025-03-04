from dataclasses import dataclass
import pytest
from typing import Any
from json import loads

from quickspirit import HttpAsyncClient


@dataclass
class SingleResp:
    message: str
    fileName: str

    def __init__(self, json: dict[str, Any]):
        self.message = json["message"]
        self.fileName = json["fileName"]


class TestUploadFile:
    @pytest.mark.asyncio
    async def test_should_send_one_file(self):
        client = HttpAsyncClient()
        data = await client.post(
            "http://localhost:7000/api/upload-single",
            files={"file": ("a.txt", open("a.txt", "rb"), "text/plain")},
        )

        assert data.Error is None
        assert data.Data is not None

        content: SingleResp = SingleResp(loads(data.Data))

        assert content.message == "Uploaded"

        print(content)
