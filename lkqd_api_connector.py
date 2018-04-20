import requests as req
import json
import pandas as pd
from payload_gen import payload_data_gen
import base64


def api_connector():

    credentials = {'Username' : '4BRrKTFu2godcuiNjBDAG9jlB48D8bJB' , 'Password': 'WrYT6g8lFJZbKLrCAzWGAScy1QkxZgpDGMYiaexxKJM'}
    credentials_string = credentials["Username"] + ":" + credentials["Password"]
    credentials_string = bytearray(credentials_string, 'utf-8')
    b64_credentials_string = base64.b64encode(credentials_string).decode("utf-8")
    credential_header =  "Basic {}".format(b64_credentials_string)
    # print(credential_header)

    offset = 0
    limit = 100000
    result_flag = True
    counter = 0
    dataframe_stack = []
    while result_flag:

        data = payload_data_gen(offset,limit)
        print(data)
        print(data['offset'])
        print(data['limit'])
        response = req.post("https://api.lkqd.com/reports", headers= {"Authorization": credential_header}, json= data)
        print(response.status_code)
        data_dict = json.loads(response.text)

        # print(data_dict)
        # print(data_dict["data"]["entries"])

        result_flag = data_dict['data']['hasMoreResults']

        counter += 1
        print("Script was ran " + str(counter) + 'times')
        offset = (limit * counter) + 1
        df = pd.DataFrame(data_dict["data"]["entries"])
        dataframe_stack.append(df)
        print(len(dataframe_stack))

    final_dataframe = pd.concat(dataframe_stack)

    return final_dataframe, counter

# print(api_connector())