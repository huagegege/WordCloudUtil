class FileLoader:

    def __init__(self, file_path='file.txt') -> None:
        global content
        with open(file_path, encoding='utf-8') as file:
            content = file.read()

    def getContent(self):
        return content
