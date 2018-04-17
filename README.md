# LKQD Reporting API

###### LKQD is an Video Advertising server and Analytics platform for publisher Networks and Ad Networks. The LKQD Reporting API is built to access required analytics reports for advanced analytics using Python scripts and MySQL queries, for optimizations on Advertiser and Publisher network on the Adserver.

Below is the documentation of dependencies and function definitions of LKQD_Reporting_API

|   Dependencies     |   Standarad Library packages    |
| ------------------ |:-------------------------------:|
| requests==2.18.4   | json                            |
| pandas==0.22.0     | sys                             | 
| SQLAlchemy==1.2.6  | datetime                        | 

### Table of Contents
**[Installation and Usage Instructions](#installation-and-usage-instructions)**<br>
**[Notes and Miscellaneous](#notes-and-miscellaneous)**<br>
**[List of Scripts and Functions with description](#list-of-scripts-and-functions-with-description)**<br>

## Installation and Usage Instructions

#### Manual/Development

1. Clone this repo.
2. Get LKQD API keys from LKQD platform : clientid and Secret
3. mySQL database payload : Hostname, port, Database Name, User ID and Password
4. Input API keys in credential dictionary in api_connector()


### List of Scripts and Functions with description

**1. lkqd_api_connector.py**
* api_connector( )
> This function lies in the top hierarchy of the project. It sends request to LKQD API to generate and return raw pandas DataFrame consistind reporting data as per reequest. It takes LKQD API secret key ID and secret key encodes them into base64 encoding for inputs along with JSON format payload from payload_gen.py to send HTTP Basic Authentication over SSL.

**2. payload_gen.py**
* payload_data_gen( )
> This function generates payload JSON data for API request to LKQD. The payload_data_gen() takes dynamic inputs from time_dimension_selected() report_type_gen() and dategen(). 

* time_dimension_selected( )

**3. report_type_gen.py**
* report_type_gen( )

**4. date_gen.py**
* dategen( )
* customdate( )

**5. API_data_parser.py**
* data_parser( )
* data_organizer( )

**6. database_input.py**
* mysql_connector( )
* data_to_table( )







