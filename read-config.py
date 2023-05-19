import http.client
import json

host = "localhost"
# host = "baidu.com"
conn = http.client.HTTPConnection(host, 3001)
conn.request("GET", "/api/config/list")
response = conn.getresponse()
configData = b''
while chunk := response.read(200):
    # print(repr(chunk))
    # print(chunk)
    configData += chunk
# print('config string:', configData)
configJson = json.loads(configData)
print(configJson[0]['params'])
conn.close()

if __name__ == '__main__':
    print('running python...')
