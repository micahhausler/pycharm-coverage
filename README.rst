pycharm-coverage
================
A demo for JetBrains to debug a partial (branch) code coverage display in pycharm 3.4.1

You can follow this issue at https://youtrack.jetbrains.com/issue/PY-8698

Walkthrough
-----------
Hey JetBrains folks,

To test this out, please run:

.. code-block:: bash

    git clone git@github.com:micahhausler/pycharm-coverage.git
    cd pycharm-coverage
    virtualenv env && . ./env/bin/activate
    pip install flake8 nose mock coverage==3.7.1
    python setup.py install

Edit Configuration
~~~~~~~~~~~~~~~~~~
.. image:: /img/01_edit_configurations.png
    :alt: Edit Configuration

Add Configuration
~~~~~~~~~~~~~~~~~
Add as a regular python script

.. image:: /img/02_add_test_runner_config.png
    :alt: Add test parameter

Configure project Coverage settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
I found that using the bundled coverage took nearly 4x as long.

.. image:: /img/03_coverage_configuration.png

Run the tests with coverage
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/04_pycharm_coverage.png

Run the same thing on command line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /img/05_cmd_line_run.png

See the HTML output
~~~~~~~~~~~~~~~~~~~

.. image:: /img/06_coverage_html.png

.. image:: /img/07_coverage_html_resource.png

For good measure
~~~~~~~~~~~~~~~~
As a sanity check I ran ``coverage xml`` and loaded it into pycharm. No dice.

.. image:: /img/08_coverage_xml.png

.. image:: /img/09_add_xml.png

.. image:: /img/10_show_selected.png

.. image:: /img/11_no_difference.png

