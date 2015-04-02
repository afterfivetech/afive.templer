from setuptools import setup, find_packages
import os

version = '1.6.dev0'

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

setup(name='sinar.templer',
      version=version,
      description="Plone templates for Sinar Project",
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
      author='Khairil Yusof',
      author_email='khairil.yusof@sinarproject.org',
      url='http://github.com/sinar/sinar.templer',
      license='MIT',
      packages=find_packages(),
      namespace_packages=['sinar'],
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
      sinar_plone = sinar.templer:SinarPlone
      sinar_policy = sinar.templer:SinarPolicy
      sinar_theme = sinar.templer:SinarTheme
      sinar_buildout = sinar.templer:SinarBuildout
      sinar_i18noverride = sinar.templer:SinarI18NOverride

      [templer.templer_sub_template]
      content_type = sinar.templer.localcommands.dexterity:DexterityContent
      behavior = sinar.templer.localcommands.dexterity:DexterityBehavior
      upgrade_profile = sinar.templer.localcommands.genericsetup:UpgradeProfile
      skin_layer = sinar.templer.localcommands.genericsetup:SkinLayer
      schemaextender = sinar.templer.localcommands.archetypes:SchemaExtender
      basic_portlet = sinar.templer.localcommands.portlet:BasicPortlet
      nonconfigurable_portlet = sinar.templer.localcommands.portlet:NonConfigurablePortlet
      viewlet = sinar.templer.localcommands.browser:Viewlet
      view = sinar.templer.localcommands.browser:View
      css = sinar.templer.localcommands.genericsetup:CSSResource
      js = sinar.templer.localcommands.genericsetup:JSResource
      vocabulary = sinar.templer.localcommands.components:Vocabulary
      """,
      )
