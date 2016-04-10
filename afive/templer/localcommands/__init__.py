from templer.localcommands import TemplerLocalTemplate

class SubTemplate(TemplerLocalTemplate):
    use_cheetah = True
    parent_templates = ['afive_plone']
