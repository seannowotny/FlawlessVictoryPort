# Flawless Victory

###### The 'Flawless Victory' strategy code is based on this [TV strategy](https://www.tradingview.com/u/Bunghole/)
###### Author of the original Pinescript strategy: [Robert Roman](https://github.com/TreborNamor)

## Go-To Commands:

For Downloading Data:

```properties
docker-compose run --rm freqtrade download-data -t 15m -c ./user_data/config.json -c ./user_data/config-private.json --timerange 20200210-20210210
```

For Back Testing:

```properties
docker-compose run --rm freqtrade backtesting --fee 0.005 --strategy-list FlawlessVictoryV1 -c ./user_data/config.json -c ./user_data/config-private.json --timerange 20200210-20210210 --export EXPORT
```

For Plotting

```properties
docker-compose run --rm freqtrade plot-dataframe -s FlawlessVictoryV1 -p BTC/USDT -c ./user_data/config.json -c ./user_data/config-private.json
```

For Hyper Opting

```properties
docker-compose run --rm freqtrade hyperopt --spaces all --hyperopt-loss SortinoHyperOptLoss -s FlawlessVictoryV1 -e 1000 -c ./user_data/config.json -c ./user_data/config-private.json
```

```properties
docker-compose run --rm freqtrade hyperopt-show --hyperopt-filename hyperopt_results_2021-02-27_13-07-20.pickle -c ./user_data/config.json -c ./user_data/config-private.json 
```
