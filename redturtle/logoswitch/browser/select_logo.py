from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from redturtle.logoswitch import logoswitchMessageFactory as _
from redturtle.logoswitch import logger


class SelectLogoView(BrowserView):
    """Vista per conoscere la dimensione totale di un oggetto folderish"""

    def __call__(self):
        """
        Check values in the request, and make the right action
        """
        if self.request.form.get('form.button.Cancel', ''):
            return self.doReturn(_(u'Action deleted'), 'info')
        elif self.request.form.get('form.button.AddFolder', ''):
            return self.createFolder()
        elif self.request.form.get('form.button.Submit', ''):
            return self.changeLogoName()
        return self.index()

    def hasLogosFolder(self):
        """
        Check if custom-logos is present in portal_skins
        """
        ps = getToolByName(self.context, 'portal_skins')
        return 'custom-logos' in ps.objectIds()

    def createFolder(self):
        ps = getToolByName(self.context, 'portal_skins')
        try:
            ps.manage_addFolder(id='custom-logos',
                                title="Custom logos",)
            logger.info("Added custom-logos folder in portal_skins")
            return self.doReturn(_(u'Folder logos created'), 'info')
        except Exception, e:
            logger.error("There was a problem while creating costom-logos folder: %s" % e)
            return self.doReturn(_(u'There was a problem while creating custom-logos folder. See log for more details.'),
                                   'error')

    def changeLogoName(self):
        """If we have selected a new logo, it will be changed the logo name in site_properties"""
        new_logo = self.request.form.get('image_selected')
        portal_properties = getToolByName(self.context, 'portal_properties')
        site_properties = getattr(portal_properties, 'site_properties')
        if site_properties.hasProperty('logo_name'):
            site_properties.manage_changeProperties(logo_name=new_logo)
            return self.doReturn(_(u'Logo updated'), 'info')

    def getImageList(self):
        """return a list of images"""
        ps = getToolByName(self.context, 'portal_skins')
        folder = self.context.unrestrictedTraverse('/'.join(ps.getPhysicalPath()) + '/custom-logos')
        return folder.values()

    def doReturn(self, message, type):
        pu = getToolByName(self.context, "plone_utils")
        root = self.context.portal_url()
        pu.addPortalMessage(message, type=type)
        self.request.RESPONSE.redirect('%s/@@select-logo' % root)
