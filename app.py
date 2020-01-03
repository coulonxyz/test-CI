from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/hello/<name>')
def page(name: str):
    return jsonify({'hello_world': name})


if __name__ == '__main__':
    app.run()
