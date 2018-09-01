#!/usr/bin/env python3
from dataclasses import dataclass
from typing import List, Tuple, Optional, Union

from easy_statblock.basic_models import Action


@dataclass
class CreatureBasics:
    name: str
    size: str
    type_and_subtype: str
    alignment: str


@dataclass
class CreatureDefense:
    armor_class: int
    provided_by: str


@dataclass
class CreatureHP:
    points: int
    dice: str


@dataclass
class CreatureMovement:
    speed: List[str]


@dataclass
class CreatureAttributes:
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int


@dataclass
class CreatureProficiencies:
    saving_throws: List[Tuple[str, int]]
    skills: List[Tuple[str, int]]


@dataclass
class CreatureResistancesAndImmunities:
    damage_resistances: List[str]
    damage_immunities: List[str]
    condition_immunities: List[str]


@dataclass
class CreatureSenses:
    passive_perception: int
    additional_senses: Optional[List[Tuple[str, int]]]


@dataclass
class CreatureLanguages:
    languages: Union[str, List[str]]


@dataclass
class CreatureChallenge:
    challenge_rating: int
    xp: int


@dataclass
class CreatureSpellcasting:
    pass


@dataclass
class CreatureActions:
    actions = List[Action]
    pass


@dataclass
class CreatureReactions(CreatureActions):
    pass


@dataclass
class CreatureLegendaryActions(CreatureActions):
    actions_per_turn: int


@dataclass
class Creature:
    basics: CreatureBasics
    defense: CreatureDefense
    hp: CreatureHP
    movement: CreatureMovement
    attributes: CreatureAttributes
    # Although it
    challenge: Optional[CreatureChallenge]

    proficiencies: Optional[CreatureProficiencies] = None
    resistancesAndImmunities: Optional[CreatureResistancesAndImmunities] = None
    senses: Optional[CreatureSenses] = None
    languages: Optional[CreatureLanguages] = None

    spellcasting: Optional[CreatureSpellcasting] = None
    actions: Optional[CreatureActions] = None
    reactions: Optional[CreatureReactions] = None
    legendaryActions: Optional[CreatureLegendaryActions] = None
