import discord
from discord.ext import commands
from ai_handler import generate_ai_response
from db import add_user
from styles import apply_style
from utils import is_valid_prompt
import config

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.command()
async def chat(ctx, *, prompt=None):
    add_user(ctx.author)

    if not is_valid_prompt(prompt):
        await ctx.send("❌ Please enter a valid prompt.")
        return

    await ctx.send("⏳ Thinking...")

    response = generate_ai_response(prompt)
    await ctx.send(response)

@bot.command()
async def styled(ctx, style_type, *, prompt=None):
    add_user(ctx.author)

    if not is_valid_prompt(prompt):
        await ctx.send("❌ Please enter a valid prompt.")
        return

    await ctx.send(f"⏳ Answering in style: **{style_type}**...")

    response = generate_ai_response(prompt)
    styled_response = apply_style(style_type, response)
    await ctx.send(styled_response)

bot.run(config.DISCORD_TOKEN)
