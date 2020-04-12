import requests
import json
from gucci_utils import *

proxypool_url = 'http://127.0.0.1:5555/random'
target_url = 'http://httpbin.org/get'

headers = {
    "Upgrade-Insecure-Requests": "1",
    "Host": "localhost:5555",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive"
}


def get_random_proxy():
    """
    get random proxy from proxypool
    :return: proxy
    """
    return requests.get(proxypool_url, headers=headers).text.strip()


def crawl(url, proxy):
    """
    use proxy to crawl page
    :param url: page url
    :param proxy: proxy, such as 8.8.8.8:8888
    :return: html
    """
    proxies = {'http': 'http://' + proxy}
    return requests.get(url, proxies=proxies).text


def main():
    """
    main method, entry point
    :return: none
    """
    proxy_list = []
    json_list = []
    a = 500
    while a:
        a = a - 1
        proxy = get_random_proxy()
        # proxy = '174.127.155.118:32505'
        print('get random proxy', proxy)
        time_sleep_second()
        try:
            html = crawl(target_url, proxy)
            html = json.loads(html)
        except Exception as e:
            print(e)
            continue
        proxy_list.append(proxy)
        json_list.append(html)
        print(html)
        if len(proxy_list) > 10:
            mycol_proxy.insert_one(proxy_list)
            proxy_list = []
    print(proxy_list)
    print(json_list)
    mycol_proxy.insert_one(proxy_list)
    mycol_proxy.insert_one(json_list)


if __name__ == '__main__':
    mycol_proxy = mydb["proxy"]
    main()

    # ['58.211.134.98:38480', '58.211.134.98:38480', '115.75.5.17:38351', '218.2.226.42:80', '115.223.7.110:80', '115.223.7.110:80', '218.2.226.42:80', '175.44.186.173:9000', '118.181.226.166:44640', '60.2.44.182:47293']
