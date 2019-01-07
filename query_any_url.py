import re
import sys

import requests

INVALID_STATUS_CODES = [400, 401, 402, 403, 404, 500, 501, 502]


class QueryApi(object):
    def __init__(self):
        self.urls = dict()
        self.url_patterns = ["^(?:http|ftp)s?://", "localhost",
                             "(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})",
                             "(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?))"]

    def is_valid_syntax(self, url):
        for pattern in self.url_patterns:
            if re.search(pattern, url):
                print("Url has valid syntax")
                return True

    def display_all_urls(self):
        print("Available urls:")
        for pos, url in self.urls.items():
            print("{0} : {1}".format(pos, url))

    def save_url(self, url):
        for key, value in self.urls.items():
            if value == url:
                return
        self.urls[len(self.urls) + 1] = url
        print("Url Saved")

    def check_status(self, url):
        status = self.get_status(url)
        if status and status not in INVALID_STATUS_CODES:
            return True

    def get_status(self, url):
        try:
            r = requests.head(url)
            code = r.status_code
            print("Status Code: %s" % code)
            return code
        except Exception as e:
            print("failed to connect: %s" % str(e))

    def get_data(self, url):
        try:
            print("Fetching data from url: %s" % url)
            res = requests.get(url)
            print(res.text)
        except Exception as e:
            print("Invalid Url: %s" % url)
            print(str(e))

    def ask_user_for_url(self):
        url = input("Please enter a url: ")
        url = self.urls.get(self.num(url), None) or url
        return url

    @staticmethod
    def num(s):
        try:
            return int(s)
        except ValueError:
            return s


def run():
    qa = QueryApi()
    choice = "y"
    while choice == "y":
        url = qa.ask_user_for_url()
        qa.save_url(url)
        if qa.is_valid_syntax(url):
            if qa.check_status(url):
                pass
                # qa.get_data(url)
        else:
            counter = 0
            while counter < 2:
                counter += 1
                print("Please enter either a valid url or choose from below (1,2,3...)")
                qa.display_all_urls()
                url = qa.ask_user_for_url()
                qa.save_url(url)
                if qa.is_valid_syntax(url):
                    if qa.check_status(url):
                        # qa.get_data(url)
                        break
            else:
                print("You have exceeded wrong attempts (2) limit")
                sys.exit(100)

        choice = input("Do you wish to continue (Y/N) ?").lower()


def main():
    run()


if __name__ == "__main__":
    main()
