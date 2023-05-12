# coding=utf-8

import os
import platform
import tkinter
from tkinter import *
from HCNetSDK import *
from PlayCtrl import *
from time import sleep

from HcnetCore import GetPlatform, SetSDKInitCfg, RealDataCallBack_V30, OpenPreview, capture, LoginDev
from client import sendPic, sendPicData
from fangfa import comparehash


# 登录的设备信息
DEV_IP = create_string_buffer(b'192.168.3.5')
DEV_PORT = 8000
DEV_USER_NAME = create_string_buffer(b'admin')
DEV_PASSWORD = create_string_buffer(b'vfes0001')

WINDOWS_FLAG = True
win = None  # 预览窗口
funcRealDataCallBack_V30 = None  # 实时预览回调函数，需要定义为全局的

PlayCtrl_Port = c_long(-1)  # 播放句柄
Playctrldll = None  # 播放库
FuncDecCB = None   # 播放库解码回调函数，需要定义为全局的

previousPic = None


if __name__ == '__main__':
# def start():
    # 创建窗口
    win = tkinter.Tk()
    #固定窗口大小
    win.resizable(0, 0)
    win.overrideredirect(True)

    sw = win.winfo_screenwidth()
    # 得到屏幕宽度
    sh = win.winfo_screenheight()
    # 得到屏幕高度

    # 窗口宽高
    ww = 520
    wh = 380
    x = (sw - ww) / 2
    y = (sh - wh) / 2
    win.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

    # 创建退出按键
    b = Button(win, text='退出', command=win.quit)
    b.pack()
    # 创建一个Canvas，设置start其背景色为白色
    cv = tkinter.Canvas(win, bg='white', width=ww, height=wh)
    cv.pack()

    # 获取系统平台
    GetPlatform()

    # 加载库,先加载依赖库
    os.chdir(r'./lib/linux')
    Objdll = cdll.LoadLibrary(r'./libhcnetsdk.so')
    Playctrldll = cdll.LoadLibrary(r'./libPlayCtrl.so')

    SetSDKInitCfg()  # 设置组件库和SSL库加载路径

    # 初始化DLL
    Objdll.NET_DVR_Init()
    # 启用SDK写日志
    Objdll.NET_DVR_SetLogToFile(3, bytes('./SdkLog_Python/', encoding="utf-8"), False)
   
    # 获取一个播放句柄
    if not Playctrldll.PlayM4_GetPort(byref(PlayCtrl_Port)):
        print(u'获取播放库句柄失败')

    # 登录设备
    (lUserId, device_info) = LoginDev(Objdll)
    if lUserId < 0:
        err = Objdll.NET_DVR_GetLastError()
        print('Login device fail, error code is: %d' % Objdll.NET_DVR_GetLastError())
        # 释放资源
        Objdll.NET_DVR_Cleanup()
        exit()

    setModeSign = Objdll.NET_DVR_SetCapturePictureMode(1)
    print('set mode:', setModeSign)

    
    # 定义码流回调函数
    funcRealDataCallBack_V30 = REALDATACALLBACK(RealDataCallBack_V30)
    # 开启预览
    lRealPlayHandle = OpenPreview(Objdll, lUserId, funcRealDataCallBack_V30)
    if lRealPlayHandle < 0:
        print ('Open preview fail, error code is: %d' % Objdll.NET_DVR_GetLastError())
        # 登出设备
        Objdll.NET_DVR_Logout(lUserId)
        # 释放资源
        Objdll.NET_DVR_Cleanup()
        exit()

    capture(Objdll)

    #show Windows
    win.mainloop()    

    # 开始云台控制
    # lRet = Objdll.NET_DVR_PTZControl(lRealPlayHandle, PAN_LEFT, 0)
    # if lRet == 0:
    #     print ('Start ptz control fail, error code is: %d' % Objdll.NET_DVR_GetLastError())
    # else:
    #     print ('Start ptz control success')

    # # 转动一秒
    # sleep(1)

    # 停止云台控制
    # lRet = Objdll.NET_DVR_PTZControl(lRealPlayHandle, PAN_LEFT, 1)
    # if lRet == 0:
    #     print('Stop ptz control fail, error code is: %d' % Objdll.NET_DVR_GetLastError())
    # else:
    #     print('Stop ptz control success')

    # 关闭预览
    Objdll.NET_DVR_StopRealPlay(lRealPlayHandle)
    print('close preview ...')
    # 停止解码，释放播放库资源
    if PlayCtrl_Port.value > -1:
        Playctrldll.PlayM4_Stop(PlayCtrl_Port)
        Playctrldll.PlayM4_CloseStream(PlayCtrl_Port)
        Playctrldll.PlayM4_FreePort(PlayCtrl_Port)
        PlayCtrl_Port = c_long(-1)

    # 登出设备
    Objdll.NET_DVR_Logout(lUserId)

    # 释放资源
    Objdll.NET_DVR_Cleanup()


# start()
# if __name__ == '__main__':
#     i = 0
#     start()
    # while i < 1:
    #     print(i)
    #     sleep(1)
    #     start()
    #     i += 1
