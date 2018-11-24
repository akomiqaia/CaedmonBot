'use strict'
 
const Telegram = require('telegram-node-bot')
const TelegramBaseController = Telegram.TelegramBaseController
const TextCommand = Telegram.TextCommand
const tg = new Telegram.Telegram('686681991:AAF7UZokmM8hfL4QwlYjndSllBefphgePfM')
 
class PingController extends TelegramBaseController {
    /**
     * @param {Scope} $ 
     */
    pingHandler($) {
        $.sendMessage('pong')
    }
 
    get routes() {
        return {
            'pingCommand': 'pingHandler'
        }
    }
}
 
tg.router
    .when(
        new TextCommand('ping', 'pingCommand'),
        new PingController()
    )