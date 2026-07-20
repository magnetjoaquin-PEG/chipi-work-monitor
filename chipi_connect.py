from msal import PublicClientApplication
import requests

TENANT_ID = "8cb3c63f-2956-4d28-b216-acb701237c25"
CLIENT_ID = "78ba13d6-5c91-43c5-98db-7c41c0a48b7f"

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

app = PublicClientApplication(
    CLIENT_ID,
    authority=AUTHORITY
)

flow = app.initiate_device_flow(
    scopes=["https://graph.microsoft.com/.default"]
)

if "user_code" not in flow:
    raise ValueError("No se pudo iniciar Device Flow.")

print("")
print("===================================")
print("CHIPI WORK MONITOR")
print("===================================")
print("")
print("Abrí:")
print(flow["verification_uri"])
print("")
print("Ingresá el código:")
print(flow["user_code"])
print("")

result = app.acquire_token_by_device_flow(flow)

if "access_token" not in result:
    print(result)
    raise Exception("No se obtuvo access token")

token = result["access_token"]

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    "https://graph.microsoft.com/v1.0/sites?search=Generacionelica",
    headers=headers
)

print("")
print("STATUS:", response.status_code)
print("")

print(response.text)