# Masonite adapter for Inertia.js

<p align="center">
<img src="https://i.imgur.com/rEXcoMn.png" width="130px">
<img src="https://avatars1.githubusercontent.com/u/47703742?s=200&v=4" width="130px">
</p>

[![Test Application](https://github.com/girardinsamuel/inertia-masonite/workflows/Test%20Application/badge.svg?branch=master)](https://github.com/girardinsamuel/inertia-masonite/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/girardinsamuel/inertia-masonite/branch/master/graph/badge.svg)](https://codecov.io/gh/girardinsamuel/inertia-masonite)
<img src="https://img.shields.io/badge/python-3.5+-blue.svg" alt="Python Version">

This repo contains the Masonite server-side adapter for [Inertia.js](https://inertiajs.com/).

## Preface

Inertia is a new approach to building classic server-driven web apps. From their own web page:

> Inertia allows you to create fully client-side rendered, single-page apps, without much of the complexity that comes with modern SPAs. It does this by leveraging existing server-side frameworks.

Inertia requires an adapter for each backend framework. This repo contains the server-side adapter for the Masonite framework.

## Requirements

To get started you will need the following:

* Masonite 2.3+
* Laravel Mix installed (new Masonite 2.3 projects come with this installed already)
* a Node.js environment (npm or yarn)

## Installation

### Install the package

```
pip install inertia-masonite
```

### Adding the ServiceProvider

We can add the provider to our `config/providers.py` file like so:

```python
# config/providers.py
# ...
from masonite.inertia import InertiaProvider

# ...
PROVIDERS = [
    # Framework Providers
    AppProvider,
    AuthenticationProvider,

    #...
    InertiaProvider,
]
```

### Adding The Middleware

This Inertia adapter comes with a middleware that will control some of the flow of data. We can add the middleware to our `config/middleware.py` file like so:

```python
# config/middleware.py
# ...
from masonite.inertia import InertiaMiddleware

# ...
HTTP_MIDDLEWARE = [
    LoadUserMiddleware,
    CsrfMiddleware,
    #...
    InertiaMiddleware,
]
```

### Installing package files

Install `inertia-masonite` config file into your project. This will create a `config/inertia.py` configuration file for the adapter.

```
python craft install:inertia
```

### Scaffold a base Vue app and a template (optional)
Then, if you want you can quicky scaffold a Vue app with two components to test Inertia behaviour by running the publish command :

```
python craft publish InertiaProvider --tag app
```

### Install NPM dependencies

First we'll need to install some NPM packages (we are using Vue here as frontend framework and `inertia-vue` as Inertia.js client-side adapter):

```
$ npm install vue @inertiajs/inertia @inertiajs/inertia-vue
```


## How to use Inertia.js with Masonite adapter

We will create two routes and a controller which will load the two components scaffolded with previous command and see Inertia.js behaviour. In order to create Inertia response in our Controller, we are going to use newly available response `InertiaResponse`. And that's it !

We can quickly create this demo (routes & controller) with the publish command :
```
$ python craft publish InertiaProvider --tag demo
```

or you can create it manually:

```
$ craft controller InertiaController
```

This will create a controller `InertiaController` but you can name it whatever you like. It would be good to keep the standard of whatever setup you have now for your home page. Then create two routes to that controller if you don't have them already:

```python
ROUTES = [
    Get('/', 'InertiaController@index'),
    Get('/helloworld', 'InertiaController@helloworld')
]
```

And finally create the controller methods. We just need to use the new `InertiaResponse` to render our controller.

```python
# app/controllers/InertiaController.py
from masonite.inertia import InertiaResponse

## ..
def inertia(self, view: InertiaResponse):
    return view.render('Index')

def helloworld(self, view: InertiaResponse):
  return view.render('HelloWorld')

## ..
```
This controller will render the view based on template `templates/app.html` and will load the Vue components into it depending on the route.
Note that instead of specifying a Jinja template like we normally do we can just specify a page here. So since we have `../pages/Index.vue` we specify to render `Index` here.


### Test it !

Ok now we need to do 2 more commands. The first thing is to run `npm run dev` (at root) to compile all of this (with webpack mix):

```
$ npm run dev
```

Now we can run the server like we normally do:

```
$ craft serve
```

When we go to our homepage we will see we see `Index.vue` component:
```
Home Page
```

Click on the link you can now see `HelloWorld` without page refresh !!!!

Congratulations! You have now setup Inertia in our project! For more information on how to use Inertia.js got to its [documentation](https://inertiajs.com/installation).


## How to contribute
TODO

### Installation

Create a virtual env and run :
```
make init
```

### Run the tests
Finally you can run the tests and start building your application.

```
$ make test
```
