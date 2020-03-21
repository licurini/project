#!/usr/bin/env python3
import requests

commit_number = int(input("Write number of commits: "))

def get_commits(commit_num, num_on_page=100, page_num=1):
    commit_list = []
    commit = requests.get("https://api.github.com/repos/freeCodeCamp/freeCodeCamp/commits?per_page={};page={}".format(num_on_page, page_num)).json()
    commit_list += commit
    if commit_num > num_on_page:
        commit_num = commit_num - num_on_page
        page_num += 1
        next_page = get_commits(commit_num, num_on_page, page_num)
        commit_list += next_page
    else:
        commit_list = commit_list[:commit_num]

    return commit_list

 
def print_commits(commits):
    i = 1
    for commit in commits:
        print(str(i) + ": SHA: " + commit['sha'])
        print("Message: " + commit['commit']['message'])
        print("URL: " + commit['url'] + "\n" + 20 * "=")
        #print()
        i += 1
print_commits(get_commits(commit_number))

