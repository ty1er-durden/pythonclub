import flask
import flask_caching
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
    return flask.render_template("index.html", repos=repos)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
