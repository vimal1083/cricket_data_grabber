import requests
import json
from pymongo import MongoClient
# Connects to default mongo host and port, for customization visit https://api.mongodb.com/python/current/tutorial.html
client = MongoClient()
db = client['cricket']
collection = db['player_profile']


player_id = 0
while player_id < 20001:
  player_id += 1
  try:
    req = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20%20cricket.player.profile%20where%20player_id%20%3D%20{0}&format=json&diagnostics=true&env=store%3A%2F%2F0TxIGQMQbObzvU4Apia0V0&callback='.format(player_id))
    # Save data if status code is 200
    if req.status_code == 200:
      content = json.loads(req.content).get('query').get('results')
      # Insert into collection
      collection.insert_one(content)
      print player_id, '  -->  ',content.get('PlayerProfile').get('PersonalDetails').get('FirstName')
  except :
    pass
