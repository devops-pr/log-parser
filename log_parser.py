#!/usr/bin/env python3
""" Generate a detailed report from a log file.
Usage:
     python3 log_parser.py -f <logfile location>
"""

__author__ = "Piyush Raj"
__version__ = "1.0.0"
__email__ = "piyushraj@outlook.in"


# ================================== Load required modules and methods =======================================#

from pprint import pprint
import argparse
# =========================================== Function definition =========================================== #


def request_summary(log_file):
    invalid_log_count = 0
    data = {}
    try:
        with open(log_file, "r") as f:
            for line in f:
                try:
                    date = line.split("[")[1].split("]")[0].split(" ")[0].split(":")[0]
                    status_code = line.split('"')[2].split(" ")[1]
                    user_agent = line.split('"')[5]
                    method = line.split('"')[1].split(" ")[0]
                    if date not in data:
                        data[date] = {"request_summary": {"request_count": 1, status_code: 1, method: 1},
                                      "user_agent_summary": {user_agent: 1}}
                    else:
                        data[date]["request_summary"]["request_count"] = \
                            data[date]["request_summary"]["request_count"] + 1
                        if method in data[date]["request_summary"]:
                            data[date]["request_summary"][method] = data[date]["request_summary"][method] + 1
                        else:
                            data[date]["request_summary"][method] = 1
                        if status_code in data[date]["request_summary"]:
                            data[date]["request_summary"][status_code] = \
                                data[date]["request_summary"][status_code] + 1
                        else:
                            data[date]["request_summary"][status_code] = 1
                        if user_agent in data[date]["user_agent_summary"]:
                            data[date]["user_agent_summary"][user_agent] = \
                                data[date]["user_agent_summary"][user_agent] + 1
                        else:
                            data[date]["user_agent_summary"][user_agent] = 1
                except IndexError:
                    invalid_log_count += 1
    except FileNotFoundError:
        print("File not found! Please specify the correct log file location.")
    return invalid_log_count, data


def req_per_day(data):
    required_data = {}
    for k, v in data.items():
        required_data[k] = v["request_summary"]["request_count"]
    return required_data


def user_agent_report(data):
    required_data = {}
    for date, v in data.items():
        value_key_pairs = ((value, key) for (key, value) in v['user_agent_summary'].items())
        sorted_value_key_pairs = sorted(value_key_pairs, reverse=True)
        ordered_dict = {k: v for v, k in sorted_value_key_pairs[0:3]}
        required_data[date] = ordered_dict
    return required_data


def get_to_post_ratio(data):
    required_data = {}
    for date, v in data.items():
        if "POST" not in v["request_summary"]:
            required_data[date] = {"GET:POST": "No POST calls on this date"}
        else:
            required_data[date] = {"GET:POST": round(v["request_summary"]["GET"] / v["request_summary"]["POST"], 2)}
    return required_data


# =========================================== Begining of Execution =========================================== #

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--log_file', default="sample.log")
    parser.add_argument("-v", "--verbose", help="modify output verbosity", action="store_true")
    args = parser.parse_args()

    invalid_logs, traffic_summary = request_summary(args.log_file)
    if invalid_logs > 0:
        print("Invalid log entries count: " + str(invalid_logs))
    if args.verbose == True:
        print("########## Printing detailed traffic summary:")
        pprint(traffic_summary)
    print("########## Number of requests served by day:")
    pprint(req_per_day(traffic_summary))
    print("\n########## 3 most frequent User Agents by day:")
    pprint(user_agent_report(traffic_summary))
    print("\n########## Ratio of GET's to POST's by day:")
    pprint(get_to_post_ratio(traffic_summary))
