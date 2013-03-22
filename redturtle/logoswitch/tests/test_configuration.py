# -*- coding: utf-8 -*-
from base import BaseTestCase
from plone.app.testing import logout
from Products.CMFCore.utils import getToolByName
from redturtle.logoswitch.testing import LOGOSWITCH_INTEGRATION_TESTING
from zope.component import getMultiAdapter
from plone.app.testing import login
from plone.app.testing import SITE_OWNER_NAME


class TestConfiguration(BaseTestCase):

    layer = LOGOSWITCH_INTEGRATION_TESTING

    def test_custom_logos_folder(self):
        """
        Check if the folder is present in portal_skins
        """
        ps = getToolByName(self.portal, 'portal_skins')
        self.assertTrue('custom-logos' in ps.objectIds())


class TestUnauthorized(BaseTestCase):

    layer = LOGOSWITCH_INTEGRATION_TESTING

    def test_selectlogo_view_protected(self):
        """
        test if the settings view is protected
        """
        from AccessControl import Unauthorized
        logout()
        self.assertRaises(Unauthorized, self.portal.restrictedTraverse, '@@select-logo')
