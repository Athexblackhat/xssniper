#!/usr/bin/env python
# -*- coding: utf-8 -*-"
# vim: set expandtab tabstop=4 shiftwidth=4:

from setuptools import setup
import os
data_files = []
doc_files = []
gtk_doc_files = []
for afile in os.listdir('doc'):
    if afile != '.svn':
        doc_files.append('doc/' + afile)
for afile in os.listdir('gtk/docs'):
    if afile != '.svn':
        gtk_doc_files.append('gtk/docs/' + afile)
data_files = ['gtk/images/world.png', 'gtk/images/xssniper.jpg',
              'gtk/images/xssnipericon_16x16.png',
              'gtk/images/xssnipericon_24x24.png',
              'gtk/map/GeoIP.dat']
gtk_files = ['gtk/xssniper.ui']
gtk_app_files = ['gtk/xssniper.desktop']
setup(
    name = "xssniper",
    version = "1.0",
    description = "Cross Site Scripter (xssniper): automatic framework to detect, exploit and report XSS vulnerabilities in web-based applications",
    author = "athex",
    author_email = "teamathex82@gmail.com",
    url = "",
    license = "GPLv3",
    python_requires = ">=3.9",
    install_requires = ['beautifulsoup4>=4.12.3', 'pycurl>=7.45.3', 'selenium>=4.20.0', 'ddgs>=9.0.0', 'fpdf2>=2.8.1'],
    packages = ['core', 'core.fuzzing', 'core.post', 'core.driver'],
    data_files = [('/usr/share/doc/xssniper/', doc_files),
                  ('/usr/share/xssniper/gtk/images/', data_files),
                  ('/usr/share/xssniper/gtk/docs/', gtk_doc_files),
                  ('/usr/share/applications/', gtk_app_files),
                  ('/usr/share/xssniper/gtk/', gtk_files)],
    scripts = ['xssniper'],
    test_suite = "tests",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
)
