# coding=utf-8
from HCNetSDK import *
from HcnetCore import startVideo
from readConfig import readConfig
from multiprocessing import Process


if __name__ == '__main__':
    config = readConfig('P01')
    print('config:', config)
    # for i in range(len(config['deviceList'])):
    #     ip = config['deviceList'][i]
    #     print('start ip:', ip)
    #     startVideo(create_string_buffer(ip.encode()), 8000, create_string_buffer(b'admin'), create_string_buffer(b'vfes0001'))
    #     # break

    for i in range(len(config['deviceList'])):
        ip = config['deviceList'][i]
        print('start ip:', ip)
        p = Process(target=startVideo, args=(ip.encode(), 8000, create_string_buffer(b'admin'), create_string_buffer(b'vfes0001')))
        p.start()
        # p.join()

    # ip = '192.168.3.5' #config['deviceList'][0]
    # print('start ip:', ip)
    # byteIp = b'192.168.3.5'
    # # startVideo(create_string_buffer(byteIp), 8000, create_string_buffer(b'admin'), create_string_buffer(b'vfes0001'))
    # startVideo(create_string_buffer(ip.encode()), 8000, create_string_buffer(b'admin'), create_string_buffer(b'vfes0001'))