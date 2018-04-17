import requests as req
import json
import pandas as pd
from payload_gen import payload_data_gen



def api_connector():

    credentials = {'Username' : '4BRrKTFu2godcuiNjBDAG9jlB48D8bJB' , 'Password': 'WrYT6g8lFJZbKLrCAzWGAScy1QkxZgpDGMYiaexxKJM'}

    data = payload_data_gen()

    print(data)

    response = req.post("https://api.lkqd.com/reports",  json = data , auth = (credentials['Username'],credentials['Password']))
    print(response.status_code)
    data_dict = json.loads(response.text)
    # print(data_dict)
    # print(data_dict["data"]["entries"])
    df = pd.DataFrame(data_dict["data"]["entries"])
    # print(df.columns.tolist())
    return df


# print(api_connector())