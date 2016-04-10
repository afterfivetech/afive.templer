import copy

from afive.templer.afive_plone import AfivePlone
from templer.core.vars import StringVar, EASY, EXPERT

from templer.localcommands import SUPPORTS_LOCAL_COMMANDS
from templer.localcommands import LOCAL_COMMANDS_MESSAGE


class AfiveI18NOverride(AfivePlone):
    _template_dir = 'templates/afive_i18noverride'
    summary = 'A package for overriding translation'
