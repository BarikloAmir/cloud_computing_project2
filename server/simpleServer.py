import socket
import requests
import uvicorn
import json
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def first_example():
    """
	simple server for cc hw2
	"""

    params = {
        'access_key': '3b782a81ab3ccfa4b8f4a454b04878ae',
        'query': 'Tehran'
    }

    api_result = requests.get(address, params)

    data = api_result.json()
    api_response = {
        "temperature": data['current']['temperature'],
        "weather_descriptions": data['current']['weather_descriptions'],
        "wind_speed": data['current']['wind_speed'],
        "humidity": data['current']['humidity'],
        "feelslike": data['current']['feelslike'],
    }

    api_response.update({"host name": str(socket.gethostname())})

    return api_response


if __name__ == "__main__":
    with open('server_config.config') as f:
        data = json.load(f)
        address = data["address"]
        port = data["port"]

    uvicorn.run(app, host="0.0.0.0", port=int(port))
