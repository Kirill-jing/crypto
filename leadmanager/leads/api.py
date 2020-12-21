from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializer import LeadSerializer
from rest_framework.response import Response
import requests
import base64
import hmac
import hashlib
import datetime
import time
import json

base_url = "https://api.sandbox.gemini.com"
endpoint = "/v1/clearing/new"
url = base_url + endpoint

gemini_api_key = "account-BJWs2SF6RKMwvMo7xFGS"
gemini_api_secret = "31K8EpisN4Ws9rvUQe2Xym9gdhc".encode()
counterparty_id = "OM9VNL1G"

t = datetime.datetime.now()

payload_nonce = str(int(time.mktime(t.timetuple())*1000))
payload = {"request": endpoint,
           "nonce": payload_nonce,
           "expires_in_hrs": 24,
           "symbol": "btcusd",
           "amount": "1",
           "price": "22716.61",
           "side": "sell"}

encoded_payload = json.dumps(payload).encode()
b64 = base64.b64encode(encoded_payload)
signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()
print(signature)

request_headers = {
    'Content-Type': "text/plain",
    'Content-Length': "0",
    'X-GEMINI-APIKEY': gemini_api_key,
    'X-GEMINI-PAYLOAD': b64,
    'X-GEMINI-SIGNATURE': signature,
    'Cache-Control': "no-cache"
}

# response = requests.post(url,
#                          data=None,
#                          headers=request_headers)

# new_clearing_order = response.json()
# print(new_clearing_order)


class LeadViewSet(viewsets.ModelViewSet):

    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer

    def list(self, request):
        print("leo test in TaskViewSet")
        response = requests.post(url,
                                 data=None,
                                 headers=request_headers)

        new_clearing_order = response.json()
        print(new_clearing_order)
        return Response({'status': new_clearing_order})
