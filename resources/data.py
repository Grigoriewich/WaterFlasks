from enum import Enum, auto

from mcresources import ResourceManager, loot_tables
from mcresources.type_definitions import Json

from mcresources import utils



def generate(rm: ResourceManager):

    rm.entity_tag('drops_bladders', 'tfc:cow', 'tfc:goat', 'tfc:yak', 'tfc:alpaca', 'tfc:musk_ox', 'tfc:sheep',
                  'tfc:donkey', 'tfc:horse', 'tfc:mule', 'tfc:polar_bear', 'tfc:grizzly_bear', 'tfc:black_bear',)

    ### MISC DATA ###
    global_loot_modifiers(rm, 'waterflasks:bladders')
    global_loot_modifier(rm, 'bladders', 'waterflasks:add_item', {'item': utils.item_stack('waterflasks:bladder'), 'chance': 0.1}, match_entity_tag('waterflasks:drops_bladders'))


## Lost animals
##case "animals/wildebeest":
##case "animals/zebu":
##case "animals/camel":
##case "animals/llama":
##case "animals/gazelle":

def global_loot_modifier(rm: ResourceManager, name: str, mod_type: str, data_in: Json, *conditions: utils.Json):
    rm.write((*rm.resource_dir, 'data', rm.domain, 'loot_modifiers', name), {
        'type': mod_type,
        'conditions': [c for c in conditions],
        **data_in
    })


# note for the mcresources dev: these work exactly the same as tags so if you implement this, do it like that
def global_loot_modifiers(rm: ResourceManager, *modifiers: str):
    rm.write((*rm.resource_dir, 'data', 'forge', 'loot_modifiers', 'global_loot_modifiers'), {
        'replace': False,
        'entries': [m for m in modifiers]
    })


def match_entity_tag(tag: str):
    return {
        'condition': 'minecraft:entity_properties',
        'predicate': {
            'type': '#' + tag
        },
        'entity': 'this'
    }