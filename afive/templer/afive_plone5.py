import copy

from templer.zope import BasicZope
from templer.core.vars import StringVar, EASY, EXPERT

from templer.localcommands import SUPPORTS_LOCAL_COMMANDS
from templer.localcommands import LOCAL_COMMANDS_MESSAGE


class AfivePlone5(BasicZope):
    _template_dir = 'templates/afive_plone5'
    summary = 'A comprehensive Plone package for Afive projects'
    help = '''
This template support local commands. These commands allow you 
to generate skeleton contenttype, behavior, upgrade profiles, 
schemaextender, etc, etc. All that common in Afive's line of
work
'''
    post_run_msg = LOCAL_COMMANDS_MESSAGE
    category = 'Plone Development'
    use_cheetah = True
    use_local_commands = True
    required_templates = []
    default_required_structures = []
    vars = copy.deepcopy(BasicZope.vars)
    vars.insert(1, StringVar(
        'title',
        title='Project Title',
        description='Title of the project',
        modes=(EASY, EXPERT),
        default='Example Name',
        help="""
This becomes the title of the project. It is used in the
GenericSetup registration for the project and, as such, appears
in Plone's Add/Remove products form.
""",
    ))

    def pre(self, command, output_dir, vars):
        super(AfivePlone5, self).pre(command, output_dir, vars)
        vars['use_localcommands'] = self.use_local_commands
        vars['author'] = 'Afive Team'
        vars['author_email'] = 'team@afterfivetech.com'
        vars['url'] = 'http://github.com/afterfivetech'
