import os
import requests
import json
# from nrql.api import NRQL
# nrql = NRQL()
api_key = os.getenv('NR_API_KEY')
account_id = os.getenv('NR_ACCOUNT_ID')

field = input("enter the value to count: ")
print(field)
values = ['host', 'hostname', 'hostStatus', 'fullHostname']
if field in values:
    print(f"This is the value entered {field}")
nrql: str = f"select count{field} FROM ContainerSample where imageName ='postgres:15' since 1 week ago LIMIT MAX "

graph_query = """{
    actor {
        account(id: %s) {
            nrql(query: \"%s\") {
                results
            }
        }
    }
}""" % (account_id, nrql)

url = "https://api.newrelic.com/graphql"
headers = {
    "Content-Type": "application/json",
    "API-Key": api_key,
}
payload = json.dumps({"query": graph_query})
response = requests.request("POST", url, headers=headers, data=payload)
print(response.json())
