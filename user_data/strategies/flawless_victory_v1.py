# pragma pylint: disable=missing-docstring, invalid-name, pointless-string-statement
# flake8: noqa: F401
# isort: skip_file
# --- Do not remove these libs ---
import numpy as np  # noqa
import pandas as pd  # noqa
from pandas import DataFrame

from freqtrade.strategy import IStrategy

# --------------------------------
# Add your lib to import here
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib


# This strategy is based on https://www.tradingview.com/script/i3Uc79fF-Flawless-Victory-Strategy-15min-BTC-Machine-Learning-Strategy/
# Author of the original Pinescript strategy: Robert Roman (https://github.com/TreborNamor)
class FlawlessVictoryV1(IStrategy):  # (V1)
    # Strategy interface version - allow new iterations of the strategy interface.
    # Check the documentation or the Sample strategy to get the latest version.
    INTERFACE_VERSION = 2

    stoploss = -999999

    # Optimal timeframe for the strategy.
    timeframe = '15m'

    # Run "populate_indicators()" only for new candle.
    process_only_new_candles = False

    # These values can be overridden in the "ask_strategy" section in the config.
    use_sell_signal = True
    sell_profit_only = False
    ignore_roi_if_buy_signal = False

    # Number of candles the strategy requires before producing valid signals
    startup_candle_count: int = 50

    # Optional order type mapping.
    order_types = {
        'buy': 'limit',
        'sell': 'limit',
        'stoploss': 'market',
        'stoploss_on_exchange': False
    }

    # Optional order time in force.
    order_time_in_force = {
        'buy': 'gtc',
        'sell': 'gtc'
    }

    plot_config = {
        'main_plot': {
            'bb_upperband': {'color': 'blue'},
            'bb_lowerband': {'color': 'blue'}
        },
        'subplots': {
            "MFI": {
                'mfi': {'color': 'green'},
            },
            "RSI": {
                'rsi': {'color': 'purple'},
                'rsi_lower': {'color': 'black'},
                'rsi_upper': {'color': 'black'}
            }
        }
    }

    def informative_pairs(self):
        return []

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['rsi'] = ta.RSI(dataframe['close'], 14)  # TODO: Hyperopt
        dataframe['mfi'] = ta.MFI(dataframe['high'], dataframe['low'], dataframe['close'], dataframe['volume'],
                                  14)  # TODO: Hyperopt

        bollinger = qtpylib.bollinger_bands(dataframe['close'], window=20, stds=1)  # TODO: Hyperopt
        dataframe['bb_upperband'] = bollinger['upper']
        dataframe['bb_lowerband'] = bollinger['lower']

        dataframe['rsi_lower'] = 43  # TODO: Hyperopt
        dataframe['rsi_upper'] = 70  # TODO: Hyperopt

        bb_long = dataframe['close'] < dataframe['bb_lowerband']
        rsi_long = dataframe['rsi'] > dataframe['rsi_lower']

        bb_short = dataframe['close'] > dataframe['bb_upperband']
        rsi_short = dataframe['rsi'] > dataframe['rsi_upper']

        dataframe['long'] = bb_long & rsi_long
        dataframe['short'] = bb_short & rsi_short

        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['buy'] = dataframe['long']
        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe['sell'] = dataframe['short']
        return dataframe
