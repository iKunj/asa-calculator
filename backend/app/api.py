from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .helper import bodyParser, roundSwitcher
import requests

# This Model is used for validation of 3 values used to calculate ASA Change
class requestItem(BaseModel):
    entry_id: str
    assembly_id: str
    interface_id: str

# This model is used for validation of toggler feature
class roundTogger(BaseModel):
    roundValue : bool
    roundingValue: int

app = FastAPI()

# Added CORS middleware so that no unwanted external requests can be made except
# the ones specified in allow_origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# The endpoint which hits the RCSB API to fetch data using the values provided from react form
@app.post("/asa-change")
async def calc_asa_change(requestItem: requestItem):
    url = "https://data.rcsb.org/rest/v1/core/interface/" + requestItem.entry_id + "/"+ requestItem.assembly_id +"/" + requestItem.interface_id
    response = requests.get(url)
    return bodyParser(response.json()) 
# bodyParser is the helper file I made to parse the response and return the formatted data
    
# The enpoint which toggles the round feature within the code from the react toggle button along with toggle value
@app.post("/is-rounded")
def toggle_round(roundValue: roundTogger):
    return roundSwitcher(roundValue.roundValue, roundValue.roundingValue)