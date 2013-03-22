from plone.app.layout.viewlets.common import LogoViewlet as BaseLogoViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter


class CustomLogoViewlet(BaseLogoViewlet):
    index = ViewPageTemplateFile('logo.pt')

    def update(self):
        super(CustomLogoViewlet, self).update()
        portal_properties = getToolByName(self.context, 'portal_properties')
        site_properties = getattr(portal_properties, 'site_properties')
        ps = getToolByName(self.context, 'portal_skins')
        custom_logos = ps.get('custom-logos', None)
        if custom_logos:
            logo_name = site_properties.getProperty('logo_name', '')
            if logo_name:
                logo = custom_logos.get(logo_name, None)
                if logo:
                    portal_state = getMultiAdapter((self.context, self.request),
                                                    name=u'plone_portal_state')
                    logo_url = "%s/%s" % (portal_state.portal_url(), logo_name)
                    logoTitle = self.portal_state.portal_title()
                    self.logo_tag = '<img src="%s" alt="" title="%s" />' % (logo_url, logoTitle)
                else:
                    self.useDefaultLogo()
            else:
                self.useDefaultLogo()
        else:
            self.useDefaultLogo()
        self.portal_title = self.portal_state.portal_title()

    def useDefaultLogo(self):
        portal = self.portal_state.portal()
        logoName = portal.restrictedTraverse('base_properties').logoName
        self.logo_tag = portal.restrictedTraverse(logoName).tag()
