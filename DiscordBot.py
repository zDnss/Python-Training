import discord
from discord.ext import commands

# Definir o prefixo
prefix = '*'

# Seu token
token = 'ODkzMTA5MDUxNDQ4MjM0MDA1.Gcwwsh.Nb-pvq6cUXsHRj6JG-dfnOIbJoHUTJH53bVUqg'

# Definindo as intenções (intents) do bot
intents = discord.Intents.default()
intents.guild_messages = True
intents.message_content = True


class Mensagens:  # Criando a classe para gerenciar as mensagens do bot
    def __init__(self, bot):
        self.bot = bot

    async def boas_vindas(self, member):  # Mensagem de boas vindas
        mensagem = 'Seja bem vindo a minha loucura tentando ser um dev'
        canal_de_boas_vindas = self.bot.get_channel(846871931202568203)
        await canal_de_boas_vindas.send(mensagem)

    async def info_ajuda(self, ctx):  # Mensagem de ajuda
        mensagem = 'Aqui estão alguns dos comandos disponíveis:\n' \
                   '`*ping`: Retorna "Pong!"\n' \
                   '`*hello`: Cumprimenta o usuário\n'
        await ctx.send(mensagem)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{ctx.author.mention} Pong!')
        print('True')

    @commands.command()
    async def hello(self, ctx):
        await self.ctx.send("Olá! Como você está?")
        print('True')


# Criando o objeto bot
bot = commands.Bot(command_prefix=prefix, intents=intents, self_bot=True)

# Instanciando a classe Mensagens
mensagens = Mensagens(bot)


# Evento que é chamado quando o bot é inicializado
@bot.event
async def on_ready():
    print(f'Bot {bot.user} está pronto!')


# Evento que é chamado quando um novo membro entra no servidor
@bot.event
async def on_member_join(member):
    await mensagens.boas_vindas(member)


# Comando para exibir informações sobre os comandos disponíveis
@bot.command
async def help(ctx):
    await mensagens.info_ajuda(ctx)


@bot.command
async def oi(bot):
    await bot.send('Fuck you bitch')


# Evento que é chamado quando uma mensagem é recebida
@bot.event
async def on_message(message):
    # Verificando se a mensagem menciona o bot e se não foi usada por ele mesmo

    if bot.user in message.mentions and message.author != bot.user:
        # Respondendo com uma mensagem predefinida
        await message.channel.send(f'Olá, {message.author.mention}! Eu sou um bot simples')

    # Importante para que os comandos continuem funcionando
    await bot.process_commands(message)


# Executando o bot com o token do seu bot
bot.run(token)
