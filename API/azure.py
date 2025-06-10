import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

AUTH_KEY = os.getenv("AUTH_KEY")
url = "https://management.azure.com/providers/Microsoft.Carbon/carbonEmissionReports?api-version=2025-04-01"

payload = json.dumps({
  "reportType": "ItemDetailsReport",
  "subscriptionList": [
    "c80e5f06-fef1-496c-9c46-2f64bd75e62d",
  ],
  "carbonScopeList": [
    "Scope3"
  ],
  "dateRange": {
    "start": "2024-05-01",
    "end": "2024-05-01"
  },
  "categoryType": "Subscription",
  "orderBy": "LatestMonthEmissions",
  "sortDirection": "Desc",
  "pageSize": 100
})

headers = {
  'Content-Type': 'application/json',
  'Host': 'management.azure.com',
  'Authorization': f"Bearer {AUTH_KEY}"
}

response = requests.request("POST", url, headers=headers, data=payload)
data = json.loads(response.text)
print(data)
with open("data.json", "w", encoding="utf-8") as json_file:
  json_file.write(json.dumps(data, indent=4, ensure_ascii=False))