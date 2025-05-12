import argparse
def create_parser():
    parser = argparse.ArgumentParser(description='A book management program')
    subparser = parser.add_subparsers(dest='command')

    add_parser = subparser.add_parser('add', help='Add a book')
    add_parser.add_argument('title', help='The book title')

    delete_parser = subparser.add_parser('delete', help='Delete a book')
    delete_parser.add_argument('title', help='The book title')

    subparser.add_parser("list", help="Show all books")

    return parser

