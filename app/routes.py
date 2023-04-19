from app import app

@app.route('/')
@app.route('/index')
def index ():
    return "Hello, World! <br> and FACK U BEACH!"

@app.route('/blog')
def blog ():
    return "HELLO THIS IS MY BLOG, NICE TO MEET U <br> and HAVE A GOOD DAY, BEACHES!"