import requests as req
import json
import pandas as pd
from payload_gen import payload_supply_demand_reports_data_gen, payload_domain_reports_data_gen






def supply_demand_report(credential_header):


    data = payload_supply_demand_reports_data_gen()
    response = req.post("https://api.lkqd.com/reports", headers={"Authorization": credential_header}, json=data)

    print(response.status_code)
    data_dict = json.loads(response.text)

    if data_dict['status'] == 'error':
        print(data_dict['errors'])
    else:
        df = pd.DataFrame(data_dict['data']['entries'])

    return df



def domains_report(credential_header):

    offset = 0
    limit = 1000000
    result_flag = True
    counter = 0
    dataframe_stack = []

    while result_flag == True:

        data = payload_domain_reports_data_gen(offset, limit)
        print(data)
        print(data['offset'])
        print(data['limit'])
        response = req.post("https://api.lkqd.com/reports", headers={"Authorization": credential_header}, json=data)

        print(response.status_code)
        data_dict = json.loads(response.text)
        # print(data_dict)

        if data_dict['status'] == 'error':
            print(data_dict['errors'])
            break
        else:
            # print(data_dict["data"]["entries"])
            result_flag = data_dict['data']['hasMoreResults']
            if result_flag == False:
                break
            elif result_flag == True:
                print(result_flag)
                counter += 1
                print("Script was ran " + str(counter) + ' times')
                offset = (limit * counter) + 1
                df = pd.DataFrame(data_dict["data"]["entries"])
                print(df.columns.tolist())
                dataframe_stack.append(df)
                print(len(dataframe_stack))

    if counter == 1:
        final_dataframe = df
    elif counter > 1:
        final_dataframe = pd.concat(dataframe_stack)

    return final_dataframe, counter