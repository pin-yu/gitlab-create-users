import gitlab

gl = gitlab.Gitlab.from_config("datalab_gitlab", ["./python-gitlab.cfg"])


def create_user(query):
    gl.users.create(query)
