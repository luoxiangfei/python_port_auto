# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Date  : 2019/2/23/023

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from common.LogInfo import logger
class SendEmail(object):
    '''发送邮件功能'''
    def __init__(self,addresser,addressee,smtp,user,passwd):
        self.addresser=addresser   #发送人地址
        self.addressee=addressee    #收件人地址
        self.smtp=smtp              #smtp地址
        self.user=user              #发送邮箱账号
        self.passwd=passwd          #邮箱密码
    def email_init(self,report,reportName):
        '''邮件发送'''
        with open(report,'rb')as f:
            mail_body = f.read()
        # 创建一个带附件的邮件实例
        msg = MIMEMultipart()
        #msg.attach(MIMEApplication(""))        #设置发送的正文
        report_file = MIMEApplication(mail_body)
        # 定义附件名称（附件的名称可以随便定义，你写的是什么邮件里面显示的就是什么）
        report_file.add_header ('Content-Disposition', 'attachment', filename=reportName)
        msg.attach(report_file) # 添加附件
        msg['Subject'] = '自动化测试报告: '+reportName # 邮件标题
        msg['From'] = self.addresser  #发件人
        msg['To'] = ",".join(self.addressee) #收件人列表
        try:
            server = smtplib.SMTP(self.smtp)
            server.login(self.user,self.passwd)
            server.sendmail(self.addresser,self.addressee,msg.as_string())
            server.quit()
            logger.info("----邮件发送成功----")

        except smtplib.SMTPException as e:
            logger.error("邮件发送失败{}".format(e))

if __name__ == '__main__':
    addressee=["290958890@qq.com","240080267@qq.com"]
    email=SendEmail("13694245189@139.com",addressee,"smtp.139.com","13694245189@139.com","199213luo")
    email.email_init(r"D:\python_project\meetyou_automation\report\report.html","report.html")
