from plone.app.layout.viewlets.common import LogoViewlet as BaseLogoViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

class CustomLogoViewlet(BaseLogoViewlet):
    index = ViewPageTemplateFile('logo.pt')

    def update(self):
        super(CustomLogoViewlet, self).update()
        portal = self.portal_state.portal()
        portal_properties = getToolByName(self.context, 'portal_properties')
        site_properties = getattr(portal_properties, 'site_properties')
        if site_properties.hasProperty('logo_name') and site_properties.getProperty('logo_name',None):
            logo_url=site_properties.getProperty('logo_name')
            self.logo_tag='<img src="%s" alt="" title="Plone" />'%logo_url
        else:
            logoName = portal.restrictedTraverse('base_properties').logoName
            self.logo_tag = portal.restrictedTraverse(logoName).tag()

        self.portal_title = self.portal_state.portal_title()
