import json
import sys
import xml.etree.ElementTree as eTree


class BaseFileManger:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read(self):
        raise NotImplementedError

    def write(self, data):
        raise NotImplementedError


class JsonFileManger(BaseFileManger):
    def read(self):
        file = open(self.input_file)
        data = file.read()
        file.close()
        return json.loads(data)

    def write(self, data):
        file = open(self.output_file, 'w')
        file.write(json.dumps(data, indent=4))
        file.close()


class XMLFileManager(BaseFileManger):
    def read(self):
        file = open(self.input_file)
        tree = eTree.parse(file)
        root = tree.getroot()
        result = []
        for item in root:
            element = {}
            for child in item:
                element[child.tag] = child.text
            result.append(element)
        file.close()
        return result

    def write(self, data):
        root = ''
        tag_str = "<{tag}>{text}</{tag}>"
        for item in data:
            item_str = ''
            for tag, text in item.items():
                item_str += tag_str.format(
                    tag=tag,
                    text=text
                ) + '\n'
            root += f'\t<item>\n\t\t{item_str}\n\t</item>'
        file = open(self.output_file, 'w')
        file.write(f'<root>\n{root}\n</root>')
        file.close()


class ConsoleFileManager(BaseFileManger):
    def read(self):
        return input()

    def write(self, data):
        print(data)


class Manger:
    _managers = {
        'json': JsonFileManger,
        'xml': XMLFileManager,
        None: ConsoleFileManager
    }

    def __init__(self, argv):
        self.argv = argv
        self.input_file = None
        self.output_file = None

    def parse_files(self):
        argv = self.argv[1:]
        arg_len = len(argv)
        if arg_len > 2 or not arg_len:
            raise Exception("Invalid input")
        if arg_len == 2:
            self.input_file, self.output_file = argv
        else:
            self.input_file, self.output_file = argv[0], None

    @classmethod
    def get_extension(cls, file_name):
        divided = file_name.rsplit('.', 1)
        if len(divided) != 2 or not divided[0]:
            raise Exception('Invalid file name')
        return divided[-1]

    def process(self):
        self.parse_files()
        input_ext = self.get_extension(self.input_file)
        output_ext = None
        if self.output_file:
            output_ext = self.get_extension(self.output_file)
        read_class = self._managers[input_ext]
        data = read_class(self.input_file, self.output_file).read()
        write_class = self._managers[output_ext]
        write_class(self.input_file, self.output_file).write(data)


if __name__ == '__main__':
    manager = Manger(sys.argv)
    manager.process()
