Installation Guide
#################################################

This page will set your machine up for working on the CS Unplugged project.
You should only need to do these installation steps once (unless the required
steps for setup change).

Requirements
=================================================

- At least 5 GB of hard drive space.
- An internet connection to download 1 to 2 GB of data.

Recommended Reading
=================================================

If you aren't familiar with the following systems, we recommend
reading tutorials first on how to use them:

- Entering terminal commands for your operating system
- Git (here are two Git tutorials: `one`_ `two`_)

Step 1: Setup Virtual Machine (optional)
=================================================

For those working on a computer in a restricted environment (for example:
a computer managed by an education insitution), then working in a
**virtual machine** is recommended.

If you wish to setup a virtual machine for development, we have a guide here:
:doc:`../other/setup_virtual_machine`.

.. _step-2-install-git:

Step 2: Install Git
=================================================

Install the version control software `Git`_ onto your computer.

.. note::

    If you are new to Git and not comfortable with using the terminal,
    you may like to use a free program like `SourceTree`_ to use Git.

Step 3: Create GitHub Account
=================================================

If you don't already have an account on GitHub, create a free account on
the `GitHub website`_.
This account will be tied to any changes you submit to the project.

Step 4: Set Git Account Values
=================================================

When you make a commit in Git (the term for changes to the project), the
commit is tied to a name and email address. We need to set name and email
address within the Git system installed on the machine.

- `Setting your username in Git`_
- `Setting your email in Git`_

You can also `keep your email address private on GitHub`_ if needed.

.. note::

    If your GitHub account is secured with two-factor authentication (2FA)
    this is a perfect time to setup `SSH keys`_.

Step 5: Download the CS Unplugged Repository
=================================================

Firstly create the directory you wish to hold the CS Unplugged repository
directory in if you wish to store the data in a specific location.
Once you have decided upon the location, clone (the Git term for download) the
project onto your computer.

If you are using terminal commands to use Git, type the following command in
terminal (you don't need to enter the ``$`` character, this shows the start of
your terminal prompt):

.. code-block:: bash

    $ git clone https://github.com/uccser/cs-unplugged.git

.. note::

    If you connect to GitHub through SSH, then type:

    .. code-block:: bash

        $ git clone git@github.com:uccser/cs-unplugged.git

Once Git has cloned the directory, checkout the repository to the development
branch ``develop``.

Step 6: Install Docker
=================================================

We use a system called `Docker`_ to run the CS Unplugged system, both on local
machine for development, and also when deployed to production.
Download the latest version of the free Docker Community Edition for your
operating system from the `Docker Store`_.

Once you have installed the software, run the following commands in a terminal
to check Docker is working as intended (you don't need to enter the ``$``
character, this shows the start of your terminal prompt).

.. code-block:: bash

    $ docker version
    $ docker compose version
    $ docker run hello-world

.. note::

    Depending on your operating system, if the above commands don't work you
    may need to set Docker to be able to run without ``sudo``.
    You will need to do this in order to use the ``dev`` helper script.

Step 7: Install Text Editor/IDE (optional)
=================================================

This is a good time to install your preferred IDE or text editor, if you don't
have one already.
Some free options we love:

- `Atom`_
- `Sublime Text`_

Step 8: Install Developer Tools (optional)
=================================================

.. note::

    You can skip this step if you're only adding content to the project.

For those developing the CS Unplugged system, you will need to install some
tools on your computer for local development.
These tools include packages for style checking and compiling documentation.

Install Python 3
------------------------------------------------------------------------------

Install Python 3 with the following command in terminal:

.. code-block:: bash

    $ sudo apt install python3

Install Python 3 PIP
------------------------------------------------------------------------------

Then install Python 3 pip (pip is a package management system used to
install and manage software packages written in Python) with the following
command in terminal:

.. code-block:: bash

    $ sudo apt install python3-pip

Install Python virtualenv
------------------------------------------------------------------------------

We recommend (though it's not required) to work within a virtual environment
(see :ref:`what-is-a-virtual-environment`).
This helps to prevent conflicts with dependencies.

Install virtualenv with the following command in terminal:

.. code-block:: bash

    $ sudo pip3 install virtualenv

.. note::

    **Optional step:** You can also install `virtualenvwrapper`_ to make it
    easier when using and managing your virtual environments.

Create Virtual Environment
------------------------------------------------------------------------------

Type the following commands in terminal to create and activate
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

Install Packages into the Virtual Environemnt
------------------------------------------------------------------------------

Now that the virtual environment is active, we can install the Python packages
into it for local development.
This allows you to run these tools without having to run these within the
Docker system.

.. code-block:: bash

    $ pip install -r requirements/local.txt

.. _installation-check-project-setup-works:

Step 9: Check Project Setup Works
=================================================

To check the project works, open a terminal in the project root directory,
which is the ``cs-unplugged/`` directory (should contain a file called
``dev``).

Type the following commands into the terminal (we will cover these commands
in more detail on the next page):

.. code-block:: bash

    $ ./dev start
    $ ./dev update

If this is the first time you're running this script, it will need to build
system images.
This can take some time, roughly 15 to 30 minutes, depending on your computer
and internet speed (we recommend grabbing a cup of tea and watching an episode
of Brooklyn Nine-Nine on Netflix).

After the helper script builds the system images, it will automatically start
the system, and will let you know when the system is ready.
You should then be able to open your preferred web browser to the URL
``cs-unplugged.localhost`` and see the CS Unplugged homepage.

Congratulations if you made it this far and everything is working,
you're all set to contribute to the CS Unplugged project.

.. _one: https://git-scm.com/docs/gittutorial
.. _two: https://try.github.io/levels/1/challenges/1
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/
.. _Git: https://git-scm.com/
.. _SourceTree: https://www.sourcetreeapp.com/
.. _GitHub website: https://github.com/
.. _SSH keys: https://help.github.com/articles/connecting-to-github-with-ssh/
.. _Setting your username in Git: https://help.github.com/articles/setting-your-username-in-git/
.. _Setting your email in Git: https://help.github.com/articles/setting-your-email-in-git/
.. _keep your email address private on GitHub: https://help.github.com/articles/keeping-your-email-address-private/
.. _Docker: https://www.docker.com/
.. _Docker Store: https://store.docker.com/search?type=edition&offering=community
.. _Verto documentation: http://verto.readthedocs.io/en/latest/install.html
.. _Atom: https://atom.io/
.. _Sublime Text: https://www.sublimetext.com/
