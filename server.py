import flask

app = flask.Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def view():
    response = flask.Response(status=204)
    response.headers['Content-Encoding'] = 'gzip'
    return response


app.run(debug=True)
