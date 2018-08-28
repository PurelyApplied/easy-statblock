{% macro gmbinder_creature_statblock(creature) -%}
{% if creature.meta.style == "wide" -%}
___
{% endif -%}
___
> ## {{creature['name']}}
>*{{creature['size']}} {{creature['type']}}, {{creature['alignment']}}*
> ___
> - **Armor Class** {{creature['armor class']}} ({{creature['armor type']}})
> - **Hit Points** {{creature['hit points']}} ({{creature['hit dice']}})
> - **Speed** {{creature['speed']| join(', ')}}
>___
>|STR|DEX|CON|INT|WIS|CHA|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|{% for stat in creature['stats'] -%}
{{'%d (%s%d)|' % (stat, '+' if stat > 10 else '', stat // 2 - 5)}}
{%- endfor -%}
>___
{% if creature['saving throws'] -%}
> - **Saving Throws** {{creature['saving throws']| join(', ')}}
{% endif -%}
{% if creature['skills'] -%}
> - **Skills** {{creature['skills']| join(', ')}}
{% endif -%}
{% if creature['damage vulnerabilities'] -%}
> - **Damage Vulnerabilities** {{creature['damage vulnerabilities']| join(', ')}}
{% endif -%}
{% if creature['resistances'] -%}
> - **Damage Resistances** {{creature['resistances']| join(', ')}}
{% endif -%}
{% if creature['damage immunities'] -%}
> - **Damage Immunities** {{creature['damage immunities']| join(', ')}}
{% endif -%}
{% if creature['condition immunities'] -%}
> - **Condition Immunities** {{creature['condition immunities']| join(', ')}}
{% endif -%}
{% if creature['senses'] -%}
> - **Senses** {{creature['senses'] | join(', ')}}, {{creature['passive perception']}}
{% endif -%}
{% if creature['languages'] -%}
> - **Languages** {{creature['languages'] | join(', ')}}
{% else -%}
> - **Languages** —
{%- endif -%}
> - **Challenge** {{creature['challenge']}}
> ___
>
> ### Actions
> ***Multiattack.*** The Creature Name makes Number and type of attacks
>
> ***Ability Description.*** *Attack Style:* Attack Bonus to hit, Reach/Range, one target. *Hit:* Damage Damage Type damage
>
> ***General Ability Description.*** General Attack Description
{%- endmacro -%}
