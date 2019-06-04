import flask
import flask_caching
import os
import repo

app = flask.Flask(__name__)
cache = flask_caching.Cache(app, config={"CACHE_TYPE": "simple"})


@cache.cached(timeout=60, key_prefix="get_git_repos")
def get_git_repos():
    return [repo["node"] for repo in repo.get_git_repos(max_repos=20)]


@app.route("/")
def index():
    try:
        repos = get_git_repos()
    except Exception:
        # Yuck.  Ugly hack for error handling.
        repos = [
            {
                "name": "Oops!",
                "updatedAt": "Cannot retrieve GitHub repositories :(",
            }
        ]
    return flask.render_template(
        "index.html",
        repos=repos,
        email_address=os.environ["EMAIL_ADDRESS"],
        github_profile=os.environ["GITHUB_PROFILE"],
        slack_channel=os.environ["SLACK_CHANNEL"],
    )


if __name__ == "__main__":
    try:
        APP_ENV = os.environ["APP_ENV"]
    except KeyError:
        APP_ENV = ""

    if APP_ENV == "production":
        app.run(host="0.0.0.0", port=80)
    else:
        app.run(host="0.0.0.0", debug=True, port=5000)
