import copy

from sinar.templer.sinar_plone import InigoPlone
from templer.core.vars import StringVar, EASY, EXPERT

from templer.localcommands import SUPPORTS_LOCAL_COMMANDS
from templer.localcommands import LOCAL_COMMANDS_MESSAGE


class InigoI18NOverride(InigoPlone):
    _template_dir = 'templates/sinar_i18noverride'
    summary = 'A package for overriding translation'
