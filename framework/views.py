
# there must be views

from wsgi_app import App

app = App()

# sample view with routing:

'''
@app.route('/', method=['GET', 'POST'])
def index(headers):
    return 'Home page'
'''
