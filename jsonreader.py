import json

def read_json():
     with open('sample.json') as f:
          jsondata = json.load(f)
          print(jsondata['menu'])
          print(jsondata)
          print(json.dumps(jsondata))

def writeJson():
     #write dictionary as json to a file
     dict={'id': 'file', 'value': 'File', 'popup': {'menuitem': [{'value': 'New', 'onclick': 'CreateNewDoc()'}, {'value': 'Open', 'onclick': 'OpenDoc()'}, {'value': 'Close', 'onclick': 'CloseDoc()'}]}}
     with open('json_writer.json','w') as jw:
          jw.write(json.dumps(dict))
     #string to json object
     str = '{"menu": {"id": "file", "value": "File", "popup": {"menuitem": [{"value": "New", "onclick": "CreateNewDoc()"}, {"value": "Open", "onclick": "OpenDoc()"}, {"value": "Close", "onclick": "CloseDoc()"}]}}}'
     print(json.loads(str))

read_json()
writeJson()

