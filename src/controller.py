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


from flask import Flask,request,jsonify,Markup
import logging,random,datetime
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
    ref=str(random.randrange(1,9))+"-"+str(random.randrange(1,9))+"-"+str(random.randrange(1111111,9999999))
    tmpresp = {'processorReference' : ref,
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
    #for child in content:
    #   print child.tag, child.attrib
    ref=str(random.randrange(1,9))+"-"+str(random.randrange(1,9))+"-"+str(random.randrange(1111111,9999999))
    currentDT = datetime.datetime.now()
    siteref = content[1][0][1].text
    orderref = content[1][1][0].text
    amount = content[1][2][0].text
    currency = content[1][2][0].attrib.get('currencycode')

    exp = ("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?><responseblock version=\"3.67\">"
          "<response type=\"RESPONSE\">"
          "<code>ACCEPTED</code>"
          "<timestamp>"+currentDT.strftime("%Y-%m-%d %H:%M:%S")+"</timestamp>"
          "<live>1</live>"
          "<reference>"+ref+"</reference>"
          "<security><address>0</address><postcode>0</postcode><securitycode>XXX</securitycode></security>"
          "<amount currencycode=\""+currency+"\">"+amount+"</amount>"
          "<error><message>Ok</message><code>0</code></error></response></responseblock>")

    tmpresp = {'processorReference' : ref,
      'ResultCode' : '0',
      'live' : 'false',
      'processorMoney': { 'amount': amount,
      'currency' : currency,
      'displayable' : amount+currency }
    }
    return jsonify(tmpresp)

    #return (exp) 

@app.route("/")
def hello():
    return "Hello World!"

app.run(debug=True)
