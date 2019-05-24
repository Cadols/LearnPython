#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pickle
import paramiko
import threading
from conf.settings import *
from core.logger import *


class FabricHost(object):
    """Fabric主机管理"""
    def __init__(self):
        # 根据文件存在状态建立主机字典
        if os.path.exists(DB_FILE_PATH):
            self.load_host_dic()
        else:
            self.host_dic = {}
        self.actived_host_list = []  # 已激活的主机信息
        # print(self.host_dic)

    def create_host(self):
        """创建新的主机信息"""
        new_hostname = input("\033[34m请输入主机的地址：\033[0m").strip()
        if not self.host_dic.get(new_hostname):
            while True:
                new_host_port = input("\033[34m请输入主机的ssh端口号：\033[0m").strip()
                if new_host_port.isdigit():
                    new_host_username = input("\033[34m请输入主机的登录用户名：\033[0m").strip()
                    new_host_password = input("\033[34m请输入主机的登录密码：\033[0m").strip()
                    new_host_dic = {
                        "hostname": new_hostname,
                        "port": int(new_host_port),
                        "username": new_host_username,
                        "password": new_host_password
                    }
                    self.host_dic[new_hostname] = new_host_dic
                    self.write_host_dic()
                    # print("\033[33m主机 %s 信息已经保存。\033[0m\n" % new_hostname)
                    logger("launcher", "info", "create_host", "主机 %s 信息已经保存。" % new_hostname)
                    break
                else:
                    print("\033[1;31m端口号应为 1-65535 的整数\033[0m")
        else:
            print("\033[1;31m主机 %s 已存在。\033[0m\n" % new_hostname)

    def delete_host(self):
        """删除已有主机信息"""
        if self.host_dic:
            self.host_info()
            selected_host = input("\033[34m请输入您要删除的主机信息：\033[0m").strip()
            if self.host_dic.get(selected_host):
                del self.host_dic[selected_host]
                self.write_host_dic()
                # print("\033[33m主机 %s 信息已经删除。\033[0m\n" % selected_host)
                logger("launcher", "info", "delete_host", "主机 %s 信息已经删除。" % selected_host)
            else:
                print("\033[1;31m没有主机 %s 的信息\033[0m\n" % selected_host)
        else:
            print("\033[1;31m没有任何主机信息\033[0m\n")

    def active_host(self):
        """激活远程主机"""
        if self.host_dic:  # 主机信息不为空时
            while True:
                self.host_info()
                choice_host = input("\033[34m请输入您要激活的主机信息（all/全部激活，back/返回）：\033[0m").strip()
                if choice_host == "back":
                    break
                try:
                    if choice_host in self.host_dic:
                        # print("正在激活主机 %s" % choice_host)
                        hosts = {choice_host: self.host_dic[choice_host]}
                    elif choice_host == "all":
                        print("准备激活所有主机...")
                        hosts = self.host_dic
                    else:
                        print("请输入正确的主机名称")
                    if hosts:
                        for host in hosts:
                            t = threading.Thread(target=self.check_host_status, args=(host,))
                            t.start()
                        while threading.active_count() != 1:  # 当存活线程数不等于1时
                            pass
                except Exception as e:
                    print("\033[1;31m请输入正确的命令\033[0m\n")
        else:
            print("\033[1;31m请先录入主机连接信息。\033[0m\n")

    def remote_host(self):
        """与已激活的远程主机交互"""
        if self.actived_host_list:
            while True:
                input_cmd = input(">> ").strip()
                if input_cmd:
                    if input_cmd.startswith("put "):
                        target_method = self.put_file
                    elif input_cmd.startswith("get "):
                        target_method = self.get_file
                    elif input_cmd == "back":
                        break
                    else:
                        target_method = self.paramiko_ssh
                    for host in self.actived_host_list:
                        t = threading.Thread(target=target_method, args=(host, input_cmd,))
                        # t.setDaemon(True)
                        t.start()
                    while threading.active_count() != 1:  # 当存活线程数不等于1时
                        pass
        else:
            print("\033[1;31m请先激活主机\033[0m\n")

    def check_host_status(self, host):
        """检查主机状态"""
        ssh = paramiko.SSHClient()  # 创建ssh对象
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_host文件中的主机
        if not self.host_dic[host]["hostname"] in self.actived_host_list:
            try:
                print("正在激活主机 %s" % host)
                ssh.connect(hostname=self.host_dic[host]["hostname"], port=self.host_dic[host]["port"],
                            username=self.host_dic[host]["username"], password=self.host_dic[host]["password"])
            except Exception as e:
                print("\033[1;31m主机 %s 激活失败，原因为：%s\033[0m" % (host, e))
            else:
                self.actived_host_list.append(host)
                print("\033[33m主机 %s 激活成功\033[0m" % self.host_dic[host]["hostname"])
                # print(self.actived_host_list)
        else:
            print("\033[1;31m主机 %s 已激活\033[0m" % self.host_dic[host]["hostname"])
        ssh.close()

    def paramiko_ssh(self, host, cmd):
        """向远程主机发送操作指令"""
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.host_dic[host]["hostname"], port=self.host_dic[host]["port"],
                    username=self.host_dic[host]["username"], password=self.host_dic[host]["password"])
        stdin, stdout, stderr = ssh.exec_command(cmd)
        stdout_res = stdout.read()
        stderr_res = stderr.read()
        print("\033[33m主机 %s 执行命令 %s 结果如下：\033[0m" % (host, cmd))
        if stdout_res:
            print(stdout_res.decode().strip())
        elif stderr_res:
            print(stderr_res.decode().strip())
        ssh.close()

    def put_file(self, host, cmd):
        """向远程主机上传文件"""
        operate, filename = cmd.split(" ")
        # print(operate, filename)
        transport = paramiko.Transport((self.host_dic[host]["hostname"], self.host_dic[host]["port"]))
        try:
            transport.connect(username=self.host_dic[host]["username"], password=self.host_dic[host]["password"])
            sftp = paramiko.SFTPClient.from_transport(transport)
            local_file_path = os.path.join(FILE_DIR_PATH, filename)
            host_file_path = '/home/' + self.host_dic[host]["username"] + "/" + filename
            # 将 local_file_path 上传至服务器 host_file_path
            print("正在向主机 %s 上传文件 %s ，请等待..." % (host, filename))
            sftp.put(local_file_path, host_file_path, callback=self.trans_size)
            # print("\n\033[33m文件 %s 已上传至主机 %s\033[0m" % (filename, host))
            logger("launcher", "info", "put_file", "文件 %s 已上传至主机 %s" % (filename, host))
        except Exception as e:
            # print("\033[1;31m主机 %s 执行时出错： %s\033[0m" % (host, e))
            logger("launcher", "error", "put_file", "主机 %s 执行时出错： %s" % (host, e))
        finally:
            transport.close()

    def get_file(self, host, cmd):
        """从远程主机下载文件"""
        operate, filename = cmd.split(" ")
        # print(operate, filename)
        transport = paramiko.Transport((self.host_dic[host]["hostname"], self.host_dic[host]["port"]))
        try:
            transport.connect(username=self.host_dic[host]["username"], password=self.host_dic[host]["password"])
            sftp = paramiko.SFTPClient.from_transport(transport)
            host_dir_path = os.path.join(DOWNLOAD_PATH, host)
            if not os.path.exists(host_dir_path):
                os.mkdir(host_dir_path)
            local_file_path = os.path.join(host_dir_path, filename)
            host_file_path = '/home/' + self.host_dic[host]["username"] + "/" + filename
            # 将remove_path 下载到本地 local_path
            print("正在从服务器 %s 下载文件 %s ，请等待..." % (host, filename))
            sftp.get(host_file_path, local_file_path, callback=self.trans_size)
            # print("\n\033[33m主机 %s 的文件 %s 已下载完成\033[0m" % (host, filename))
            logger("launcher", "info", "get_file", "主机 %s 的文件 %s 已下载完成" % (host, filename))
        except IOError as e:
            os.remove(local_file_path)
            # print("\033[1;31m主机 %s 执行时出错： %s\033[0m" % (host, e))
            logger("launcher", "error", "get_file", "主机 %s 执行时出错： %s" % (host, e))
        except Exception as e:
            # print("\033[1;31m主机 %s 执行时出错： %s\033[0m" % (host, e))
            logger("launcher", "error", "get_file", "主机 %s 执行时出错： %s" % (host, e))
        finally:
            transport.close()

    def write_host_dic(self):
        """写入主机信息"""
        pickle.dump(self.host_dic, open(DB_FILE_PATH, 'wb'))

    def load_host_dic(self):
        """读取主机信息"""
        self.host_dic = pickle.load(open(DB_FILE_PATH, 'rb'))

    def host_info(self):
        """打印保存的主机信息"""
        print("当前所有主机信息：")
        for i in self.host_dic:
            if i in self.actived_host_list:
                print("\033[32m" + i + "（已激活）\033[0m")
            else:
                print(i + "（未激活）")

    def trans_size(self, transferred, to_be_transferred):
        """进度条"""
        rate = (transferred / to_be_transferred)
        bar_str = "\r%d%%" % int(rate * 100)
        sys.stdout.write(bar_str)
        sys.stdout.flush()
