from FileLoader import FileLoader
from Generator import Generater

generator = Generater()
file_loader = FileLoader()

content = file_loader.getContent()
generator.generate('name', content)
