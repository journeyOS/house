conda activate py39house

pip install scrapy
pip install dataset

pip install requests

scrapy crawl lianjia -a city=sh -a type=ershoufang -a district=pudong 