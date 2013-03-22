# -*- coding: utf-8 -*-
from redturtle.logoswitch.testing import LOGOSWITCH_INTEGRATION_TESTING
from base import BaseTestCase
from Products.CMFCore.utils import getToolByName
from transaction import commit
from plone.app.testing import SITE_OWNER_NAME, SITE_OWNER_PASSWORD
from plone.testing.z2 import Browser


class TestEmptyLogos(BaseTestCase):

    layer = LOGOSWITCH_INTEGRATION_TESTING

    def setUp(self):
        """
        """
        app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.markRequestWithLayer()
        self.portal_url = self.portal.absolute_url()
        self.browser = Browser(app)
        self.browser.addHeader('Authorization', 'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD,))

    def test_settings_empty(self):
        """
        Check if custom-logos folder is empty
        """
        self.browser.open("%s/@@select-logo" % self.portal_url)
        self.assertTrue(u"No images in the folder." in self.browser.contents)


class TestChangeLogo(BaseTestCase):

    layer = LOGOSWITCH_INTEGRATION_TESTING

    def setUp(self):
        """
        make setup and get 2 images from test folder
        """
        app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.rt_logo, self.ploneit_logo = self.get_logos()
        self.markRequestWithLayer()
        self.portal_url = self.portal.absolute_url()
        self.browser = Browser(app)
        self.browser.addHeader('Authorization', 'Basic %s:%s' % (SITE_OWNER_NAME, SITE_OWNER_PASSWORD,))

    def test_change_logo(self):
        """
        Try to change log
        """
        ps = getToolByName(self.portal, 'portal_skins')
        custom_logos = ps.get('custom-logos', None)
        rt_logo = custom_logos.manage_addImage('rt_logo', self.rt_logo, "RedTurtle")
        ploneit_logo = custom_logos.manage_addImage('ploneit_logo', self.ploneit_logo,)
        self.assertTrue(rt_logo)
        self.assertTrue(ploneit_logo)
        commit()
        self.browser.open("%s/@@select-logo" % self.portal_url)
        self.assertTrue(u"http://nohost/plone/logo.png" in self.browser.contents)
        self.assertFalse(u"No images in the folder." in self.browser.contents)
        #try to set rt_logo as logo
        images_radio = self.browser.getControl(name='image_selected')
        self.assertEquals(images_radio.options, ['rt_logo', 'ploneit_logo'])
        images_radio.value = ['rt_logo']
        self.browser.getControl(name='form.button.Submit').click()
        self.assertTrue(u"Logo updated" in self.browser.contents)
        self.assertTrue('<img src="http://nohost/plone/rt_logo" alt="" title="Plone site" />' in self.browser.contents)
        #try to set ploneit_logo as logo
        images_radio = self.browser.getControl(name='image_selected')
        self.assertEquals(images_radio.options, ['rt_logo', 'ploneit_logo'])
        images_radio.value = ['ploneit_logo']
        self.browser.getControl(name='form.button.Submit').click()
        self.assertTrue(u"Logo updated" in self.browser.contents)
        self.assertTrue('<img src="http://nohost/plone/ploneit_logo" alt="" title="Plone site" />' in self.browser.contents)

    def tearDown(self):
        """
        Delete images in custom-logos folder
        """
        ps = getToolByName(self.portal, 'portal_skins')
        custom_logos = ps.get('custom-logos', None)
        custom_logos.manage_delObjects(custom_logos.keys())
        commit()
