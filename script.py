import requests
import argparse

yourHandle = input("Enter your CF handle: ")

url = f"https://codeforces.com/api/user.info?handles={yourHandle}&checkHistoricHandles=false"

response = requests.get(url)

if response.status_code==200:
    data = response.json()
    user_data = data["result"][0]
    your_handle = user_data["handle"]
    your_rating = str(user_data["rating"])
    your_rank = user_data["rank"]
    print("Your info: ")
    print("Handle- "+your_handle)
    print("Rating- "+your_rating+" ("+your_rank+")")
