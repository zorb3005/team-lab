from app.cli.parser import create_parser
from app.cli import commands

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "add":
        commands.add_book(args.title)
    elif args.command == "delete":
        commands.delete_book(args.title)
    elif args.command == "list":
        commands.list_books()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()