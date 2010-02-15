To use this Product, after installing it, you should do some more steps:
- create a folder manually in portal_skins called "custom_logos" that will contains all the logo images that the users can choose.
- copy the current configuration in the configure.zcml of your theme or product with a layer, to override the base logo viewlet:
  <!-- The logo custom -->
  <browser:viewlet
        name="plone.logo"
        manager="plone.app.layout.viewlets.interfaces.IPortalHeader"
        class="redturtle.logoswitch.viewlets.common.CustomLogoViewlet"
        permission="zope2.View" 
        />
- hide plone.logo in the viewlet manager