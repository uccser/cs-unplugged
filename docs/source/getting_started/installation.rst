Installation Guide
#################################################

This page will set your machine up for working on the CS Unplugged project.
You should only need to do these installation steps once (unless the required
steps for setup change).

Recommended Reading
=================================================

If you aren't familiar with the following systems, we recommend
reading a tutorial first on how to use them:

- Basic terminal commands
- Git (here are two Git tutorials: `one`_ `two`_)

.. warning::

  The following steps are written for developing with a Linux operating
  system. You may need to adapt the instructions if you are working on
  Windows, OS X, etc.

Step 1: Setup Virtual Machine (optional)
=================================================

For those working on a computer in a restricted environment (for example:
a computer managed by an education insitution) or wish to be able to follow
the following instructions exactly, then working in a **virtual machine** is
recommended.

If you wish to setup a virtual machine for development, we have a guide here:
:doc:`../other/setup_virtual_machine`.

.. _step-2-install-python-3-and-pip:

Step 2: Install Python 3 and pip
=================================================

Install Python 3 with the following command in terminal (you don't need
to enter the ``$`` character, this shows the start of your terminal prompt):

.. code-block:: bash

    $ sudo apt install python3

Then install Python 3 pip (pip is a package management system used to
install and manage software packages written in Python) with the following
command in terminal:

.. code-block:: bash

    $ sudo apt install python3-pip

Step 3: Install Python virtualenv
=================================================

We recommend (though it's not required) to work within a virtual environment
(see :ref:`what-is-a-virtual-environment`).
This helps to prevent conflicts with dependencies.

Install virtualenv with the following command in terminal:

.. code-block:: bash

    $ sudo pip3 install virtualenv

.. note::

  **Optional step:** You can also install `virtualenvwrapper`_ to make it
  easier when using and managing your virtual environments.

Step 4: Install Git
=================================================

Install Git (version control software) with the following command in terminal:

.. code-block:: bash

    $ sudo apt install git

Step 5: Create GitHub Account
=================================================

If you don't already have an account on GitHub, create an account on
the `GitHub website`_.
This account will be tied to any changes you submit to the project.

Step 6: Set Git Account Values
=================================================

When you make a commit in Git (the term for changes to the project), the
commit is tied to a name and email address. We need to set name and email
address within the Git system installed on the machine.

Set the name and email Git values following command in terminal:

.. code-block:: bash

    $ git config --global user.name “<your name>”
    $ git config --global user.email “<your GitHub email>”

For example:

.. code-block:: bash

    $ git config --global user.name “John Doe”
    $ git config --global user.email johndoe@gmail.com”

.. note::

    If your GitHub account is secured with two-factor authentication (2FA)
    this is a perfect time to setup `SSH keys`_.

Step 7: Install Postgres
=================================================

Postgres is an open source database system we use to store project
data. Install Postgres and required connection packages with the following
commands in terminal:

.. code-block:: bash

    $ sudo apt-get install postgresql
    $ sudo apt-get install python-psycopg2
    $ sudo apt-get install libpq-dev

Step 8: Create User and Database in Postgres
=================================================

We will now create a user (called a 'role') for accessing the database.
By default, the CS Unplugged project connects with a role as the same name
as the user logged into the operating system.
If you can't remember your username, it's the text before the ``@`` symbol in
the terminal prompt.
For example, if the terminal prompt is:

.. code-block:: bash

    taylor@taylor-VirtualBox:~/Projects/cs-unplugged$

Your username is ``taylor``.

Firstly type the following command in terminal to switch to the ``postgres``
user (that has admin permissions for the database):

.. code-block:: bash

    $ sudo -i -u postgres

The terminal prompt should have now changed and begins with ``postgres@``.
Now enter the following commands to create the role:

.. code-block:: bash

    $ createuser --interactive
    $ Enter name of role to add: <your name>
    $ Shall the new role be a superuser? (y/n): y

For example:

.. code-block:: bash

    $ createuser --interactive
    $ Enter name of role to add: taylor
    $ Shall the new role be a superuser? (y/n): y

To create the database, type the following command in terminal:

.. code-block:: bash

    $ createdb csunplugged -e

To logout of the ``postgress`` user and return to your normal terminal, enter
the following command in terminal:

.. code-block:: bash

    $ logout

.. note::

    If you wish to use a different role, database name, database post, or use a
    password, then you can define these in the ``.env`` file.

Step 9: Download the CS Unplugged Project
=================================================

Firstly create the directory you wish to hold the CS Unplugged project
directory in if you wish to store the data in a specific location.
Once you have decided upon the location, change the working directory of the
terminal to this directory.

To clone (the Git term for download) the project directory, type the
following command in terminal:

.. code-block:: bash

    $ git clone https://github.com/uccser/cs-unplugged.git

.. note::

    If you connect to GitHub through SSH, then type:

    .. code-block:: bash

        $ git clone git@github.com:uccser/cs-unplugged.git

Once Git has cloned the directory, type the following commands in terminal to
change the working directory to inside the project repository and checkout
to the development branch:

.. code-block:: bash

    $ cd cs-unplugged
    $ git checkout develop

Step 10: Create Virtual Environment
=================================================

If you installed ``virtualenv`` in Step 3, then it's time to create a virtual
environment. Type the following commands in terminal to create and activate
a virtualenv named ``venv``.
You can change the virtual environment name to whatever you wish.
You will need to replace the ``x`` with the version number of Python you
have (for example: ``python3.5``):

.. code-block:: bash

    $ python -m virtualenv --python=python3.x venv
    $ . venv/bin/activate

.. note::

    If you installed ``virtualenvwrapper``, then type the following command to
    to create a virtual environment called ``csunplugged``, with Python within
    the virtual environment already set to Python 3.

    .. code-block:: bash

        $ mkvirtualenv --python=/usr/bin/python3.x csunplugged

You should now have the name of your virtual environment before the terminal
prompt.

Step 11: Install Project Requirements
=================================================

To install the project requirements, type the following commands in terminal
from the project root directory (contains a file called ``requirements.txt``):

.. code-block:: bash

    $ sudo apt-get install curl
    $ curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
    $ sudo apt-get install -y nodejs
    $ sudo apt-get install libffi-dev libcairo2-dev libjpeg-dev libgif-dev
    $ pip install -r requirements/local.txt
    $ pip install -r requirements/verto.txt
    $ pip install git+git://github.com/uccser/verto.git
    $ cd csunplugged
    $ npm install
    $ sudo npm install gulp-cli --global

Step 12: Install Text Editor/IDE (optional)
=================================================

This is a good time to install your preferred IDE or text editor.
Some free options we love:

- `Atom`_
- `Sublime Text`_

.. _installation-check-project-setup-works:

Step 13: Check Project Setup Works
=================================================

To check the project works, change your working directory to the
``csunplugged/csunplugged/`` directory (should contain a file called
``manage.py``).

Type the following commands in terminal (we will cover these commands
in more detail on the next page):

.. code-block:: bash

    $ python3 manage.py migrate
    $ python3 manage.py updatedata
    $ python3 manage.py runserver

Leave this terminal running and open a new terminal in the same
directory and type the following command:

.. code-block:: bash

    $ gulp

The final command should open your preferred web browser to
``localhost:3000`` and you should see the CS Unplugged homepage.

Congratulations if you made it this far and everything is working,
you're all set to contribute to the CS Unplugged project.

.. _one: https://git-scm.com/docs/gittutorial
.. _two: https://try.github.io/levels/1/challenges/1
.. _virtual environment:
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/
.. _GitHub website: https://github.com/
.. _SSH keys: https://help.github.com/articles/connecting-to-github-with-ssh/
.. _Verto documentation: http://verto.readthedocs.io/en/latest/install.html
.. _Atom: https://atom.io/
.. _Sublime Text: https://www.sublimetext.com/
