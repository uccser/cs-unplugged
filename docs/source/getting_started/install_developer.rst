Setting up for developement
#################################################

This page will set your machine up for working on the CS Unplugged project.
You should only need to do these steps once (unless the required steps for
setup change).

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

Step 2: Install Python 3
=================================================


.. _Oracle VirtualBox: https://www.virtualbox.org/
.. _Ubuntu 16.04.2 LTS: https://www.ubuntu.com/download/desktop
