#-*— coding:UTF-8 -*-
#/usr/bin/env python
"""
module descript
"""
import time

from django.shortcuts import render_to_response


class BaseResponse(object):
    """
    这个类类似于Django的通用视图，response_name是要输出的消息模版
    msg是用户输入消息的一个字典,如果要自定义消息，只要自定义context
    就可以了，消息内容格式由微信官方指定
    """
    response_type = "application/xml"

    def __init__(self, msg, template_name="lib/text.xml"):
        self.msg = msg
        self.template_context = {'ToUserName': msg['FromUserName'],
                                 'FromUserName': msg['ToUserName'],
                                 'CreateTime': time.time()}
        self.template_name = template_name

    def get_response(self, context=None):
        if context:
            self.template_context.update(context)
        res = render_to_response(self.template_name, self.template_context,
                                 mimetype=self.response_type)
        return res
