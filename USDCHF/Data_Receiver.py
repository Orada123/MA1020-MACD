from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
import json
from urllib3.exceptions import MaxRetryError
from requests.exceptions import SSLError
import time

# Global list
global TI

def main_job():
    global data_EMA_10, data_EMA_20, data_MACD, data_BBands, data_Price

    API_key = '5LDF8BV8UHC3F4Y7'
    TI = TechIndicators(key=API_key, output_format='json')
    TS = TimeSeries(key=API_key, output_format='json')

    Stop_1 = True
    while Stop_1:
        try:
            symbol = 'USDCHF'
            interval = '5min'
            slowperiod = '26'
            signalperiod = '9'
            fastperiod = '12'
            series_type = 'close'
            time_period = '20'
            outputsize = "compact"

            data_Price, meta_data_Price = TS.get_intraday(symbol=symbol, interval=interval, outputsize=outputsize)

            data_BBands, meta_data_BBands = TI.get_bbands(symbol=symbol, interval=interval, time_period=time_period
                                                          , series_type=series_type)
            time_period = '10'
            data_EMA_10, meta_data_EMA_50 = TI.get_ema(symbol=symbol, interval=interval, time_period=time_period
                                                       , series_type=series_type)

            time_period = '20'
            data_EMA_20, meta_data_EMA_200 = TI.get_ema(symbol=symbol, interval=interval, time_period=time_period
                                                         , series_type=series_type)

            data_MACD, meta_data_MACD = TI.get_macd(symbol=symbol, interval=interval, series_type=series_type,
                                                    fastperiod=fastperiod, slowperiod=slowperiod,
                                                    signalperiod=signalperiod)

            Stop_1 = False
        except (UnboundLocalError, ValueError, MaxRetryError, ConnectionError, SSLError) as e:
            print(e)
            time.sleep(60)
            pass

    # print(data_EMA_10)
    # print(data_EMA_20)


    # Retrieve EMA 10 and EMA 20 data
    """EMA 10"""
    EMA_10 = list(data_EMA_10.values())

    """Current ema 10"""
    level = EMA_10[0].values()
    current_ema_10 = (float([x for x in level][0]))

    """Previous ema 10"""
    level = EMA_10[1].values()
    previous_ema_10 = (float([x for x in level][0]))

    """EMA 20"""
    EMA_20= list(data_EMA_20.values())

    """Current ema 20"""
    level = EMA_20[0].values()
    current_ema_20 = (float([x for x in level][0]))

    """Previous ema 20"""
    level = EMA_20[1].values()
    previous_ema_20 = (float([x for x in level][0]))

    # Check for crossover between EMA 10 and EMA 20

    current_diff = current_ema_10 - current_ema_20
    prev_diff = previous_ema_10 - previous_ema_20

    file_name = 'Crossing_Flags_EMA.json'

    with open(file_name) as f_obj:
        data = f_obj.read()
        retrieve = json.loads(data)

    Prev_Cross_Up = retrieve['Cross_Up']
    Prev_Cross_Down = retrieve['Cross_Down']

    Crossing_Flag = {}

    if current_diff >= 0 > prev_diff:
        Crossing_Flag['Cross_Up'] = Prev_Cross_Up
        Crossing_Flag['Cross_Down'] = True
    elif current_diff <= 0 < prev_diff:
        Crossing_Flag['Cross_Up'] = True
        Crossing_Flag['Cross_Down'] = Prev_Cross_Down
    else:
        Crossing_Flag['Cross_Up'] = Prev_Cross_Up
        Crossing_Flag['Cross_Down'] = Prev_Cross_Down

    # Update the Crossing flag folder
    file_name = "Crossing_Flags_EMA.json"

    with open(file_name, "w") as f_obj:
        json.dump(Crossing_Flag, f_obj)

    # Retrieve MACD data
    """MACD"""
    MACD = list(data_MACD.values())
    current_Hist = float(MACD[0]['MACD_Hist'])
    prev_Hist = float(MACD[1]['MACD_Hist'])

    file_name = 'Crossing_Flags_MACD.json'

    with open(file_name) as f_obj:
        data = f_obj.read()
        retrieve = json.loads(data)

    Prev_Cross_Up = retrieve['Cross_Up']
    Prev_Cross_Down = retrieve['Cross_Down']

    Crossing_Flag = {}

    if prev_Hist > 0 > current_Hist:
        Crossing_Flag['Cross_Up'] = Prev_Cross_Up
        Crossing_Flag['Cross_Down'] = True
    elif prev_Hist < 0 < current_Hist:
        Crossing_Flag['Cross_Up'] = True
        Crossing_Flag['Cross_Down'] = Prev_Cross_Down
    else:
        Crossing_Flag['Cross_Up'] = Prev_Cross_Up
        Crossing_Flag['Cross_Down'] = Prev_Cross_Down

    file_name = "Crossing_Flags_MACD.json"

    with open(file_name, "w") as f_obj:
        json.dump(Crossing_Flag, f_obj)

    # Retrieve crossing data for EMA and MACD
    file_name = 'Crossing_Flags_MACD.json'

    with open(file_name) as f_obj:
        data = f_obj.read()
        retrieve = json.loads(data)

    MACD_Up = retrieve['Cross_Up']
    MACD_Down = retrieve['Cross_Down']

    file_name = 'Crossing_Flags_EMA.json'

    with open(file_name) as f_obj:
        data = f_obj.read()
        retrieve = json.loads(data)

    EMA_Up = retrieve['Cross_Up']
    EMA_Down = retrieve['Cross_Down']

    # Retrieve price and bollinger band data
    BBands = list(data_BBands.values())
    middle_band = float(BBands[0]['Real Middle Band'])

    Price = list(data_Price.values())
    Price = float(Price[0]['4. close'])

    Trigger_Flags = {}

    if MACD_Up and EMA_Up:
        if Price < middle_band:
            Buy_flag = True
            Sell_flag = False
        else:
            Buy_flag = False
            Sell_flag = False
    elif MACD_Down and EMA_Down:
        if Price > middle_band:
            Buy_flag = False
            Sell_flag = True
        else:
            Buy_flag = False
            Sell_flag = False
    else:
        Buy_flag = False
        Sell_flag = False

    Trigger_Flags["Buy_flag"] = Buy_flag
    Trigger_Flags["Sell_flag"] = Sell_flag

    file_name = "Trigger_Flags.json"
    with open(file_name, "w") as f_obj:
        json.dump(Trigger_Flags, f_obj)

