# -*- coding: utf-8 -*-
from redturtle.logoswitch.browser.interfaces import ILogoSwitchLayer
from zope import interface
import os
import StringIO
import unittest


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        """
        """
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.markRequestWithLayer()

    def markRequestWithLayer(self):
        # to be removed when p.a.testing will fix https://dev.plone.org/ticket/11673
        request = self.layer['request']
        interface.alsoProvides(request, ILogoSwitchLayer)

    def get_logos(self):
        image_path = '/'.join(
                              os.path.realpath(__file__).split(os.path.sep)[:-2]
                              )
        rt_logo = '%s/tests/redturtle_logo.jpg' % image_path
        ploneit_logo = '%s/tests/ploneit_logo.png' % image_path
        fd1 = open(rt_logo, 'rb')
        fd2 = open(ploneit_logo, 'rb')
        data1 = StringIO.StringIO(fd1.read())
        data2 = StringIO.StringIO(fd2.read())
        fd1.close()
        fd2.close()
        return data1, data2
