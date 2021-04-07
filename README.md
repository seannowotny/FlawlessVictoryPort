# Flawless Victory

## Getting Started

```docker-compose run --rm freqtrade create-userdir --userdir user_data```

```docker-compose run --rm freqtrade new-config --config user_data/config.json```

## Commands

#### Download Data
```docker-compose run --rm freqtrade download-data -t 15m -c ./user_data/config.json -c ./user_data/config-private.json --timerange 20200210-20210210```

#### Backtest
```docker-compose run --rm freqtrade backtesting --fee 0.005 --strategy-list FlawlessVictory -c ./user_data/config.json -c ./user_data/config-private.json --timerange 20200210-20210210 --export EXPORT```

#### Plot
```docker-compose run --rm freqtrade plot-dataframe -s FlawlessVictory -p BTC/USDT -c ./user_data/config.json -c ./user_data/config-private.json```

#### Hyperopt
```docker-compose run --rm freqtrade new-hyperopt --hyperopt FlawlessVictoryOPT  -c ./user_data/config.json -c ./user_data/config-private.json```

```docker-compose run --rm freqtrade hyperopt --spaces all --hyperopt FlawlessVictoryOPT --hyperopt-loss SortinoHyperOptLoss -s FlawlessVictory -e 1000 -c ./user_data/config.json -c ./user_data/config-private.json```

```docker-compose run --rm freqtrade hyperopt-show --hyperopt-filename hyperopt_results_2021-02-27_13-07-20.pickle -c ./user_data/config.json -c ./user_data/config-private.json ```

#### Trade
```docker-compose run --rm freqtrade trade -s FlawlessVictory -c ./user_data/config.json -c ./user_data/config-private.json```

#### Docker
```docker-compose pull```?

```docker-compose up --build --force-recreate```?

## Things to Remember

###### Delete .pickle files for strategy if it or related files were changed or they will be used for future hyper-opting!

## How to move into production

- set dry_run to false
- set bid_strategy.use_order_book to true
- set bid_strategy.ask_last_balance to 1.0


