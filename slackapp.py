# -*- coding: utf-8 -*-
import urllib
import urllib.request
import urllib.parse
import os
import todoist
from datetime import timedelta, date, datetime

slack_icon_url = 'https://pbs.twimg.com/profile_images/644169103750512640/zWCOmZLI.png'


def get_today_items():
    today_items = []
    api = todoist.TodoistAPI(token=os.environ["TODOIST_TOKEN"])
    response = api.sync(resource_types=['items'])
    for item in response['Items']:
        if item['due_date'] != None:
            due_date = datetime.strptime(item['due_date'], '%a %d %b %Y %H:%M:%S +0000')
            if date.today() == due_date.date():
                today_items.append(item['content'])
    # print(today_items)
    return today_items


def get_uncompleted_items():
    uncompleted_items = []
    api = todoist.TodoistAPI(token=os.environ["TODOIST_TOKEN"])
    response = api.sync(resource_types=['items'])
    for item in response['Items']:
        if item['due_date'] != None:
            due_date = datetime.strptime(item['due_date'], '%a %d %b %Y %H:%M:%S +0000')
            if date.today() != due_date.date():
                uncompleted_items.append(item['content'])
    # print(uncompleted_items)
    return uncompleted_items


def get_yesterday_completed_items():
    yesterday_completed_items = []
    yesterday = date.today() - timedelta(days=1)
    api = todoist.TodoistAPI(token=os.environ["TODOIST_TOKEN"])
    response = api.get_all_completed_items(kwargs='')
    for item in response['items']:
        completed_date = datetime.strptime(item['completed_date'], '%a %d %b %Y %H:%M:%S +0000')
        if yesterday == completed_date.date():
            yesterday_completed_items.append(item['content'])
    # print(yesterday_completed_items)
    return yesterday_completed_items

def get_today_completed_items():
    today_completed_items = []
    today = date.today()
    api = todoist.TodoistAPI(token=os.environ["TODOIST_TOKEN"])
    response = api.get_all_completed_items(kwargs='')
    for item in response['items']:
        completed_date = datetime.strptime(item['completed_date'], '%a %d %b %Y %H:%M:%S +0000')
        if today == completed_date.date():
            today_completed_items.append(item['content'])
    # print(yesterday_completed_items)
    return today_completed_items


def generate_posts():
    posts = ["\n:heavy_check_mark: *Yesterday's completed task*\n"]
    yesterday_completed_items = get_yesterday_completed_items()
    if len(yesterday_completed_items) != 0:
        for item in yesterday_completed_items:
            posts.append(':ballot_box_with_check: ' + item + '\n')
    else:
        posts.append('Nothing.:sob:\n')

    posts.append("\n:heavy_check_mark: *Today's completed task*\n")
    today_completed_items = get_today_completed_items()
    if len(today_completed_items) != 0:
        for item in today_completed_items:
            posts.append(':ballot_box_with_check: ' + item + '\n')
    else:
        posts.append('Nothing.:sob:\n')

    posts.append("\n\n:warning: *Today's uncompleted task*\n")
    today_items = get_today_items()
    if len(today_items) != 0:
        for item in today_items:
            posts.append(':white_medium_square: ' + item + '\n')
    else:
        posts.append('Nothing.:sleepy:\n')

    posts.append("\n\n:warning: *Other uncompleted task*\n")
    uncompleted_items = get_uncompleted_items()
    if len(uncompleted_items) != 0:
        for item in uncompleted_items:
            posts.append(':white_medium_square: ' + item + '\n')
    else:
        posts.append(':white_flower:Nothing! Excellent!!\n')

    slack_post(''.join(posts))


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
    generate_posts()


if __name__ == '__main__':
    main()
