"use strict";

const Telegram = require("telegram-node-bot");
const TelegramBaseController = Telegram.TelegramBaseController;
const TextCommand = Telegram.TextCommand;
const tg = new Telegram.Telegram(
  "686681991:AAF7UZokmM8hfL4QwlYjndSllBefphgePfM",
  {
    workers: 1
  }
);

class StartController extends TelegramBaseController {
  /**
   * @param {Scope} $
   */
  startHandler($) {
    $.sendMessage("the user has been added");
  }

  get routes() {
    return {
      startCommand: "startHandler"
    };
  }
}
class StopController extends TelegramBaseController {
  /**
   * @param {Scope} $
   */
  stopHandler($) {
    $.sendMessage("The actions has been cancelled");
  }

  get routes() {
    return {
      stopCommand: "stopHandler"
    };
  }
}

class OtherwiseController extends TelegramBaseController {
  handle() {
    console.log("otherwise");
  }
}

tg.router
  .when(new TextCommand("/start", "startCommand"), new StartController())
  .when(new TextCommand("/stop", "stopCommand"), new StopController())
  .otherwise(new OtherwiseController());

