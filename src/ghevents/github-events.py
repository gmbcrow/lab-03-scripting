
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'


def retrieve_events(url):
    """Fetch events from the given GitHub API url and return them as Python data."""
    data = requests.get(url).text
    events = json.loads(data)
    return events


def print_events(events, n=5):
    """Print the first n events in the form 'type :: repo'."""
    for x in events[:n]:
        event = x['type'] + ' :: ' + x['repo']['name']
        print(event)


def main():
    """Fetch and print recent GitHub events for GHUSER."""
    print(GHUSER)
    print(url)
    events = retrieve_events(url)
    print_events(events)


if __name__ == "__main__":
    main()