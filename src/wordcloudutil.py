from collections import Counter

import yaml
from pkuseg import pkuseg
from pyecharts import WordCloud


class WordCloudUtil:
    properties_file = "./properties.yaml"

    def __init__(self) -> None:
        self.analyzer = pkuseg()
        self.load_properties()
        self.load_stop_word()
        self.load()

    def load_properties(self):
        with open(self.properties_file, encoding='utf-8') as file:
            props = yaml.load(file)
            self.stop_word_file_path = props.get('stop_word_file_path')
            self.file_path = props.get('file_path')
            self.shape = props.get('shape')
            self.word_gap = props.get('word_gap')
            self.word_size_range = props.get('word_size_range')
            self.rotate_step = props.get('rotate_step')

    def load_stop_word(self):
        with open(self.stop_word_file_path, encoding='utf-8') as file:
            self.stop_word = file.read()

    def load(self):
        global content
        with open(self.file_path, encoding='utf-8') as file:
            content = file.read()

    def generate(self):

        words = self.analyzer.cut(content)

        final_word = []
        for word in words:
            if word not in self.stop_word:
                final_word.append(word)

        name = 'file'
        attr = []
        val = []
        counter = Counter(final_word).most_common(100)
        for count in counter:
            attr.append(count[0])
            val.append(count[1])

        wordcloud = WordCloud()
        wordcloud.add(name, attr, val, shape=self.shape, word_gap=self.word_gap, word_size_range=self.word_size_range,
                      rotate_step=self.rotate_step)
        wordcloud.render()


if __name__ == '__main__':
    wordcloudutil = WordCloudUtil()
    wordcloudutil.generate()
