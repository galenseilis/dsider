from dsider.copier_runner import create_project

from dsider.template_registry import TEMPLATES


def add_arguments(parser):
    parser.add_argument("template_id", help="Template to use")
    parser.add_argument("project_name", help="Name of the new project")


def run(args):
    template_path = TEMPLATES.get(args.template_id)
    if not template_path:
        print(f"Error: unknown template '{args.template_id}'")
        return
    create_project(template_path, args.project_name)
    print(f"Project '{args.project_name}' created from template '{args.template_id}'")
