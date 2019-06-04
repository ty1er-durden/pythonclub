# pythonclub

## Run on Local Machine (on port 5000)

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

Create a GitHub toke as per:
https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line

Set Environmet variables (substituting for actual values):

```bash
cd pythonclub
echo APP_ENV=dev > .env
echo SLACK_CHANNEL=https://{{ workspace }}.slack.com/messages/{{ channel }}/ >> .env
echo EMAIL_ADDRESS={{ email }} >> .env
echo GITHUB_PROFILE={{ github_profile }} >> .env
echo GITHUB_API_TOKEN={{ github_token }} >> .env
set -o allexport && source .env && set +o allexport
```

Start web server:

```bash
cd pythonclub/pythonclub
python pythonclub/main.py
```

Browse to http://localhost:5000/

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
