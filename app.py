from json import loads

from requests import get, post

from creds import authorize

auth = authorize()

headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'authorization': "Bearer %s" % auth['token'],
    'Postman-Token': "36cc45e2-6417-41fb-9bba-57695f89e215"
}

detailsUrl = "https://api.studi.se/users/%s" % auth['user_id']

detailsResponse = get(detailsUrl, headers=headers)
detailsData = loads(detailsResponse.text)
print('Inloggad som %s, du har %d poäng' % (detailsData['display_name'], detailsData['points']))

url = "https://api.studi.se/lessons/quizReport"
payload = "{\"quiz_level_id\":2278,\"user_id\":" + auth[
    'user_id'] + ",\"result\":[{\"question_id\":17362,\"result\":true,\"answers\":[\"0.7%\"],\"language_code\":\"sv\"},{\"question_id\":17361,\"result\":true,\"answers\":[\"0.2%\"],\"language_code\":\"sv\"},{\"question_id\":17364,\"result\":true,\"answers\":[\"4.6%\"],\"language_code\":\"sv\"},{\"question_id\":17363,\"result\":true,\"answers\":[\"0.0035\"],\"language_code\":\"sv\"},{\"question_id\":17360,\"result\":true,\"answers\":[\"0.075\"],\"language_code\":\"sv\"}],\"subject_id\":55686,\"passed\":true}"


def send_request():
    response = post(url, data=payload, headers=headers)
    data = loads(response.text)
    print('Fick %s poäng' % data['points'])


while True:
    send_request()
