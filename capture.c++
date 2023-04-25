#include <stdio.h>
#include <string.h>
#include <iostream>
#include "unistd.h"
#include "PlayM4.h"
using namespace std;

LONG     g_lPort                =  -1;
CString  m_strCapPicPath        = _T("");
CString  sFilePath              = _T("");
UINT	   m_npic_bmp             = 0;

HWND hWnd = 0;  //Linux系统如果使用Qt进行界面开发，可以获取窗口句柄

void CALLBACK DisplayCBFun(long nPort,char * pBuf,long nSize,long nWidth,long nHeight,long nStamp,long nType,long nReserved)
{
	TRACE("zytest: get vid pic !\n");

	if(m_strCapPicPath.Compare(""))
	{
         sFilePath.Format("%s\\capture%02d.bmp", "g:\\", m_npic_bmp++);
	}
	else
	{
         sFilePath.Format("C:\\capture%02d.bmp", m_npic_bmp++);
	}

	//连续抓BMP图片
	PlayM4_ConvertToBmpFile(pBuf,nSize,nWidth,nHeight,nType,sFilePath.GetBuffer(sFilePath.GetLength()));
}

void main() 
{
   	BOOL   bFlag          = FALSE;
	DWORD  dwErr          = 0;
	LONG dwWidth          = 0;
	LONG dwHeight         = 0;
	DWORD dwSize          = 0;
	DWORD dwCapSize       = 0;

    //获取播放库端口号
      if (g_lPort == -1)
      {
          bFlag = PlayM4_GetPort(&g_lPort);
          if (bFlag == FALSE)
          {
               dwErr = PlayM4_GetLastError(g_lPort);
               return;
           }
        }

    //打开待播放的文件
    bFlag = PlayM4_OpenFile(g_lPort,"test.mp4");

    //设置显示回调
    PlayM4_SetDisplayCallBack(g_lPort,DisplayCBFun);

    //解码显示
    bFlag = PlayM4_Play(g_lPort,hWnd);


    sleep(10000);

    //获取当前视频文件的分辨率
    bFlag  = PlayM4_GetPictureSize(g_lPort,&dwWidth,&dwHeight);
    dwSize = dwWidth * dwHeight * 5;
	
    //申请抓图内存
    if (m_pCapBuf == NULL)
    {
          m_pCapBuf = new BYTE[dwSize];
          if (m_pCapBuf == NULL)
          {
                return;
           }
      }

    //抓图BMP图片
    bFlag = PlayM4_GetBMP(g_lPort,m_pCapBuf,dwSize,&dwCapSize);
    if (bFlag == FALSE)
    {
         dwErr = PlayM4_GetLastError(m_lPort);
     }


    
    if (m_pCapBuf != NULL)
    {
        delete [] m_pCapBuf;
        m_pCapBuf = NULL;
    }

    //停止解码
    PlayM4_Stop(g_lPort);

    //关闭文件
    PlayM4_CloseFile(g_lPort);

    //释放端口号
    PlayM4_FreePort(g_lPort);

     g_lPort = -1;

}