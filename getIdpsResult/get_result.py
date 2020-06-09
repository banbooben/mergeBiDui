#!/usr/bin python3
# -*- coding: utf-8 -*-

# @Author: shangyameng
# @Email: shangyameng@datagrand.com
# @Date: 2020-05-29 12:23:29
# @LastEditTime: 2020-06-03 11:09:57
# @FilePath: /code/getIdpsResult/get_result.py


import requests
import json


class MergeResult(object):
    access_token = ""
    username = "superadminpro"
    password = "BEgPDsMumFlc"
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }

    def __init__(self, login_url):
        self.login_url = login_url

    def get_request_result_by_get(self, url, id):
        new_url = url + str(id)
        request_result = requests.get(url=new_url, headers=self.headers)
        res = json.loads(request_result.text)
        return res

    def login_by_user(self):
        res = None
        if not self.access_token:
            if self.login_url:
                data = {"username": self.username, "password": self.password}
                request_result = requests.post(url=self.login_url, data=data, headers=self.headers)
                if request_result.status_code == 200:
                    result = json.loads(request_result.text)
                    if result:
                        res = "Bearer " + result.get("access_token", None)
                        self.access_token = res
                        return "登录成功"
                for i in range(re_try=3):
                    self.login_by_user()
                return "登录失败"
            return "缺少登录地址"
        return "已是登录状态"
        
                

    def login_and_get_result(self, params):
        status = self.login_by_user()
        if self.access_token:
            self.headers.update({"Authorization": self.access_token})
                # 请求获取对比结果
            id = params.get("id", None)
            diff_url = params.get("diff_url", None)
            if id and diff_url:
                res = self.get_request_result_by_get(diff_url, id)
                return res
            else:
                return "缺少任务id"
        else:
            return status



if __name__ == "__main__":
    diff_url = "http://idps2-zybk.datagrand.cn/api/diff/history/"
    extract_result = "http://idps2-zybk.datagrand.cn/api/extracting/retry?id="
    login_url = "http://idps2-zybk.datagrand.cn/api/login"

    # 获取对比结果的params
    # params = {"id": "3", "diff_url": diff_url}

    # 获取抽取结果的params
    params = {"id": "106", "diff_url": extract_result}
    res = MergeResult(login_url).login_and_get_result(params)
    print(res)
    # with open("./tmp_diff_result.json", "w", encoding="utf-8") as f:
    #     f.write(json.dumps(res, ensure_ascii=False))
