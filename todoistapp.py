# -*- coding: utf-8 -*-
import todoist
import os

api = todoist.TodoistAPI()
user = api.login(os.environ["TODOIST_USER"], os.environ["TODOIST_SECRET"])

response = api.sync(resource_types=['all'])
for project in response['Projects']:
    print(project['name'])

