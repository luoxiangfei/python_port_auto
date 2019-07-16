# -*- coding: utf-8 -*-
# @Author: 罗湘飞
# @Date  : 2019/2/22/022
import pymysql
from common.LogInfo import logger
class Mysql(object):
    '''mysql数据库操作'''
    def __init__(self,host,port,user,passwd,db):
        try:
            self.log=logger
            self.conn = pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=db )  # 连接数据库
            self.cur = self.conn.cursor()   # 创建游标
            self.log.info("数据库【{}】连接成功".format(host))
        except Exception as e:
            self.log.error("数据库连接失败，程序退出，请重新连接数据库再重试")
    def __del__(self):
        self.cur.close()
        # 关闭连接对象
        self.conn.close()
        # self.log.info("数据库关闭")
    def sql_select(self,sql):
        '''查询数据库'''
        #sql="SELECT * FROM t_code;"
        self.cur.execute(sql)    # 查询lcj表中存在的数据
        ret1 = self.cur.fetchall()   # fetchall:获取lcj表中所有的数据
        self.conn.commit()
        return ret1
    def sql_insert_into(self,sql):
        '''插入数据库'''
        self.cur.execute(sql)
        self.conn.commit ()
        self.log.info("数据插入成功")
    def sql_delete(self,sql):
        '''删除数据'''
        self.cur.execute(sql)
        self.conn.commit ()
if __name__ == '__main__':
    my=Mysql(host="192.168.203.202",port=6033,user="root",passwd="mysql#123",db="andfans_activity")
    l=my.sql_insert_into("UPDATE `andfans_activity`.`t_report_record` SET `date` = '2019-06-1' , `resource` = '1' , `join_members` = '1' , `receive_members` = '1' , `login_members` = '1' , `create_time` = '2019-07-11 09:49:53' WHERE `id` = '6';")

