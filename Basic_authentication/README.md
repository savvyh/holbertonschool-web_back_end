# Basic Authentication

## Resources

**Read or watch**:

*   [REST API Authentication Mechanisms](/rltoken/Kb7ELziV7EkpqtPTUXY2ZQ "REST API Authentication Mechanisms")
*   [Base64 in Python](/rltoken/1xQ0i3osSq-4lpe9rz4xyQ "Base64 in Python")
*   [HTTP header Authorization](/rltoken/UR1ydNZBterguf-rCaR24w "HTTP header Authorization")
*   [Flask](/rltoken/kqL4y5TV5Orgazqpwl8ZNg "Flask")
*   [Base64 - concept](/rltoken/97wy7KWBzuiVkbKOSDUzng "Base64 - concept")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/cJmYXZqDAUuOvTffnjeRng "explain to anyone"), **without the help of Google**:

### General

*   What authentication means
*   What Base64 is
*   How to encode a string in Base64
*   What Basic authentication means
*   How to send the Authorization header

## Requirements

### Python Scripts

*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.9)
*   All your files should end with a new line
*   The first line of all your files should be exactly `#!/usr/bin/env python3`
*   A `README.md` file, at the root of the folder of the project, is mandatory
*   Your code should use the `pycodestyle` style (version 2.5)
*   All your files must be executable
*   The length of your files will be tested using `wc`
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks

### 1.

Download and start your project from this [archive.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/11/ec2f874b061bd3a2915949f081f4f5f055104f20.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250606%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20250606T072637Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=bbbedb16111ab5c6d637c53dbfeb1ee78cf56fef459de753c50955b18da33fb8 "archive.zip")

In this archive, you will find a simple API with one model: `User`. Storage of these users is done via a serialization/deserialization in files.

#### Setup and start server
```
bob@dylan:~$ pip3 install -r requirements.txt
...
bob@dylan:~$
bob@dylan:~$ API\_HOST=0.0.0.0 API\_PORT=5000 python3 -m api.v1.app
 \* Serving Flask app "app" (lazy loading)
...
bob@dylan:~$
```
#### Use the API _(in another tab or in your browser)_
```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status" -vvv
\*   Trying 0.0.0.0...
\* TCP\_NODELAY set
\* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/status HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: \*/\*
> 
\* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: application/json
< Content-Length: 16
< Access-Control-Allow-Origin: \*
< Server: Werkzeug/1.0.1 Python/3.7.5
< Date: Mon, 18 May 2020 20:29:21 GMT
< 
{"status":"OK"}
\* Closing connection 0
bob@dylan:~$
```
  

### 2.

What the HTTP status code for a request unauthorized? `401` of course!

Edit `api/v1/app.py`:

*   Add a new error handler for this status code, the response must be:
    *   a JSON: `{"error": "Unauthorized"}`
    *   status code `401`
    *   you must use `jsonify` from Flask

For testing this new error handler, add a new endpoint in `api/v1/views/index.py`:

*   Route: `GET /api/v1/unauthorized`
*   This endpoint must raise a 401 error by using `abort` - [Custom Error Pages](/rltoken/EDsuKhhXJLQ8Z0k-LNOzvQ "Custom Error Pages")

By calling `abort(401)`, the error handler for 401 will be executed.

In the first terminal:
```
bob@dylan:~$ API\_HOST=0.0.0.0 API\_PORT=5000 python3 -m api.v1.app
 \* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In a second terminal:
```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/unauthorized"
{
  "error": "Unauthorized"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/unauthorized" -vvv
\*   Trying 0.0.0.0...
\* TCP\_NODELAY set
\* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/unauthorized HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: \*/\*
> 
\* HTTP 1.0, assume close after body
< HTTP/1.0 401 UNAUTHORIZED
< Content-Type: application/json
< Content-Length: 30
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sun, 24 Sep 2017 22:50:40 GMT
< 
{
  "error": "Unauthorized"
}
\* Closing connection 0
bob@dylan:~$
```
  

### 3.

What the HTTP status code for a request where the user is authenticate but not allowed to access to a resource? `403` of course!

Edit `api/v1/app.py`:

*   Add a new error handler for this status code, the response must be:
    *   a JSON: `{"error": "Forbidden"}`
    *   status code `403`
    *   you must use `jsonify` from Flask

For testing this new error handler, add a new endpoint in `api/v1/views/index.py`:

*   Route: `GET /api/v1/forbidden`
*   This endpoint must raise a 403 error by using `abort` - [Custom Error Pages](/rltoken/EDsuKhhXJLQ8Z0k-LNOzvQ "Custom Error Pages")

By calling `abort(403)`, the error handler for 403 will be executed.

In the first terminal:
```
bob@dylan:~$ API\_HOST=0.0.0.0 API\_PORT=5000 python3 -m api.v1.app
 \* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In a second terminal:
```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/forbidden"
{
  "error": "Forbidden"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/forbidden" -vvv
\*   Trying 0.0.0.0...
\* TCP\_NODELAY set
\* Connected to 0.0.0.0 (127.0.0.1) port 5000 (#0)
> GET /api/v1/forbidden HTTP/1.1
> Host: 0.0.0.0:5000
> User-Agent: curl/7.54.0
> Accept: \*/\*
> 
\* HTTP 1.0, assume close after body
< HTTP/1.0 403 FORBIDDEN
< Content-Type: application/json
< Content-Length: 27
< Server: Werkzeug/0.12.1 Python/3.4.3
< Date: Sun, 24 Sep 2017 22:54:22 GMT
< 
{
  "error": "Forbidden"
}
\* Closing connection 0
bob@dylan:~$
```
  

### 4.

Now you will create a class to manage the API authentication.

*   Create a folder `api/v1/auth`
*   Create an empty file `api/v1/auth/__init__.py`
*   Create the class `Auth`:
    *   in the file `api/v1/auth/auth.py`
    *   import `request` from `flask`
    *   class name `Auth`
    *   public method `def require_auth(self, path: str, excluded_paths: List[str]) -> bool:` that returns `False` - `path` and `excluded_paths` will be used later, now, you don’t need to take care of them
    *   public method `def authorization_header(self, request=None) -> str:` that returns `None` - `request` will be the Flask request object
    *   public method `def current_user(self, request=None) -> TypeVar('User'):` that returns `None` - `request` will be the Flask request object

This class is the template for all authentication system you will implement.
```
bob@dylan:~$ cat main\_0.py
#!/usr/bin/env python3
""" Main 0
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.require\_auth("/api/v1/status/", \["/api/v1/status/"\]))
print(a.authorization\_header())
print(a.current\_user())

bob@dylan:~$ 
bob@dylan:~$ API\_HOST=0.0.0.0 API\_PORT=5000 ./main\_0.py
False
None
None
bob@dylan:~$
```
  

### 5.

Update the method `def require_auth(self, path: str, excluded_paths: List[str]) -> bool:` in `Auth` that returns `True` if the `path` is not in the list of strings `excluded_paths`:

*   Returns `True` if `path` is `None`
*   Returns `True` if `excluded_paths` is `None` or empty
*   Returns `False` if `path` is in `excluded_paths`
*   You can assume `excluded_paths` contains string path always ending by a `/`
*   This method must be slash tolerant: `path=/api/v1/status` and `path=/api/v1/status/` must be returned `False` if `excluded_paths` contains `/api/v1/status/`
```
bob@dylan:~$ cat main\_1.py
#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.require\_auth(None, None))
print(a.require\_auth(None, \[\]))
print(a.require\_auth("/api/v1/status/", \[\]))
print(a.require\_auth("/api/v1/status/", \["/api/v1/status/"\]))
print(a.require\_auth("/api/v1/status", \["/api/v1/status/"\]))
print(a.require\_auth("/api/v1/users", \["/api/v1/status/"\]))
print(a.require\_auth("/api/v1/users", \["/api/v1/status/", "/api/v1/stats"\]))

bob@dylan:~$
bob@dylan:~$ API\_HOST=0.0.0.0 API\_PORT=5000 ./main\_1.py
True
True
True
False
False
True
True
bob@dylan:~$
```
  

### 6.

Now you will validate all requests to secure the API:

Update the method `def authorization_header(self, request=None) -> str:` in `api/v1/auth/auth.py`:

*   If `request` is `None`, returns `None`
*   If `request` doesn’t contain the header key `Authorization`, returns `None`
*   Otherwise, return the value of the header request `Authorization`

Update the file `api/v1/app.py`:

*   Create a variable `auth` initialized to `None` after the `CORS` definition
*   Based on the environment variable `AUTH_TYPE`, load and assign the right instance of authentication to `auth`
    *   if `auth`:
        *   import `Auth` from `api.v1.auth.auth`
        *   create an instance of `Auth` and assign it to the variable `auth`

Now the biggest piece is the filtering of each request. For that you will use the Flask method [before\_request](/rltoken/UZQCfuQf9PG4mBHY9iKBog "before_request")

*   Add a method in `api/v1/app.py` to handler `before_request`
    *   if `auth` is `None`, do nothing
    *   if `request.path` is not part of this list `['/api/v1/status/', '/api/v1/unauthorized/', '/api/v1/forbidden/']`, do nothing - you must use the method `require_auth` from the `auth` instance
    *   if `auth.authorization_header(request)` returns `None`, raise the error `401` - you must use `abort`
    *   if `auth.current_user(request)` returns `None`, raise the error `403` - you must use `abort`

In the first terminal:
```
bob@dylan:~$ API\_HOST=0.0.0.0 API\_PORT=5000 AUTH\_TYPE=auth python3 -m api.v1.app
 \* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In a second terminal:
```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status/"
{
  "status": "OK"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{
  "error": "Forbidden"
}
bob@dylan:~$
```
  

### 7.

Create a class `BasicAuth` that inherits from `Auth`. For the moment this class will be empty.

Update `api/v1/app.py` for using `BasicAuth` class instead of `Auth` depending of the value of the environment variable `AUTH_TYPE`, If `AUTH_TYPE` is equal to `basic_auth`:

*   import `BasicAuth` from `api.v1.auth.basic_auth`
*   create an instance of `BasicAuth` and assign it to the variable `auth`

Otherwise, keep the previous mechanism with `auth` an instance of `Auth`.

In the first terminal:
```
bob@dylan:~$ API\_HOST=0.0.0.0 API\_PORT=5000 AUTH\_TYPE=basic\_auth python3 -m api.v1.app
 \* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In a second terminal:
```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status/"
{
  "status": "OK"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{
  "error": "Forbidden"
}
bob@dylan:~$
```
  

### 8.

Add the method `def extract_base64_authorization_header(self, authorization_header: str) -> str:` in the class `BasicAuth` that returns the Base64 part of the `Authorization` header for a Basic Authentication:

*   Return `None` if `authorization_header` is `None`
*   Return `None` if `authorization_header` is not a string
*   Return `None` if `authorization_header` doesn’t start by `Basic` (with a space at the end)
*   Otherwise, return the value after `Basic` (after the space)
*   You can assume `authorization_header` contains only one `Basic`
```
bob@dylan:~$ cat main\_2.py
#!/usr/bin/env python3
""" Main 2
"""
from api.v1.auth.basic\_auth import BasicAuth

a = BasicAuth()

print(a.extract\_base64\_authorization\_header(None))
print(a.extract\_base64\_authorization\_header(89))
print(a.extract\_base64\_authorization\_header("Holberton School"))
print(a.extract\_base64\_authorization\_header("Basic Holberton"))
print(a.extract\_base64\_authorization\_header("Basic SG9sYmVydG9u"))
print(a.extract\_base64\_authorization\_header("Basic SG9sYmVydG9uIFNjaG9vbA=="))
print(a.extract\_base64\_authorization\_header("Basic1234"))

bob@dylan:~$
bob@dylan:~$ API\_HOST=0.0.0.0 API\_PORT=5000 ./main\_2.py
None
None
None
Holberton
SG9sYmVydG9u
SG9sYmVydG9uIFNjaG9vbA==
None
bob@dylan:~$
```
  

### 9.

Add the method `def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:` in the class `BasicAuth` that returns the decoded value of a Base64 string `base64_authorization_header`:

*   Return `None` if `base64_authorization_header` is `None`
*   Return `None` if `base64_authorization_header` is not a string
*   Return `None` if `base64_authorization_header` is not a valid Base64 - you can use `try/except`
*   Otherwise, return the decoded value as UTF8 string - you can use `decode('utf-8')`
```
bob@dylan:~$ cat main\_3.py
#!/usr/bin/env python3
""" Main 3
"""
from api.v1.auth.basic\_auth import BasicAuth

a = BasicAuth()

print(a.decode\_base64\_authorization\_header(None))
print(a.decode\_base64\_authorization\_header(89))
print(a.decode\_base64\_authorization\_header("Holberton School"))
print(a.decode\_base64\_authorization\_header("SG9sYmVydG9u"))
print(a.decode\_base64\_authorization\_header("SG9sYmVydG9uIFNjaG9vbA=="))
print(a.decode\_base64\_authorization\_header(a.extract\_base64\_authorization\_header("Basic SG9sYmVydG9uIFNjaG9vbA==")))

bob@dylan:~$
bob@dylan:~$ API\_HOST=0.0.0.0 API\_PORT=5000 ./main\_3.py
None
None
None
Holberton
Holberton School
Holberton School
bob@dylan:~$
```
  

### 10.

Add the method `def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str)` in the class `BasicAuth` that returns the user email and password from the Base64 decoded value.

*   This method must return 2 values
*   Return `None, None` if `decoded_base64_authorization_header` is `None`
*   Return `None, None` if `decoded_base64_authorization_header` is not a string
*   Return `None, None` if `decoded_base64_authorization_header` doesn’t contain `:`
*   Otherwise, return the user email and the user password - these 2 values must be separated by a `:`
*   You can assume `decoded_base64_authorization_header` will contain only one `:`
```
bob@dylan:~$ cat main\_4.py
#!/usr/bin/env python3
""" Main 4
"""
from api.v1.auth.basic\_auth import BasicAuth

a = BasicAuth()

print(a.extract\_user\_credentials(None))
print(a.extract\_user\_credentials(89))
print(a.extract\_user\_credentials("Holberton School"))
print(a.extract\_user\_credentials("Holberton:School"))
print(a.extract\_user\_credentials("bob@gmail.com:toto1234"))

bob@dylan:~$
bob@dylan:~$ API\_HOST=0.0.0.0 API\_PORT=5000 ./main\_4.py
(None, None)
(None, None)
(None, None)
('Holberton', 'School')
('bob@gmail.com', 'toto1234')
bob@dylan:~$
```
  

### 11.

Add the method `def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):` in the class `BasicAuth` that returns the `User` instance based on his email and password.

*   Return `None` if `user_email` is `None` or not a string
*   Return `None` if `user_pwd` is `None` or not a string
*   Return `None` if your database (file) doesn’t contain any `User` instance with email equal to `user_email` - you should use the class method `search` of the `User` to lookup the list of users based on their email. Don’t forget to test all cases: “what if there is no user in DB?”, etc.
*   Return `None` if `user_pwd` is not the password of the `User` instance found - you must use the method `is_valid_password` of `User`
*   Otherwise, return the `User` instance
```
bob@dylan:~$ cat main\_5.py
#!/usr/bin/env python3
""" Main 5
"""
import uuid
from api.v1.auth.basic\_auth import BasicAuth
from models.user import User

""" Create a user test """
user\_email = str(uuid.uuid4())
user\_clear\_pwd = str(uuid.uuid4())
user = User()
user.email = user\_email
user.first\_name = "Bob"
user.last\_name = "Dylan"
user.password = user\_clear\_pwd
print("New user: {}".format(user.display\_name()))
user.save()

""" Retreive this user via the class BasicAuth """

a = BasicAuth()

u = a.user\_object\_from\_credentials(None, None)
print(u.display\_name() if u is not None else "None")

u = a.user\_object\_from\_credentials(89, 98)
print(u.display\_name() if u is not None else "None")

u = a.user\_object\_from\_credentials("email@notfound.com", "pwd")
print(u.display\_name() if u is not None else "None")

u = a.user\_object\_from\_credentials(user\_email, "pwd")
print(u.display\_name() if u is not None else "None")

u = a.user\_object\_from\_credentials(user\_email, user\_clear\_pwd)
print(u.display\_name() if u is not None else "None")

bob@dylan:~$
bob@dylan:~$ API\_HOST=0.0.0.0 API\_PORT=5000 ./main\_5.py 
New user: Bob Dylan
None
None
None
None
Bob Dylan
bob@dylan:~$
```
  

### 12.

Now, you have all pieces for having a complete Basic authentication.

Add the method `def current_user(self, request=None) -> TypeVar('User')` in the class `BasicAuth` that overloads `Auth` and retrieves the `User` instance for a request:

*   You must use `authorization_header`
*   You must use `extract_base64_authorization_header`
*   You must use `decode_base64_authorization_header`
*   You must use `extract_user_credentials`
*   You must use `user_object_from_credentials`

With this update, now your API is fully protected by a Basic Authentication. Enjoy!

In the first terminal:
```
bob@dylan:~$ cat main\_6.py
#!/usr/bin/env python3
""" Main 6
"""
import base64
from api.v1.auth.basic\_auth import BasicAuth
from models.user import User

""" Create a user test """
user\_email = "bob@hbtn.io"
user\_clear\_pwd = "H0lbertonSchool98!"
user = User()
user.email = user\_email
user.password = user\_clear\_pwd
print("New user: {} / {}".format(user.id, user.display\_name()))
user.save()

basic\_clear = "{}:{}".format(user\_email, user\_clear\_pwd)
print("Basic Base64: {}".format(base64.b64encode(basic\_clear.encode('utf-8')).decode("utf-8")))

bob@dylan:~$
bob@dylan:~$ API\_HOST=0.0.0.0 API\_PORT=5000 ./main\_6.py 
New user: 9375973a-68c7-46aa-b135-29f79e837495 / bob@hbtn.io
Basic Base64: Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh
bob@dylan:~$
bob@dylan:~$ API\_HOST=0.0.0.0 API\_PORT=5000 AUTH\_TYPE=basic\_auth python3 -m api.v1.app
 \* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In a second terminal:
```
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
{
  "status": "OK"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
{
  "error": "Unauthorized"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
{
  "error": "Forbidden"
}
bob@dylan:~$ 
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic test"
{
  "error": "Forbidden"
}
bob@dylan:~$
bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"
\[
  {
    "created\_at": "2017-09-25 01:55:17", 
    "email": "bob@hbtn.io", 
    "first\_name": null, 
    "id": "9375973a-68c7-46aa-b135-29f79e837495", 
    "last\_name": null, 
    "updated\_at": "2017-09-25 01:55:17"
  }
\]
bob@dylan:~$
```