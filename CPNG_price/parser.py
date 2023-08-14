import math
import random
from currency_converter import CurrencyConverter

def calculator(data):
    current_price = int(data['current_price'])
    week_ago_price = int(data['week_ago_price'])
    month_ago_price = int(data['month_ago_price'])

    # 달러 > 원 변환
    c = CurrencyConverter()
    kst_current_price = math.trunc(c.convert(current_price, 'USD', 'KRW'))
    kst_week_ago_price = math.trunc(c.convert(week_ago_price, 'USD', 'KRW'))
    kst_month_ago_price = math.trunc(c.convert(month_ago_price, 'USD', 'KRW'))

    float_week_rate = ((kst_current_price - kst_week_ago_price) / abs(kst_week_ago_price)) * 100
    week_rate = int(float_week_rate)
    float_month_rate = ((kst_current_price - kst_month_ago_price) / abs(kst_month_ago_price)) * 100
    month_rate = int(float_month_rate)

    krw_dict = {
        'current_price': kst_current_price,
        'week_price': kst_week_ago_price,
        'month_price': kst_month_ago_price,
        'week_rate': week_rate,
        'month_rate': month_rate
    }

    return krw_dict


def msg_template(data):
    krw_dict = calculator(data)
    current_price = krw_dict['current_price']
    week_ago_price = krw_dict['week_price']
    month_ago_price = krw_dict['month_price']
    weak_rate = krw_dict['week_rate']
    month_rate = krw_dict['month_rate']

    if current_price >= week_ago_price and current_price >= month_ago_price:
        message = f"영섭이의 쿠팡 가격을 전달드려요!\n 현재 가격은 **{current_price}원** 입니다 :grinning:" \
                  f"\n 일주일 전 가격인 **{week_ago_price}원**에 비해 **약 {weak_rate}%** 올랐네요" \
                  f"\n 심지어 한달 전 가격인 **{month_ago_price}원**에 비해서도 **약 {month_rate}%** 올랐어요 :rage:" \
                  f"\n 개빡치지만 전체적으로 우하향이 예상되며," \
                  f"\n 골드만삭스, 워렌 버핏, 복제성, 랄로, 박정민 등 우수한 트레이더와 최신 인공지능의 5년 뒤 쿠팡 예상 가격은..." \
                  f"\n **{random.randint(0, 1000)}원** 입니다 :wink:"
        return message

    elif current_price >= week_ago_price and current_price <= month_ago_price:
        message = f"영섭이의 쿠팡 가격을 전달드려요!\n 현재 가격은 **{current_price}원** 입니다 :grinning:" \
                  f"\n 좋은 소식은 한달 전 가격인 **{month_ago_price}원**에 비해 **약 {month_rate}%** 떡락했어요 :blush:" \
                  f"\n 나쁜 소식은 일주일 전 가격인 **{week_ago_price}원**에 비해 **약 {weak_rate}%** 올랐네요 :rage:" \
                  f"\n 전체적으로 우하향이 예상되며," \
                  f"\n 골드만삭스, 워렌 버핏, 복제성, 랄로, 박정민 등 우수한 트레이더와 최신 인공지능의 5년 뒤 쿠팡 예상 가격은..." \
                  f"\n **{random.randint(0, 1000)}원** 입니다 :wink:"
        return message

    elif current_price <= week_ago_price and current_price >= month_ago_price:
        message = f"영섭이의 쿠팡 가격을 전달드려요!\n 현재 가격은 **{current_price}원** 입니다 :grinning:" \
                  f"\n 좋은 소식은 일주일 전 가격인 **{week_ago_price}원**에 비해 **약 {weak_rate}%** 개떡락했어요 :blush:" \
                  f"\n 나쁜 소식은 아직도 한달 전 가격인 **{month_ago_price}원**에 비해 **약 {month_rate}%**정도 오른 상태네요 :rage:" \
                  f"\n 전체적으로 우하향이 예상되며," \
                  f"\n 골드만삭스, 워렌 버핏, 복제성, 랄로, 박정민 등 우수한 트레이더와 최신 인공지능의 5년 뒤 쿠팡 예상 가격은..." \
                  f"\n **{random.randint(0, 1000)}원** 입니다 :wink:"
        return message

    elif current_price <= week_ago_price and current_price <= month_ago_price:
        message = f"영섭이의 쿠팡 가격을 전달드려요!\n 현재 가격은 **{current_price}원** 입니다 :grinning:" \
                  f"\n ㅋㅋ 웃고 시작할게요 ㅋㅋ" \
                  f"\n 일주일 전 가격인 **{week_ago_price}원**에 비해 **{weak_rate}%** 떡락했구요" \
                  f"\n 심지어 한달 전 가격인 **{month_ago_price}원**에 비해서도 **{month_rate}%** 개같이 떡락했네요 :blush:" \
                  f"\n 지금처럼 전체적으로 우하향이 예상되며 ㅋㅋ," \
                  f"\n 골드만삭스, 워렌 버핏, 복제성, 랄로, 박정민 등 우수한 트레이더와 최신 인공지능의 5년 뒤 쿠팡 예상 가격은..." \
                  f"\n **{random.randint(0, 1000)}원** 입니다 :wink:"
        return message


def only_mention_msg_template():
    message = "제 기능은 다음과 같아요!" \
              "\n 매일 오전 9시, 오후 9시 쿠팡 주가를 안내해드려요 :blush:" \
              "\n 저를 멘션해주시고, **쿠팡**이 포함된 단어를 입력해주시면 답변을 드려요!" \
              "\n 한달 전, 일주일 전, 현재가를 기반으로 다양한 답변이 준비되어 있어요." \
              "\n 인류 사상 최강개발자 **갓종원**님께서 제작한 봇이니 확실한 정보만 알려드려요. :wink:"
    return message