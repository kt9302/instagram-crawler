import argparse

from inscrawler import InsCrawler


def usage():
    return """
        python crawler.py [tag]
    """


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Instagram Liker custom logic", usage=usage())
    parser.add_argument(
        "-n", "--number", type=int, default=1000, help="number of posts to like"
    )
    args = parser.parse_args()
    ins_crawler = InsCrawler(has_screen=True)
    ins_crawler.auto_like_louise(maximum=args.number)
