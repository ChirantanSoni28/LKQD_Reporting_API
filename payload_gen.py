from date_gen import dategen
from report_type_gen import report_type_gen
import sys






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



def payload_data_gen():

    dimensions, metrics = report_type_gen()
    start_date, end_date = dategen()

    data = {
        "timeDimension": time_dimension_selected(),
        "reportType": dimensions,
        "reportFormat": "JSON",
        "startDate": start_date,
        "endDate": end_date,
        "timezone": "UTC",
        "metrics": metrics,
        "limit": "100000"
    }


    return data

# print(payload_data_gen())