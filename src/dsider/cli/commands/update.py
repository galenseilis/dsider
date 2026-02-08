from dsider.copier_runner import update_project


def add_arguments(parser):
    parser.add_argument("project_path", help="Path to the project to update")


def run(args):
    update_project(args.project_path)
    print(f"Project at '{args.project_path}' updated")
