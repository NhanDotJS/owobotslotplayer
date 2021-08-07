import pyautogui
import sys
import time
import discord
import random
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# client = discord.Client()

# client = discord.Client(activity=discord.Game(name='Nghiện cờ bạc time'))
# value = 1
# time.sleep(1)
# pyautogui.click(x=497, y=853)
# pyautogui.write('owo s '+str(value))
# pyautogui.press('enter')


# @client.event
# async def on_ready():
#     print(client.user)

# @client.event
# async def on
class MyClient(discord.Client):
    def betbung(self):
        if self.randomvar in range(16, 19):
            pyautogui.click(x=33, y=692)
            time.sleep(0.5)
            pyautogui.click(x=497, y=853)
            pyautogui.write('owo h')
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.write('owo b')
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click(x=37, y=645)
            time.sleep(0.5)
            pyautogui.click(x=497, y=853)
            pyautogui.write('owo s '+str(self.value))
            pyautogui.press('enter')
        else:
            pyautogui.click(x=497, y=853)
            pyautogui.write('owo s '+str(self.value))
            pyautogui.press('enter')

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        self.value = 200
        self.randomvar = random.randint(12, 20)
        time.sleep(1)
        self.betbung()
        # self.value = 1

    # async def on_message(self, message):
        # print('Message from {0.author}: {0.content}'.format(message))

    async def on_message_edit(self, before, after):
        # self.randomvarhandler()
        self.randomvar = random.randint(14, 22)
        # if self.randomvar in range(15, 18):
        #     time.sleep(1)
        #     pyautogui.click(x=497, y=853)
        #     pyautogui.write('owo cash')
        #     pyautogui.press('enter')
        #     time.sleep(2)
        #     pyautogui.write('owo h')
        #     pyautogui.press('enter')
        #     time.sleep(2)
        #     pyautogui.write('owo b')
        #     pyautogui.press('enter')
        #     time.sleep(self.randomvar)
        #     self.betbung()
        # else:
        # print(after.content)
        if "and won <:cowoncy:416043450337853441>" in after.content:
            if ":eggplant:" in after.content:
                print("won but stupid")
                await after.channel.send("won but stupid")
                print('The value now is:' + str(self.value))
                await after.channel.send('The value now is:' + str(self.value))
                time.sleep(self.randomvar)
                self.betbung()
            else:
                print("won")
                await after.channel.send("won")
                self.value = 200
                print('The value now is:' + str(self.value))
                await after.channel.send('The value now is:' + str(self.value))
                time.sleep(self.randomvar)
                self.betbung()

        elif "won nothing" in after.content:
            print("lost")
            await after.channel.send("lost")
            self.value = self.value*2
            print('The value now is:' + str(self.value))
            await after.channel.send('The value now is:' + str(self.value))
            time.sleep(self.randomvar)
            self.betbung()

        else:
            print("none")
# if message.author.id == "408785106942164992":
#     if "won" in message.content:
#         print("won")
#     elif "":


client = MyClient(activity=discord.Game(name='Nghiện cờ bạc time'))

client.run(os.environ.get("TOKEN"))

# 497, 853
