import copy

from afive.templer.afive_plone import AfivePlone
from templer.core.vars import StringVar, EASY, EXPERT

from templer.localcommands import SUPPORTS_LOCAL_COMMANDS
from templer.localcommands import LOCAL_COMMANDS_MESSAGE


class AfiveTheme(AfivePlone):
    _template_dir = 'templates/afive_theme'
    summary = 'A comprehensive Plone package for Afive theme projects'
