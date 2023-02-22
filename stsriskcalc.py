import json
import requests
import json


class STSRiskCalc:

    ENDPOINT = "https://riskcalc.sts.org/stswebriskcalc/v1/calculate/stsall"

    def __init__(self, payload={}):
        self.payload = payload
        self.results = {}

    def set_payload(self, payload={}):
        self.payload = payload

    def calc_risks(self, payload=None) -> 'json':
        """Uses stored payload if payload is not passed in as an argument."""
        if payload is None:
            payload = self.payload

        data = json.dumps(payload)
        res = requests.post(STSRiskCalc.ENDPOINT, data=data, headers={
                            "Content-Type": "application/json"})
        res.raise_for_status()
        self.results = res.json()
        return self.results
