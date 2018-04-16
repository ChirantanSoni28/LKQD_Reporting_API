from lkqd_api_connector import api_connector
import sys

type_of_report = ['supply_report', 'demand_report', 'supply_domain_report', 'supply_app_bundleid_report']

def data_organizer():


    if sys.argv[2] == type_of_report[0]:

        supply_columns_filtered = ['adImpressions', 'adOpportunities', 'adViewabilityMeasuredRate', 'adViewabilityRate', 'adViewableImps', 'cpm', 'dimension2Id', 'dimension2Name', 'dimension3Name', 'fieldId', 'fieldName', 'fillRate', 'profit', 'revenue', 'siteCost', 'timeDimension']

        columns_renamed = ['impressions', 'opportunities','viewablity_measured_rate','viewability_rate', 'viewable_impressions', 'cpm', 'supply_source_id', 'supply_source_name' ,'source_enviornment', 'supply_partner_id', 'supply_partner_name', 'fillrate' ,'profit', 'revenue', 'cost', 'date']

        columns_reindexed = ['date', 'source_enviornment', 'supply_partner_id', 'supply_partner_name', 'supply_source_id', 'supply_source_name', 'opportunities', 'impressions' , 'fillrate', 'cpm', 'revenue', 'cost','profit', 'viewablity_measured_rate','viewability_rate', 'viewable_impressions' ]










def data_parser():

    data = api_connector()
    print(data.columns.tolist())

    # if sys.argv[2] == type_of_report[0]:
    #
    #     new_df = data.filter(, axis=1)
    #
    #     new_df.columns =
    #
    #     new_df = new_df.reindex(, axis=1)
    #
    # print(new_df)






data_parser()