import discord
from discord.ext import commands
import logging
import asyncio
import random
import os

#Prefijo para llamar al bot desde Discord
command_prefix='$'
#definimos el bot
bot = commands.Bot(command_prefix)


#TOKENS
#BETA="Mzk2NTU1MzE0MDEyMzU2NjE5.DSjIzw.ygHynfMgnYoaiqcliSqaF8TakhY"
MAIN="Mzk2MTk3NDEwODE0MTY1MDAy.DSd-mA.pBRCF1IhhWhgkuIqQ0H3c9Ta-Y0"

 
#Aca definimos cuando el bot genere algun evento como conectarse al servidor
@bot.event
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print(bot.user.id)
    print("-------------------")
    print("SkullBot Version 0.0.3-Release")

#aca el primer comando de prueba
@bot.command()
async def test(): #el nombre de la funcion es como se manda a llamar en discord, por ejemplo este se llamaria con $test
    await bot.say("testing? Testing") #el async y el await no estoy muy seguro como funciona, pero si no lo pones no funciona :v 


@bot.command(pass_context = True) #Aca es para definir si el comando se va a ejecutar en un contexto (osea si va a ser en x canal o cosas asi)
async def ban(ctx, *, member:discord.Member=None): #en esta funcion le mandamos un contexto, el * no estoy seguro que hace pero hace algo, y luego en teoria le enviamos un usuario que por ley tiene que ser miembro en el server
    if (member == bot.user ): #aca verificamos que no sea el bot a quien le estamos mandando para banear
        await bot.say(ctx.message.author.mention + " No puedes banearme nub")
        await bot.delete_message(ctx.message)
    else:
        if (ctx.message.channel.permissions_for(ctx.message.author).ban_members): #aca verificamos si el usuario que envio el comando tiene acceso a ban
            if (member == ctx.message.author): #y aca se verifica que el usuario no se este baneando a si mismo
                await bot.say(ctx.message.author.mention + " No puedes banearte a ti mismo")
                await bot.delete_message(ctx.message)
            else:
                await bot.say(ctx.message.author.mention + " Bans " + member.mention )
                await bot.ban(member)
                await bot.delete_message(ctx.message)
        elif(member==None):
            await bot.say(ctx.message.author.mention + " No has seleccionado a nadie nub" )
            await bot.delete_message(ctx.message)
        else:
            await bot.say(ctx.message.author.mention + " No tienes permiso para usar este comando")
            await bot.delete_message(ctx.message)



@bot.command(pass_context = True)
async def kill(ctx,*,member:discord.Member=None):
        
    #Diccionario de Homicidios
    kill={1:" asesino friamente usando una pala a ",2:" enveneno la comida de ", 3: " violo hasta matar a ", 4: " fue al pasado para darle pastillas de aborto a la madre de ",5: " le hizo tanto bullying a"}  
    eleccion= kill[random.randrange(1,6)]


    if (member == bot.user):
        await bot.say(ctx.message.author.mention + " Asi que estas intentando matarme? Preparate ")
        await bot.say(member.mention + eleccion + ctx.message.author.mention)
        await bot.delete_message(ctx.message)
    elif(member==None):
        await bot.say(ctx.message.author.mention + " No has seleccionado a nadie nub" )
        await bot.delete_message(ctx.message)
    elif(member == ctx.message.author):
        await bot.delete_message(ctx.message)
        await bot.say(member.mention + " cometio suicidio porque es niño rata" )
    else:
        await bot.delete_message(ctx.message)
        await bot.say(ctx.message.author.mention + eleccion + member.mention)

@bot.command(pass_context= True)
async def ayuda(ctx,*,member:discord.Member=None):
    await bot.send_message(ctx.message.author," \n=======LISTA DE COMANDOS=======\n$unban          -- Temporalmente desactivado \n$test           -- Testing, testing?\n$kill           -- Asesina a tus amigos de una manera comica\n$ban            -- Banea a un usuario // Requiere que tengas el permiso de Ban User\n$ayuda          -- Despliega la Lista de Comandos actuales")
    await bot.delete_message(ctx.message)
    
@bot.command(pass_context= True)
async def kick(ctx,*,member:discord.Member=None):
    if (member == bot.user ): #aca verificamos que no sea el bot a quien le estamos mandando para kickear
        await bot.say(ctx.message.author.mention + " No puedes kickearme nub")
        await bot.delete_message(ctx.message)
    else:
        if (ctx.message.channel.permissions_for(ctx.message.author).kick_members): #aca verificamos si el usuario que envio el comando tiene acceso a ban
            if (member == ctx.message.author): #y aca se verifica que el usuario no se este baneando a si mismo
                await bot.say(ctx.message.author.mention + " No puedes kickearte a ti mismo")
                await bot.delete_message(ctx.message)
            else:
                await bot.say(ctx.message.author.mention + " Kicks " + member.mention )
                await bot.kick(member)
                await bot.delete_message(ctx.message)
        elif(member==None):
            await bot.say(ctx.message.author.mention + " No has seleccionado a nadie nub" )
            await bot.delete_message(ctx.message)
        else:
            await bot.say(ctx.message.author.mention + " No tienes permiso para usar este comando")
            await bot.delete_message(ctx.message)



bot.run(MAIN) #aca se ejecuta el bot, lo que esta en el parentesis es el token.
