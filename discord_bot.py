import os
import io
import math
import hashlib
import random
import discord
from PIL import Image
from dotenv import load_dotenv

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
        for part in parts:
            if len(temp) + len(part) <= len(prompt)/math.ceil(len(prompt)/1024):
                temp += part + ","
            else:
                result_list.append(temp)
                temp = part + ","
        if temp:
            result_list.append(temp)
    else:
        result_list = [prompt]

    return result_list

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        invite_url = discord.utils.oauth_url(
            client_id=1114205027616178256, permissions=discord.Permissions(permissions=2419452944))
        print(f'Invite url is {invite_url}')
        print('------')

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent,):
        if payload.emoji.name=='ℹ️':
            reaction_member = payload.member
            channel = self.get_channel(payload.channel_id)
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
                                await message.remove_reaction('ℹ️', reaction_member)
                                await message.add_reaction('❎')
                                continue

                    else:
                        # Not a PNG file
                        await message.remove_reaction('ℹ️', reaction_member)
                        await message.add_reaction('❎')

                    # Process parameter
                    start_index = parameter.find('Negative prompt: ')
                    end_index = parameter.find("\n", start_index)
                    prompts = parameter[0:start_index]
                    nprompts = parameter[start_index+17:end_index]
                    extras = parameter[end_index:len(parameter)]

                    # Building DM embed message
                    dm_channel = await reaction_member.create_dm()
                    embed=discord.Embed(title=f"『{generate_spell('attachment.id')}』", description="",colour=discord.Colour.from_rgb(127, 0, 32),url=message_link)
                    
                    # Setup prompt field
                    prompt_list = split_prompt(prompts)
                    if len(prompt_list) > 1:
                        for i,prompt in enumerate(prompt_list, 1):
                            embed.add_field(name=f"提示詞 {i}", value=prompt,inline=False)
                    else:
                        embed.add_field(name="提示詞", value=prompts,inline=False)
                    
                    # Setup negtive prompt field
                    nprompt_list = split_prompt(nprompts)
                    if len(nprompt_list) > 1:
                        for i,nprompt in enumerate(nprompt_list, 1):
                            embed.add_field(name=f"反向提示詞 {i}", value=nprompt,inline=False)
                    else:
                        embed.add_field(name="反向提示詞", value=nprompts,inline=False)
                    
                    # Setup extra field
                    extra_list = split_prompt(extras)
                    if len(extra_list) > 1:
                        for i,extra in enumerate(extra_list, 1):
                            embed.add_field(name=f"其他資訊 {i}", value=extra,inline=False)
                    else:
                        embed.add_field(name="其他資訊", value=extras,inline=False)

                    # Setup other embed elements
                    embed.set_image(url=attachment.url)
                    embed.set_author(name=author_name,icon_url=author_avatar_url)
                    embed.set_footer(text=f'來自{guild_name}',icon_url=guild_icon_url)

                    # Send DM
                    await dm_channel.send(embed=embed)
            else:
                await message.remove_reaction('ℹ️', reaction_member)

intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)
load_dotenv()
client.run(os.getenv('DISCORD_TOKEN'))
