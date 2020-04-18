#!/usr/bin/python
# _*_ coding:utf-8 _*_
"""
Python批量管理主机(paramiko、fabric与pexpect)
1. paramiko：方便嵌套系统平台中，擅长远程执行命令，文件传输。
2. fabric：方便与shell脚本结合，擅长批量部署，任务管理。
3. pexpect：擅长自动交互，比如ssh、ftp、telnet。
"""

import sys, os
import paramiko, fabric, pexpect

def paramiko_ssh_ip(ip, port, username, password, command):
    """
    paramiko ssh密码认证，远程执行命令
    :param ip: 主机IP
    :param port: 主机端口
    :param username: 主机用户名
    :param password: 主机密码
    :param command: 在主机上执行的命令
    :return: 返回执行结果
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port, username, password, timeout=5)
    stdin, stdout, stderr = client.exec_command(command)
    res = stdout.read()
    error = stderr.read()
    if not error:
        print(res.decode('utf-8'))
    else:
        print(error.decode('utf-8'))
    client.close()

def paramiko_ssh_key(ip, port, username, key_file, command):
    """
    paramiko ssh密钥认证，远程执行命令
    :param ip: 主机IP
    :param port: 主机端口
    :param username: 主机用户名
    :param key_file: 本地主机的私钥
    :param command: 在主机上执行的命令
    :return: 返回执行结果
    """
    client = paramiko.SSHClient()
    key = paramiko.RSAKey.from_private_key_file(key_file)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port, username, pkey=key, timeout=5)
    stdin, stdout, stderr = client.exec_command(command)
    res = stdout.read()
    error = stderr.read()
    if not error:
        print(res.decode('utf-8'))
    else:
        print(error.decode('utf-8'))
    client.close()

def paramiko_upload_file(ip, port, username, key_file, local_path, remote_path):
    if not os.path.isfile(local_path):
        print(local_path + "文件不存在")
        sys.exit(1)
    try:
        s = paramiko.Transport((ip, port))
        s.connect(username=username, key_file=key_file)
    except Exception as e:
        print(e)
        sys.exit(1)
    sftp = paramiko.SFTPClient.from_transport(s)
    sftp.put(local_path, remote_path)

    try:
        sftp.stat(remote_path)
        print("上传成功")
    except IOError:
        print("上传失败")
    finally:
        s.close()

if __name__ == "__main__":
    ip = '10.199.136.134'
    port = 22
    username = 'root'
    password = 'Servy0u'
    command = 'df -h'
    key_file = '~/.ssh/id_rsa'
    local_path = '/root/res.txt'
    remote_path = '/opt/res.txt'
    # paramiko_ssh_ip(ip, port, username, password, command)
    # paramiko_ssh_key(ip, port, username, key_file, command)
    paramiko_upload_file(ip, port, username, key_file, local_path, remote_path)
