import argparse

from dsider.cli.commands import list_templates, new, update


def main():
    parser = argparse.ArgumentParser(
        # INFO:
        description="dsider: Data Science project scaffolding tool",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # INFO: new command
    new_parser = subparsers.add_parser(
        "new", help="Create a new project from a template",
    )
    new.add_arguments(new_parser)

    # INFO: update command
    update_parser = subparsers.add_parser("update", help="Update an existing project")
    update.add_arguments(update_parser)

    # INFO: list command
    list_parser = subparsers.add_parser("list", help="List available templates")
    list_templates.add_arguments(list_parser)

    args = parser.parse_args()

    if args.command == "new":
        new.run(args)
    elif args.command == "update":
        update.run(args)
    elif args.command == "list":
        list_templates.run(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
