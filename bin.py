#!/usr/bin/env python3

import os
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
from time import sleep

def print_account_balance():
    total=0
    for x in client.get_account()['balances']:
        if float(x['free'])>0:
            symb=str(x['asset'])+"USDT"
            price=0
            try:
                price=client.get_symbol_ticker(symbol=symb)['price']
            except:
                print(symb)
            amount=x['free']
            balance=float(str(x['free']))*float(str(price))
            total=total+balance
            token=x['asset']
            print(token+": "+amount+" $"+str(balance))
    print("total: "+str(total))


def btc_trade_history(msg):
    if msg['e'] != 'error':
        print(msg['c'])
        btc_price['last']=msg['c']
        btc_price['bid']=msg['b']
        btc_price['last']=msg['a']
    else:
        btc_price['error']=True

def token_ticker():
    bsm=BinanceSocketManager(client)
    conn_key=bsm.start_symbol_ticker_socket('BTCUSDT', btc_trade_history)
    bsm.start()
    sleep(5)
    bsm.stop_socket(conn_key)
    reactor.stop()

if __name__=="__main__":
    api_key=os.environ.get('binance_api')
    api_secret=os.environ.get('binance_secret')

    client=Client(api_key,api_secret)
    btc_price={'error':False}

    #print_account_balance()
    token_ticker()
