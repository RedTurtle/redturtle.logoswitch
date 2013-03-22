# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from redturtle.logoswitch import logger


def import_various(context):
    if context.readDataFile('redturtle.logoswitch_various.txt') is None:
        return
    portal = context.getSite()
    createFolder(portal)
    insertLogoProperty(portal)


def createFolder(context):
        ps = getToolByName(context, 'portal_skins')
        if'custom-logos' not in ps.objectIds():
            try:
                ps.manage_addFolder(id='custom-logos',
                                    title="Custom logos",)
                logger.info("Added custom-logos folder in portal_skins")
            except Exception, e:
                logger.info("There was a problem while creating costom-logos folder: %s" % e)


def insertLogoProperty(context):
    """
    insert logo_name in portal_properties
    """
    portal_properties = getToolByName(context, 'portal_properties')
    site_properties = getattr(portal_properties, 'site_properties')
    if not site_properties.hasProperty('logo_name'):
        site_properties.manage_addProperty(id='logo_name', value='', type='string')
        logger.info("Added logo_name property")
