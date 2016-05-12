# -*- coding: utf-8 -*-
import urllib
import os
import todoist

api = todoist.TodoistAPI()
user = api.login(os.environ["TODOIST_USER"], os.environ["TODOIST_SECRET"])
url = "https://slack.com/api/chat.postMessage"
params = dict(token=os.environ["SLACK_TOKEN"], channel=os.environ["SLACK_CHANNEL"], username='Todoist',
              icon_url='https://pbs.twimg.com/profile_images/644169103750512640/zWCOmZLI.png', text='test post')
params = urllib.urlencode(params)


def fetch_list():
    response = api.sync(resource_types=['all'])
    for project in response['Projects']:
        print(project['name'])

def test_post():
    req = urllib.Request(url)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    req.add_data(params)
    res = urllib.urlopen(req)
    res.read()


def main():
    print("test post")
    #test_post()
    fetch_list()


if __name__ == '__main__':
    main()
