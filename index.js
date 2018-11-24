const TelegramBot = require("telegram-node-bot");

const token = "686681991:AAF7UZokmM8hfL4QwlYjndSllBefphgePfM";

const bot = new TelegramBot(token, { polling: true });

bot.on("message", msg => {
  var Hi = "hi";
  if (
    msg.text
      .toString()
      .toLowerCase()
      .indexOf(Hi) === 0
  ) {
    bot.sendMessage(msg.chat.id, "Hello dear user");
  }
});
