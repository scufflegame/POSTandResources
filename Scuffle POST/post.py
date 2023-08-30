import requests


# url = "https://discord.com/api/v8/applications/971996284930105395/guilds/934778735482273823/commands/977050761156513812"
# url = "https://discord.com/api/v8/applications/971996284930105395/guilds/934778735482273823/commands/977050761156513812"
url = "https://discord.com/api/v8/applications/971996284930105395/commands"


# json = {
#     "name": "roll",
#     "type": 1,
#     "description": "Roll a set of random Scuffle legal commanders"
# }

# For authorization, you can use either your bot token
headers = {
    "Authorization": "Bot OTcxOTk2Mjg0OTMwMTA1Mzk1.GyYma1.DlEEq7VH2_a9tTl-wtySrtU5rzsovOlMNMc2H4"
}

# r = requests.delete(url, headers=headers)
r = requests.get(url, headers=headers)
# r = requests.post(url, headers=headers, json=json)
print(r.status_code)
print(r.text)