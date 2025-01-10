# Quick Spirit

An easy to use HTTP client with a fast downloader.

This library was made with the famous [HTTPX](https://www.python-httpx.org/) library!

I originally intended to make a small module to refactor my networking layer in my apps using httpx, and ended up creating a library !

--

## Install

```sh
# PIP:

pip install quickspirit

# Poetry:

poetry add quickspirit

# UV:

uv add quickspirit
```

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

## License

This project is under the GPL 3.0 License. See [Corresponding file](/LICENSE)
