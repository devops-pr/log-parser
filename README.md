&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)

# LOG PARSER

## Features
- Parse a log file and generate detailed report as below:

    - What are the number of requests served by day?
    - What are the 3 most frequent User Agents by day?
    - What is the ratio of GET's to POST's by OS by day?
   
- If executed in verbose mode with -v, it provides additional detailed report about the traffic pattern.

## Setup
``` 
git clone https://github.com/devops-pr/log-parser.git
cd log-parser
python3 -f <log_file> [-v]
```

## Sample Run

- Getting help
```
(venv) ➜  log-parser (main) ✗ python3 log_parser.py -h              
usage: log_parser.py [-h] [-f LOG_FILE] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -f LOG_FILE, --log_file LOG_FILE
  -v, --verbose         modify output verbosity
```
- Execution
```
(venv) ➜  log-parser (main) ✗ python3 log_parser.py -f sample.log   
########## Number of requests served by day:
{'01/Dec/2011': 2822,
 '01/Foo/2011': 1,
 '02/Dec/2011': 2572,
 '03/De/2011': 1,
 '03/Dec/2011': 604}

########## 3 most frequent User Agents by day:
{'01/Dec/2011': {'Mozilla/5.0 (compatible; Ezooms/1.0; ezooms.bot@gmail.com)': 245,
                 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)': 456,
                 'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)': 324},
 '01/Foo/2011': {'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)': 1},
 '02/Dec/2011': {'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)': 364,
                 'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)': 281,
                 'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)': 178},
 '03/De/2011': {'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)': 1},
 '03/Dec/2011': {'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)': 36,
                 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)': 142,
                 'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)': 68}}

########## Ratio of GET's to POST's by day:
{'01/Dec/2011': {'GET:POST': 9.61},
 '01/Foo/2011': {'GET:POST': 'No POST calls on this date'},
 '02/Dec/2011': {'GET:POST': 8.29},
 '03/De/2011': {'GET:POST': 'No POST calls on this date'},
 '03/Dec/2011': {'GET:POST': 8.12}}

```