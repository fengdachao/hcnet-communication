import http.client
import json

from constant import HOST

# host = "192.168.3.2"
# host = "baidu.com"

def read(url):
    conn = http.client.HTTPConnection(HOST, 3001)
    conn.request("GET", url)
    response = conn.getresponse()
    configData = b''
    while chunk := response.read(200):
        # print(repr(chunk))
        # print(chunk)
        configData += chunk
    # print('config string:', configData)
    configJson = json.loads(configData)
    conn.close()
    return configJson
def readConfig(number):
    res = read('/api/config/list')
    if res:
        for i in range(len(res)):
            item = res[i]
            if (item['number'] == number):
                return item
    return None

def readParam():
    return read('/api/config/param')
    

if __name__ == '__main__':
    config = readConfig()
    print('config:', config)
