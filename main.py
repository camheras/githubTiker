import requests
from github import Github
from apscheduler.schedulers.blocking import BlockingScheduler
import argparse

tab = []
parser = argparse.ArgumentParser()
parser.add_argument("--repo", type=str,
                    help="The repository ({github_user}/{repository})")
parser.add_argument("--token", type=str,
                    help="Your github token")


def some_job():
    global tab
    args = parser.parse_args()
    token = args.token
    rep = args.repo
    g = Github(token)
    repo = g.get_repo(rep)

    tmp = []
    for id, i in enumerate(repo.get_projects()[0].get_columns()):
        tmp.append([])
        for card in i.get_cards():
            tmp[id].append(card)

    if not tmp == tab:
        for tmpcards in tmp:
            for id1, card in enumerate(tmpcards):
                for tabcards in tab:
                    for id2, card2 in enumerate(tabcards):
                        if not tabcards[id2] == tmpcards[id1]:
                            print("CAVAPAS")
    else:
        print("yatoutquiva")
    tab = tmp


def p():
    scheduler = BlockingScheduler()
    scheduler.add_job(some_job, 'interval', seconds=3)
    scheduler.start()


p()
