# python-rest-api-docker



```bash
sudo docker build -t dockreg01.local:5000/simulator/simple .
sudo docker push dockreg01.local:5000/simulator/simple
```

- [Flak rest article](http://blog.luisrei.com/articles/flaskrest.html)
- [Full stack python flask](https://www.fullstackpython.com/flask.html)                                                                   - [Flask documentation](http://flask.pocoo.org/)     
- [xml element tree](https://docs.python.org/2/library/xml.etree.elementtree.html)



#steps to run the sample rest service on docker -

                                                                                       
1. Navigate to http://locahost:5152/ for the simple web entry                          
                                                                                       
2. to access xml content:                                                              
you will need to poitn to http://localhost:5152/v1/xml                                 

Ex. --

```bash
curl --header "Content-Type:  text/xml;charset=utf-8" --requet POST --data '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><requestblock version="3.67"><alias>pegasus-demo@concentric.global</alias><request type="REFUND"><operation><accounttypedescription>CFT</accounttypedescription><sitereference>test_mifinitythirteen71401</sitereference></operation><merchant><orderreference>1603fcd1-8965XX804-af7f-763b2dfeb2c6</orderreference><chargedescription>PMC with Card included</chargedescription></merchant><billing><amount currencycode="GBP">479</amount><payment><expirydate>01/2022</expirydate><pan>XXXXXXXXXX</pan></payment></billing></request></requestblock>' http://127.0.0.1:5000/v1/xml
```

2. json
http://localhost:5152/v1/api 
