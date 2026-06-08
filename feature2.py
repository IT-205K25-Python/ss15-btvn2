atm_vault_balance = 50000000
user_account_balance = 10000000

def deposit_money(amount):
    global atm_vault_balance
    global user_account_balance
    
    atm_vault_balance += amount
    user_account_balance += amount
    
    print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,}")
    return True

amount_recharge = None
while True:
    try:
        amount_recharge = int(input("Nhập số tiền muốn nạp: "))
    except ValueError:
        print("Số tiền nhập vào không hợp lệ vui lòng nhập lại")
    else:
        if amount_recharge > 0:
            break
        print("Số tiền nạp phải lớn hơn 0")

deposit_money(amount_recharge)
