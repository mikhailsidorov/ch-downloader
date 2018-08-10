# CH-Downloader
## Courses downloader for coursehunters.net

### Requirements

* [Python 3.6](https://www.python.org/downloads/release/python-366/) or higher. 

### Installation

```
git clone https://github.com/mikhailsidorov/ch-downloader.git
cd ch-downloader
pip install -r requirements.txt
```

### Usage

```
scrapy crawl ch -a url=course_url [-a start=start_lesson] [-a end=end_lesson]
```
