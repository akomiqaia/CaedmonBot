"use strict";

const Telegram = require("telegram-node-bot");
const TelegramBaseController = Telegram.TelegramBaseController;
const TextCommand = Telegram.TextCommand;
const tg = new Telegram.Telegram(
  "686681991:AAF7UZokmM8hfL4QwlYjndSllBefphgePfM"
);

class PingController extends TelegramBaseController {
  /**
   * @param {Scope} $
   */
  pingHandler($) {
    $.sendMessage("png");
  }

  get routes() {
    return {
      pingCommand: "pingHandler"
    };
  }
}

tg.router.when(new TextCommand("hello", "pingCommand"), new PingController());

tg.router
  .when(new TextCommand("/start", "startCommand"), new StartController())
  .when(new TextCommand("/stop", "stopCommand"), new StopController())
  .when(new TextCommand("/restart", "restartCommand"), new RestartController())
  .otherwise(new OtherwiseController());
