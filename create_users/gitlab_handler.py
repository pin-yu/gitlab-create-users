import gitlab

gl = gitlab.Gitlab.from_config("datalab_gitlab", ["./python-gitlab.cfg"])


def create_user(query):
    try:
        gl.users.create(query)
        print("create a user: {}".format(query))
    except gitlab.exceptions.GitlabHttpError:
        print("user exists".format(query))
