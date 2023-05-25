import http.client
import json

host = "192.168.3.2"
# host = "baidu.com"

def read(url):
    conn = http.client.HTTPConnection(host, 3001)
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
def readConfig():
    return read('/api/config/list')

def readParam():
    return read('/api/config/param')
    

if __name__ == '__main__':
    config = readConfig()
    print('config:', config)
