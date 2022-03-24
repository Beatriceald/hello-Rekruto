from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def query():
    name = request.args.get('name')
    message = request.args.get('message')
    return '''
              <h1>Hello, {}!</h1>
              <h1>{}</h1>'''.format(name, message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)              
