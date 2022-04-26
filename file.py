import os, sys, discord, subprocess
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready(): print("o/")

def cleanup_code(content):
	if content.startswith('```') and content.endswith: return '\n'.join(content.split('\n')[1:-1])
	return content.strip('` \n')

@client.command()
async def cexec(ctx, *, body):
	body = cleanup_code(body)
	if os.path.isfile("./a.out"): os.system("rm -r ./a.out")
	if os.path.isfile("./file1.c"): os.system("rm -r ./file1.c")
	f = open("./file1.c", "w")
	f.write(body)
	f.close()
	c = subprocess.run("gcc ./file1.c", capture_output=True, text=True, shell=True)
	if c.returncode != 0: return await ctx.send(f"```c\n{c.stderr}```")
	p = subprocess.check_output("./a.out", shell=True)
	return await ctx.send(f"```c\n{p.decode()}\n```")

client.run(token)
