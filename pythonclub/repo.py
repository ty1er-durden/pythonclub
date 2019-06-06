import json
import logging
import os
import requests

logger = logging.getLogger(__name__)

GITHUB_API_URL = "https://api.github.com/graphql"

try:
    GITHUB_API_TOKEN = os.environ["GITHUB_API_TOKEN"]
except KeyError:
    GITHUB_API_TOKEN = ""


def get_git_repos(max_repos: int = 10):
    """Gets information pertaining to repositories in a GitHub account

    Args:
        api_Token (str): GitHub API token (generated as per https://github.com/blog/1509-personal-api-tokens)

    Returns:
        list: A list of repositories with associated information:

    """

    headers = {"Authorization": "token {t}".format(t=GITHUB_API_TOKEN)}
    query = (
        f"{{\n"
        f"  viewer {{\n"
        f"  repositories(first: {max_repos}) {{\n"
        f"      totalCount\n"
        f"      pageInfo {{\n"
        f"        hasNextPage\n"
        f"        endCursor\n"
        f"      }}\n"
        f"      edges {{\n"
        f"        node {{\n"
        f"          name\n"
        f"          description\n"
        f"          updatedAt\n"
        f"          url\n"
        f"          releases(first:1) {{\n"
        f"            nodes {{\n"
        f"              name\n"
        f"            }}\n"
        f"          }}\n"
        f"        }}\n"
        f"      }}\n"
        f"    }}\n"
        f"  }}\n"
        f"}}\n"
    )

    req = requests.post(
        url=GITHUB_API_URL, json={"query": query}, headers=headers, timeout=5
    )
    if req.status_code != 200:
        raise RuntimeError(
            "GitHub API query failed. HTTP Error, status {n}: {text}".format(
                n=req.status_code, text=req.text
            )
        )
    else:
        result = json.loads(req.text)

    return result["data"]["viewer"]["repositories"]["edges"]
