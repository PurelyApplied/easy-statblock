from dataclasses import dataclass
from typing import Optional, Set, Dict

# Some CR 0 creatures grant 0 XP.
XP_BY_CHALLENGE_RATING = {'0': 10, '1/8': 25, '1/4': 50, '1/2': 100,
                          '1': 200, '2': 450, '3': 700, '4': 1100, '5': 1800,
                          '6': 2300, '7': 2900, '8': 3900, '9': 5000, '10': 5900,
                          '11': 7200, '12': 8400, '13': 10000, '14': 11500, '15': 13000,
                          '16': 15000, '17': 18000, '18': 20000, '19': 22000, '20': 25000,
                          '21': 33000, '22': 41000, '23': 50000, '24': 62000, '25': 75000}

# Lowest level that grants the indicated bonus.  E.g., CR 9-12 have proficiency bonus +4
PROFICIENCY_BONUS_BY_CHALLENGE_RATING = {0: 2,
                                         5: 3,
                                         9: 4,
                                         13: 5,
                                         17: 6,
                                         21: 7,
                                         25: 8,
                                         29: 9}


# XP, level, proficiency bonus:
# 0, 1, +2
# 300, 2, +2
# 900, 3, +2
# 2,700, 4, +2
# 6,500, 5, +3
# 14,000, 6, +3
# 23,000, 7, +3
# 34,000, 8, +3
# 48,000, 9, +4
# 64,000, 10, +4
# 85,000, 11, +4
# 100,000, 12, +4
# 120,000, 13, +5
# 140,000, 14, +5
# 165,000, 15, +5
# 195,000, 16, +5
# 225,000, 17, +6
# 265,000, 18, +6
# 305,000, 19, +6
# 355,000, 20, +6


@dataclass
class NamedDescription:
    name: str
    description: str


@dataclass
class Action(NamedDescription):
    pass


@dataclass
class LegendaryAction(Action):
    count_per_turn: int


@dataclass
class WeaponAttack(Action):
    pass


@dataclass
class Trait(NamedDescription):
    associatedAction: Optional[Action]
    pass


@dataclass
class MaterialComponent:
    name: str
    cost: Optional[int]
    is_consumed_by_spell: bool = False


@dataclass
class Spell:
    name: str
    school: str
    level: int
    can_be_cast_as_ritual: Optional[bool]

    casting_time: str
    range: str

    verbal_component: Optional[bool]
    somatic_component: Optional[bool]
    material_component: Optional[MaterialComponent]

    duration: str

    description: str
    at_higher_levels: Optional[str]

    is_cast_before_combat: bool = False
    is_prepared: bool = True

    # For instance, "the hand is invisible" in an instance of Mage Hand for a psionic's innate spellcasting.
    descriptive_modifier: str = None


@dataclass
class Spellcasting:
    level: int
    spellcasting_attribute: str
    DC: int
    to_hit: int
    prepared: Set[Spell]
    known: Optional[Set[Spell]]

    # Level -> Slots available.  Cantrips presumed "at will"
    spell_slots = Dict[int, int]

    spells_cast_before_combat = Optional[Set[Spell]]

    def prepared_spells_as_dict(self):
        levels = set(s.level for s in self.prepared)
        return {l: sorted(list(s
                               for s in self.prepared
                               if s.level == l))
                for l in levels}


@dataclass
class InnateSpellcasting:
    @staticmethod
    def get_standard_description():
        return ("***Innate Spellcasting.***"
                "The {{creature.name}}'s innate spellcasting ability is {{this.spellcasting_attribute|capitalize}}"
                # Open a paren if either type of spell is present
                "{% if this.DC or this.to_hit %} ( {%- endif %}"
                # Post the DC first, if it exists.  If both are present, add a comma to separate
                "{% if this.DC -%} spell save DC {{ this.DC }} {%- if this.to_hit -%} , {% endif -%} {% endif %}"
                # If attack spells are present, add the + to attack
                "{% if this.to_hit -%} {{ this.to_hit | with_plus_or_minus }} to hit with spell attacks {% endif %}"
                # Close the paren if any of this mattered.
                "{% if this.DC or this.to_hit -%} ) {%- endif %}"
                ".  "
                "It can innately cast the following spells, requiring no material components: "
                "{{ this.display_spell_list() }}")

    description: str = get_standard_description()
