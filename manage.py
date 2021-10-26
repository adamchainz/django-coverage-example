#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import multiprocessing
import os
import sys


def main():
    try:
        command = sys.argv[1]
    except IndexError:
        command = "help"

    if command == "test" and sys.platform == "darwin":
        # Workaround for https://code.djangoproject.com/ticket/31169
        if os.environ.get("OBJC_DISABLE_INITIALIZE_FORK_SAFETY", "") != "YES":
            print(
                (
                    "Set OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES in your"
                    + " environment to work around use of forking in Django's"
                    + " test runner."
                ),
                file=sys.stderr,
            )
            sys.exit(1)
        multiprocessing.set_start_method("fork")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
