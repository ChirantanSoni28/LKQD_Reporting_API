import sqlalchemy as sql
from API_data_parser import data_parser
import sys
import pandas as pd


payload = {"host" : "@thrivehq.cusrikqjbmvm.us-east-1.rds.amazonaws.com",
            "pnum" : "3306",
            "dbname": "lkqd_api",
            "id": "Thriveplus2017",
            "pwd":  "321happy"}


data = data_parser()

def mysql_connector(credentials):

    url = "mysql+pymysql://" + credentials['id'] + ":" + credentials['pwd'] + credentials['host'] + ":" + \
                  credentials['pnum'] + "/" + credentials['dbname']


    engine = sql.create_engine(url)
    connection = engine.connect()


    return connection


def data_to_table():

    connection = mysql_connector(payload)
    report_type = sys.argv[2]
    report_types = ['supply_report', 'demand_report', 'supply_domain_report', 'supply_app_bundleid_report']

    if report_type == report_types[0]:

        data.to_sql(name=report_types[0], con=connection, if_exists='replace', index=False, dtype={'date':sql.types.DATE,
                                                                                                   'source_enviornment':sql.types.VARCHAR(length=225),
                                                                                                   'supply_partner_id': sql.types.INTEGER(),
                                                                                                   'supply_partner_name': sql.types.VARCHAR(length=225),
                                                                                                   'supply_source_id': sql.types.INTEGER(),
                                                                                                   'supply_source_name': sql.types.VARCHAR(length=225),
                                                                                                   'opportunities': sql.types.INTEGER(),
                                                                                                   'impressions': sql.types.INTEGER(),
                                                                                                   'fillrate': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'cpm': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'revenue': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'cost': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'profit': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'viewablity_measured_rate': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'viewability_rate': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'viewable_impressions': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   })
        print(report_types[0])

    elif report_type == report_types[1]:

        data.to_sql(name=report_types[1], con=connection, if_exists='replace', index=False, dtype={'date': sql.types.DATE,
                                                                                                   'demand_enviornment':sql.types.VARCHAR(length=225),
                                                                                                   'demand_partner_id':sql.types.INTEGER(),
                                                                                                   'demand_partner_name':sql.types.VARCHAR(length=225),
                                                                                                   'demand_deal_id':sql.types.INTEGER(),
                                                                                                   'demand_deal_name':sql.types.VARCHAR(length=225),
                                                                                                   'demand_tag_id':sql.types.INTEGER(),
                                                                                                   'demand_tag_name':sql.types.VARCHAR(length=225),
                                                                                                   'requests':sql.types.INTEGER(),
                                                                                                   'response':sql.types.INTEGER(),
                                                                                                   'impressions':sql.types.INTEGER(),
                                                                                                   'cpm': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'revenue': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'cost': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'profit': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'viewablity_measured_rate': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'viewability_rate': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'viewable_impressions':sql.types.INTEGER(),
                                                                                                   'vast_ads':sql.types.INTEGER(),
                                                                                                   'vpaid_ads':sql.types.INTEGER(),
                                                                                                   'vpaid_attempts':sql.types.INTEGER(),
                                                                                                   'vpaid_timeouts':sql.types.INTEGER(),
                                                                                                   'vpaid_errors':sql.types.INTEGER(),
                                                                                                   'vpaid_responses':sql.types.INTEGER(),
                                                                                                   'wins':sql.types.INTEGER(),
                                                                                                   'win_rate': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   })

        print(report_types[1])

    elif report_type == report_types[2]:

        data.to_sql(name=report_types[2], con=connection, if_exists='replace', index=False, dtype={'date':sql.types.DATE,
                                                                                                   'supply_source_id': sql.types.INTEGER(),
                                                                                                   'supply_source_name': sql.types.VARCHAR(length=225),
                                                                                                   'domains': sql.types.VARCHAR(length=225),
                                                                                                   'opportunities': sql.types.INTEGER(),
                                                                                                   'impressions': sql.types.INTEGER(),
                                                                                                   'fillrate': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'cpm': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'revenue': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'cost': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'profit': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'viewablity_measured_rate': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'viewability_rate': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'viewable_impressions': sql.types.INTEGER(),
                                                                                                   })
        print(report_types[2])

    elif report_type == report_types[3]:

        data.to_sql(name=report_types[3], con=connection, if_exists='replace', index=False, dtype={'date':sql.types.DATE,
                                                                                                   'supply_source_id': sql.types.INTEGER(),
                                                                                                   'supply_source_name': sql.types.VARCHAR(length=225),
                                                                                                   'app_name': sql.types.VARCHAR(length=225),
                                                                                                   'bundle_id': sql.types.VARCHAR(length=225),
                                                                                                   'opportunities': sql.types.INTEGER(),
                                                                                                   'impressions': sql.types.INTEGER(),
                                                                                                   'fillrate': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'cpm': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'revenue': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'cost': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'profit': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'viewablity_measured_rate': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'viewability_rate': sql.types.FLOAT(precision=4, asdecimal=True),
                                                                                                   'viewable_impressions': sql.types.INTEGER(),
                                                                                                   })

        print(report_types[3])


data_to_table()
# mysql_connector(payload)