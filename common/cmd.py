import os,re
from common.appium_cmd import  AppiumCmd
class Cmd:

    def get_cmd_result(self,cmd):
        list = []
        reslut = os.popen(cmd,'r').readlines()

        for i in reslut:
            if i == '\n' or 'List' in i:
                continue
            list.append(i.rstrip('\n'))
        return list

    def execute_cmd(self,cmd):
        os.system(cmd)

    def get_device_model(self,cmd,device):
        data = self.get_cmd_result(cmd)

        device_info = ""
        for info in data:
            if device in info:
                device_info = info
        pattern = re.compile("model:(.*?)device")
        result = re.findall(pattern, device_info)
        return result[0].strip()

    def get_appium_server_port(self,serial):
        """
        获取 appium-server 端口号
        :param serial: 启动 appium-server 的序列号
        :return:
        """
        return AppiumCmd().get_value("appium_cmd_"+ str(serial),"port")

    def get_appium_server_pid(self,serial):
        """
        获取 appium-server 进程号
        :param serial:
        :return:
        """
        port = self.get_appium_server_port(serial)
        result = self.get_cmd_result("netstat -ano | findstr " + str(port))
        if result:
            for dt in result:
                if 'LISTENING' in dt:
                    pid = dt.split("LISTENING")[1].strip()
                    return pid
        else:
            return str(port) + "端口没有处于监听状态!"

    def close_appium_server(self,serial):
        """
        关闭 serial 对应的 appium-server 的进程
        :param serial:
        :return:
        """
        pid = self.get_appium_server_pid(serial)
        if pid.isdigit():
            self.execute_cmd("taskkill -F -PID " + str(pid))
            print("---- 关闭 appium-server 成功---")
        else:
            print("---- 当前 appium-server 不存在 ----")


if __name__ == '__main__':
    c = Cmd()
    data = c.close_appium_server(4700)
