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

    def get_type_info(self, name):
        types = getToolByName(self.portal, 'portal_types')
        return types.getTypeInfo('trust.content.MemberSite')

    def test_types__trust_content_MemberSite__i18n_domain(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertEqual(ctype.i18n_domain, 'trust.content')

    def test_types__trust_content_MemberSite__meta_type(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertEqual(ctype.meta_type, 'Dexterity FTI')

    def test_types__trust_content_MemberSite__title(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertEqual(ctype.title, 'Member Site')

    def test_types__trust_content_MemberSite__description(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertEqual(ctype.description, '')

    def test_types__trust_content_MemberSite__content_icon(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertEqual(ctype.getIcon(), 'group.png')

    def test_types__trust_content_MemberSite__allow_discussion(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertFalse(ctype.allow_discussion)

    def test_types__trust_content_MemberSite__global_allow(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertFalse(ctype.global_allow)

    def test_types__trust_content_MemberSite__filter_content_types(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertTrue(ctype.filter_content_types)

    def test_types__trust_content_MemberSite__allowed_content_types(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertEqual(ctype.allowed_content_types, ('Image',))

    def test_types__trust_content_MemberSite__schema(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertEqual(ctype.schema, 'trust.content.schema.IMemberSite')

    def test_types__trust_content_MemberSite__klass(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertEqual(ctype.klass, 'plone.dexterity.content.Container')

    def test_types__trust_content_MemberSite__add_permission(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertEqual(ctype.add_permission, 'trust.content.AddMemberSite')

    def test_types__trust_content_MemberSite__behaviors(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertEqual(ctype.behaviors, (
                'plone.app.content.interfaces.INameFromTitle',
                'plone.app.dexterity.behaviors.metadata.IDublinCore'))

    def test_types__trust_content_MemberSite__default_view(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertEqual(ctype.default_view, 'view')

    def test_types__trust_content_MemberSite__default_view_fallback(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertFalse(ctype.default_view_fallback)

    def test_types__trust_content_MemberSite__view_methods(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertEqual(ctype.view_methods, ('view',))

    def test_types__trust_content_MemberSite__default_aliases(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        self.assertEqual(ctype.default_aliases, {
            '(Default)': '(dynamic view)',
            'edit': '@@edit',
            'sharing': '@@sharing',
            'view': '(selected layout)',
        })

    def test_types__trust_content_MemberSite__action__view__title(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.title, 'View')

    def test_types__trust_content_MemberSite__action__view__condition(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.condition, '')

    def test_types__trust_content_MemberSite__action__view__url_expr(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.getActionExpression(), 'string:${folder_url}/')

    def test_types__trust_content_MemberSite__action__view__visible(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        action = ctype.getActionObject('object/view')
        self.assertTrue(action.visible)

    def test_types__trust_content_MemberSite__action__view__permissions(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        action = ctype.getActionObject('object/view')
        self.assertEqual(action.permissions, (u'View',))

    def test_types__trust_content_MemberSite__action__edit__title(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.title, 'Edit')

    def test_types__trust_content_MemberSite__action__edit__condition(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.condition, '')

    def test_types__trust_content_MemberSite__action__edit__url_expr(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.getActionExpression(), 'string:${object_url}/edit')

    def test_types__trust_content_MemberSite__action__edit__visible(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        action = ctype.getActionObject('object/edit')
        self.assertTrue(action.visible)

    def test_types__trust_content_MemberSite__action__edit__permissions(self):
        ctype = self.get_type_info('trust.content.MemberSite')
        action = ctype.getActionObject('object/edit')
        self.assertEqual(action.permissions, (u'Modify portal content',))

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
