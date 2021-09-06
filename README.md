## USER FRIENDLY USERBOT FOR TG!

----

<div align="center">
  <img src="https://telegra.ph/file/2482d6bc7556b05ebb329.jpg" width="700" height="600" >
  <h1>ᴀᴠᴀᴛᴀʀ UserBot</h1>
</div>
<p align="center">

ᴀᴠᴀᴛᴀʀ UserBot is a bot that makes it easy for you to use Telegram. It is completely open source and free.
    <br>
        <a href="https://t.me/HiTechRockets">Telegram Group</a> |
        <a href="https://t.me/AsenaUserBot">Telegram Channel</a>
    <br>
</p>

----
![Docker Pulls](https://img.shields.io/docker/pulls/fusuf/asenauserbot?style=flat-square) ![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/fusuf/asenauserbot?style=flat-square)
## SET UP
### VERY SIMPLE METHOD
[Youtube Videosu](https://www.youtube.com/watch?v=mUUQ53TYqI0) ![YouTube Video Views](https://img.shields.io/youtube/views/mUUQ53TYqI0?style=flat-square)

**Android:** 
Open Termux and paste this code: `bash <(curl -L https://kutt.it/88I5KA)`

**iOS:** 
Open iSH and paste this code: `apk update && apk add bash && apk add curl && curl -L -o asena_installer.sh https://t.ly/vATX && chmod +x asena_installer.sh && bash asena_installer.sh`

**Windows 10:** [Python](https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l#activetab=pivot:overviewtab) indirin ardından PowerShell bu kodu yapıştırın: `Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://kutt.it/aYTzCx')`

### SIMPLE METHOD

If you have no idea about installing the bot , read here: [Thilina Weerasekara](https://github.com/Thilinaweerasekara2003/AvatarUserBot/)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Thilinaweerasekara2003/AvatarUserBot)
### THE HARD METHOD
```python
git clone https://github.com/Quiec/AsenaUserBot.git
cd AsenaUserBot
pip install -r requirements.txt
# Config.env oluşturun ve düzenleyin. #
python3 main.py
```

## EXAMPLE PLUGIN
```python
from userbot.events import register
from userbot.cmdhelp import CmdHelp # <-- Bunu ekleyin.

@register(outgoing=True, pattern="^.deneme")
async def deneme(event):
    await event.edit('Gerçekten deneme!')

Help = CmdHelp('deneme') # Bilgi ekleyeceğiz diyoruz.
Help.add_command('deneme', # Komut
    None, # Komut parametresi varsa yazın yoksa None yazın
    'Gerçekten deneme yapıyor!', # Komut açıklaması
    'deneme' # Örnek kullanım.
    )

Help.add_info('Made by @Fusuf.') # You can add information.
# Or warning --> Help.add_warning('DO NOT USE!')
Help.add() # And let's add.
```
___

## TO INFORM
If you have any requests & complaints & suggestions you can reach [HiTecRockets](https://t.me/HiTechRockets).

```
    
    Because of Userbot; Your Telegram account may be banned.
    This is an open source project, you are responsible for every action you take. Absolutely Asena managers do not accept responsibility.
    By installing Asena, you are deemed to accept these responsibilities.
```

## CREDITS
Thanks for ;

[Seden UserBot](https://github.com/TeamDerUntergang/Telegram-UserBot)

[Userge](https://github.com/UsergeTeam/Userge)

[Spechide](https://github.com/Spechide)

  # Special Credits ❤
  
**[𝗂𝗆_𝖻𝖻](https://github.com/im-bb)
**[𝙋𝙧𝙖𝙗𝙝𝙖𝙨𝙝𝙖](https://github.com/prabhasha-p)
**[𝘿𝙚𝙨𝙝𝙖𝙙𝙚𝙚𝙩𝙝](https://github.com/Deshadeeth-Thisarana)
**[Thilina Weerasekara](https://github.com/Thilinaweerasekara2003)
