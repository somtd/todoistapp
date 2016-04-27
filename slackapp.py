# -*- coding: utf-8 -*-
import urllib
import urllib2
import os

url = "https://slack.com/api/chat.postMessage"

params = {'token': os.environ["SLACK_TOKEN"],
          'channel': os.environ["SLACK_CHANNEL"],
          'username': 'Todoist Bot',
          'icon_url': 'https://blog.todoist.com/wp-content/uploads/2015/09/todoist-logo.png',
          'text': 'test post'
          }

params = urllib.urlencode(params)
req = urllib2.Request(url)

req.add_header('Content-Type', 'application/x-www-form-urlencoded')
req.add_data(params)
res = urllib2.urlopen(req)

body = res.read()

