from connector_type import supply_demand_report, domains_report
import sys
import base64






def api_connector():

    credentials = {'Username' : '' , 'Password': ''}
    credentials_string = credentials["Username"] + ":" + credentials["Password"]
    credentials_string = bytearray(credentials_string, 'utf-8')
    b64_credentials_string = base64.b64encode(credentials_string).decode("utf-8")
    credential_header =  "Basic {}".format(b64_credentials_string)
    # print(credential_header)

    if sys.argv[2] == 'supply_report' or sys.argv[2] == 'demand_report':

        data = supply_demand_report(credential_header)

        return data

    elif sys.argv[2] == "supply_domain_report" or sys.argv[2] == "supply_app_bundleid_report":

        data, counter =  domains_report(credential_header)

        return data,counter



# print(api_connector())
