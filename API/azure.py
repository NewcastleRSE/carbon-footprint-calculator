import requests
import json

url = "https://management.azure.com/providers/Microsoft.Carbon/carbonEmissionReports?api-version=2025-04-01"

payload = json.dumps({
  "reportType": "ItemDetailsReport",
  "subscriptionList": [
    "c80e5f06-fef1-496c-9c46-2f64bd75e62d"
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
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkNOdjBPSTNSd3FsSEZFVm5hb01Bc2hDSDJYRSIsImtpZCI6IkNOdjBPSTNSd3FsSEZFVm5hb01Bc2hDSDJYRSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuYXp1cmUuY29tIiwiaXNzIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvOWM1MDEyYzktYjYxNi00NGMyLWE5MTctNjY4MTRmYmUzZTg3LyIsImlhdCI6MTc0ODUyMjYxMCwibmJmIjoxNzQ4NTIyNjEwLCJleHAiOjE3NDg1MjY1MTAsImFpbyI6ImsyUmdZQkFVZXRiajh2NXRuY0tuMVN1VnRwblpBd0E9IiwiYXBwaWQiOiJhNmZiMzQwZC01NjcwLTQxYTktYTE0Mi0wYmU3ODk2Zjg4MzciLCJhcHBpZGFjciI6IjEiLCJpZHAiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85YzUwMTJjOS1iNjE2LTQ0YzItYTkxNy02NjgxNGZiZTNlODcvIiwiaWR0eXAiOiJhcHAiLCJvaWQiOiJlOGFmMWVhOS0yMDM3LTQzNWUtOTg3OS0zN2QzZjM1ZWUxN2IiLCJyaCI6IjEuQVNFQXlSSlFuQmEyd2tTcEYyYUJUNzQtaDBaSWYza0F1dGRQdWtQYXdmajJNQk9HQUFBaEFBLiIsInN1YiI6ImU4YWYxZWE5LTIwMzctNDM1ZS05ODc5LTM3ZDNmMzVlZTE3YiIsInRpZCI6IjljNTAxMmM5LWI2MTYtNDRjMi1hOTE3LTY2ODE0ZmJlM2U4NyIsInV0aSI6InFaMGRrelNkYlVDMHVuZ1JuVFVpQUEiLCJ2ZXIiOiIxLjAiLCJ4bXNfZnRkIjoiMkFIX1dSVEhQWTh5SkdKOGNGZU9WX0hlMDVjcXgwRVRaSkl6Y3JVUmc4Z0JaWFZ5YjNCbGJtOXlkR2d0WkhOdGN3IiwieG1zX2lkcmVsIjoiNyAyMiIsInhtc19yZCI6IjAuNDJMbFlCSmlWQlFTNFdBWEVvaTgyYnp1d3FHdHpsTjViZ21jMEYxMUh5aktLU1RBSWQ5LTN2TE9CLThwTHlzM3R5ODRNQVVveWlFazRPWlJYOG13NjdyX0x1ZGJCMzk4TXhBR0FBIiwieG1zX3RjZHQiOjEzMzQwNTU1MTd9.AN7ODksU0bhfgZV0ZiEfmz0jO-hjeQrYbvQIuE-s4xfgZ7eKqtzNy9dWPG3RI_ijJBE__gLMZF3fyR_px0zIoc2Fsa6I3Jl9PBIWr7e7XiObi2pQw18rrBbjGBlwte6Fcx0KOcyR8Dm92xp-MzT8Lw5HW1pSIvLM1Fb1hu-ff0QA7mpeIWjCpNRzlrmhpr6f-clQx7Xim-Vxy0I2FG5Vhrtwy-i-_y68pRMP7mvxI9jKTQMYqPXpDJXwsNrEtuQa2EbKQk33imdW1tbIyxoU_6dX7mx3DPtlCLF6mStkdQhAHAMgmpptQ5JvDP0Taaoq_TYSh0Lds-1zwZ4-_ZcAOw'
}

response = requests.request("POST", url, headers=headers, data=payload)
data = json.loads(response.text)
print(data)
with open("data.json", "w", encoding="utf-8") as json_file:
  json_file.write(json.dumps(data, indent=4, ensure_ascii=False))
