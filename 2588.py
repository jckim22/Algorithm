# from sys import stdin
# num = list()
# for x in range(0,2):
#     num.append(int(stdin.readline()))
# print(num[0]*(num[1]%10))
# print(num[0]*(num[1]%100//10))
# print(num[0]*(num[1]//100))
# print(num[0]*num[1])
# a,b=int(input()),input()
# print(*[a*int(n) for n in b[::-1]],a*int(b))

def compound_interest(principal, interest_rate, years):
    # 복리 이자 계산 공식을 적용
    total_amount = principal * (1 + interest_rate)**years
    # 각 연도마다의 원금과 복리 이자 출력
    for year in range(1, years+1):
        amount = principal * (1 + interest_rate)**year
        interest = amount - principal
        print(f"Year {year}: Principal = {principal:.2f}, Interest = {interest:.2f}, Amount = {amount:.2f}")
    # 총액 반환
    return total_amount

# 예시
principal = 10000000 # 원금
interest_rate = 0.1 # 이자율 (10%)
years = 10 # 기간 (10년)
total_amount = compound_interest(principal, interest_rate, years)
print(f"Total amount after {years} years: {total_amount:.2f}")