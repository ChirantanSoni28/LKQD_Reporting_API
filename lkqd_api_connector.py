import requests as req
import json
import pandas as pd



credentials = {'Username' : '4BRrKTFu2godcuiNjBDAG9jlB48D8bJB' , 'Password': 'WrYT6g8lFJZbKLrCAzWGAScy1QkxZgpDGMYiaexxKJM'}

data = {
    "timeDimension": "DAILY",
    "reportType": ["PARTNER","SITE","ENVIRONMENT"],
    "reportFormat": "JSON",
    "startDate": "2018-04-11",
    "endDate": "2018-04-11",
    "timezone": "UTC",
    "metrics": ["OPPORTUNITIES","IMPRESSIONS","FILL_RATE"]
}


response = req.post("https://api.lkqd.com/reports",  json = data , auth = ('4BRrKTFu2godcuiNjBDAG9jlB48D8bJB','WrYT6g8lFJZbKLrCAzWGAScy1QkxZgpDGMYiaexxKJM'))
print(response.status_code)
data_dict = json.loads(response.text)
# print(data_dict["data"]["entries"])




df = pd.DataFrame(data_dict["data"]["entries"])
new_df = df.filter(['adImpressions', 'adOpportunities', 'dimension2Id', 'dimension2Name','dimension3Name', 'fieldId', 'fieldName', 'fillRate', 'timeDimension'], axis=1)
new_df.columns=['Impressions','Opportunities','supply_source_id','supply_source_name', 'source_enviornment','supply_partner_id','supply_partner_name','fillrate', 'Date']
new_df = new_df.reindex(['Date','source_enviornment','supply_partner_id','supply_partner_name','supply_source_id','supply_source_name','Opportunities','Impressions','fillrate'],axis=1)
print(new_df)
# print(df.columns.tolist())

