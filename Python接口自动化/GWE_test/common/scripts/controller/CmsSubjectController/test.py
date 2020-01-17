import requests

def get_api_list():
    url='http://apidoc.gearbest-beta.com/server/index.php?g=Web&c=Api&o=getApiList'
    data={'projectID':94,'groupID':3,'asc':0}
    header = {'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8','Cookie':'PHPSESSID=su5vhrrc8faesba8nm2d84oj5g',
              'Host':'apidoc.gearbest-beta.com','Origin':'http://apidoc.gearbest-beta.com'
              }

    res = requests.post(url=url,data=data,headers=header)
    print(res.json())

if __name__ == '__main__':
    get_api_list()