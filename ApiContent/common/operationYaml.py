import yaml
from common.pubilc import PublicFunction

pb = PublicFunction()


class OperationYaml:
    def readYaml(self):
        with open(pb.filepath('data', 'data.yaml'), 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def dictYaml(self, filedir, filename):
        with open(pb.filepath(filedir=filedir, filename=filename), 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)


# a = OperationYaml()
# print(type((a.readYaml())['login']['data']))