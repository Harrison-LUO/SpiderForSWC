import os
import requests
from bs4 import BeautifulSoup

# url前缀
preurl = 'https://swcregistry.io/docs/'

# 从url获取解析
def geturl(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup

#提取文件名、文件内容
def savefile(dirname, soup):
    solname = soup.select(
        'body > div.navPusher > div > div.container.mainContainer > div > div.post > article > div > span > h3')
    content = soup.select('body > div.navPusher > div > div.container.mainContainer > div > div.post > article > '
                          'div > span > pre > code')
    yamlname = soup.select(
        'body > div.navPusher > div > div.container.mainContainer > div > div.post > article > div > span > h4')
    print('Num of solname:', len(solname))
    print('Num of yamlname:', len(yamlname))
    print('Num of content:', len(content))
    path = 'SWC/' + dirname
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)
    i = 0
    for sol, yaml in zip(solname, yamlname):
        print(sol.text)
        print(yaml.text)

        with open(path + '/' + sol.text, 'w') as f:
            f.write(content[i].text)
            f.close()
        with open(path + '/' + yaml.text, 'w') as f:
            f.write(content[i + 1].text)
            f.close()
        i += 2


if __name__ == '__main__':
    for swcid in range(100, 137):
        dirname = 'SWC-' + str(swcid)
        print(preurl + dirname)
        url = preurl + dirname
        soup = geturl(url)
        savefile(dirname, soup)
