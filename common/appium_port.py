from common.cmd import Cmd

class Port:

    def port_is_used(self,port):
        """
        判断 appium 启动端口是否被占用
        :param port:
        :return:
        """
        cmd = Cmd()
        result = cmd.get_cmd_result("netstat -ano | findstr "+str(port))

        if result:
            return True
        else:
            return False

    def create_appium_port(self,start_port,devices):
        """
        根据设备数，创建对应的端口号
        :param start_port: appium 起始端口号
        :param devices:  设备列表
        :return: 返回 appium 端口号
        """
        port = []
        if devices:
            while(len(port) != len(devices)):
                if self.port_is_used(start_port) != True:
                    port.append(start_port)
                start_port +=1
            return port
        else:
            print("设备列表为空!")
            return None


if __name__ == '__main__':
    p = Port()
    devices = [1,2,3]
    print(p.create_appium_port(4723,devices))