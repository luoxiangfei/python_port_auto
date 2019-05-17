# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Date  : 2019/2/15/015

import hashlib
import time
import random
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5
class md5Page(object):
    def strMD5(self,strNum):
        '''时间戳MD5加密'''
        # 待加密信息
        m = hashlib.md5 ()
        m.update (strNum.encode("utf-8"))
        MD5 = m.hexdigest ()
        return MD5.upper()
    def suiji_shu(self):
        '''获取随机12位数'''
        s=random.randint(1,999999999999)
        return str(s)
    def shijian(self):
        '''获取时间戳格式'''
        ct = time.time ()
        local_time = time.localtime (ct)
        data_head = time.strftime ("%Y-%m-%d %H:%M:%S", local_time)
        data_secs = (ct - int (ct)) * 1000
        time_stamp = "%s.%03d" % (data_head, data_secs)
        stamp = ("".join (time_stamp.split ()[0].split ("-")) + "".join (time_stamp.split ()[1].split (":"))).replace (
            '.', '')
        return stamp
    def time_str(self):
        data_time=time.strftime("%Y%m%d%H%M%S")
        return data_time
    def strRSA(self,privateKey,data):
        '''获取RSA数据签名'''
        private_keyBytes = base64.b64decode(privateKey)
        priKey = RSA.importKey(private_keyBytes)
        # priKey = RSA.importKey(privateKey)
        signer = PKCS1_v1_5.new(priKey)
        hash_obj = MD5.new(str(data).encode('utf-8'))
        signature = base64.b64encode(signer.sign(hash_obj))
        signature1 = str(signature, encoding="utf8")
        return signature1
    def strBase64(self,data):
        encodeStrTest = base64.b64encode(bytes(str(data), encoding="utf-8"))
        base=str(encodeStrTest, encoding="utf-8")
        return base
if __name__ == '__main__':
    M=md5Page()
    M.strRSA("sdfsdfs","sdfsdfsd")