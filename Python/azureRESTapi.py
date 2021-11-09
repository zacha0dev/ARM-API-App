#------------------------------------------------------------------------------   
#   
#    
# THIS CODE AND ANY ASSOCIATED INFORMATION ARE PROVIDED “AS IS” WITHOUT   
# WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT   
# LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS   
# FOR A PARTICULAR PURPOSE. THE ENTIRE RISK OF USE, INABILITY TO USE, OR    
# RESULTS FROM THE USE OF THIS CODE REMAINS WITH THE USER.   
#   
#------------------------------------------------------------------------------ 

# Title: ARM REST API App 
# Author: Zachary Allen 
# Version: 1.0 
# Start Date: November 9th, 2021

# import libraries 
# requires running below install
# 'pip install requests adal'
import adal
import requests
import os
import json

# Set Environment Variables 
# sub variable stored for later use 
sub = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
# env variables for use in the call 
os.environ['AZURE_TENANT_ID'] = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
os.environ['AZURE_CLIENT_ID'] = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
os.environ['AZURE_CLIENT_SECRET'] = "abcd1234wxyz"

# Call Environment Variables 
tenant = os.environ['AZURE_TENANT_ID']
authority_url = 'https://login.microsoftonline.com/' + tenant
client_id = os.environ['AZURE_CLIENT_ID']
client_secret = os.environ['AZURE_CLIENT_SECRET']
resource = 'https://management.azure.com/'

# Receive an Authorization Token 
context = adal.AuthenticationContext(authority_url)
# Extract the Bearer authorization token
token = context.acquire_token_with_client_credentials(resource, client_id, client_secret)

# Build a request to the ARM API 
headers = {'Authorization': 'Bearer ' + token['accessToken'], 'Content-Type': 'application/json'}

# Create a query-string parameter 
params = {'api-version': '2016-06-01'}

# URL for request 
url = 'https://management.azure.com/' + 'subscriptions'

# Preform request and print the response
r = requests.get(url, headers=headers, params=params)
print(json.dumps(r.json(), indent=4, separators=(',', ': ')))

# References 
# 1 ] https://docs.microsoft.com/en-us/rest/api/ 
# 2] https://lnx.azurewebsites.net/azure-resource-manager-api-calls-from-python/