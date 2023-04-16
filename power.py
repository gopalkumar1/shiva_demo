# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)

@app.route('/power')
def power():
    num1 = request.args.get('num')
    # calculate the square of num1
    result = int(num1) ** 3
    # return the result as a string
    return str(result)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
