# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.path.abspath('../'))
from rqalpha import run_file

config = {
  "base": {
    "start_date": "2016-01-01",
    "end_date": "2017-12-01",
    "accounts": {
      "stock": 100000000
    },
    "benchmark": "HK_FUTURE.999010",
    "frequency": "1d",
    # 运行类型，`b` 为历史数据回测，`p` 为实时数据模拟交易, `r` 为实时数据实盘交易。
    "run_type":  "b",
  },
  "extra": {
    "log_level": "verbose",
  },
  "mod": {
    "sys_analyser": {
      "enabled": True,
      "plot": True
    },
    "sys_simulation":
    {
      'enabled': False,
    },
    "sys_stock_realtime":
    {
      'enabled': False,
    },
  }
}

#strategy_file_path = "./test_strategy.py"
strategy_file_path = "./strategy/macd.py"
#strategy_file_path = "./strategy/golden_cross.py"
#strategy_file_path = "./strategy/turtle.py"

run_file(strategy_file_path, config)
