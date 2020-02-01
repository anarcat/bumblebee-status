# pylint: disable=C0111,R0903

"""Test module
"""

import core.widget
import core.module

class Module(core.module.Module):
    def __init__(self):
        super().__init__(core.widget.Widget('test'))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
