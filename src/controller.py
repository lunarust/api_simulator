#!/usr/bin/env python
#===============================================================================
#         FILE:
#         JIRA: ---
#        USAGE: ---
#  DESCRIPTION: ---
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: Celine H, henka@protonmail.com
# CONTRIBUTOR :
# ORGANIZATION:
#      VERSION: 0.0.1
#      CREATED:
#     REVISION:
#         TODO:
#===============================================================================


from flask import Flask,request,jsonify,Response
import logging,random,datetime,string
import xml.etree.ElementTree as ET

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route('/v1/api', methods=['POST'])
def postSomeThing():
    data = request.data
    #dataDict = json.dumps(xmltodict.parse(data))
    dataDict = json.loads(data)
    traceid = dataDict['traceId']
    trxamount = dataDict['money']['amount']
    trxcur = dataDict['money']['currency']

    logger.info('trace: %s',traceid)
    tmpresp = {'processorReference' : randomRef(),
      'ResultCode' : '0',
      'live' : 'false',
      'processorMoney': { 'amount': trxamount,
      'currency' : trxcur,
      'displayable' : trxamount+trxcur },
      'traceid': traceid
    }
    return jsonify(tmpresp)

@app.route('/v1/xml', methods=['POST'])
def getXLM():
    content = ET.fromstring(request.data)
    
    currentDT = datetime.datetime.now()
    siteref = content[1][0][1].text
    orderref = content[1][1][0].text
    amount = content[1][2][0].text
    currency = content[1][2][0].attrib.get('currencycode')

    exp = ("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><responseblock version=\"3.67\">"
          "<response type=\"RESPONSE\">"
          "<code>OK</code>"
          "<timestamp>"+currentDT.strftime("%Y-%m-%d %H:%M:%S")+"</timestamp>"
          "<live>0</live>"
          "<reference>"+randomRef()+"</reference>"
          "<security><address>0</address><postcode>0</postcode><securitycode>"+randomString(9)+"</securitycode></security>"
          "<amount currencycode=\""+currency+"\">"+amount+"</amount>"
          "<error><message>Ok</message><code>0</code></error></response></responseblock>")
    
    return Response(exp, mimetype='text/xml')    



@app.route("/")
def hello():
    return "-- Hi, should probably add a little readme in here"

def randomRef():                                                                                                                                       │Digest: sha256:89bb2ff47ea2d8fe387c7d1bdc13c9e9f5be2bc7be35b93407a571a0a67bc2da
    return str(random.randrange(1,9))+"-"+str(random.randrange(1,9))+"-"+str(random.randrange(1111111,9999999))                                        │Status: Image is up to date for nonpci-peg-dockreg01.prod.cdps.local:5000/simulator/s
                                                                                                                                                       │imple:latest
def randomString(stringLength):                                                                                                                        │Creating network "stsimulator_default" with the default driver
    letters = string.ascii_letters                                                                                                                     │Creating stsimulator_app_1
    return ''.join(random.choice(letters) for i in range(stringLength))                                                                                │Attaching to stsimulator_app_1
                                                                                                                                                       │app_1  |  * Serving Flask app "controller"
#app.run(debug=True)
