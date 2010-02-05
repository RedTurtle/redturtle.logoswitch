from Products.Five import BrowserView

from Products.CMFCore.utils import getToolByName

class SelectLogoView(BrowserView):
    """Vista per conoscere la dimensione totale di un oggetto folderish"""
    
    def hasLogosFolder(self):
        """"""
        ps=getToolByName(self.context,'portal_skins')
        return 'custom_logos' in ps.objectIds()
    
    def createFolder(self):
        ps=getToolByName(self.context,'portal_skins')
        try:
            ps.manage_addFolder(id='custom_logos', 
                                title = "Custom logos",)
            self.context.plone_log("Added custom_logos folder in portal_skins")
        except Exception,e:
            self.context.plone_log("There was a problem while creating costom_logos folder: %s"%e)
        self.doReturn('Folder Logos created','info')
       
    def changeLogoName(self):
        """If we have selected a new logo, it will be changed the logo name in site_properties"""
        
        if self.request.form.get('form.button.Cancel',''):
            self.doReturn('Action deleted','info')
        
        if not self.request.form.get('form.button.Submit',''):
            self.doReturn('Wrong action','error')
        new_logo=self.request.form.get('image_selected')
        portal_properties = getToolByName(self.context, 'portal_properties')
        site_properties = getattr(portal_properties, 'site_properties')
        if site_properties.hasProperty('logo_name'):
            site_properties.manage_changeProperties(logo_name=new_logo)
            self.doReturn('Logo updated','info')
            
    def getImageList(self):
        """return a list of images"""
        ps=getToolByName(self.context,'portal_skins')
        folder=self.context.unrestrictedTraverse('/'.join(ps.getPhysicalPath())+'/custom_logos')
        return folder.values() 

    def doReturn(self,message,type):
        pu = getToolByName(self.context, "plone_utils")
        pu.addPortalMessage(message, type=type)
        self.request.RESPONSE.redirect(self.request.HTTP_REFERER)