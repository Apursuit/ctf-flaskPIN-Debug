from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'At /read,you can read what you want by url?filename='

@app.route('/read',methods=['GET','POST'])
def read_file():
    filename = request.args.get('filename')
    if filename:
        with open(filename, 'r') as f:
            data = f.read()
    return data

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='8080')

