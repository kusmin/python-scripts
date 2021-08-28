import instaloader

bot = instaloader.Instaloader()

username = "pycodebr"

print(bot.download_profile(username, profile_pic_only=True))
