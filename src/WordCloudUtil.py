from Generator import Generator
from Loader import UrlLoader

generator = Generator()
loader = UrlLoader("https://blog.csdn.net/on_my_way20xx/article/details/83114095")

content = loader.getContent()
generator.generate('name', content)
