import hashlib
import random
import math
import os
import json


def generate_spell(input_text):
    magic_spells = [
        '⚡✨Zephyrus Alakazamia✨⚡', '🌟✨Lumina Seraphicus✨🌟', '🌌🌟Astra Eternus🌟🌌', '🌙✨Mysticus Vorpalus✨🌙', '🔥✨Solarius Incantatio✨🔥', '🌪️✨Aquilo Spiralis✨🌪️', '🐉🔥Ignis Draconis🔥🐉', '🌿🌳Veridia Arborum🌳🌿', '🌌⭐Celestis Mirabilis⭐🌌', '🌑🌙Umbra Nocturna🌙🌑',
        '✨⚡Divinus Fulgor⚡✨', '🌧️🌊Tempestas Fluvius🌊🌧️', '🌍🌱Terra Vitalis🌱🌍', '🦅✨Volatus Levitas✨🦅', '🔮✨Arcanus Omnipotens✨🔮', '💜✨Amethysta Magica✨💜', '🛡️✨Fortis Protego✨🛡️', '❓🌌Enigma Invisus🌌❓', '⚔️🌌Bellum Caelum🌌⚔️', '🌳🌿Sylva Perpetua🌿🌳',
        '🔥🌌Flamara Infernalis🌌🔥', '✨🌌Aetherius Radiance🌌✨', '🌐🔗Meridianus Nexus🔗🌐', '🌈🌌Spectra Illusionis🌌🌈', '🌌🔮Nexus Portentia🔮🌌', '🕊️🌬️Volucris Velocitas🌬️🕊️', '🔮🌌Mirus Transmutatio🌌🔮', '⚡✨Fulgurante Lumine✨⚡', '🌺🌟Harmonia Elysium🌟🌺',
        '🌌✨Luminara Effervescens✨🌌', '🌸✨Flora Viventia✨🌸', '🔥🌪️Ignis Turbinis🌪️🔥', '🌟🌌Stellae Infinitas🌌🌟', '⚡🌊Fulgor Aqua🌊⚡', '🌑🦉Umbra Noctua🦉🌑', '🌞🌙Lux Lunaris🌙🌞', '🍃✨Aura Vitalis✨🍃', '🔮🌌Magia Arcana🌌🔮', '🌹✨Rosaceus Lumina✨🌹', '🌌🗝️Cosmos Clavis🗝️🌌',
        '🌪️🌊Tempestas Mare🌊🌪️', '🔥⚔️Ignis Gladius⚔️🔥', '🌈🔮Iris Divinatio🔮🌈', '💫✨Siderea Splendor✨💫', '🌙🦋Noctis Papilio🦋🌙', '🔥🌿Ignis Herba🌿🔥', '⚡🌪️Fulgur Turbo🌪️⚡', '🌌✨Astrum Luminis✨🌌', '🌺🌊Flora Maris🌊🌺', '🌙🔮Luna Divinatrix🔮🌙', '🌟🌿Stella Viridis🌿🌟'
    ]

    # Convert to MD5 hash value
    md5_hash = hashlib.md5(input_text.encode()).hexdigest()

    # Convert MD5 hash value to integer
    hash_int = int(md5_hash, 16)

    # Randomly choose a spell
    random.seed(hash_int)
    random_spell = random.choice(magic_spells)

    return random_spell


def extra_parameter(parameter, scope):
    start_index = parameter.find(scope)
    if start_index > 0:
        parameter_length = parameter[start_index:len(parameter)].find(',')
        if parameter_length < 0:
            parameter_length = len(parameter)
        return parameter[start_index + len(scope):start_index + parameter_length]
    else:
        return '-'


def split_prompt(prompt):
    if len(prompt) > 1024:

        parts = prompt.split(',')
        result_list = []
        temp = ""

        slice_num = len(prompt) / math.ceil(len(prompt) / 1024)
        if slice_num * 1.1 >= 1024:
            slice_num = 1024
        else:
            slice_num = slice_num * 1.1

        for part in parts:
            if len(temp) + len(part) <= slice_num:
                temp += part + ","
            else:
                result_list.append(temp)
                temp = part + ","
        if temp:
            result_list.append(temp)
    else:
        result_list = [prompt]

    return result_list


def load_guild_params(guild_id, param_id):
    guild_config_path = './config/guild_config.json'
    default_config_path = './config/config.json'
    if guild_id == 'default_guild' or not os.path.exists(guild_config_path):
        with open(default_config_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            return data[guild_id][param_id]
    else:
        with open(guild_config_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            return data[guild_id][param_id]
