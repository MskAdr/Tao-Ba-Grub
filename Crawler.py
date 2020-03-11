import requests
import zlib
import json
import base64
import time
from Structure import Project,Record

def AddSalt(ori:bytearray):
    Salt = '%#54$^%&SDF^A*52#@7'
    i = 0
    for ch in ori:
        if i%2==0:
            ch = ch ^ ord(Salt[(i//2) % len(Salt)])
        ori[i]=ch
        i+=1
    return ori

def EncodeData(ori:str):
    Length = len(ori)
    Message = str.encode(ori)
    Compressed = bytearray(zlib.compress(Message))
    Salted = AddSalt(Compressed)
    Result = base64.b64encode(Salted).decode('utf-8')
    return str(Length) + '$' + Result

def DecodeData(ori:str):
    Source = ori.split('$')[1]
    B64back = bytearray(base64.b64decode(Source))
    Decompressed = AddSalt(B64back)
    Result = zlib.decompress(Decompressed).decode('utf-8')
    return json.loads(Result)

def SendRequest(url:str,data:str):
    Headers = {
        'Content-Type': 'application/json', 
        'Origin': 'https://www.tao-ba.club', 
        'Cookie': 'l10n=zh-cn', 
        'Accept-Language': 'zh-cn', 
        'Host': 'www.tao-ba.club', 
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15', 
        'Referer': 'https://www.tao-ba.club/', 
        'Accept-Encoding': 'gzip, deflate, br', 
        'Connection': 'keep-alive'
    }
    Data = EncodeData(data)
    Res = requests.post(url=url,data=Data,headers=Headers)
    ResText = Res.text
    return DecodeData(ResText)

def GetDetail(pro_id:int):
    Data='{{"id":"{0}","requestTime":{1},"pf":"h5"}}'.format(pro_id,int(time.time()*1000))
    Response=SendRequest('https://www.tao-ba.club/idols/detail',Data)
    return Project(int(Response['datas']['id']),
        Response['datas']['title'],
        int(Response['datas']['start']),
        int(Response['datas']['expire']),
        float(Response['datas']['donation']),
        int(Response['datas']['sellstats'])
    )
    
def GetPurchaseList(pro_id:int):
    Data='{{"ismore":false,"limit":15,"id":"{0}","offset":0,"requestTime":{1},"pf":"h5"}}'.format(pro_id,int(time.time()*1000))
    Response=SendRequest('https://www.tao-ba.club/idols/join',Data)
    Founderlist = []
    Cleared = False
    pages=0
    while not Cleared:
        for thisRecord in Response['list']:
            Founderlist.append(Record(pro_id,
                int(thisRecord['userid']),
                thisRecord['nick'],
                float(thisRecord['money']),
            ))
        if len(Response['list']) == 15:
            pages += 1
            Data='{{"ismore":true,"limit":15,"id":"{0}","offset":{2},"requestTime":{1},"pf":"h5"}}'.format(pro_id,int(time.time()*1000),pages*15)
            Response=SendRequest('https://www.tao-ba.club/idols/join',Data)
        else:
            Cleared = True
    return Founderlist