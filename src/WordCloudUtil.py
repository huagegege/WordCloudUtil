from Generator import Generator
from Loader import UrlLoader, FileLoader
import argparse

if __name__ == '__main__':

    generator = Generator()

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str)
    parser.add_argument('--file', type=str)
    args = parser.parse_args()

    url = args.url
    file = args.file

    if (url is None) & (file is None):
        print('--url或--file为空 使用--url指定文章链接，或使用--file指定文件路径')
        exit()

    loader = None

    if url is not None:
        loader = UrlLoader(url)

    if file is not None:
        loader = FileLoader(file)

    content = loader.getContent()
    generator.generate('wordcloud', content)
