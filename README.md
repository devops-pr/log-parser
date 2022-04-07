<p align="center"><img src="https://raw.githubusercontent.com/devops-pr/walmart_hackathon/develop/media/walmart_logo.png" width="328px"><p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
<br><br>

<p align="center"><img src="https://raw.githubusercontent.com/devops-pr/walmart_hackathon/develop/media/walmart-screenshot.png" width="100%"><p>

#LOG PARSER
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