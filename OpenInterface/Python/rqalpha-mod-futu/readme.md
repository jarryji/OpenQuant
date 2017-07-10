# rqalpha_mod_futu安装步骤
**1. 安装python3.5**

下载[Anaconda](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-4.2.0-Windows-x86_64.exe)，并安装。

**2. 安装rqalpha_develop**

在命令行中输入如下命令，这里需要安装的是rqalpha的develop分支。

```
pip install git+https://github.com/ricequant/rqalpha.git@develop
```

**3. 安装futu_api**

在命令行中输入如下命令。

```
git clone https://github.com/FutunnOpen/OpenQuant.git
cd OpenQuant
git checkout futu_rqalpha #切换到futu_rqalpha分支
```

根据[富途牛牛行情交易API入门指引](https://github.com/FutunnOpen/OpenQuant/blob/master/OpenInterface/Python/%E5%85%A5%E9%97%A8%E6%8C%87%E5%BC%95%E5%8F%8A%E6%8E%A5%E5%8F%A3%E6%96%87%E6%A1%A3/%E5%AF%8C%E9%80%94%E7%89%9B%E7%89%9B%E8%A1%8C%E6%83%85%E4%BA%A4%E6%98%93API%E5%85%A5%E9%97%A8%E6%8C%87%E5%BC%95.md)的指引，搭建富途API环境。

**4. 安装futu_mod**

在OpenQuant\OpenInterface\Python\rqalpha-mod-futu文件夹下打开命令行，输入以下命令。
```
rqalpha mod install -e . #此命令会扫描当前目录下的setup.py文件，执行安装
rqalpha mod list #查看当前有哪些mod,如果安装成功，应该会看到futu的mod
rqalpha mod enable futu #开户futu的mod
rqalpha mod disable sys_simulation # 关闭sys_simulation
```

**5. 开始编写策略**
```
cd OpenInterface\Python\rqalpha-mod-futu\rqalpha_mod_futu
```

在strategy文件夹中编写你自己的策略文件mystrategy.py。修改debug_run_file.py中的配置如下。


```
# -*- coding: utf-8 -*-

from rqalpha import run_file

config = {
  "base": {
  ... #这部分不用改，按照原来的配置即可
    "run_type": "b", #设为回测
  },
  ... #这部分不用改，按照原来的配置即可
}

strategy_file_path = "./strategy/mystrategy.py" # 设置策略文件

run_file(strategy_file_path, config)
```

然后运行debug_run_file.py文件即可。

关于如何编写你的mystrategy.py，请参考[文档](http://rqalpha.readthedocs.io/zh_CN/latest/intro/overview.html)。


**使用说明**
* 目前暂时只支持日K级别的回测
* 港股下单不支持市价单，只支持限价单
* 历史数据需要用户本地下载，历史K线下载指引参见(https://github.com/FutunnOpen/OpenQuant/blob/master/OpenInterface/Python)的入门指引及接口文档
