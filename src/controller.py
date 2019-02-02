from flask import Flask,request,jsonify
import logging
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/v1/api', methods=['POST'])
def postSomeThing():
    content = request.json
    name = content['name']
    logger.info('name: %s',name)
    return jsonify(
        processorReference='1-9-4285769',
        secureTradingResultCode='0'
    )

@app.route("/")
def hello():
    return "Hello World!"
