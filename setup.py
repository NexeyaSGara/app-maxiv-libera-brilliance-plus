#!/usr/bin/env python

from setuptools import setup

setup(name="taurusgui-libera-brilliance-plus",
      version="2.2.2",
      description="TaurusGUI for the MAX IV liberas brilliance plus",
      author="KITS team",
      author_email="kitscontrols@maxlab.lu.se",
      license="GPLv3",
      url="http://www.maxlab.lu.se",
      package_dir={'': 'src'},
      packages=['tgconf_libera_brilliance_plus', 'tgconf_libera_brilliance_plus.panels'],
      include_package_data=True,
      package_data={'tgconf_libera_brilliance_plus': ['images/maxivlogo.png']},
      data_files=[('/usr/share/applications',
                   ['maxiv-libera-brilliance-plus.desktop']),
                  ('/home/controlroom/Desktop',
                   ['maxiv-libera-brilliance-plus.desktop'])],
      scripts=['scripts/ctLiberaBrilliancePlus']
      )
