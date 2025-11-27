"""
CP1404/CP5632 Practical
Program to get a Wikipedia page title, and then and display information about that page.
"""

import wikipedia
from wikipedia import DisambiguationError
from wikipedia import PageError


def main():
    """Get Wikipedia page title, and display information about that page."""
    title = input("Enter page title: ")
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print(page.title)
            print(wikipedia.summary(page, sentences=3))
            print(page.url)
            print()
        except DisambiguationError:
            print("We need a more specific title. Try one of the following, or a new search: ")
            print(wikipedia.search(title), "\n")
        except PageError:
            print(f"Page id \"{title}\" does not match any pages. Try another id!\n")
        title = input("Enter page title: ")
    print("Thank you.")


main()
