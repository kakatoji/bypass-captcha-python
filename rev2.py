import requests,time,json,sys,os

def countdown(self,second):
        while second:
            mins,secs = divmod(second,60)
            timer = "  \033[1;33m✒ \033[1;37mWaiting\033[1;37m \033[37m⟨\033[0;36m{:02d}:{:02d}\033[1;37m⟩ ".format(mins,secs)
            print(timer,end="\r")
            sleep(1)
            second -= 1
def setCaptcha(key,web,sitekey):
    url='https://api.anycaptcha.com/';
    header={'Host': 'api.anycaptcha.com','Content-Type': 'application/json'}
    data={
        'clientKey': key,
        'task':{
            'type':'RecaptchaV2TaskProxyless',
            'websiteURL':web,
            'websiteKey':sitekey,
            'isInvisible':False
        }
    }
    awal = requests.post(url+'createTask',json=data,headers=header).text
    task = json.loads(awal)
    if task["taskId"] == False:
        print("saldo abis kira-kira")
    data = {
        'clientKey': key,
        'taskId' : task["taskId"]
    }
    while True:
        print("wait for solution",end="\r")
        news = requests.post(url+"getTaskResult",json=data,headers=header).text
        rest = json.loads(news)
        if rest['status'] == 'processing':
            print("sedang memproses",end="\r")
            time.sleep(7)
            continue
        return rest['solution']['gRecaptchaResponse']
    

ss=setCaptcha('xxxxxxkey lu','https://www.ltcclick.com',"6LeDnY4UAAAAADU25pfECqAtJp3Nf34NKs7ebR6W")
print(ss)