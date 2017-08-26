'''
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Aug 22, 2017

@author: jrm
'''
from atom.api import set_default
from enamlnative.widgets.activity_indicator import ProxyActivityIndicator

from .android_progress_bar import AndroidProgressBar


class AndroidActivityIndicator(AndroidProgressBar, ProxyActivityIndicator):
    """ An Android implementation of an Enaml ProxyActivityIndicator.

    """
    #: Set it to be an indeterminate progress bar
    indeterminate = set_default(True)