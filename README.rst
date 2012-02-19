A Django template tag to render noun icons from the totally sweet `Noun Project <http://thenounproject.com>`_!

Installation
============

1. ``python setup.py install``
2. Add ``noun_project`` to your ``INSTALLED_APPS``

Usage
=====

Inside a template:

  ``{% load noun_icon %}``

then simply:

  ``{% noun_icon "coffee" %}``

To make a pretty coffee icon appear!

Examples:

  ``{% noun_icon "coffee" width="50px" %}``

  ``{% noun_icon "coffee" width="50px" height="200px" %}``

  ``{% noun_icon "coffee" as coffee %}``
