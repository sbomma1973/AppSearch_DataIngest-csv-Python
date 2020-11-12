######################
#Appsearch CSV data loader Created by
# Satish Bommma -- Solutions Architect at Elastic
# Please email or conact me at satish.bomma@elastic.co
# date: Nov 12 2020
#######################
# Elastic Enterprise Search AppSearch csv data load using Python Client
# Pre-requsites install the Elastic client
# Setup up elasticsearch in the cloud usnig (Cloud.elastic.co)
# Config.yml Steps
# get the private key and url configure it in config.yml file
# Create an engine in and configure the engine name.
# get your csv file/files and proovide the path for the csv file..


import csv
import json
import yaml
import elastic_enterprise_search
from elastic_enterprise_search import AppSearch


def read_from_file():
    with open('config.yml') as f:
        data = yaml.load (f, Loader=yaml.FullLoader)
        return data

def make_json(csvFilePath, engine, url, private_key,batch_size):
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath) as csvf:
        csvReader = csv.DictReader(csvf)
        #lines = len(list(csvReader))
        #print ("lines",lines)
        #batch_size = batch_size
        batch = []
        count = 0
        for row in csvReader:
            if count >= batch_size:
                print (batch)
                json_data = json.dumps(batch)
                #print (json_data)
                batch = []
                count = 0
                ingest_data(engine, url, private_key, json_data)
            batch.append(row)
            count += 1
        if batch:
            json_data = json.dumps(batch)
            ingest_data(engine, url, private_key, json_data)
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

#make_json(csvFilePath, jsonFilePath)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data=read_from_file()
    csv_path = data['csvPath']
    engine = data['Engine']
    url = data['cloud_url']
    private_key = data['pvt_key']
    batch_size = data['batch_size']

    print ("csvpath:", csv_path)

    print ("Engine:", engine)
    make_json(csv_path,engine, url, private_key, batch_size)

    #insert_status=ingest_data(engine, url, private_key, json_data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
