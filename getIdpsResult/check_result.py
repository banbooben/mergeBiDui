#!/usr/bin python3
# -*- coding: utf-8 -*-

# @Author: shangyameng
# @Email: shangyameng@datagrand.com
# @Date: 2020-06-03 11:08:56
# @LastEditTime: 2020-06-03 11:47:39
# @FilePath: /code/getIdpsResult/check_result.py

from get_result import MergeResult


def get_all_result():
    pass


class DiffResultCheck(object):
    login_url = "http://idps2-zybk.datagrand.cn/api/login"
    diff_url = "http://idps2-zybk.datagrand.cn/api/diff/history/"

    def __init__(self, diff_id, tmp_id="5"):
        self.merger = MergeResult(self.login_url)
        self.tmp_id = tmp_id
        self.diff_id = diff_id
        self.result = {}
        self.tmp_result = self.merger.login_and_get_result({"id": self.tmp_id, "diff_url": self.diff_url})
        self.request_result = self.merger.login_and_get_result({"id": self.diff_id, "diff_url": self.diff_url})

    def get_result(self):
        if self.tmp_result and self.request_result:
            diff_res = self.request_result["result"]["diff"]["result"]
            tmp_res = self.tmp_result["result"]["diff"]["result"]
            print(f"比对结果个数：{len(diff_res)}")
            print(f"模版结果个数：{len(tmp_res)}")
            for diff_item in tmp_res:
                if diff_item in diff_res:
                    diff_res.remove(diff_item)

            print(f"比对结果处理后结果个数：{len(diff_res)}")
            # for key in self.tmp_result.keys():
            #     if key != "result":
            #         print(key, self.tmp_result[key])
            #     else:
            #         for keyy in self.tmp_result[key].keys():
            #             print(keyy, self.tmp_result[key][keyy])
            # print("\n\n")
            # for diff_key in self.request_result.keys():
            #     print(diff_key, self.request_result[diff_key])


if __name__ == "__main__":
    DiffResultCheck("6").get_result()
