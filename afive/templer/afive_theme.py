import copy

from sinar.templer.sinar_plone import SinarPlone
from templer.core.vars import StringVar, EASY, EXPERT

from templer.localcommands import SUPPORTS_LOCAL_COMMANDS
from templer.localcommands import LOCAL_COMMANDS_MESSAGE


class SinarTheme(SinarPlone):
    _template_dir = 'templates/sinar_theme'
    summary = 'A comprehensive Plone package for Sinar theme projects'
