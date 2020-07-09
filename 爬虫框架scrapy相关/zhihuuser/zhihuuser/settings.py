# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5",
  'cookie': '_zap=e32316b0-0c66-46ef-b1d2-74744a4e65b2; d_c0="ADAZeIe8SRGPTvBVrsOrseRufxOoI0u3UTw=|1589786144"; __guid=74140564.2034189215159957200.1589786149217.8076; _ga=GA1.2.162120985.1589786153; _xsrf=fbvl3CFnjC7L4ZjrSd6gRWhx1Cugn9Tx; _gid=GA1.2.1830822410.1592555956; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1592321049,1592322078,1592555956,1592556076; SESSIONID=qt0OtmWTgC3UGkRVk6elJfbA8pV8vMDqUCzn9S0hwch; JOID=V18dAkil1Oi3rXWudqEQdz6Jctlq1q_R-t8a9ivEldTr6Bj-L8qoD-2peKh9s0NwoIMGO7x3GUyL1VZp1ZAAwTQ=; osd=V1EdAEKl2ui1p3WgdqMadzCJcNNq2K_T8N8U9inOldrr6hL-IcqqBe2neKp3s01wookGNbx1E0yF1VRj1Z4Awz4=; l_n_c=1; r_cap_id="MjFiZTU3MDI0MDg4NGQ0M2I0NjM4YzA3YmZiYzU4NmE=|1592556333|21157407fdc1e4c61a8a32a04f6be680db905735"; cap_id="YTFmNjljNjkwYWEzNDJlY2EzODBmZDM5ZDkyODAzMjI=|1592556333|db642200f0cd1ef112a742965489d0a300f80fbd"; l_cap_id="OTk4OTI3YjNkOTk2NGQ5ZWFlNDBlNGJjYzk0ZTUzYjc=|1592556333|179ed340e5d0b3c6ab23ecf9d0512263166c96f2"; n_c=1; client_id="QkEyOUVEMTJGOTg2RjAyMUNEQjQwMTc3NTJGOTMwRDU=|1592556352|2357852dce84343e344041e5a6cda46ec9e10344"; anc_cap_id=ef83e7bdc1d74e0baaec9c9b13c8d091; capsion_ticket="2|1:0|10:1592568642|14:capsion_ticket|44:Yzk1MDg4ZDU3M2QxNDZiNmJkOTljM2RkNzA0ZmRmOWU=|59263022fc5fc646df49e4b6a2b2d30342ecde13baad6af652a3ca19991e1c61"; z_c0="2|1:0|10:1592568684|4:z_c0|92:Mi4xMWpvT0hBQUFBQUFBTUJsNGg3eEpFU1lBQUFCZ0FsVk5hX25aWHdBR3I5ZzdXQld0ODF5cjBfUzZRMzlkRWNDc1lR|a52ae96601aa3331d8a68608f034eaa1e76b39556e407c3a1f18fad871597990"; monitor_count=23; _gat_gtag_UA_149949619_1=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1592568635; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1592568688|1592556005'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'zhihuuser.middlewares.ProxyMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihuuser.pipelines.ZhihuuserPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
