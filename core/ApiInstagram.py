from instabot import Bot


class PostInstagram:
    def __init__(self, username, password, imagem, description):
        self.description = description
        self.username = username
        self.password = password
        self.imagem = imagem

    def postar_foto(self):
        bot = Bot
        bot.login(username=self.username, password=self.password)
        bot.upload_photo(self.imagem, caption=self.description)
        bot.upload_story_photo(self.imagem)
