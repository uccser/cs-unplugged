Installation guide
#################################################

This page will set your machine up for working on the CS Unplugged project.
You should only need to do these installation steps once (unless the required
steps for setup change).

Recommended Reading
=================================================

If you aren't familiar with the following systems, we recommend
reading a tutorial first on how to use them:

- Basic terminal commands
- `Git`_

.. warning::

  The following steps are written for developing with a Linux operating
  system. You may need to adapt the instructions if you are working on
  Windows, OS X, etc.

Step 1: Setup virtual machine (optional)
=================================================

For those working on a computer in a restricted environment (for example:
a computer managed by an education insitution) or wish to be able to follow
the following instructions exactly, then working in a **virtual machine** is
recommended.

The following steps are just one way to set up an Linux virtual machine
for development, and are intended for those new to setting up virtual
machines.

1. Download and install `Oracle VirtualBox`_.
2. Download installation of preferred Linux operating system.
   A common choice is `Ubuntu 16.04.2 LTS`_.
3. Open VirtualBox and click ``New``.
4. Enter a name for your virtual machine, for example "CS Unplugged".
   Also select the type and version of your operating system.
   If you downloaded the Ubuntu linked above, the type is "Linux",
   and version is "Ubuntu (64-bit)". Click "Next".
5. Choose the memory you wish to allocate (2048 MB to 4096 MB is recommended).
   Click "Next".
6. Select "Create a virtual hard disk now". Click "Create".
7. Keep the default selection of "VDI (VirtualBox Disk Image)".
   Click "Next".
8. Keep the default selection of "Dynamically allocated".
   Click "Next".
9. Change the name and location of the hard drive for the virtual
   machine if required (default is usually fine).
10. Select the maximum size that the hard drive can grow to (be aware of
    how much space you have available on your machine).
    We recommend 20 GB to 40 GB. Click "Create".
11. Right click on your newly created virtual machine and click settings.
    Within these settings you can also setup a shared clipboard between the
    host and virtual machines, plus increase the number of processors the
    virtual machine can use. There are plenty of guides available online for
    how to enable them.
12. Click the "Storage" category. Under "Controller: IDE" click "Empty".
    On the right of the window click the disk icon and select "Choose
    Virtual Optical Disk File" and select the operating system installation
    file that you downloaded earlier. Close the Settings window.
13. Start the virtual machine, and the operating system installation screen
    should appear upon starting. Install the operating system, and once that
    has completed, move onto Step 2.

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

We recommend (though it's not required) to work within a virtual environment.
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

Step 5: Create GitHub account
=================================================

If you don't already have an account on GitHub, create an account on
the `GitHub website`_.
This account will be tied to any changes you submit to the project.

Step 6: Set Git account values
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

Step 8: Create user and database in Postgres
=================================================

Firstly type the following command in terminal to login to the Postgres
server with the default ``postgres`` account:

.. code-block:: bash

    $ sudo -i -u postgres

The terminal prompt should have now changed and begins with ``postgres@``.
Now enter the following commands to create a user (called a 'role'):

.. note::

    Remember the user name and password you use, as you
    will need these in Step 13.

.. code-block:: bash

    createuser --interactive --pwprompt
    Enter name of role to add: <your name>
    Enter password for new role: <your password>
    Enter it again: <your password>
    Shall the new role be a superuser? (y/n): y

For example:

.. code-block:: none

    createuser --interactive --pwprompt
    Enter name of role to add: johndoe
    Enter password for new role: s3cr3t_p@ssw0rd
    Enter it again: s3cr3t_p@ssw0rd
    Shall the new role be a superuser? (y/n): y

To create the database, type the following command in terminal:

.. code-block:: none

    createdb csunplugged -e

To quit the Postgres prompt and return to the normal terminal, type the following command in terminal:

.. code-block:: none

    logout

Step 9: Download the CS Unplugged project
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

Step 10: Create virtual environment
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

Step 11: Install project requirements
=================================================

To install the project requirements, type the following commands in terminal
from the project root directory (contains a file called ``requirements.txt``):

.. code-block:: bash

    $ curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
    $ sudo apt-get install -y nodejs
    $ sudo apt-get install libffi-dev libcairo2-dev libjpeg-dev libgif-dev
    $ pip install -r requirements/local.txt
    $ cd csunplugged
    $ npm install
    $ sudo npm install gulp-cli --global

Step 12: Install text editor/IDE (optional)
=================================================

This is a good time to install your preferred IDE or text editor.
Some free options we love:

- `Atom`_
- `Sublime Text`_
- `Vim`_

Step 13: Complete project settings file
=================================================

Open the ``csunplugged/config/`` directory, and make a copy of
``settings_secret_template.py`` called ``settings_secret.py``.

Using the values you used in Step 8:

- Change the value of ``USER`` to the user name you set.
- Change the value of ``PASSWORD`` to the password you set.

The ``settings_secret.py`` file is ignored by the version control, so
it's not uploaded to the public server for everyone to see.

.. note::

    The process of storing secret setting values will be changed in
    the near future.

.. _installation-check-project-setup-works:

Step 14: Check project setup works
=================================================

To check the project works, change your working directory to the
``csunplugged/csunplugged/`` directory (should contain a file called
``manage.py``).

Type the following commands in terminal (we will cover these commands
in more detail on the next page):

.. code-block:: bash

    $ python3 manage.py migrate
    $ python3 manage.py loaddata
    $ python3 manage.py runserver

Leave this terminal running and open a new terminal in the same
directory and type the following command:

.. code-block:: bash

    $ gulp

The final command should open your preferred web browser to
``localhost:3000`` and you should see the CS Unplugged homepage.

Congratulations if you made it this far and everything is working,
you're all set to contribute to the CS Unplugged project.

.. _Git: https://git-scm.com/
.. _Oracle VirtualBox: https://www.virtualbox.org/
.. _Ubuntu 16.04.2 LTS: https://www.ubuntu.com/download/desktop
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/
.. _GitHub website: https://github.com/
.. _SSH keys: https://help.github.com/articles/connecting-to-github-with-ssh/
.. _Kordac documentation: http://kordac.readthedocs.io/en/latest/install.html
.. _Atom: https://atom.io/
.. _Sublime Text: https://www.sublimetext.com/
.. _Vim: http://www.vim.org/
