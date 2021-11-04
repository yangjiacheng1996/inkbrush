#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import paramiko

class SSH(object):
    def __init__(self,**kwargs):
        self.remote_host = kwargs.get("remote_host",None)
        if not self.remote_host:
            logging.error("No host found , system down.")
            raise KeyError
        self.remote_user = kwargs.get("remote_user",None)
        self.remote_password = kwargs.get("remote_password",None)
        self.private_key_file_path = kwargs.get("private_key_file_path")
        #if not self.private_key_file_path:

    def put_dir_to_remote(self,local_dir, remote_dir):
        # 先判断要上传的是不是目录
        if not os.path.isdir(local_dir):
            logging.error("you must give a dir path as local path ,not file path")
            return False
        try:
            # 建立sftp通信
            t = paramiko.Transport((osip, 22))
            t.connect(username=user, password=passwd)
            logging.info("ssh connect success, start transport.")
            sftp = paramiko.SFTPClient.from_transport(t)

            # 扫描你要上传的目录，root是上传的目录的根路径，dirs是所有子目录，files是所有文件。
            # 先检测所有子目录，然后现在远程机器上的路径下先创建这些子目录，然后再把所有文件上传，这样能保证所有文件都能上传成功。
            for root, dirs, files in os.walk(local_dir):
                # 创建所有子目录
                for name in dirs:
                    local_path = os.path.join(root, name)
                    a = local_path.replace(local_dir, '').lstrip("/")
                    remote_path = os.path.join(remote_dir, a)
                    try:
                        sftp.mkdir(remote_path)
                    except Exception as e:
                        logging.error(e)
                for filespath in files:
                    local_file = os.path.join(root, filespath)
                    tmp = local_file.replace(local_dir, '').lstrip("/")
                    remote_file = os.path.join(remote_dir, os.path.basename(root), tmp)
                    try:
                        sftp.put(local_file, remote_file)
                    except Exception as e:
                        sftp.mkdir(os.path.split(remote_file)[0])
                        sftp.put(local_file, remote_file)
            return True
        except Exception as e:
            logging.error(e)
            raise Exception(e)


