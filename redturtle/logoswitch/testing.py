# -*- coding: utf-8 -*-

from zope.configuration import xmlconfig

from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.testing import z2


class LogoSwitchSandboxLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import redturtle.logoswitch
        xmlconfig.file('configure.zcml',
                       redturtle.logoswitch,
                       context=configurationContext)
        z2.installProduct(app, 'redturtle.logoswitch')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'redturtle.logoswitch:default')
        setRoles(portal, TEST_USER_ID, ['Member', 'Contributor', 'Editor'])


LOGOSWITCH_FIXTURE = LogoSwitchSandboxLayer()
LOGOSWITCH_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(LOGOSWITCH_FIXTURE, ),
                       name="LogoSwitch:Integration")
LOGOSWITCH_FUNCTIONAL_TESTING = \
    FunctionalTesting(bases=(LOGOSWITCH_FIXTURE, ),
                      name="LogoSwitch:Functional")
