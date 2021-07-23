#We have 4 different most widely used http methods GET, PUT, POST and DELETE

#More info on rest is at
#https://www.educative.io/courses/web-application-software-architecture-101/qADAzX6yorR?aid=5082902844932096&utm_source=google&utm_medium=cpc&utm_campaign=dynamic2&utm_term=&utm_campaign=Dynamic+Search+ads+-+India+-+NEW&utm_source=adwords&utm_medium=ppc&hsa_acc=5451446008&hsa_cam=11957940667&hsa_grp=113685778257&hsa_ad=489097595984&hsa_src=g&hsa_tgt=aud-477877425076:dsa-904715088424&hsa_kw=&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQjwxdSHBhCdARIsAG6zhlVAs3dtg0SoZztSUwkX2zMrR8foTe8cOWcLFiGsEhAAmax2C4aeZYgaAjgwEALw_wcB

'''a GET request, by specification, can be resubmitted with the assumption that it will not change anything on the server.
This is not the case for a HTTP POST which by specification can change the status of the application running on the server.

So, by specification, one can perform an HTTP GET against a page N number of times without worrying of being changing its status.
'''

'''
while PUT is generally used to update existing state of an application and DELETE is used to delete any record and change state of application
'''

import requests
import json

response = requests.get('https://postman-echo.com/get?test=123')
print(response.status_code)
print(json.dumps(response.json()))

