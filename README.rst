Example project demonstrating using Django’s test runner with Coverage.py

Set up with:

.. code-block:: console

    python -m venv --prompt . venv
    source venv/bin/activate
    python -m pip install -r requirements.txt

Run tests in parallel mode with coverage with this combination of commands:

.. code-block:: console

    coverage erase && coverage run manage.py test --parallel 2 && coverage combine && coverage report

You can also omit the number ``2`` to use as many test processes as there are CPU cores.
But on Django < 4.0 this will trigger a warning:

.. code-block:: text

    CoverageWarning: No data was collected. (no-data-collected)

This warning is due to Django launching more test processes than there are test cases, meaning there’s no coverage data to collect in those processes.
This was fixed in `Ticket #27734 <https://code.djangoproject.com/ticket/27734>`__.

With larger projects using you won’t encounter this warning except when running a subset of tests.

Also note that ``manage.py`` has been patched to run on macOS, as per `this blog post <https://adamj.eu/tech/2020/07/21/how-to-use-djangos-parallel-testing-on-macos-with-python-3.8-plus/>`__.
