# azure_functions_HttpTriggerPython
Exemple of an Azure Functions HTTP Trigger Python that get and dump results from HTTP request.

## Exemple of execution with module requests
```Python
import requests
import json
url = "https://myapp.azurewebsites.net/api/HttpTriggerPython1?code=fctName"
userdata = { 'name': "John",
             'age' : 44 }
r = requests.post(url, params=userdata)
```

Results are obtain with the json formatting
```Python
r.json() # Dict of the results or info containing the error

r.status_code # 200 if call sucedded;  
              # 404 if url not found;
              # 500 if error in run.py (url found)
              
r.raise_for_status() # to manage error
```
