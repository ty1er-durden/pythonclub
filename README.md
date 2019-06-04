# pythonclub

## Run on Local Machine (on port 80)

Install poetry:

```bash
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

Clone the repo:

```bash
git clone https://github.com/ty1er-durden/pythonclub
```

Create and activate virtual environment:

```bash
python3 -m venv .venv
. .venv/bin/activate
```

Install dependencies:

```bash
poetry install
```

Start web server:

```bash
cd pythonclub/pythonclub
python main.py
```

## Run on Docker (on port 80)

Clone the repo:

```bash
git clone https://github.com/ty1er-durden/pythonclub
```

```bash
cd pythonclub
docker build -t pythonclub .
docker run --name pythonclub -e GITHUB_API_TOKEN=${GITHUB_API_TOKEN} -p 80:80 pythonclub:latest
```
