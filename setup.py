#!/usr/bin/python
#Last-modified: 17 Jul 2017 11:00:55 AM

#         Module/Scripts Description
# 
# Copyright (c) 2008 Yunfei Wang <yfwang0405@gmail.com>
# 
# This code is free software; you can redistribute it and/or modify it
# under the terms of the BSD License (see the file COPYING included with
# the distribution).
# 
# @status:  experimental
# @version: 1.1.0
# @author:  Yunfei Wang
# @contact: yfwang0405@gmail.com

# ------------------------------------
# python modules
# ------------------------------------

import os,sys
from setuptools import setup, find_packages, Extension

# ------------------------------------
# constants
# ------------------------------------

# ------------------------------------
# Misc functions
# ------------------------------------

# ------------------------------------
# Classes
# ------------------------------------

# ------------------------------------
# Main
# ------------------------------------

if __name__ == '__main__':
    
    # includepy = "%s/include/python%s" % (sys.prefix, sys.version[:3])
    with open("README.rst",'r') as fh:
        long_description = fh.read()
        idx = long_description.find('\n')
        description = long_description[:idx].rstrip()
    # ngsplot version
    PROG, VERSION = 'pycircos','1.0.1'

    # Compile Kent lib
    if 'clean' in sys.argv:
        print >>sys.stderr, "Clean dist and egg info ..."
        os.system('if [ -d dist ]; then rm -rf dist; fi')
        os.system('if [ -f {0}.egg-info ]; then rm {0}.egg-info; fi'.format(PROG))
        os.system('if [ -d {0}.egg-info ]; then rm -rf {0}.egg-info; fi'.format(PROG))
    
    # install requirement
    install_requires = [["numpy >= 1.4.1"],
                        ["matplotlib >= 2.0.0"],
                        ["pandas >= 0.18.0"]]
    # more options depends on python version
    if float(sys.version[:3]) == 2.6:
        install_requires.append(["argparse >= 1.2.1"])
        package_dir={PROG:'v2'}
    elif float(sys.version[:3])==2.7:
        package_dir={PROG:'v2'}
    elif float(sys.version[:3])>=3.4:
        package_dir={PROG:'v3'}

    setup(name=PROG,
          version=VERSION,
          author='Yunfei Wang',
          author_email='yfwang0405@gmail.com',
          url='https://github.com/tsznxx/{0}'.format(PROG),
          license="GNU General Public License (GPL)",
          keywords = "Python NGS plot",
          description = (description),
          long_description = long_description,
          package_dir=package_dir,
          packages = [PROG],
          scripts=[],
          ext_modules=[],
          classifiers=['Environment :: Console',
                       'Development Status :: 3 - Alpha',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved :: GNU General Public License (GPL)',
                       'License :: Free for non-commercial use',
                       'Operating System :: Unix',
                       'Programming Language :: Python :: 2.7',
                       'Topic :: Scientific/Engineering :: Bio-Informatics'],
          install_requires=install_requires)

