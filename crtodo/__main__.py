"""CR To-Do entry point script."""
# crtodo/__main__.py

from crtodo import cli, __app_name__

def main():
    cli.app(prog_name=__app_name__)
    

if __name__ == "__main__":
    raise SystemExit(main())