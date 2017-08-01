import os
import json

name = os.environ['REQ_QUERY_NAME']
age = os.environ['REQ_QUERY_AGE']

response = open(os.environ['res'], 'w')
json.dump({'name':name,'age':age}, response)
response.close()
