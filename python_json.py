import json


def getJSON(json_file):
    with open(json_file, 'r') as fp:
        data = json.load(fp)
    print(data)

#print(json.dumps('./MOCK_DATA.json'))
myObj = getJSON('./MOCK_DATA.json')

#print(myObj.get("id", ""))