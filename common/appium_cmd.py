import yaml
import os
import platform

class AppiumCmd:

    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.getcwd()),"data","appium_cmd.yaml")

    def read_data(self):
        """
        读取 cmd 命令
        :return:
        """
        with open(self.path,'r') as fp:
            return yaml.load(fp,Loader=yaml.FullLoader)

    def get_value(self,section,key):
        """
        获取命令参数值
        :param section:
        :param key:
        :return:
        """
        data = self.read_data()
        value = data[section][key]
        return value

    def clear_yaml(self):
        """
        清空 appium 启动命令数据
        :return:
        """
        with open(self.path,'w') as fp:
            fp.truncate()
        fp.close()

    def write_data(self,i,port,bp,device,model):
        """
        保存创建的 port、bp port、device
        :param i:
        :param port:
        :param bp:
        :param device:
        :return:
        """
        data = self.join_cmd(i,port,bp,device,model)
        with open(self.path,'a') as fp:
            yaml.dump(data,fp)

    def join_cmd(self,i,port,bp,device,model):

        info = {
            "appium_cmd_"+ str(i) : {
                "port": port,
                "bp": bp,
                "device": device,
                "model": model
            }
        }
        return info

    def count_cmd(self):
        data = self.read_data()
        if data != None:
            return len(data)
        return 0


if __name__ == '__main__':
    cmd = AppiumCmd()
    print(cmd.path)