import sys


def report_type_gen(report_type_selected = input("please enter")):

    # report_type_selected = input("please enter")

    type_of_report = ['supply_report','demand_report','supply_domain_report','supply_app_bundleid_report','supply_source_enviorment_report','demand_Source_enviorment_report']

    dimension = ['PARTNER','SITE','SOURCE','DEAL','TAG','DOMAIN','APP_NAME','BUNDLE_ID','ENVIRONMENT']
    supply_metrics = ['OPPORTUNITIES','FILL_RATE']
    supply_demand_metrics = ['IMPRESSIONS','CPM','REVENUE','COST','PROFIT','VIEWABILITY_MEASURED_RATE','VIEWABILITY_RATE','VIEWABLE_IMPRESSIONS']
    demand_metrics = ['REQUESTS','VAST_ADS','VPAID_RESPONSES','VPAID_ATTEMPTS','VPAID_ADS','VPAID_TIMEOUTS','VPAID_ERRORS','WINS','WIN_RATE']


    if report_type_selected == type_of_report[0]:

        dim = dimension[0:2]
        met = supply_metrics + supply_demand_metrics

    elif report_type_selected == type_of_report[1]:

        dim = dimension[2:5]
        met = supply_demand_metrics + demand_metrics

    elif report_type_selected == type_of_report[2]:

        dim =dimension


report_type_gen("supply_report")