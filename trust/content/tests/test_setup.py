from Products.CMFCore.utils import getToolByName
from trust.content.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_trust_content_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('trust.content'))

    def test_browserlayer(self):
        from trust.content.browser.interfaces import ITrustContentLayer
        from plone.browserlayer import utils
        self.failUnless(ITrustContentLayer in utils.registered_layers())

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-trust.content:default'), u'0')

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['trust.content'])
        self.failIf(installer.isProductInstalled('trust.content'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['trust.content'])
        from trust.content.browser.interfaces import ITrustContentLayer
        from plone.browserlayer import utils
        self.failIf(ITrustContentLayer in utils.registered_layers())
