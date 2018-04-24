from date_gen import dategen
from report_type_gen import report_type_gen
import sys

dimensions, metrics = report_type_gen()
start_date, end_date = dategen()



def time_dimension_selected():

    time_dimensions_selected = sys.argv[1]

    # time_dimensions_selected = input("time dimension")

    time_dimensions = ['OVERALL','MONTHLY','DAILY','HOURLY']

    if time_dimensions_selected == "overall":

        return time_dimensions[0]

    elif time_dimensions_selected == "monthly":

        return time_dimensions[1]

    elif time_dimensions_selected == "daily":

        return time_dimensions[2]

    elif time_dimensions_selected == "hourly":

        return time_dimensions[3]



def payload_supply_demand_reports_data_gen():


    data = {
        "timeDimension": time_dimension_selected(),
        "reportType": dimensions,
        "reportFormat": "JSON",
        "startDate": start_date,
        "endDate": end_date,
        "timezone": "UTC",
        "metrics": metrics,

    }



    # if sys.argv[2] == 'supply_report' or sys.argv[2] == 'demand_report':

    return data

# print(payload_data_gen())


def payload_domain_reports_data_gen(offset,limit):



    # if sys.argv[2] == "supply_domain_report" or sys.argv[2] == "supply_app_bundleid_report":

    data = {
        "timeDimension": time_dimension_selected(),
        "reportType": dimensions,
        "reportFormat": "JSON",
        "startDate": start_date,
        "endDate": end_date,
        "timezone": "UTC",
        "metrics": metrics,
        "sort": [{
            "field": "field_name1",
            "order": "desc", }, {
            "field": "field_name2",
            "order": "desc",
        }],
        "offset": offset,
        "limit": limit
    }


    return data