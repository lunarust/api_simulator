from flask import Flask,request,jsonify
import logging,random
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ref=str(random.randrange(1,9))+"-"+str(random.randrange(1,9))+"-"+str(random.randrange(1111111,9999999))

@app.route('/v1/api', methods=['POST'])
def postSomeThing():
    content = request.json
    name = content['name']
    logger.info('name: %s',name)
    return jsonify(
        processorReference=ref,
        secureTradingResultCode='0'
    )

@app.route("/")
def hello():
    return "Hello World!"
