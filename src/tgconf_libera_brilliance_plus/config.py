#!/usr/bin/env python

#############################################################################
##
## This file is part of Taurus, a Tango User Interface Library
##
## http://www.tango-controls.org/static/taurus/latest/doc/html/index.html
##
## (copyleft) CELLS / ALBA Synchrotron, Bellaterra, Spain
##
## This is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
##
## This software is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, see <http://www.gnu.org/licenses/>.
###########################################################################

"""
configuration file for an example of how to construct a GUI based on TaurusGUI

This configuration file determines the default, permanent, pre-defined
contents of the GUI. While the user may add/remove more elements at run
time and those customizations will also be stored, this file defines what a
user will find when launching the GUI for the first time.
"""

# =============================================================================
# Import section. You probably want to keep this line. Don't edit this block
# unless you know what you are doing
from taurus.qt.qtgui.taurusgui.utils import PanelDescription, Qt_Qt
import PyTango
# (end of import section)
# =============================================================================


# ==============================================================================
# General info.
# ==============================================================================
GUI_NAME = 'LiberaBrilliancePlus'
ORGANIZATION = 'MAXIV'
CUSTOM_LOGO = 'images/maxivlogo.png'

# ==============================================================================
# If you want to have a main synoptic panel, set the SYNOPTIC variable
# to the file name of a jdraw file. If a relative path is given, the directory
# containing this configuration file will be used as root
# (comment out or make SYNOPTIC=None to skip creating a synoptic panel)
# ==============================================================================
# SYNOPTIC = ['images/delaygen.jdw']

# ==============================================================================
# Set INSTRUMENTS_FROM_POOL to True for enabling auto-creation of
# instrument panels based on the Pool Instrument info
# ==============================================================================
# INSTRUMENTS_FROM_POOL = False

# ==============================================================================
# Define panels to be shown.
# To define a panel, instantiate a PanelDescription object (see documentation
# for the gblgui_utils module)
# ==============================================================================

# Build libera models

libera_models = {
'Libera-1': ['R3-301M1/DIA/BPM-01/'],
'Libera-2': ['R3-301M1/DIA/BPM-02/'],
'Libera-3': ['R3-301M2/DIA/BPM-01/'],
'Libera-4': ['R3-301M2/DIA/BPM-02/'],
'Libera-5': ['R3-301U1/DIA/BPM-01/'],
'Libera-6': ['R3-301U2/DIA/BPM-01/'],
'Libera-7': ['R3-301U3/DIA/BPM-01/'],
'Libera-8': ['R3-301U3/DIA/BPM-02/'],
'Libera-9': ['R3-301U4/DIA/BPM-01/'],
'Libera-10': ['R3-301U5/DIA/BPM-01/'],
'Libera-11': ['R3-302M1/DIA/BPM-01/'],
'Libera-12': ['R3-302M1/DIA/BPM-02/'],
'Libera-13': ['R3-302M2/DIA/BPM-01/'],
'Libera-14': ['R3-302M2/DIA/BPM-02/'],
'Libera-15': ['R3-302U1/DIA/BPM-01/'],
'Libera-16': ['R3-302U2/DIA/BPM-01/'],
'Libera-17': ['R3-302U3/DIA/BPM-01/'],
'Libera-18': ['R3-302U3/DIA/BPM-02/'],
'Libera-19': ['R3-302U4/DIA/BPM-01/'],
'Libera-20': ['R3-302U5/DIA/BPM-01/'],
'Libera-21': ['R3-303M1/DIA/BPM-01/'],
'Libera-22': ['R3-303M1/DIA/BPM-02/'],
'Libera-23': ['R3-303M2/DIA/BPM-01/'],
'Libera-24': ['R3-303M2/DIA/BPM-02/'],
'Libera-25': ['R3-303U1/DIA/BPM-01/'],
'Libera-26': ['R3-303U2/DIA/BPM-01/'],
'Libera-27': ['R3-303U3/DIA/BPM-01/'],
'Libera-28': ['R3-303U3/DIA/BPM-02/'],
'Libera-29': ['R3-303U4/DIA/BPM-01/'],
'Libera-30': ['R3-303U5/DIA/BPM-01/'],
}
test = {
'Libera-31': ['R3-304M1/DIA/BPM-01/'],
'Libera-32': ['R3-304M1/DIA/BPM-02/'],
'Libera-33': ['R3-304M2/DIA/BPM-01/'],
'Libera-34': ['R3-304M2/DIA/BPM-02/'],
'Libera-35': ['R3-304U1/DIA/BPM-01/'],
'Libera-36': ['R3-304U2/DIA/BPM-01/'],
'Libera-37': ['R3-304U3/DIA/BPM-01/'],
'Libera-38': ['R3-304U3/DIA/BPM-02/'],
'Libera-39': ['R3-304U4/DIA/BPM-01/'],
'Libera-40': ['R3-304U5/DIA/BPM-01/'],
'Libera-41': ['R3-305M1/DIA/BPM-01/'],
'Libera-42': ['R3-305M1/DIA/BPM-02/'],
'Libera-43': ['R3-305M2/DIA/BPM-01/'],
'Libera-44': ['R3-305M2/DIA/BPM-02/'],
'Libera-45': ['R3-305U1/DIA/BPM-01/'],
'Libera-46': ['R3-305U2/DIA/BPM-01/'],
'Libera-47': ['R3-305U3/DIA/BPM-01/'],
'Libera-48': ['R3-305U3/DIA/BPM-02/'],
'Libera-49': ['R3-305U4/DIA/BPM-01/'],
'Libera-50': ['R3-305U5/DIA/BPM-01/'],
'Libera-51': ['R3-306M1/DIA/BPM-01/'],
'Libera-52': ['R3-306M1/DIA/BPM-02/'],
'Libera-53': ['R3-306M2/DIA/BPM-01/'],
'Libera-54': ['R3-306M2/DIA/BPM-02/'],
'Libera-55': ['R3-306U1/DIA/BPM-01/'],
'Libera-56': ['R3-306U2/DIA/BPM-01/'],
'Libera-57': ['R3-306U3/DIA/BPM-01/'],
'Libera-58': ['R3-306U3/DIA/BPM-02/'],
'Libera-59': ['R3-306U4/DIA/BPM-01/'],
'Libera-60': ['R3-306U5/DIA/BPM-01/'],
'Libera-61': ['R3-307M1/DIA/BPM-01/'],
'Libera-62': ['R3-307M1/DIA/BPM-02/'],
'Libera-63': ['R3-307M2/DIA/BPM-01/'],
'Libera-64': ['R3-307M2/DIA/BPM-02/'],
'Libera-65': ['R3-307U1/DIA/BPM-01/'],
'Libera-66': ['R3-307U2/DIA/BPM-01/'],
'Libera-67': ['R3-307U3/DIA/BPM-01/'],
'Libera-68': ['R3-307U3/DIA/BPM-02/'],
'Libera-69': ['R3-307U4/DIA/BPM-01/'],
'Libera-70': ['R3-307U5/DIA/BPM-01/'],
'Libera-71': ['R3-308M1/DIA/BPM-01/'],
'Libera-72': ['R3-308M1/DIA/BPM-02/'],
'Libera-73': ['R3-308M2/DIA/BPM-01/'],
'Libera-74': ['R3-308M2/DIA/BPM-02/'],
'Libera-75': ['R3-308U1/DIA/BPM-01/'],
'Libera-76': ['R3-308U2/DIA/BPM-01/'],
'Libera-77': ['R3-308U3/DIA/BPM-01/'],
'Libera-78': ['R3-308U3/DIA/BPM-02/'],
'Libera-79': ['R3-308U4/DIA/BPM-01/'],
'Libera-80': ['R3-308U5/DIA/BPM-01/'],
'Libera-81': ['R3-309M1/DIA/BPM-01/'],
'Libera-82': ['R3-309M1/DIA/BPM-02/'],
'Libera-83': ['R3-309M2/DIA/BPM-01/'],
'Libera-84': ['R3-309M2/DIA/BPM-02/'],
'Libera-85': ['R3-309U1/DIA/BPM-01/'],
'Libera-86': ['R3-309U2/DIA/BPM-01/'],
'Libera-87': ['R3-309U3/DIA/BPM-01/'],
'Libera-88': ['R3-309U3/DIA/BPM-02/'],
'Libera-89': ['R3-309U4/DIA/BPM-01/'],
'Libera-90': ['R3-309U5/DIA/BPM-01/'],
'Libera-91': ['R3-310M1/DIA/BPM-01/'],
'Libera-92': ['R3-310M1/DIA/BPM-02/'],
'Libera-93': ['R3-310M2/DIA/BPM-01/'],
'Libera-94': ['R3-310M2/DIA/BPM-02/'],
'Libera-95': ['R3-310U1/DIA/BPM-01/'],
'Libera-96': ['R3-310U2/DIA/BPM-01/'],
'Libera-97': ['R3-310U3/DIA/BPM-01/'],
'Libera-98': ['R3-310U3/DIA/BPM-02/'],
'Libera-99': ['R3-310U4/DIA/BPM-01/'],
'Libera-100': ['R3-310U5/DIA/BPM-01/'],
'Libera-101': ['R3-311M1/DIA/BPM-01/'],
'Libera-102': ['R3-311M1/DIA/BPM-02/'],
'Libera-103': ['R3-311M2/DIA/BPM-01/'],
'Libera-104': ['R3-311M2/DIA/BPM-02/'],
'Libera-105': ['R3-311U1/DIA/BPM-01/'],
'Libera-106': ['R3-311U2/DIA/BPM-01/'],
'Libera-107': ['R3-311U3/DIA/BPM-01/'],
'Libera-108': ['R3-311U3/DIA/BPM-02/'],
'Libera-109': ['R3-311U4/DIA/BPM-01/'],
'Libera-110': ['R3-311U5/DIA/BPM-01/'],
'Libera-111': ['R3-312M1/DIA/BPM-01/'],
'Libera-112': ['R3-312M1/DIA/BPM-02/'],
'Libera-113': ['R3-312M2/DIA/BPM-01/'],
'Libera-114': ['R3-312M2/DIA/BPM-02/'],
'Libera-115': ['R3-312U1/DIA/BPM-01/'],
'Libera-116': ['R3-312U2/DIA/BPM-01/'],
'Libera-117': ['R3-312U3/DIA/BPM-01/'],
'Libera-118': ['R3-312U3/DIA/BPM-02/'],
'Libera-119': ['R3-312U4/DIA/BPM-01/'],
'Libera-120': ['R3-312U5/DIA/BPM-01/'],
'Libera-121': ['R3-313M1/DIA/BPM-01/'],
'Libera-122': ['R3-313M1/DIA/BPM-02/'],
'Libera-123': ['R3-313M2/DIA/BPM-01/'],
'Libera-124': ['R3-313M2/DIA/BPM-02/'],
'Libera-125': ['R3-313U1/DIA/BPM-01/'],
'Libera-126': ['R3-313U2/DIA/BPM-01/'],
'Libera-127': ['R3-313U3/DIA/BPM-01/'],
'Libera-128': ['R3-313U3/DIA/BPM-02/'],
'Libera-129': ['R3-313U4/DIA/BPM-01/'],
'Libera-130': ['R3-313U5/DIA/BPM-01/'],
'Libera-131': ['R3-314M1/DIA/BPM-01/'],
'Libera-132': ['R3-314M1/DIA/BPM-02/'],
'Libera-133': ['R3-314M2/DIA/BPM-01/'],
'Libera-134': ['R3-314M2/DIA/BPM-02/'],
'Libera-135': ['R3-314U1/DIA/BPM-01/'],
'Libera-136': ['R3-314U2/DIA/BPM-01/'],
'Libera-137': ['R3-314U3/DIA/BPM-01/'],
'Libera-138': ['R3-314U3/DIA/BPM-02/'],
'Libera-139': ['R3-314U4/DIA/BPM-01/'],
'Libera-140': ['R3-314U5/DIA/BPM-01/'],
'Libera-141': ['R3-315M1/DIA/BPM-01/'],
'Libera-142': ['R3-315M1/DIA/BPM-02/'],
'Libera-143': ['R3-315M2/DIA/BPM-01/'],
'Libera-144': ['R3-315M2/DIA/BPM-02/'],
'Libera-145': ['R3-315U1/DIA/BPM-01/'],
'Libera-146': ['R3-315U2/DIA/BPM-01/'],
'Libera-147': ['R3-315U3/DIA/BPM-01/'],
'Libera-148': ['R3-315U3/DIA/BPM-02/'],
'Libera-149': ['R3-315U4/DIA/BPM-01/'],
'Libera-150': ['R3-315U5/DIA/BPM-01/'],
'Libera-151': ['R3-316M1/DIA/BPM-01/'],
'Libera-152': ['R3-316M1/DIA/BPM-02/'],
'Libera-153': ['R3-316M2/DIA/BPM-01/'],
'Libera-154': ['R3-316M2/DIA/BPM-02/'],
'Libera-155': ['R3-316U1/DIA/BPM-01/'],
'Libera-156': ['R3-316U2/DIA/BPM-01/'],
'Libera-157': ['R3-316U3/DIA/BPM-01/'],
'Libera-158': ['R3-316U3/DIA/BPM-02/'],
'Libera-159': ['R3-316U4/DIA/BPM-01/'],
'Libera-160': ['R3-316U5/DIA/BPM-01/'],
'Libera-161': ['R3-317M1/DIA/BPM-01/'],
'Libera-162': ['R3-317M1/DIA/BPM-02/'],
'Libera-163': ['R3-317M2/DIA/BPM-01/'],
'Libera-164': ['R3-317M2/DIA/BPM-02/'],
'Libera-165': ['R3-317U1/DIA/BPM-01/'],
'Libera-166': ['R3-317U2/DIA/BPM-01/'],
'Libera-167': ['R3-317U3/DIA/BPM-01/'],
'Libera-168': ['R3-317U3/DIA/BPM-02/'],
'Libera-169': ['R3-317U4/DIA/BPM-01/'],
'Libera-170': ['R3-317U5/DIA/BPM-01/'],
'Libera-171': ['R3-318M1/DIA/BPM-01/'],
'Libera-172': ['R3-318M1/DIA/BPM-02/'],
'Libera-173': ['R3-318M2/DIA/BPM-01/'],
'Libera-174': ['R3-318M2/DIA/BPM-02/'],
'Libera-175': ['R3-318U1/DIA/BPM-01/'],
'Libera-176': ['R3-318U2/DIA/BPM-01/'],
'Libera-177': ['R3-318U3/DIA/BPM-01/'],
'Libera-178': ['R3-318U3/DIA/BPM-02/'],
'Libera-179': ['R3-318U4/DIA/BPM-01/'],
'Libera-180': ['R3-318U5/DIA/BPM-01/'],
'Libera-181': ['R3-319M1/DIA/BPM-01/'],
'Libera-182': ['R3-319M1/DIA/BPM-02/'],
'Libera-183': ['R3-319M2/DIA/BPM-01/'],
'Libera-184': ['R3-319M2/DIA/BPM-02/'],
'Libera-185': ['R3-319U1/DIA/BPM-01/'],
'Libera-186': ['R3-319U2/DIA/BPM-01/'],
'Libera-187': ['R3-319U3/DIA/BPM-01/'],
'Libera-188': ['R3-319U3/DIA/BPM-02/'],
'Libera-189': ['R3-319U4/DIA/BPM-01/'],
'Libera-190': ['R3-319U5/DIA/BPM-01/'],
'Libera-191': ['R3-320M1/DIA/BPM-01/'],
'Libera-192': ['R3-320M1/DIA/BPM-02/'],
'Libera-193': ['R3-320M2/DIA/BPM-01/'],
'Libera-194': ['R3-320M2/DIA/BPM-02/'],
'Libera-195': ['R3-320U1/DIA/BPM-01/'],
'Libera-196': ['R3-320U2/DIA/BPM-01/'],
'Libera-197': ['R3-320U3/DIA/BPM-01/'],
'Libera-198': ['R3-320U3/DIA/BPM-02/'],
'Libera-199': ['R3-320U4/DIA/BPM-01/'],
'Libera-200': ['R3-320U5/DIA/BPM-01/'],
'Libera-0': ['R3-301L/DIA/BPM-01/'],
                    }
libera_models___ = {'Libera-0': ['kitslab/dia/bpm-01/'],}
libera_attributes = ['XPosSP', 'YPosSP', 'SumSP']
libera_models_attr = {}

# Build panels

for key, models in libera_models.iteritems():
    device = models[0].upper()
    index = device.rfind("-")
    l_model = []
    for attr in libera_attributes:
        l_model.append(device + attr)

    locals()[key] = PanelDescription(
        device[:index] + device[index + 1:],
        classname='LiberaBrilliancePlusMini',
        modulename='tgconf_libera_brilliance_plus.panels',
        model=l_model
    )

# Build alarm panel

# PanicGuiWidget = PanelDescription('Panic Taurus Widget',
#                                   classname = 'TaurusAlarmGUI',
#                                   modulename= "PanicGUI.gui",
#                                   model="I/PSS/Watchdog",
#                                   )

# ==============================================================================
# Define which External Applications are to be inserted.
# To define an external application, instantiate an ExternalApp object
# See TauMainWindow.addExternalAppLauncher for valid values of ExternalApp
# ==============================================================================
# xterm = ExternalApp(cmdargs=['xterm','spock'], text="Spock",
#                     icon='utilities-terminal')
# hdfview = ExternalApp(["hdfview"])
# pymca = ExternalApp(['pymca'])

# ==============================================================================
# Macro execution configuration
# (comment out or make MACRO_SERVER=None to skip creating a macro execution
# infrastructure)
# ==============================================================================
# MACROSERVER_NAME =''
# DOOR_NAME = ''
# MACROEDITORS_PATH = ''

# ==============================================================================
# Monitor widget
# ==============================================================================
# MONITOR = ['sys/tg_test/1/double_scalar_rww']
