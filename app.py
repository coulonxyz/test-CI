from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/hello/<name>')
def page(name: str):
    if name.lower().startswith('j'):
        return jsonify({'hello': 'j-dog'})
    return jsonify({'hello': name})


if __name__ == '__main__':
    app.run()
