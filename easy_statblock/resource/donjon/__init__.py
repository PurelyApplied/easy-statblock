import json
import os


def _load_json_data(filename):
    with open(filename) as in_file:
        return json.load(in_file)


item_data = _load_json_data(os.path.join(os.path.dirname(__file__), 'item_data.json'))
monster_data = _load_json_data(os.path.join(os.path.dirname(__file__), 'monster_data.json'))
npc_data = _load_json_data(os.path.join(os.path.dirname(__file__), 'npc_data.json'))
spell_data = _load_json_data(os.path.join(os.path.dirname(__file__), 'spell_data.json'))
