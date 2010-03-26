from plone.app.layout.viewlets.common import LogoViewlet as BaseLogoViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

class CustomLogoViewlet(BaseLogoViewlet):
    index = ViewPageTemplateFile('logo.pt')

    def update(self):
        super(CustomLogoViewlet, self).update()
        portal_properties = getToolByName(self.context, 'portal_properties')
        site_properties = getattr(portal_properties, 'site_properties')
        ps=getToolByName(self.context,'portal_skins')
        if 'custom_logos' in ps.objectIds():
            if site_properties.hasProperty('logo_name') and site_properties.getProperty('logo_name',None):
                logo_url=site_properties.getProperty('logo_name')
                folder_items=self.context.unrestrictedTraverse('/'.join(ps.getPhysicalPath())+'/custom_logos')
                logo=[item.absolute_url() for item in folder_items.values() if item.absolute_url()==logo_url]
                if logo:
                    self.logo_tag='<img src="%s" alt="" title="%s" />'%(logo_url,portal_properties.Title())
                else:
                    self.useDefaultLogo()
            else:
                self.useDefaultLogo()
        else:
                self.useDefaultLogo()
        self.portal_title = self.portal_state.portal_title()
        
    def useDefaultLogo(self):
        portal=self.portal_state.portal()
        logoName = portal.restrictedTraverse('base_properties').logoName
        self.logo_tag = portal.restrictedTraverse(logoName).tag()