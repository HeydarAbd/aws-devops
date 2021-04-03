from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "Hello madafaka World!"

@app.route('/HYDR')
def my_function():
    return "This is my fucking page, bitches!"


@app.route('/third/subthird')
def last_function():
    return "Shut the fuck up"


@app.route("/fourth/<string:id>")
def fourth(id):
    return f'ID of this page is {id}'



if __name__=='__main__':
    app.run(debug = True)

