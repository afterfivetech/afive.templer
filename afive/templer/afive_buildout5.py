import copy

from templer.buildout import BasicBuildout
from templer.core.vars import StringVar, EASY, EXPERT

from templer.localcommands import SUPPORTS_LOCAL_COMMANDS
from templer.localcommands import LOCAL_COMMANDS_MESSAGE


class AfiveBuildout5(BasicBuildout):
    _template_dir = 'templates/afive_buildout5'
    summary = 'A Plone 5 buildout with dev/prod cfg'
    help = ''''''
    post_run_msg = LOCAL_COMMANDS_MESSAGE
    category = 'Plone Development'
    use_cheetah = True
    use_local_commands = True
    required_templates = []
    default_required_structures = []
    vars = copy.deepcopy(BasicBuildout.vars)
