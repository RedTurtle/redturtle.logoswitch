
def install(portal):
    setup_tool = portal.portal_setup
    setup_tool.setImportContext('profile-redturtle.logoswitch:default')
    setup_tool.runAllImportSteps()
    
    root = ('/').join(portal.getPhysicalPath())
    portal_skins=portal.unrestrictedTraverse('%s/portal_skins'%root)
    import pdb;pdb.set_trace()
    if not 'custom_logos' in portal_skins.objectIds():
        try:
            portal_skins.manage_addFolder(id='custom_logos', 
                                          title = "Custom logos",)
            portal.plone_log("Added custom_logos folder in portal_skins")
        except Exception,e:
            portal.plone_log("There was a problem while creating costom_logos folder: %s"%e)
            

#def uninstall(portal):
#    setup_tool = portal.portal_setup
#    setup_tool.setImportContext('profile-redturtle.logoswitch:uninstall')
#    setup_tool.runAllImportSteps()
