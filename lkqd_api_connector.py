from connector_type import supply_demand_report, domains_report
import sys
import base64



# response = req.get("https://lkqd-api.firebaseio.com/")
# print(response.status_code)

reports = ['supply_domain_report','supply_app_bundleid_report','demand_domain_report','demand_app_bundleid_report']

def api_connector():

    credentials = {'Username' : '4BRrKTFu2godcuiNjBDAG9jlB48D8bJB' , 'Password': 'WrYT6g8lFJZbKLrCAzWGAScy1QkxZgpDGMYiaexxKJM'}
    credentials_string = credentials["Username"] + ":" + credentials["Password"]
    credentials_string = bytearray(credentials_string, 'utf-8')
    b64_credentials_string = base64.b64encode(credentials_string).decode("utf-8")
    credential_header =  "Basic {}".format(b64_credentials_string)
    # print(credential_header)

    if sys.argv[2] == 'supply_report' or sys.argv[2] == 'demand_report':

        data = supply_demand_report(credential_header)

        return data

    elif sys.argv[2] in reports:

        data, counter =  domains_report(credential_header)


        return data,counter



print(api_connector())