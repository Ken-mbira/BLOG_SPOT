from . import blog

@blog.route('/')
def view():
    return 'Hello world'