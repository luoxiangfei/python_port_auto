# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Date  : 2019/3/13/013

import time
from appium import webdriver
import os
class get_Token():
    '''这个APP自动化获取token的类'''
    def __init__(self):
        de=os.popen("adb shell getprop ro.boot.serialno")
        ve = os.popen ("adb shell getprop ro.build.version.release")
        self.devicenName= de.read().replace('\n', '')
        self.getVersion=ve.read().replace('\n', '')
    def dl_app(self,deviceName="172.168.70.193:5555"):
        '''打开APP'''
        try:
            self.desired_caps = {}
            self.desired_caps['platformName'] = 'Android'  # 平台
            self.desired_caps['deviceName'] = self.devicenName  # 手机ID
            self.desired_caps['platformVersion'] = self.getVersion  # 系统版本
            # self.desired_caps['app'] = 'E:/autotestingPro/app/UCliulanqi_701.apk'   # 指向.apk文件，如果设置appPackage和appActivity，那么这项会被忽略
            self.desired_caps['appPackage'] = 'com.cmic.college'     # APK包名
            self.desired_caps['appActivity'] = 'com.cmcc.cmrcs.android.ui.activities.WelcomeActivity'     # 被测程序启动时的Activity
            self.desired_caps['unicodeKeyboard'] = 'true'   # 是否支持unicode的键盘。如果需要输入中文，要设置为“true”
            self.desired_caps['resetKeyboard'] = 'true' # 是否在测试结束后将键盘重轩为系统默认的输入法。
            self.desired_caps['newCommandTimeout'] = '120' # Appium服务器待appium客户端发送新消息的时间。默认为60秒
            self.desired_caps['noReset'] = True # true:不重新安装APP，false:重新安装app
            #self.desired_caps['automationName'] = "uiautomator2"
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",self.desired_caps)
        except Exception as e:
            raise e
        self.driver.implicitly_wait(10)
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("消息")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("欧欧欧")').click()
    def get_tk(self):
        """获取token"""
        driver=self.driver
        driver.find_element_by_android_uiautomator('new UiSelector().text("http://192.168.203.250:8180/miyou/interface/index.html")').click()
        time.sleep(2)
        token1=driver.find_element_by_xpath('//android.widget.FrameLayout[1]/android.widget.'
                                            'FrameLayout[1]/android.widget.FrameLayout[1]/android.'
                                            'widget.LinearLayout[1]/android.widget.ScrollView[1]/an'
                                            'droid.widget.LinearLayout[1]/android.widget.TextView[1]')
        token2 = token1.text[10:]
        if __name__ == '__main__':
            print(token2)
        driver.find_element_by_xpath("//android.widget.TextView[@text='确定']").click()
        driver.keyevent(4)   #使用物理返回键一次
        time.sleep(2)
        print(token2)
        return token2
    def quit_dr(self):
        '''关闭driver'''
        self.driver.quit()
    def run_token(self):
        tk=get_Token()
        tk.dl_app()
        while True:
            try:
                tk.get_tk()
            except:
                tk.quit_dr()
                tk.dl_app()
                continue
if __name__ == '__main__':
    token=get_Token()
    token.run_token()