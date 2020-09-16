import requests
from github import Github
import streamlit as st

from apscheduler.schedulers.blocking import BlockingScheduler
import argparse
import fbchat
from getpass import getpass

tab = []
parser = argparse.ArgumentParser()
parser.add_argument("--repo", type=str,
                    help="The repository ({github_user}/{repository})")
parser.add_argument("--token", type=str,
                    help="Your github token")
parser.add_argument("--fb_username", type=str,
                    help="Your facebook username (email)")
parser.add_argument("--fb_password", type=str,
                    help="Your facebook password")
parser.add_argument("--fb_group", type=str,
                    help="Your facebook password")


def some_job():
    global tab
    args = parser.parse_args()
    token = args.token
    rep = args.repo
    password = args.fb_password
    username = args.fb_username
    fb_group = args.fb_group
    g = Github(token)
    repo = g.get_repo(rep)
    try:
        fileRead = open("./cards.txt")
    except:
        fileRead = open("./cards.txt", "x")

    tmp = []
    for id, i in enumerate(repo.get_projects()[0].get_columns()):
        tmp.append([])
        for card in i.get_cards():
            tmp[id].append(card.note)

    if fileRead.readable():
        for line in fileRead.readlines():
            tab.append(eval(line))

        if not tmp == tab:
            for id in range([len(tmp), len(tab)][len(tmp) > len(tab)]):
                res = set(tab[id]).symmetric_difference(tmp[id])
                print(res)
                if res is not None:
                    session = fbchat.Session.login(username, password)
                    thread = fbchat.Group(session=session, id=fb_group)
                    thread.send_text(str(res))

        else:
            print("Up to date")

    file = open("./cards.txt", "w")
    for cards in tmp:
        file.write(str(cards))
        file.write("\n")


some_job()
