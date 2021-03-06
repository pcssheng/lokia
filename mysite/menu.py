#-*— coding:UTF-8 -*-
#/usr/bin/env python
"""
module descript
"""
import json
import token
import requests
import sys

from django.conf import settings
reload(sys)
sys.setdefaultencoding('utf-8')
"""
这个文件中包含的是微信的自定义菜单
"""
MENU = {
    "button": [
        {
            "name": "公司咨询",
            "sub_button": [
                {
                    "type": "click",
                    "name": "公司介绍",
                    "key": "about"
                },
                {
                    "type": "view",
                    "name": "公司新闻",
                    "url": "http://v.qq.com/"
                },
                {
                    "type": "click",
                    "name": "招聘信息",
                    "key": "你吗"
                },
                {
                    "type": "view",
                    "name": "优惠活动",
                    "url": "http://v.qq.com/"
                },
                {
                    "type": "click",
                    "name": "联系我们",
                    "key": "contact"
                }]
        },
        {
            "name": "服务信息",
            "sub_button": [
                {
                    "type": "view",
                    "name": "服务介绍",
                    "url": "http://www.soso.com/"
                },
                {
                    "type": "view",
                    "name": "编辑团队",
                    "url": "http://v.qq.com/"
                },
                {
                    "type": "click",
                    "name": "订单追踪",
                    "key": "order"
                },
                {
                    "type": "view",
                    "name": "成功案例",
                    "url": "http://v.qq.com/"
                },
                {
                    "type": "view",
                    "name": "常见问题",
                    "url": "http://v.qq.com/"
                }]
        },
        {
            "name": "留学咨询",
            "sub_button": [
                {
                    "type": "view",
                    "name": "申请规划",
                    "url": "http://www.soso.com/"
                },
                {
                    "type": "view",
                    "name": "选校信息",
                    "url": "http://v.qq.com/"
                },
                {
                    "type": "click",
                    "name": "文书指导",
                    "key": "你吗"
                },
                {
                    "type": "view",
                    "name": "网申投递",
                    "url": "http://v.qq.com/"
                },
                {
                    "type": "view",
                    "name": "就业信息",
                    "url": "http://v.qq.com/"
                }]
        }]
}


@token.ensure_access_token_effective
def create_menu():
    menu_data = {"access_token": token.ACCESS_TOKEN}
    r = requests.post(settings.COMPANY_URL['menu']['CREATE_MENU_URL'],
                      params=menu_data, data=json.dumps(MENU))
    return r.text


if __name__ == '__main__':
    print  create_menu()