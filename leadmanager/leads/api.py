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


# base_url = "https://exchange.sandbox.gemini.com/signin/2fa?redirect=ba5e6000f30dc773635701d04d8c9167c823f67e-1608577152223-%2Fauth%3Fresponse_type%3Dcode%26client_id%3D5fe0ef60-b223-45f5-915a-c3cc988e2f12%26redirect_uri%3Dhttps%253A%252F%252Fsolidblock.me%252Fconfirmation%252F1%26scope%3Daddresses%253Aread%252Chistory%253Aread%252Corders%253Acreate%252Caccount%253Aread%252Cpayments%253Asend%252Corders%253Aread%252Cclearing%253Acreate%252Cpayments%253Aread%252Cpayments%253Acreate%252Ccrypto%253Asend%252Cbalances%253Aread%252Cbanks%253Aread%252Cclearing%253Aread%26state%3D5fe0ef609945427481ab91c01d6ddf26&sudo=true&sms=true"
url = "https://api.sandbox.gemini.com/v1/balances"

# url = 'https://exchange.sandbox.gemini.com/auth/token?client_id=5fe0ef60-b223-45f5-915a-c3cc988e2f12&client_secret=5fe0ef60-619a-4c05-8270-002d146731f7&code=DHUrq10vEa20VZbZUtrUFG3rWnTDb8DtdqgHp5AB3gU&redirect_uri=https://solidblock.me/marketplace&grant_type=authorization_code'

{'access_token': 'Bx0jja5AD40JdXoM2PbdHuh7XxYPLPd7ncEw19wdHkR5', 'expires_in': 86399, 'scope': 'crypto:send,orders:create,banks:read,clearing:create,payments:read,orders:read,clearing:read,payments:create,account:read,payments:send,balances:read,addresses:read',
    'refresh_token': 'qwMTtv5FtOWIx5KMWAZDjiDzhyAX359mkVTZxTGQAuX', 'token_type': 'Bearer'}


access_token = "Bearer Bx0jja5AD40JdXoM2PbdHuh7XxYPLPd7ncEw19wdHkR5"


payload = {
    "request": "/v1/balances",
    "symbol": "btcusd"
}

encoded_payload = json.dumps(payload).encode()
b64 = base64.b64encode(encoded_payload)

request_headers = {
    "Authorization": access_token,
    "X-GEMINI-PAYLOAD": b64
}

print('dswefrefrfrfrfrfrfrfrffr')
# headers = {"client_id": "5fe0ef60-b223-45f5-915a-c3cc988e2f12",
#            "client_secret": "5fe0ef60-619a-4c05-8270-002d146731f7",
#            "code": "MyFe1lXIGXJxB5dT3nBMfH28qeDMSKzbbYwRBcTTw73r",
#            "redirect_uri": "https://solidblock.me/marketplace",
#            "grant_type": "authorization_code"
#            }


class LeadViewSet(viewsets.ModelViewSet):

    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer

    def list(self, request):
        price_lte = request.GET['price_lte']
        print(price_lte)
        print("leo test in TaskViewSet")
        response = requests.post(url,
                                 data=None,
                                 headers=request_headers,
                                 verify=True)

        new_clearing_order = response.json()
        print(new_clearing_order)

        return Response({'status': new_clearing_order})
