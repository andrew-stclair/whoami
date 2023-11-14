"""Flask version of whoami"""
import platform
import json
from flask import request, Flask, Response

app = Flask(__name__)

@app.route("/")
def index():
    """Index function, just returns request headers"""
    response = "Client:\n"
    for key in request.headers:
        response += f"  {key[0]}: {key[1]}\n"
    response += "\nServer:\n"
    ip = request.remote_addr
    if "X-Forwarded-For" in request.headers:
        ip = request.headers['X-Forwarded-For']
    response += f"  Ip: {ip}\n"
    response += f"  Server: {platform.node()}"
    result = Response(response)
    result.headers['Content-Type'] = "text/plain; charset=utf-8"
    return result

@app.route("/json")
def json_api():
    """Index function, just returns request headers"""
    response = {"Client":{},"Server":{}}
    for key in request.headers:
        response['Client'][key[0]] = key[1]
    response['Server']['Ip'] = request.remote_addr
    if "X-Forwarded-For" in request.headers:
        response['Server']['Ip'] = request.headers['X-Forwarded-For']
    response['Server']['Server'] = platform.node()
    result = Response(json.dumps(response, indent=2))
    result.headers['Content-Type'] = "application/json; charset=utf-8"
    return result

if __name__ == "__main__":
    app.run(debug=True)
