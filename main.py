from app.cli.parser import create_parser
from app.services import book_service

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "add":
        commands.add_book(args.title)
    elif args.command == "delete":
        commands.delete_book(args.title)
    elif args.command == "list":
        commands.list_books()
    elif args.command == "get":
        commands.get_book(args.title)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()