## Callbacks and Promises in Asynchronous Programming

Callbacks and Promises are two fundamental concepts used to manage asynchronous operations in programming. Let's break down their definitions and how they differ:

Callbacks: A callback is a function passed as an argument to another function. This function is then invoked after the first function completes its asynchronous task. The callback typically receives the result (or error) from the asynchronous operation.

Example: Imagine ordering food at a restaurant. You tell the waiter our order (the function), and then provide our phone number (the callback). The waiter (the asynchronous function) prepares our food. Once done, they call you (execute the callback) with our order ready for pickup (the result).

Promises: A Promise is an object representing the eventual completion (or failure) of an asynchronous operation. It provides a more structured approach compared to callbacks. A promise has three states:

Pending: Initial state, signifying the operation is ongoing.
Resolved: Operation completed successfully, with a resulting value.

Rejected: Operation encountered an error.
Importance of Asynchronous Operations in Web Development:

Web development heavily relies on asynchronous operations because web applications are inherently interactive and communicate with external resources. 

Callbacks and Promises for Non-Blocking I/O

Traditional synchronous programming involves blocking I/O (Input/Output) operations. The program execution halts until the I/O operation (like reading data from a file or network) finishes. 

Callbacks and Promises in Django

While Django itself doesn't directly utilize promises, it does support asynchronous operations through callbacks and other mechanisms. Here's how these concepts apply in the context of Django:

Callbacks in Django:

Asynchronous Tasks: Django provides libraries like django.core.signals and third-party libraries like Celery that allow you to define tasks to be executed asynchronously. These tasks can be triggered by events (like a user saving data) and often involve callbacks. The callback function would handle the actual processing of the task in the background.

Signals: Django's signal system allows you to connect functions (callbacks) to be executed when specific events occur within the framework. For example, you could define a callback to be triggered after a user is saved, allowing you to perform additional actions like sending an email notification.

Non-Blocking I/O with Callbacks:

Database Operations: Although Django provides an ORM for database access, some operations might involve raw SQL 

queries. Libraries like asyncpg allow for asynchronous database interactions using callbacks. You can initiate the query and define a callback to receive the results later without blocking the main thread.

Limitations of Callbacks:

Callback Hell: As the number of asynchronous operations and nested callbacks increases, code can become difficult to read and maintain, known as "callback hell."

Alternatives to Callbacks:

Async/Await: While not directly built-in, Python 3.5+ introduces async and await keywords for writing asynchronous code. This syntax offers a more readable and sequential approach compared to callbacks. Third-party libraries like Django Channels can be integrated with Django to enable writing asynchronous views and handlers using async/await.

Step 3: Real-life Examples

Duration: 8 minutes

Let's break down the concepts of callbacks and promises in our Django code with a beginner-friendly approach:

Imagine a Movie Booking Website:
You (the user) want to see available movies and theatres.
The website (Django application) needs to fetch this information from the database.

Synchronous vs. Asynchronous Operations:

Synchronous (Traditional):


Like waiting in a single line at a concession stand - the website waits for movie data, then theatre data, before showing them to you. (This is what our sync_view function does).
This can be slow if one operation takes a long time (like waiting at a crowded concession stand).

Asynchronous (Modern):


Like having two lines at the concession stand - the website fetches movie data and theatre data at the same time, showing them to you as soon as they're available. (This is what our async_view function aims to do).
This can be faster as the website doesn't have to wait for one operation to finish before starting another.

Callbacks in our code:

Think of callbacks as little messengers.

In our code, functions like get_movies and get_theatres act like these messengers.

In a synchronous approach, these functions "wait" for their data (like waiting in line) and then "report back" (return the data) to the main function (the view).

Promises (not directly used in our code):

Promises are like more advanced messengers that can tell you the status of the information they're fetching (pending, resolved, rejected).

Django doesn't directly use promises, but some libraries can introduce them for a more structured asynchronous approach.

our Code Breakdown:

We have two view functions: sync_view and async_view.

sync_view uses the synchronous approach, calling get_movies and get_theatres one after another, leading to potential delays.

async_view tries to be asynchronous, using asyncio and functions like get_movies_async and get_theatres_async. 

However, it's currently not fully asynchronous because you're still "waiting" for both tasks to finish before returning the response.

Next Steps:

To make async_view truly asynchronous, we can use await asyncio.gather(get_movies_async(), get_theatres_async()) within the function. This tells Python to wait for both asynchronous tasks to finish simultaneously, improving performance.

Keep in mind:

While asynchronous approaches can be faster, they can add complexity to the code. Start with understanding the basics and explore asynchronous libraries further when comfortable.


Step 4: Coded Example

Duration: 10 minutes

Setting up Python Virtual Environment for Django Demo

---

Step 1: Install Virtualenv

Ensure you have `virtualenv` installed. If not, you can install it using pip:

```bash
pip install virtualenv
```

Step 2: Create a New Directory for our Project

Navigate to the directory where you want to create our Django project and virtual environment:

```bash
mkdir django_async_api
cd django_async_api
```

Step 3: Create a Virtual Environment

Create a new Python virtual environment inside our project directory:

```bash
virtualenv venv
```

This will create a directory named `venv` containing an isolated Python environment.

Step 4: Activate the Virtual Environment

Activate the virtual environment. On Windows, use:

```bash
venv\Scripts\activate
```

On Unix or MacOS, use:

```bash
source venv/bin/activate
```

You'll see the virtual environment's name in our command prompt, indicating that it's active.

Step 5: Deactivate the Virtual Environment

Once you're done with the demo, deactivate the virtual environment:

```bash
deactivate
``

---

To run the demo showcasing the MVC pattern with Django, follow these steps:

1. Install Django if you haven't already:

```bash
pip install django
```

2. Create a new Django project:

```bash
django-admin startproject async_api

```

3. Navigate to the project directory:

```bash
cd async_api
```

4. Create a new Django app:

```bash
python manage.py startapp movies
```


To run the Django demo using ASGI (Asynchronous Server Gateway Interface) or WSGI (Web Server Gateway Interface), you'll need to configure our Django application accordingly. Here's what you need to do for each:

ASGI (Asynchronous Server Gateway Interface):

1. Ensure you have installed the required ASGI server. Popular choices include Daphne, uvicorn, and Hypercorn.

   ```bash
   pip install daphne
   ```

   or

   ```bash
   pip install uvicorn
   ```

2. Modify our project's `asgi.py` file to include the ASGI application:

   ```python
   import os

   from django.core.asgi import get_asgi_application

   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

   application = get_asgi_application()
   ```

3. Run our ASGI server using the appropriate command. For example, if you're using Daphne:

   ```bash
   daphne myproject.asgi:application
   ```

   or if you're using uvicorn:

   ```bash
   uvicorn async_api.asgi:application
   ```


WSGI (Web Server Gateway Interface):

1. Ensure you have a WSGI server installed. Popular choices include Gunicorn and uWSGI.

   ```bash
   pip install gunicorn
   ```

   or

   ```bash
   pip install uwsgi
   ```

2. Modify our project's `wsgi.py` file to include the WSGI application:

   ```python
   import os

   from django.core.wsgi import get_wsgi_application

   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

   application = get_wsgi_application()
   ```

3. Run our WSGI server using the appropriate command. For example, if you're using Gunicorn:

   ```bash
   gunicorn myproject.wsgi:application
   ```

   or if you're using uWSGI:

   ```bash
   uwsgi --http :8000 --module myproject.wsgi
   ```

Ensure that you replace `myproject` with the name of our Django project.

Step 6: Q&A and Troubleshooting

Duration: 10 minutes

- Open the floor for questions and discussion regarding the MVC pattern, callbacks, promises, and running the demo.
- Address any issues or confusion students may have encountered during the demonstration.
- Provide additional clarification or examples as needed.

This structured approach will help students grasp the concepts effectively while providing hands-on experience with running Django demos. Let me know if you need further assistance or if you'd like to delve deeper into any specific aspect!

https://docs.djangoproject.com/en/5.0/topics/async/
