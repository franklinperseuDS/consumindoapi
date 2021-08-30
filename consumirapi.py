#!/usr/bin/env python
# coding: utf-8


## Import Libraries

import streamlit as st
import urllib.request
import json


# título
st.title("Web Data Credit Risck") 
# subtítulo
st.markdown("Este é um Data App utilizado para prever risco de crédito. O app é baseado em um modelo treinado no Azure Machine Learning Studio https://studio.azureml.net")
# subtítulo
st.markdown("Este é um Data App for desenvolvido pelo Prof.Fábio Santos (fssilva@uea.edu.r)")


Col1 = st.text_input("Status of checking account", key="Col1", value="A11")
Col2 = st.text_input("Duration in months", key="Col2", value="6")
Col3 = st.text_input("Credit history", key="Col3", value="A34")
Col4 = st.text_input("Purpose", key="Col4", value="A43")
Col5 = st.text_input("Credit amount", key="Col5", value="1169")
Col6 = st.text_input("Savings account/bond", key="Col6", value="A65")
Col7 = st.text_input("Present employment since", key="Col7", value="A75")
Col8 = st.text_input("Installment rate in percentage of disposable income", key="Col8", value="4")
Col9 = st.text_input("Personal status and sex", key="Col9", value="A93")
Col10 = st.text_input("Other debtors", key="Col10", value="A101")
Col11 = st.text_input("Present residence since", key="Col11", value="4")
Col12 = st.text_input("Property", key="Col12", value="A121")
Col13 = st.text_input("Age in years", key="Col13", value="67")
Col14 = st.text_input("Other installment plans", key="Col14", value="A143")
Col15 = st.text_input("Housing", key="Col15", value="A152")
Col16 = st.text_input("Number of existing credits", key="Col16", value="2")
Col17 = st.text_input("Job", key="Col17", value="A173")
Col18 = st.text_input("Number of people providing maintenance for", key="Col18", value="1")
Col19 = st.text_input("Telephone", key="Col19", value="A192")
Col20 = st.text_input("Foreign worker", key="Col20", value="A201")

# inserindo um botão na tela
btn_predict = st.button("Realizar Previsão")

if btn_predict:
    data = {
        "Inputs": {
                "input1":
                [
                    {
                            'Col1': Col1,   
                            'Col2': Col2,   
                            'Col3': Col3,   
                            'Col4': Col4,   
                            'Col5': Col5,   
                            'Col6': Col6,   
                            'Col7': Col7,   
                            'Col8': Col8,   
                            'Col9': Col9,   
                            'Col10': Col10,   
                            'Col11': Col11,   
                            'Col12': Col12,   
                            'Col13': Col13,   
                            'Col14': Col14,   
                            'Col15': Col15,   
                            'Col16': Col16,   
                            'Col17': Col17,   
                            'Col18': Col18,   
                            'Col19': Col19,   
                            'Col20': Col20,   
                            'Col21': "",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/69230cb4ad874e3faaaf3661c7a32e4a/services/551db395143e46018c6eb1471622c270/execute?api-version=2.0&format=swagger'
    api_key = 'jyOxencEHfed9nwFyQUkTG7r0xWbmJFXMvcsm9AfBVTh8tHZHKbz+/fTLuzC5ibEk7HvbM9b5VirmrS+GPBFnA==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        print(result )
        parsed_json = (json.loads(result))

        print(parsed_json)
        y = json.loads(json.dumps(parsed_json, indent=4, sort_keys=True))
        x = y['Results']
        z = x['output1']
        m = z[0]
        #print(m['Scored Labels'])
             
        if m['Scored Labels'] == '1':
            st.markdown("Previsão de Risco = Baixo Risco")
        else:
            st.markdown("Previsão de Risco = Alto Risco")
            
       
                 
        
            
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
else:
    print("error")
    
	
	
