import requests as r
from common.scripts.parama import  logger
import json



def send_request(url,data):
    cookies = {
        'PHPSESSID=su5vhrrc8faesba8nm2d84oj5g'
    }
    headers = {'content-type': 'application/json'}
    result = r.post(url=url,data=data,headers=dict(headers),cookies=cookies)
    return result.json()



#登陆实效性为1天，需要写个登陆的接口，目前是静态的放在cookies里面的
def get_lts_apiID():
    '''获取接口文档每个接口对应的apiID'''
    url = 'https://www.eolinker.com/apiManagementPro/Api/getApiListByCondition'
    data = {
        'spaceKey': '8exT2vp438dcd6bd05a52776d06e9e63b0c4d4348072afb',
        'projectHashKey': '8exT2vp438dcd6bd05a52776d06e9e63b0c4d4348072afb',
        'groupID': -1,
        'orderBy': 4,
        'asc': 1,
        'pageSize': 300,
        'page': 1,
        'condition': 0,
        'apiStatus': 0
    }
    #发送请求
    res=send_request(url=url,data=data)
    ll = [res['apiList'][i]['apiID'] for i in range(len(res['apiList']))]
    api_set = set(ll)
    # 拿到最终需要请求的api集合
    # return list(api_set)
    return get_lts_apiID






def get_api_info(apilist=get_lts_apiID()):
    '''调用查询接口详情信息，获取想要的接口信息'''
    url = 'https://www.eolinker.com/apiManagementPro/Api/getApi'
    data = {
        'spaceKey': '8exT2vp438dcd6bd05a52776d06e9e63b0c4d4348072afb',
        'projectHashKey': '8exT2vp438dcd6bd05a52776d06e9e63b0c4d4348072afb',
        'apiID':apilist[0] if isinstance(type(apilist),list) else apilist
    }
    res = send_request(url=url, data=data)
    return res

ff=get_api_info(apilist=466417)
print(ff['apiInfo'])

if __name__ == '__main__':
    f=send_request(url='http://apidoc.gearbest-beta.com/server/index.php?g=Web&c=User&o=getUserInfo',data='')
    print(f)

# import os
# file_name = '/Users/lyg/ly/common/service'
# os.mkdir(file_name)

# class Create_domain():
#     '''创建业务域文件'''
#     dir = 'service'
#     open()