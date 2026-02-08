from dsider.template_registry import TEMPLATES


def add_arguments(parser):
    # No extra args needed
    pass


def run(args):
    print("Available templates:")
    for template_id in TEMPLATES:
        print(f" - {template_id}")
