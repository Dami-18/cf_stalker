import requests
import time
import random
import hashlib
import asyncio
import aiohttp
import getpass as gp

async def fetch_friend_info(session, handle):
  profile_url = f"https://codeforces.com/api/user.info?handles={handle}&checkHistoricHandles=false"
  async with session.get(profile_url) as resp:
    if resp.status == 200:
      friend_data = await resp.json()
      friend_info = friend_data["result"][0]
      rating = str(friend_info["rating"])
      rank = friend_info["rank"]
      print(f"{handle:{30}} {rating:{4}} ({rank})")
    else:
      print(f"Error fetching data for {handle}: {resp.status}")

async def main():
  async with aiohttp.ClientSession() as session:
    handles = res["result"]  
    tasks = [fetch_friend_info(session, handle) for handle in handles]
    await asyncio.gather(*tasks)

print("Enter your api key and secret. For security, characters won't be echoed on screen")
key = gp.getpass("API key: ")
secret = gp.getpass("API secret key: ")
unix_time = int(time.time())
rand = random.randrange(112191,921791)
data = f"{rand}/user.friends?apiKey={key}&onlyOnline=false&time={unix_time}#{secret}"
data_encoded = data.encode('utf-8')
sha512_hash = hashlib.sha512()
sha512_hash.update(data_encoded)
sha512_digest = sha512_hash.digest()
sha512_hex = sha512_digest.hex()

auth_url = f"https://codeforces.com/api/user.friends?onlyOnline=false&apiKey={key}&time={unix_time}&apiSig={rand}{sha512_hex}"

auth_response = requests.get(auth_url)

if auth_response.status_code==200:
  res = auth_response.json()
  print("Stalking your friends....")
  asyncio.run(main())

else:
  print(auth_response)
