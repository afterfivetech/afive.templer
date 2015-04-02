import copy

from sinar.templer.sinar_plone import SinarPlone
from templer.core.vars import StringVar, EASY, EXPERT

from templer.localcommands import SUPPORTS_LOCAL_COMMANDS
from templer.localcommands import LOCAL_COMMANDS_MESSAGE


class SinarI18NOverride(SinarPlone):
    _template_dir = 'templates/sinar_i18noverride'
    summary = 'A package for overriding translation'
