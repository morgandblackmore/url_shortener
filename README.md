# url_shortener

Url Shortener is a Flask application to take any given url and shorten it. 

The app takes a long url and returns a base url with a randomly generated 5 character hash as an endpoint. Copying that shortened url into your browser will redirect you to the original. Additionally, you have the option of reentering the original and the shortened urls, thereby generating a base url with with a randomly generated 10 character hash as an endpoint.
The hash algorithm is simply done by using random.choices to select the number of characters from a set of all string.digits and string.ascii_letters. These are stored together in a SQLite database for future retrieval.

To run locally you'll need to do the following:

1. clone this repo locally

2. create a virtual environment and activate  
`python -m venv my_env`  
`source my_env/bin/activate` (or `my_env\Scripts\activate` if on Windows)

3. run Flask  
`flask run`

Resources:  
Building a URL Shortener in Flask: https://youtu.be/rGQKHpjMn_M  
Flask Mega Tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world  
flask_unittest: https://github.com/TotallyNotChase/flask-unittest
