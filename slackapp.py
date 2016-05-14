# -*- coding: utf-8 -*-
import urllib
import urllib.request
import urllib.parse
import os
import todoist

#api = todoist.TodoistAPI()
#user = api.login(os.environ["TODOIST_USER"], os.environ["TODOIST_SECRET"])
slack_icon_url = 'https://pbs.twimg.com/profile_images/644169103750512640/zWCOmZLI.png'


def get_all_completed_items():
    api = todoist.TodoistAPI(token=os.environ["TODOIST_TOKEN"])
    response = api.get_all_completed_items()
    print(response)


def fetch_list():
    response = api.sync(resource_types=['all'])
    for project in response['Projects']:
        print(project['name'])


def slack_post(text):
    url = "https://slack.com/api/chat.postMessage"
    params = dict(token=os.environ["SLACK_TOKEN"],
                  channel=os.environ["SLACK_CHANNEL"],
                  username='Todoist',
                  icon_url=slack_icon_url,
                  text=text)
    params = urllib.parse.urlencode(params)
    params = params.encode('ascii')
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    request = urllib.request.Request(url, data=params, headers=headers)
    with urllib.request.urlopen(request) as response:
        response.read()


def main():
    print("test post")
    get_all_completed_items()
    #slack_post('test test test')


if __name__ == '__main__':
    main()
