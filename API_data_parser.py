from lkqd_api_connector import api_connector
import sys
import pandas as pd



def data_organizer():

    type_of_report = ['supply_report', 'demand_report', 'supply_domain_report', 'supply_app_bundleid_report']

    if sys.argv[2] == type_of_report[0]:

        report = type_of_report[0]

        columns_filtered = ['adImpressions', 'adOpportunities', 'adViewabilityMeasuredRate', 'adViewabilityRate', 'adViewableImps', 'cpm', 'dimension2Id', 'dimension2Name', 'dimension3Name', 'fieldId', 'fieldName', 'fillRate', 'profit', 'revenue', 'siteCost', 'timeDimension']

        columns_renamed = ['impressions', 'opportunities','viewablity_measured_rate','viewability_rate', 'viewable_impressions', 'cpm', 'supply_source_id', 'supply_source_name' ,'source_enviornment', 'supply_partner_id', 'supply_partner_name', 'fillrate' ,'profit', 'revenue', 'cost', 'date']

        columns_reindexed = ['date', 'source_enviornment', 'supply_partner_id', 'supply_partner_name', 'supply_source_id', 'supply_source_name', 'opportunities', 'impressions' , 'fillrate', 'cpm', 'revenue', 'cost','profit', 'viewablity_measured_rate','viewability_rate', 'viewable_impressions' ]

    elif sys.argv[2] == type_of_report[1]:

        report = type_of_report[1]

        columns_filtered = ['adImpressions', 'adRequests', 'adResponses' , 'adViewabilityMeasuredRate', 'adViewabilityRate', 'adViewableImps', 'adVpaidAttempts', 'adVpaidErrors', 'adVpaidResponses', 'adVpaidTimeouts', 'adWins', 'cpm', 'dimension2Id', 'dimension2Name', 'dimension3Id', 'dimension3Name', 'dimension4Name', 'fieldId', 'fieldName', 'profit', 'revenue', 'siteCost', 'timeDimension', 'vastAds', 'vpaidAds', 'winRate']

        columns_renamed = ['impressions','requests','responses', 'viewablity_measured_rate','viewability_rate', 'viewable_impressions', 'vpaid_attempts', 'vpaid_errors', 'vpaid_responses','vpaid_timeouts', 'wins', 'cpm' , 'demand_deal_id', 'demand_deal_name', 'demand_tag_id', 'demand_tag_name', 'demand_enviornment', 'demand_partner_id', 'demand_partner_name', 'profit', 'revenue', 'cost', 'date' , 'vast_ads', 'vpaid_ads' , 'win_rate']

        columns_reindexed = ['date', 'demand_enviornment', 'demand_partner_id', 'demand_partner_name', 'demand_deal_id', 'demand_deal_name', 'demand_tag_id', 'demand_tag_name', 'requests', 'response','impressions' , 'cpm', 'revenue', 'cost','profit', 'viewablity_measured_rate','viewability_rate', 'viewable_impressions', 'vast_ads','vpaid_ads', 'vpaid_attempts', 'vpaid_timeouts', 'vpaid_errors','vpaid_responses', 'wins','win_rate']


    # elif sys.argv[2] == type_of_report[2]:




    return report, columns_filtered, columns_renamed,columns_reindexed





def data_parser():

    data = api_connector()
    print(data.columns.tolist())
    print(data)

    # report_type, filter,renamed, reindexed  =  data_organizer()
    #
    # sys.argv[2] == report_type
    #
    #     new_df = data.filter(filter, axis=1)
    #     # print(new_df)
    #     new_df.columns = renamed
    #
    #     new_df = new_df.reindex(reindexed, axis=1)
    #







print(data_parser())