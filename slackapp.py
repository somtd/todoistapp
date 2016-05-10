# -*- coding: utf-8 -*-
import urllib
import urllib2
import os

url = "https://slack.com/api/chat.postMessage"

params = {'token': os.environ["SLACK_TOKEN"],
          'channel': os.environ["SLACK_CHANNEL"],
          'username': 'Todoist',
          'icon_url': 'https://pbs.twimg.com/profile_images/644169103750512640/zWCOmZLI.png',
          'text': 'test post'
          }
params = urllib.urlencode(params)

def test_post():
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_data(params)
    res = urllib2.urlopen(req)
    res.read()


def main():
    test_post()

if __name__ == '__main__':
    main()
