import yfinance as yf
import datetime
from pytz import timezone


def cpng_price():
    # 타겟 주식 심볼
    coupang_sym = "CPNG"

    # 현재가, 일주일 전 가격, 40일 전 가격 파싱
    current = datetime.datetime.now(timezone('Asia/Seoul'))
    week_ago = current - datetime.timedelta(weeks=1)
    month_ago = current - datetime.timedelta(days=40)

    str_weak_ago = str(week_ago).split(" ")[0]
    str_month_ago = str(month_ago).split(" ")[0]


    # 가격 정보 다운로드 (현재 ~ 40일 전)
    stock_data = yf.download(coupang_sym, start=month_ago, end=current)

    # Convert the index to datetime.date for comparison
    stock_data['Date'] = stock_data.index.date

    # 크롤링 데이터 파싱
    now_price = stock_data['Close'][-1]
    week_ago_price = stock_data['Close'].loc[str_weak_ago]
    month_ago_price = stock_data['Close'].loc[str_month_ago]
    price_dict = {
        'current_price': now_price,
        'week_ago_price': week_ago_price,
        'month_ago_price': month_ago_price
    }

    return price_dict