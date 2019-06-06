import flask
import flask_caching
import os
import config
import logging
import repo

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)


app = flask.Flask(__name__)

cache = flask_caching.Cache(app, config={"CACHE_TYPE": "simple"})


@cache.cached(timeout=600, key_prefix="get_git_repos")
def get_git_repos():
    return [repo["node"] for repo in repo.get_git_repos(max_repos=20)]


@app.route("/")
def index():
    try:
        repos = get_git_repos()
    except Exception as e:
        # Yuck.  Ugly hack for error handling.
        logger.warning("Failed to retrieve repos: {e}".format(e=e))
        repos = [
            {
                "name": "Oops!",
                "updatedAt": "Cannot retrieve GitHub repositories :(",
            }
        ]
    return flask.render_template(
        "index.html",
        repos=repos,
        email_address=config.EMAIL_ADDRESS,
        github_profile=config.GITHUB_PROFILE,
        slack_channel=config.SLACK_CHANNEL,
    )


if __name__ == "__main__":

    try:
        APP_ENV = os.environ["APP_ENV"]
    except KeyError:
        APP_ENV = "dev"

    port = 5000
    debug = True
    if APP_ENV == "production":
        port = 80
        debug = False
    logger.info(
        "Bringing up app in environment '{env}' on port {p}".format(
            env=APP_ENV, p=port
        )
    )
    app.run(host="0.0.0.0", debug=debug, port=port)
