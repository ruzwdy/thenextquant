# -*- coding:utf-8 -*-

"""
Order object.

Author: HuangTao
Date:   2018/05/14
Email:  huangtao@ifclover.com
"""

from quant.utils import tools


# Order type.
ORDER_TYPE_LIMIT = "LIMIT"  # Limit order.
ORDER_TYPE_MARKET = "MARKET"  # Market order.

# Order direction.
ORDER_ACTION_BUY = "BUY"  # Buy
ORDER_ACTION_SELL = "SELL"  # Sell

# Order status.
ORDER_STATUS_NONE = "NONE"  # New created order, no status.
ORDER_STATUS_SUBMITTED = "SUBMITTED"  # The order that submitted to server successfully.
ORDER_STATUS_PARTIAL_FILLED = "PARTIAL-FILLED"  # The order that filled partially.
ORDER_STATUS_FILLED = "FILLED"  # The order that filled fully.
ORDER_STATUS_CANCELED = "CANCELED"  # The order that canceled.
ORDER_STATUS_FAILED = "FAILED"  # The order that failed.

# Future order trade type.
TRADE_TYPE_NONE = 0  # Unknown type, some Exchange's order information couldn't known the type of trade.
TRADE_TYPE_BUY_OPEN = 1  # Buy open, action = BUY & quantity > 0.
TRADE_TYPE_SELL_OPEN = 2  # Sell open, action = SELL & quantity < 0.
TRADE_TYPE_SELL_CLOSE = 3  # Sell close, action = SELL & quantity > 0.
TRADE_TYPE_BUY_CLOSE = 4  # Buy close, action = BUY & quantity < 0.


class Order:
    """ Order object.

    Attributes:
        account: Trading account name, e.g. test@gmail.com.
        platform: Exchange platform name, e.g. binance/bitmex.
        strategy: Strategy name, e.g. my_test_strategy.
        order_no: order id.
        symbol: Trading pair name, e.g. ETH/BTC.
        action: Trading side, BUY/SELL.
        price: Order price.
        quantity: Order quantity.
        remain: Remain quantity that not filled.
        status: Order status.
        avg_price: Average price that filled.
        order_type: Order type.
        trade_type: Trade type, only for future order.
        ctime: Order create time, microsecond.
        utime: Order update time, microsecond.
    """

    def __init__(self, account=None, platform=None, strategy=None, order_no=None, symbol=None, action=None, price=0,
                 quantity=0, remain=0, status=ORDER_STATUS_NONE, avg_price=0, order_type=ORDER_TYPE_LIMIT,
                 trade_type=TRADE_TYPE_NONE, ctime=None, utime=None):
        self.platform = platform
        self.account = account
        self.strategy = strategy
        self.order_no = order_no
        self.action = action
        self.order_type = order_type
        self.symbol = symbol
        self.price = price
        self.quantity = quantity
        self.remain = remain if remain else quantity
        self.status = status
        self.avg_price = avg_price
        self.trade_type = trade_type
        self.ctime = ctime if ctime else tools.get_cur_timestamp_ms()
        self.utime = utime if utime else tools.get_cur_timestamp_ms()

    def __str__(self):
        info = "[platform: {platform}, account: {account}, strategy: {strategy}, order_no: {order_no}, " \
               "action: {action}, symbol: {symbol}, price: {price}, quantity: {quantity}, remain: {remain}, " \
               "status: {status}, avg_price: {avg_price}, order_type: {order_type}, trade_type: {trade_type}, " \
               "ctime: {ctime}, utime: {utime}]".format(
            platform=self.platform, account=self.account, strategy=self.strategy, order_no=self.order_no,
            action=self.action, symbol=self.symbol, price=self.price, quantity=self.quantity,
            remain=self.remain, status=self.status, avg_price=self.avg_price, order_type=self.order_type,
            trade_type=self.trade_type, ctime=self.ctime, utime=self.utime)
        return info

    def __repr__(self):
        return str(self)
