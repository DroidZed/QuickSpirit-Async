# Quick Spirit

An easy to use HTTP client with a fast downloader.

This library was made with the famous [HTTPX](https://www.python-httpx.org/) library!

I originally intended to make a small module to refactor my networking layer in my apps using httpx, and ended up creating a library !

----

## Install

```sh
# PIP:

pip install quickspirit

# Poetry:

poetry add quickspirit

# UV:

uv add quickspirit
```

## Usage:

The library's getter function returns a bytes data repersenting the bytes coming in from the network. Since we don't know the shape of the data, I delegated the responsibility to you to figure out how to parse it to your liking.

A sample code would look like this:

```py
from quickspirit import HttpAsyncClient
from asyncio import run
from json import joads
from typing import Any

async def main():
    result = await HttpAsyncClient().get("https://some distant url returning json hopefully")

    if result.Error:
        raise result.Error


    data: dict[str, Any] = loads(result.Data)

    # do whatever you need now that you have the data...


if __name__ == "__main__":
    run(main())

```

A complete example can be found in the `example` directory.

## Testing:

Clone with git:

```bash
git clone https://github.com/DroidZed/QuickSpirit-Async && cd QuickSpirit-Async
```

Create a virtual env:

```sh
python3 -m venv .venv && .venv/Scripts/activate
```

Run the tests with pytest (install it first using your package manager of choice):

```sh
# Here I'm using uv to run the tests, but the command should be the same for other package manager:

pytest -vs .
```

