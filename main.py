import feedparser
import click

@click.command()
@click.argument("url", type=str, metavar="RSS_URL")
def read_rss(url):
    """Read an RSS feed in the terminal."""
    feed = feedparser.parse(url)

    if "bozo_exception" in feed and feed.bozo_exception:
        print(f"Error parsing the feed: {feed.bozo_exception}")
        return

    print(f"Feed Title: {feed.feed.title}")
    print(f"Feed Description: {feed.feed.description}")
    print("-" * 40)

    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Published: {entry.published}")
        print(f"Link: {entry.link}")
        print("-" * 40)

if __name__ == "__main__":
    read_rss()

