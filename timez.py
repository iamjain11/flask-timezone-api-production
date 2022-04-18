from flask import Flask, jsonify, make_response, request
import pytz
import logging
from sys import stderr

log_format = '[%(asctime)s] %(name)s:%(levelname)s %(module)s:%(funcName)s %(message)s'

logging.basicConfig(
    stream=stderr,
    format=log_format,
    level=logging.INFO
)

app = Flask(__name__)

@app.route("/timezone/<timezone_name>")
def get_timezone(timezone_name):

    logging.info("get_timezone executed successfully")

    return jsonify(pytz.all_timezones)


if __name__=="__main__":
    app.run(debug=True, port=8080)