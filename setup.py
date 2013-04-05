"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
import py2app

# Build the .app file
setup(
    options=dict(
        py2app=dict(
            iconfile='static/icon.icns',
            packages=['PySide','numpy'],
#            includes=['xml.etree.ElementTree'],
            excludes=['matplotlib', 'scipy','_xmlplus'],
            #'_ssl', 'doctest', 'pdb', 'unittest', 'difflib', 'inspect',],
            site_packages=True,
            optimize=2,
            resources=['static', 'examples', 'db', 'identities', 'html','icons'],
            plist=dict(
                CFBundleName               = "MetaPath",
                CFBundleShortVersionString = "1.0.0",     # must be in X.X.X format
                CFBundleGetInfoString      = "MetaPath 1.0.0",
                CFBundleExecutable         = "MetaPath",
                CFBundleIdentifier         = "com.ables.metapath",
            ),
        ),
    ),
    app=[ 'metapath-qt.py' ],
)
