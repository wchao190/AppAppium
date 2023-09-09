#conding=utf-8
from common.cmd import Cmd
from common.appium_port import Port
from common.appium_cmd import AppiumCmd
import threading
import time

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

class Server:

    def __init__(self):
        self.cmd = Cmd()
        self.appium_cmd = AppiumCmd()
        self.devices = self.get_devices()

    def get_devices(self):
        """
        获取设备列表
        :return:
        """
        result = self.cmd.get_cmd_result("adb devices")
        devices = []
        if len(result) >= 1:
            for dev in result:
                info = dev.split("\t")
                if "device" == info[1]:
                    devices.append(info[0])
            return devices
        else:
            return None

    def create_appium_port(self,start_port):
        """
        创建端口号
        :param start_port:
        :return:
        """
        p = Port()
        return p.create_appium_port(start_port,self.get_devices())

    def create_cmd_list(self,i):
        """
        根据连接的设备多少，创建启动命令
        :param i:
        :return:
        """
        cmd_list = []
        appium_port = self.create_appium_port(4700)
        bp_port = self.create_appium_port(4900)
        cmd = "appium -p " + str(appium_port[i]) + " -bp " + str(bp_port[i]) + " -U " + str(self.devices[i]) + " --session-override --no-reset"

        cmd_list.append(cmd)

        device_id = self.cmd.get_device_model("adb devices -l",self.devices[i])
        self.appium_cmd.write_data(i,appium_port[i],bp_port[i],self.devices[i],device_id)
        return cmd_list

    def start_server(self,i):
        """
        创建 appium 执行命令，并启动
        :param i:
        :return:
        """
        start_list = self.create_cmd_list(i)
        self.cmd.execute_cmd(start_list[0])

    def kill_server(self):
        """
        根据创建的 appium 端口号，关闭 对应的 appium
        :param port:
        :return:
        """

        pid = self.cmd.get_cmd_result("tasklist | findstr node.exe")
        if len(pid)>0:
            self.cmd.execute_cmd("taskkill -F -PID node.exe")

        # pid = self.cmd.get_cmd_result("tasklist | findstr "+ str(port))
        # if len(pid)>0:
        #     self.cmd.execute_cmd("taskkill -F -PID " + str(port))

    def start_thead(self):
        """
        多线程启动 appium 服务
        :return:
        """
        thread_list = []

        # count_cmd = self.appium_cmd.count_cmd()
        # if count_cmd != None:
        #     for i in range(count_cmd):
        #         port = self.appium_cmd.get_value("appium_cmd_" + str(i),"port")
        #         self.kill_server(port)

        self.kill_server()
        self.appium_cmd.clear_yaml()

        for n in range(len(self.devices)):
            start_appium = threading.Thread(target = self.start_server, args=(n,))
            thread_list.append(start_appium)

        for k in thread_list:
            k.start()

        # 等待启动 appium
        time.sleep(6)
