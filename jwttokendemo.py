import jwt
import time
from datetime import datetime

"""the Unix timestamp is a way to track time as a running total of seconds. This count starts at the Unix Epoch on January 1st, 1970 at UTC.
 Therefore, the Unix timestamp is merely the number of seconds between a particular date and the Unix Epoch"""
class validateToken:
  def validate(self, token):
    decodedtoken = self.decode(token)
    print(decodedtoken['exp'])
    print(datetime.utcfromtimestamp(int(decodedtoken['exp'])).strftime('%Y-%m-%d %H:%M:%S'))
    if(time.time() < decodedtoken['exp']):
      print("Valid token")
  def encode(self, payload):
    encoded = jwt.encode(payload=userpayload, key="secret")
    return encoded
  def decode(self, encodedToken):
    decoded = jwt.decode(encodedToken, "secret", algorithms=["HS256"])
    return decoded


userpayload = {
  "grp": [
    "TestDataEngineeringWG",
    "TestDataEngineering",
    "Leads",
    "Alpha",
    "Platform"
  ],
  "sub": "vmani2",
  "iat": 1626333364,
  "exp": 1626419764
}

validate = validateToken()
encodedToken = validate.encode(userpayload)
print(encodedToken)
validate.validate(encodedToken)


'''
internal facing APIs: these are accessable only on the company(private) network
External facing APIs: These APIs are deployed and accessable from public internet
'''
