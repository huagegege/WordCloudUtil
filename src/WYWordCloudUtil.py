import argparse
from Generator import Generator
from WYMusicCrawler import WYMusicCrawler

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('--keyword', type=str)
    parse.add_argument('--pagesize', type=int, default=20, required=False)
    args = parse.parse_args()
    keyword = args.keyword
    if keyword is None:
        print('--keyword为空 keyword指歌名')
        exit()
    crawler = WYMusicCrawler()
    generator = Generator()
    music_list = crawler.searchMusic(keyword)
    url = music_list.pop(0).url
    comments = crawler.turunPage(url, max_page=args.pagesize)
    generator.generateFromArr('name', comments)
    crawler.driver.close()
