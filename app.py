import requests
from time import sleep
import json

while True:
    id = input("ID: ")
    if not id.isdigit():
        print("ID måste vara en siffra")
        continue
    break

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'authorization': "Bearer IfvQEKEIDQngklrMERD3TkanLQaYKUVtFaALlmTh",
    'Postman-Token': "36cc45e2-6417-41fb-9bba-57695f89e215"
}

loginUrl = "https://api.studi.se/users/%s" % id

loginResponse = requests.request("GET", loginUrl, headers=headers)
loginData = json.loads(loginResponse.text)
print('Inloggad som %s, du har %d poäng' % (loginData['display_name'], loginData['points']))

url = "https://api.studi.se/lessons/quizReport"
payload = "{\"quiz_level_id\":2278,\"user_id\":" + id + ",\"result\":[{\"question_id\":17362,\"result\":true,\"answers\":[\"0.7%\"],\"language_code\":\"sv\"},{\"question_id\":17361,\"result\":true,\"answers\":[\"0.2%\"],\"language_code\":\"sv\"},{\"question_id\":17364,\"result\":true,\"answers\":[\"4.6%\"],\"language_code\":\"sv\"},{\"question_id\":17363,\"result\":true,\"answers\":[\"0.0035\"],\"language_code\":\"sv\"},{\"question_id\":17360,\"result\":true,\"answers\":[\"0.075\"],\"language_code\":\"sv\"}],\"subject_id\":55686,\"passed\":true}"


while True:
    sleep(0.75)
    response = requests.request("POST", url, data=payload, headers=headers)
    data = json.loads(response.text)
    print('Fick %s poäng' % data['points'])
