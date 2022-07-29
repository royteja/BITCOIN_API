 import pandas as pd 


import smtplib
import websocket
import datetime

def on_message(ws, message):
    print()
    print(str(datetime.datetime.now()) + ": ")
    print(message)

def on_error(ws, error):
    print(error)

def on_close(close_msg):
    print("### closed ###" + close_msg)

def streamKline(currency, interval):
    websocket.enableTrace(False)
    socket = f'wss://stream.binance.com:9443/ws/{currency}@kline_{interval}'
    ws = websocket.WebSocketApp(socket,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()

data, meta_data=streamKline('bitcoin', '1m')
sender_email = "youremail@email.com" 
rec_email = "receivingemail@email.com" 
password = ("password") 
message = " The coin prize is at above price you set " + "%.6f" % last_price 
target_sell_price = 33000 
if last_price > target_sell_price:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password) 
    print("Login Success")
    server.sendmail(sender_email, rec_email, message)
    print("Email was sent")
