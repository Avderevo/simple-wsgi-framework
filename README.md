# Simple wsgi framework

A simple WSGI compliant framework.


### Installation


Create a new directory and clone the application.

```
git clone https://github.com/Avderevo/simple-wsgi-framework.git
```

### Requirements

```
$ pip3 install uwsgi
```


In the app-test.py file, there is a presentation for the test demonstration of the framework.



### For the test run the file:


```
$ python3  app-test.py
```

In the Browser, open the page at: http://localhost:8000/ 
 or:   http://localhost:8000/product/
 
### For custom funcion of views use the file views.py


example:


```
from wsgi_app import App

app = App()

# sample view with routing:

@app.route('/', method=['GET', 'POST'])
def index(headers):
    return 'Home page'

```
### Requirements:

- python 3.5+
- uWSGI 2.0+
