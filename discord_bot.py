import os
import io
import math
import hashlib
import random
import discord
from PIL import Image
from dotenv import load_dotenv
load_dotenv()
trigger_reaction = os.getenv('TRIGGER_REACTION')

def generate_spell(input_text):
    magic_spells = [
    '⚡✨Zephyrus Alakazamia✨⚡',
    '🌟✨Lumina Seraphicus✨🌟',
    '🌌🌟Astra Eternus🌟🌌',
    '🌙✨Mysticus Vorpalus✨🌙',
    '🔥✨Solarius Incantatio✨🔥',
    '🌪️✨Aquilo Spiralis✨🌪️',
    '🐉🔥Ignis Draconis🔥🐉',
    '🌿🌳Veridia Arborum🌳🌿',
    '🌌⭐Celestis Mirabilis⭐🌌',
    '🌑🌙Umbra Nocturna🌙🌑',
    '✨⚡Divinus Fulgor⚡✨',
    '🌧️🌊Tempestas Fluvius🌊🌧️',
    '🌍🌱Terra Vitalis🌱🌍',
    '🦅✨Volatus Levitas✨🦅',
    '🔮✨Arcanus Omnipotens✨🔮',
    '💜✨Amethysta Magica✨💜',
    '🛡️✨Fortis Protego✨🛡️',
    '❓🌌Enigma Invisus🌌❓',
    '⚔️🌌Bellum Caelum🌌⚔️',
    '🌳🌿Sylva Perpetua🌿🌳',
    '🔥🌌Flamara Infernalis🌌🔥',
    '✨🌌Aetherius Radiance🌌✨',
    '🌐🔗Meridianus Nexus🔗🌐',
    '🌈🌌Spectra Illusionis🌌🌈',
    '🌌🔮Nexus Portentia🔮🌌',
    '🕊️🌬️Volucris Velocitas🌬️🕊️',
    '🔮🌌Mirus Transmutatio🌌🔮',
    '⚡✨Fulgurante Lumine✨⚡',
    '🌺🌟Harmonia Elysium🌟🌺',
    '🌌✨Luminara Effervescens✨🌌',
    '🌸✨Flora Viventia✨🌸',
    '🔥🌪️Ignis Turbinis🌪️🔥',
    '🌟🌌Stellae Infinitas🌌🌟',
    '⚡🌊Fulgor Aqua🌊⚡',
    '🌑🦉Umbra Noctua🦉🌑',
    '🌞🌙Lux Lunaris🌙🌞',
    '🍃✨Aura Vitalis✨🍃',
    '🔮🌌Magia Arcana🌌🔮',
    '🌹✨Rosaceus Lumina✨🌹',
    '🌌🗝️Cosmos Clavis🗝️🌌',
    '🌪️🌊Tempestas Mare🌊🌪️',
    '🔥⚔️Ignis Gladius⚔️🔥',
    '🌈🔮Iris Divinatio🔮🌈',
    '💫✨Siderea Splendor✨💫',
    '🌙🦋Noctis Papilio🦋🌙',
    '🔥🌿Ignis Herba🌿🔥',
    '⚡🌪️Fulgur Turbo🌪️⚡',
    '🌌✨Astrum Luminis✨🌌',
    '🌺🌊Flora Maris🌊🌺',
    '🌙🔮Luna Divinatrix🔮🌙',
    '🌟🌿Stella Viridis🌿🌟'
    ]

    
    # Convert to MD5 hash value
    md5_hash = hashlib.md5(input_text.encode()).hexdigest()

    # Convert MD5 hash value to integer
    hash_int = int(md5_hash, 16)

    # Randomly choose a spell
    random.seed(hash_int)
    random_spell = random.choice(magic_spells)

    return random_spell


def split_prompt(prompt):
    if len(prompt) > 1024:
        
        parts = prompt.split(',')
        result_list = []
        temp = ""

        slice_num = len(prompt)/math.ceil(len(prompt)/1024)
        if slice_num*1.1 >= 1024:
            slice_num = 1024
        else:
            slice_num=slice_num*1.1

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

def extra_parameter(parameter,scope):
    start_index = parameter.find(scope)
    if start_index > 0:
        parameter_length = parameter[start_index:len(parameter)].find(',')
        if parameter_length < 0 :
            parameter_length = len(parameter)
        return parameter[start_index+len(scope):start_index+parameter_length]
    else:
        return '-'

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})', flush=True)
        invite_url = discord.utils.oauth_url(
            client_id=self.application_id, permissions=discord.Permissions(permissions=2419452944))
        print(f'Invite url is {invite_url}', flush=True)
        print('------', flush=True)

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent,):
        if payload.emoji.name==trigger_reaction:
            reaction_member = payload.member
            channel = self.get_channel(payload.channel_id)
            channel_name = channel.name
            message = await channel.fetch_message(int(payload.message_id))
            message_link = message.jump_url
            guild = message.guild
            guild_name = guild.name
            guild_icon_url = guild.icon

            try:
                # Get the member object of the message author
                author = await message.guild.fetch_member(message.author.id)

                # Get the member's server nickname
                author_name = author.nick
                if not author_name:
                    # If the member does not have a server nickname, use the username
                    author_name = author.name
                # Get author avatar url
                author_avatar_url = author.avatar
            except discord.NotFound:
                # If unable to fetch the member object, use the username of the message author
                author_name = message.author.name
                author_avatar_url = ''


            attachments=message.attachments
            if attachments:
                for attachment in attachments:

                    # Check if the attachment is a PNG file
                    if attachment.filename.endswith('.png'):

                        # Read attachment data into memory
                        image_data = io.BytesIO(await attachment.read())
                        
                        # Open the image from memory
                        with Image.open(image_data) as img:
                            img.load()
                            try:
                                parameter = img.info['parameters']
                            except KeyError:
                                # Parameters not found
                                await message.remove_reaction(trigger_reaction, reaction_member)
                                await message.add_reaction('❎')
                                continue

                    else:
                        # Not a PNG file
                        await message.remove_reaction(trigger_reaction, reaction_member)
                        await message.add_reaction('❎')

                    # Process parameter                 
                    nprompt_index = parameter.find('Negative prompt: ')
                    steps_index = parameter.find('Steps: ')
                    prompts = parameter[0:nprompt_index]
                    nprompts = parameter[nprompt_index+17:steps_index]
                    extras = parameter[steps_index:len(parameter)]

                    # Building DM embed message
                    dm_channel = await reaction_member.create_dm()
                    title=f"『{generate_spell(str(attachment.id))}』"
                    color=discord.Colour.from_rgb(127, 0, 32)
                    embed=discord.Embed(title=title, description="",colour=color,url=message_link)
                    
                    # Setup prompt field
                    prompt_list = split_prompt(prompts)
                    if len(prompt_list) > 1:
                        for i,prompt in enumerate(prompt_list, 1):
                            embed.add_field(name=f"Prompt {i}", value=prompt,inline=False)
                    else:
                        embed.add_field(name="Prompt", value=prompts,inline=False)
                    
                    # Setup negtive prompt field
                    nprompt_list = split_prompt(nprompts)
                    if len(nprompt_list) > 1:
                        for i,nprompt in enumerate(nprompt_list, 1):
                            embed.add_field(name=f"Negative Prompt {i}", value=nprompt,inline=False)
                    else:
                        embed.add_field(name="Negative Prompt", value=nprompts,inline=False)

                    # Setup parameter field
                    parameter_fields = ["Steps","CFG scale","Seed","Sampler","Model","Model hash","Size","Version","Hires upscale","Hires steps","Hires upscaler","Denoising strength"]
                    embed.add_field(name='Parameters', value='',inline=False)
                    for field in parameter_fields:
                        # check if Hires exist print hires info else break loop
                        if field == 'Hires upscale' and parameter.find('Hires upscale: ') < 0:
                            break
                        elif field == 'Hires upscale':
                            embed.add_field(name='Hires info', value='',inline=False)
                        embed.add_field(name=field, value=extra_parameter(parameter,f'{field}: '))

                    # Setup extra field
                    for field in parameter_fields:
                        extras = extras.replace(f'{field}: {extra_parameter(parameter,f"{field}: ")}, ',"")
                        extras = extras.replace(f'{field}: {extra_parameter(parameter,f"{field}: ")}',"")
                    extra_list = split_prompt(extras)
                    if len(extra_list) > 1:
                        for i,extra in enumerate(extra_list, 1):
                            embed.add_field(name=f"extra info {i}", value=extra,inline=False)
                    else:
                        embed.add_field(name="extra info", value=extras,inline=False)
                    
                    # Setup other embed elements
                    embed.set_image(url=attachment.url)
                    embed.set_author(name=author_name,icon_url=author_avatar_url)
                    embed.set_footer(text=f'from「{guild_name}」{channel_name}channel',icon_url=guild_icon_url)

                    # Send DM
                    if len(embed) >= 6000:
                        await dm_channel.send(content=f"Infinite Magic Projection has exceeded its capacity, Celefira is running out of mana!\n{message_link}")
                        # DM limit exceeded
                        await message.remove_reaction(trigger_reaction, reaction_member)
                        await message.add_reaction('❎')
                    else:
                        await dm_channel.send(embed=embed)
                    print(f'DM sent to {reaction_member.name}.', flush=True)
            else:
                await message.remove_reaction(trigger_reaction, reaction_member)

intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
client.run(os.getenv('DISCORD_TOKEN'))
