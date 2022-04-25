# WoW Scanner V2

WoW Scanner is a Python script working with Influx Database and a monitoring dashboard (like Grafana).
The idea is to track the minimum and average price at the Auction House for your WoW server.

Ideally, it should be installed on a 24/7 computer (a Raspberry Pi works well).

## Installation

Download the content of this repo, and put it somewhere in your 24/7 PC.
You should also have installed Python 3 and InfluxDB.

## Configuration
### Needed tokens
You will need 2 tokens:
* One for the API
* The second for your InfluxDB

You can have the API one from a Blizzard developper account. You'll need to create a new project to get an client ID and client secret.
You can get the token for your InfluxDB from the UI of Influx.

You will have to create a new file in 'utils/' called 'api_ids.json'. Fill it with this data (using your ID, your secret and your token):

```json
{
  "blizzard": {
    "client_id" : "Your_Client_Id_Goes_Here",
    "client_secret" : "Your_Client_Secret_Goes_Here"
  },
  "influxdb": {
    "token" : "Your_Influx_Db_Token_Goes_Here"
  }
}

```
### Setting the items list
Once this is done, create a new txt file called 'items_list.txt' at the root folder (e.g. where 'main.py' is). You can add all the items that you want to track in this file. Set one item ID per line.
FYI, you can get the item ID using sites like [wowhead](https://www.wowhead.com).

### Setting the crontab
As I run it on a Raspberry using a Debian Server OS, I use the crontab to run periodically the script. I usually run it every hour as Blizzard updates the API's data every hour.
The file to execute is the 'main.py' file.

Congratulations, you just created a new way to make statistics on the WoW AH!
Of course, we could speak about Grafana's setup, but this is not really part of the project/code created here. If you need help to install InfluxDB or Grafana, you can get in touch with me, I'll try to help you.

## Usage

Nothing. Once the crontab is set, the script will run automatically. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

*Created by C. CATHEBRAS for training and self-enjoyment purposes. I can not be held responsible in case of banishment following the use of my project.*
