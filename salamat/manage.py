#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    #
    # sys.path.insert(0, os.path.abspath(os.path.join(
    #                 os.path.dirname(__file__), 'django-filesoup')))

    sys.path.insert(0, os.path.abspath(os.path.join(
                    os.path.dirname(__file__), '..')))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'salamat.baseapp.settings.develop')
    import django

    django.setup()

    from django.utils import text
    from baseapp.helpers import slugify
    text.slugify = slugify

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
