import os
from typing import Optional
from requests import post
from fastapi import FastAPI

app = FastAPI()

ha_ip = os.environ['HA_IP'] 
ha_port = os.environ['HA_PORT'] 
ha_entity = os.environ['HA_ENTITY'] 
ha_token = os.environ['HA_TOKEN'] 
ha_domain = ha_entity.split('.')[0]

base_url = str("http://" + ha_ip + ":" + ha_port + "/api/services/" + ha_domain + "/")
headers = {
    "Authorization": str("Bearer " + ha_token),
    "Content-Type": "application/json"
}

payload = {"entity_id": ha_entity}

@app.post("/off")
def off():
    url = base_url + "turn_off"
    post(url,headers=headers,json=payload)

@app.post("/on")
def on():
    url = base_url + "turn_on"
    post(url,headers=headers,json=payload)