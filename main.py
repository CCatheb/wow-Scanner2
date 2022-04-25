from utils.ahprocessing import DataProcessing
from utils.restclient import RestClient
from utils.influxdb import InfluxDb

url = "https://eu.api.blizzard.com/data/wow/"
token = None

AHP = DataProcessing()
IC = InfluxDb()
RC = RestClient()

RC.setup()
IC.setup()

server_list = ["hyjal", "dalaran", "ysondre", "archimonde"]
items_ids = open("items_list.txt").read().splitlines()
for i in range(len(items_ids)):
    items_ids[i] = int(items_ids[i])

token_value = RC.get_token_value()
IC.write_token_to_db(token_value)


for server in server_list:
    RC.server = server
    print("Getting all auctions in {}".format(server))
    (status , RC.realm_id) = RC.get_realm_id(RC.server, RC.access_token)
    auctions = RC.get_auctions()
    for item in items_ids:
            AHP.item_id = item
            items_list = AHP.get_auctions_by_id(auctions)
            (quantity, av_value, min_value) = AHP.process_data(items_list)
            print("For item {} on {}, there is {} items with an average price of {}\nThe minimal price is {}".format(AHP.item_id, RC.server, quantity, av_value, min_value))
            IC.write_to_db(server, item, av_value, min_value, quantity)
            


