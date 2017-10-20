from setuptools import setup, find_packages
import os

version = '1.7.3'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='afive.templer',
      version=version,
      description="Plone templates for Afive Projects",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Code Generators",
        ],
      keywords='',
      author='Holden Hao',
      author_email='holden@afterfivetech.com',
      url='http://github.com/afterfivetech/afive.templer',
      license='MIT',
      packages=find_packages(),
      namespace_packages=['afive'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'templer.core',
          'templer.zope',
          'templer.localcommands',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      afive_plone = afive.templer:AfivePlone
      afive_plone5 = afive.templer:AfivePlone5
      afive_policy = afive.templer:AfivePolicy
      afive_theme = afive.templer:AfiveTheme
      afive_buildout = afive.templer:AfiveBuildout
      afive_buildout5 = afive.templer:AfiveBuildout5
      afive_i18noverride = afive.templer:AfiveI18NOverride

      [templer.templer_sub_template]
      content_type = afive.templer.localcommands.dexterity:DexterityContent
      behavior = afive.templer.localcommands.dexterity:DexterityBehavior
      upgrade_profile = afive.templer.localcommands.genericsetup:UpgradeProfile
      skin_layer = afive.templer.localcommands.genericsetup:SkinLayer
      schemaextender = afive.templer.localcommands.archetypes:SchemaExtender
      basic_portlet = afive.templer.localcommands.portlet:BasicPortlet
      nonconfigurable_portlet = afive.templer.localcommands.portlet:NonConfigurablePortlet
      viewlet = afive.templer.localcommands.browser:Viewlet
      view = afive.templer.localcommands.browser:View
      css = afive.templer.localcommands.genericsetup:CSSResource
      js = afive.templer.localcommands.genericsetup:JSResource
      vocabulary = afive.templer.localcommands.components:Vocabulary
      """,
      )
