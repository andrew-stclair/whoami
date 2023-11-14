"""Flask version of whoami"""
from flask import request, Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
    """Index function, just returns request headers"""
    response = f"{request.remote_addr}\n"
    for key in request.headers:
        response += f"{key[0]}: {key[1]}\n"
    result = Response(response)
    result.headers['Content-Type'] = "text/plain; charset=utf-8"
    return result

if __name__ == "__main__":
    app.run(debug=True)
