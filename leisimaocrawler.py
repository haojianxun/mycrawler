import requests
from lxml import html
import os
import shutil
from multiprocessing.dummy import Pool

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'6U2l_2132_saltkey=tCqmnQwC; 6U2l_2132_lastvisit=1523777275; 6U2l_2132_sid=Twn3V8; Hm_lvt_6a60b923391636750bd84d6047523609=1523779927; 6U2l_2132_sendmail=1; 6U2l_2132_region=yes; 6U2l_2132_st_p=0%7C1523781128%7C1289162a252d0d1123daa78468da1255; 6U2l_2132_visitedfid=40D122; 6U2l_2132_viewid=tid_18116; Hm_lpvt_6a60b923391636750bd84d6047523609=1523780180; 6U2l_2132_lastact=1523781129%09region.php%09',
    'DNT':'1',
    'Host':'www.lesmao.me',
    
}

baseurl = 'http://www.lesmao.me/'

def get_page(pagenum):
    pagehtml = html.fromstring(requests.get(baseurl , headers=headers).content)
    urls = []
    for i in pagehtml.xpath('//div[@class="bution"]/h2/a/@href'):
        urls.append(baseurl+i)
    return urls
        

def getpagelink(u):
    link = html.fromstring(requests.get(u , headers=headers).content)
    
    title = link.xpath('//div[@class="thread-down-c"]/h2/text()')
    
    totle = link.xpath('//div[@class="pg"]/a[last()-1]/text()')
    
    pageurls = [u]
    
    for i in link.xpath('//div[@class="pg"]/a/@href'):
        pageurls.append(baseurl + i)
    return pageurls
        
    print(pageurls)




def save_image(purl):
    hea = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Host':'p.tao1o.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    
}
    s = html.fromstring(requests.get(purl , headers=headers).content)
    title = s.xpath('//div[@class="thread-down-c"]/h2/text()')
    totle = s.xpath('//div[@class="pg"]/a[last()-1]/text()')[0]
    jpglink = s.xpath('//ul[@class="adw"]/li/img/@src')
    num = len(jpglink)
    dirpath = r"C:\Users\Administrator"
    dirname = u"【{}P】{}".format(totle , title)
    
    path = os.path.join(dirpath , dirname)
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        os.chdir(path)
    n = 1
    for i in range(num):
        print(jpglink[i-1])
        try:
            filename = '%s/%s.jpg' % (path, n)
            print(u'开始下载图片:%s 第%s张' % (dirname, n))
            print("图片下载中.....")
            with open(filename, "wb+") as f:
                f.write(requests.get(jpglink[i-1], headers=hea).content)
                
            n += 1
            
        except:
            pass
        
      
    

    #print(pageurls[:-1])
pag = input(u'请输入页码：')    
a = (get_page(pag))
pool = Pool(4)
bb = pool.map(getpagelink, a) 
for i in bb:
    pool.map(save_image , i)
        