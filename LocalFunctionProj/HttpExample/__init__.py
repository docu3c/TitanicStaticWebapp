import logging
import json
import os
import ssl
import requests 

import azure.functions as func
# from azure.functions import HttpResponse



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP-triggered function processed a request.")

    if req.method == 'POST':
        data = req.get_json()
        body = str.encode(json.dumps([data]))
        
        
        def allowSelfSignedHttps(allowed):
            # bypass the server certificate verification on client side
            if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
                ssl._create_default_https_context = ssl._create_unverified_context
        
        allowSelfSignedHttps(True)
        
        #body = str.encode(json.dumps([data]))
        
        url = "http://8497b35f-5aee-4ab4-882f-43cea7a2fb8e.eastus.azurecontainer.io/score"

        api_key = 'QgdsQr60k3sOVtOYOwXcZYOdKui1NUg9'
        if not api_key:
            raise Exception("A key should be provided to invoke the endpoint")
        


        headers = {'Content-Type':'application/json', 'Authorization':('Bearer ' + api_key)}

        r = requests.post(url=url, data=body, headers=headers)
        print(r.status_code)
        print(r.content)

        result = r.content
         
    return func.HttpResponse(result)
    
