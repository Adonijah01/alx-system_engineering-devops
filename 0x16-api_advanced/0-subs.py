#!/usr/bin/python3
"""
0-subs
"""

import requests


def number_of_subscribers(subreddit):
    # Define the URL for the subreddit's about.json endpoint
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'My Reddit API Client'}

    try:
        # Make the HTTP GET request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Extract the number of subscribers from the JSON data
        subscribers = data['data']['subscribers']

        return subscribers
    except requests.exceptions.RequestException:
        # Handle request-related exceptions
        return 0
    except KeyError:
        # Handle JSON parsing errors or missing data
        return 0


if __name__ == '__main__':
    # You can add command-line argument handling here if needed
    subreddit = "programming"  # Replace with the subreddit you want to check
    subscribers = number_of_subscribers(subreddit)
    print(subscribers)
