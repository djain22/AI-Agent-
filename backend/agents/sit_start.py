import requests
from langchain_anthropic import ChatAnthropic
import subprocess
import json

result = subprocess.run(
    ['curl', '-s', 'https://api.sleeper.app/v1/user/465705098111086592/leagues/nfl/2024'
],
    capture_output=True,
    text=True
)
#print(result.stdout)

data = json.loads(result.stdout)

for league in data:
    print(league['name'])
    print(league['league_id'])