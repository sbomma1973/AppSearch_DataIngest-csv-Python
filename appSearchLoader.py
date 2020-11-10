# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import json
import yaml
import elastic_enterprise_search
from elastic_enterprise_search import AppSearch

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.

def read_from_file():
    with open('config.yml') as f:
        data = yaml.load (f, Loader=yaml.FullLoader)
        return data

def make_json(csvFilePath, engine, url, private_key):
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath) as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            key = rows
            data  = rows
            json_data = json.dumps(data)
            ingest_data(engine, url, private_key,json_data)

            # Open a json writer, and use the json.dumps()
    # function to dump data
    #print ('data', json_data)

    return json_data

    # Driver Code
def ingest_data(engine, url,pvt_key, json_data):
    print ("ingest rows into appsearch")
    print (json_data)
    app_search = AppSearch(
        url,
        http_auth = pvt_key,
    )
    app_search.index_documents(
        engine_name=engine,
        body=json_data
    )
# Decide the two file paths according to your:
# computer system
#csvFilePath = r'Names.csv'
#jsonFilePath = r'Names.json'

# Call the make_json function
#make_json(csvFilePath, jsonFilePath)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    data=read_from_file()
    csv_path = data['csvPath']
    engine = data['Engine']
    url = data['cloud_url']
    user = data['username']
    password = data['password']
    private_key = data['pvt_key']

    print ("csvpath:", csv_path)

    print ("Engine:", engine)
    json_data=make_json(csv_path,engine, url, private_key)

    #insert_status=ingest_data(engine, url, private_key, json_data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
