# 붕어빵 재고  데이터 생성
stock = {
  "팥붕어빵" : 10,
  "슈크림붕어빵": 8,
  "초코붕어빵": 5
}

# 1. 한번에 맛과 개수 받기
# 2. map함수를 이용해서 bread_count 코드를 개선하는 것

order = {}
bread_type = input("주문할 붕어빵 종류를 입력하세요: (팥붕어빵, 슈크림붕어빵, 초코붕어빵 중 한가지를 골라주세요")
bread_count = int(input("주문할 붕어빵 개수를 입력하세요: "))

order[bread_type] = bread_count # ["팥붕어빵"] = 10
print(f"주문 내역 : {order}")

print("----------------------------------")
#len(stock) = 함수, stock.items() = 메소드
for bread, quantity in stock.items():
  print(f"{bread} : {quantity}")