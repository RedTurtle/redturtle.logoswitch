# -*- coding: utf-8 -*-


def install(portal):
    setup_tool = portal.portal_setup
    setup_tool.runAllImportStepsFromProfile('profile-redturtle.logoswitch:default')


def uninstall(portal, reinstall=False):
    if not reinstall:
        setup_tool = portal.portal_setup
        setup_tool.runAllImportStepsFromProfile('profile-redturtle.logoswitch:uninstall')
