from icrawler.builtin import BingImageCrawler

my_filter = dict(type='photo',date='pastyear')

########## toronto images ###########

bing_crawler_1 = BingImageCrawler(downloader_threads=4,storage={'root_dir': '/Users/chloepappas/Documents/GitHub/city-skyline-classifier/toronto_images'})

keywords_toronto = ['cn tower skyline', 'cn tower', 'toronto skyline']

for word in keywords_toronto:
    bing_crawler_1.crawl(keyword=word, filters=my_filter, offset=0, max_num=1000, min_size=(200,200), max_size=None, file_idx_offset='auto')

########## new york images ###########

bing_crawler_2 = BingImageCrawler(downloader_threads=4,storage={'root_dir': '/Users/chloepappas/Documents/GitHub/city-skyline-classifier/new_york_images'})

keywords_ny = ['empire state building skyline', 'empire state building', 'new york empire state']

for word in keywords_ny:
    bing_crawler_2.crawl(keyword=word, filters=my_filter, offset=0, max_num=1000, min_size=(200,200), max_size=None, file_idx_offset='auto')

############ paris images ############

bing_crawler_3 = BingImageCrawler(downloader_threads=4,storage={'root_dir': '/Users/chloepappas/Documents/GitHub/city-skyline-classifier/paris_images'})

keywords_paris = ['eiffel tower skyline', 'eiffel tower', 'paris skyline']

for word in keywords_paris:
    bing_crawler_3.crawl(keyword=word, filters=my_filter, offset=0, max_num=1000, min_size=(200,200), max_size=None, file_idx_offset='auto')

