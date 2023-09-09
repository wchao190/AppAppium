import configparser
import os

class OperateIni:

    def __init__(self,file_path):

        if file_path:
            self.path = file_path
        else:
            self.path = None
        self.ini = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        if os.path.isfile(self.path):
            try:
                read_ini.read(self.path, encoding="utf-8")
                return read_ini
            except Exception as e:
                return str(e)
        else:
            return None

    def get_ini(self, section, key):
        if self.ini != None:
            try:
                value = self.ini.get(section, key)
                return value

            except Exception as e:
                return str(e)
        else:
            return "ini 文件不存在!"


if __name__ == '__main__':
    ini = OperateIni(os.path.join(os.path.dirname(os.getcwd()),"data/logout.ini"))
    print(ini.get_ini("logout","apply"))