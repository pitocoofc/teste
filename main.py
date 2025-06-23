import discord
import os
import openai
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

openai.api_key = os.environ["OPENAI_API_KEY"]
CRIADOR_DO_BOT = "animeangelrv"

async def gerar_resposta(mensagem):
    response = await openai.ChatCompletion.acreate(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente amigável e útil."},
            {"role": "user", "content": mensagem}
        ],
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

@client.event
async def on_ready():
    print(f'{client.user} está online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        await message.channel.send("Estou processando sua mensagem...")

        resposta = await gerar_resposta(message.content)
        await message.channel.send(resposta)

client.run(os.environ["DISCORD_TOKEN"])
