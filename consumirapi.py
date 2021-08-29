import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Col1': "A11",   
                            'Col2': "6",   
                            'Col3': "A34",   
                            'Col4': "A43",   
                            'Col5': "1169",   
                            'Col6': "A65",   
                            'Col7': "A75",   
                            'Col8': "4",   
                            'Col9': "A93",   
                            'Col10': "A101",   
                            'Col11': "4",   
                            'Col12': "A121",   
                            'Col13': "67",   
                            'Col14': "A143",   
                            'Col15': "A152",   
                            'Col16': "2",   
                            'Col17': "A173",   
                            'Col18': "1",   
                            'Col19': "A192",   
                            'Col20': "A201",   
                            'Col21': "1",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/88cee1267b3f4781be5764f390ed1fa2/services/125490b1f7b544d281c2bb1e6d430e86/execute?api-version=2.0&format=swagger'
api_key = 'jyOxencEHfed9nwFyQUkTG7r0xWbmJFXMvcsm9AfBVTh8tHZHKbz+/fTLuzC5ibEk7HvbM9b5VirmrS+GPBFnA==' 
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))