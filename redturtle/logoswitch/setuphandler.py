# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName

def insertLogoProperty(context):
    """
    insert the sp key in catalog
    """
    portal=context.getSite()
    if context.readDataFile('redturtle.logoswitch_various.txt') is None:
        return
    portal_properties = getToolByName(context, 'portal_properties')
    site_properties = getattr(portal_properties, 'site_properties')
    if not site_properties.hasProperty('logo_name'):
        site_properties.manage_addProperty(id='logo_name',value='',type='string')
        portal.plone_log("Added logo_name property")
    
     