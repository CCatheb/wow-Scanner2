from datetime import datetime
import os
import json

import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

class InfluxDb:
    
    def __init__(self):
        self.token = None
        self.org = "wowscanner"
        self.bucket = "wowscanner"
        self.InfluxClient = None
        self.url = "http://localhost:8086"

    def setup(self):

        print("--- START OF INFLUXDB SETUP ---")
        if self.token is None:
            print("No token found for Influx DB. \nGetting the token from 'api_ids.json'...")
            try:
                f = open("utils/api_ids.json",'r')
                data = json.load(f)
                self.token = data['influxdb']['token']
                print("Done.")
            except IOError:
                print("File api_ids.json not found in directory '{}'. Please create the file.".format(os.path.dirname(os.path.realpath(__file__))))
                return
        
        if self.InfluxClient is None:
            print("No InfluxDB Client available. Creating a new one...")
            self.InfluxClient = influxdb_client.InfluxDBClient(
                url=self.url,
                token=self.token,
                org=self.org
            )
            print("Created a new client for:\n\tURL = {}\n\tORG = {}".format(self.url, self.org))
        
        print("--- END OF INFLUXDB SETUP ---")


    def write_to_db(self, server, item_id, avg_price, min_price, qty, bucket="wowscanner"):
        """
            This function is used to write directly to the InfluxDB linked to the class client.

            Args: 
                item_id: Item ID number
                avg_price: Item average price
                min_price: Item minimum price
                qty: Quantity of items currently on auctions
                bucket: Bucket to write on (reffers to the InfluxDB Bucket)
        
        
        
        """

        write_api = self.InfluxClient.write_api(write_options=SYNCHRONOUS)
        p = influxdb_client.Point("items").tag("realm", server)\
                                            .tag("id", item_id)\
                                            .field("average", avg_price)\
                                            .field("qty", qty)\
                                            .field("min_price", min_price)

        write_api.write(bucket=bucket, org=self.org, record=p)

    def write_token_to_db(self, token_value, bucket="token"):

        write_api = self.InfluxClient.write_api(write_options=SYNCHRONOUS)
        p = influxdb_client.Point("token").field("value", token_value)

        write_api.write(bucket=bucket, org=self.org, record=p)