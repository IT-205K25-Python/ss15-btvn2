atm_vault_balance = 50000000
user_account_balance = 10000000

def check_withdrawal_rules(amount):
    '''
    Validate withdrawal request and calculate total deduction.

    Args:
        - amount: int
            Amount of money the user wants to withdraw.

    Returns:
        - tuple
            (total_deduction, status)

        Status:
        - "INVALID_MULTIPLE"
        - "INSUFFICIENT_FUNDS"
        - "ATM_OUT_OF_CASH"
        - "OK"
    '''
    fee = 1100
    total_deduction = amount + fee
    
    if(total_deduction < user_account_balance):
        return total_deduction, "INSUFFICIENT_FUNDS"
    if(total_deduction > atm_vault_balance):
        return total_deduction, "ATM_OUT_OF_CASH"
    if(amount % 50000 != 0):
        return total_deduction, "INVALID_MULTIPLE"
    return total_deduction, "OK"

def execute_withdrawal(total_deduction, amount_to_dispense):
    '''
    Execute withdrawal transaction and update balances.

    Args:
        - total_deduction: int
            Total amount deducted from user account.

        - amount_to_dispense: int
            Actual cash amount dispensed from ATM.

    Returns:
        - None
    '''
    global user_account_balance
    global atm_vault_balance


    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense
    print("Giao dịch đang xử lý ...")
    print("Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,}")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,}")


amount_width_draw_money = None

while True:
    try:
        amount_width_draw_money = int(input("Nhập số tiền cần rút: "))
    except ValueError:
        print("Không hợp lệ. Vui lòng nhập lại")
    else:
        if amount_width_draw_money > 0:
            break
        print("Số tiền rút phải lớn hơn 0")


total_deduction, msg = check_withdrawal_rules(amount_width_draw_money)
if(msg == "INSUFFICIENT_FUNDS"):
    print("Tài khoản quý khách không đủ tiền để rút")
elif(msg == "ATM_OUT_OF_CASH"):
    print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ")
elif(msg == "INVALID_MULTIPLE"):
    print("Số tiền rút phải là bội số của 50,000")
else:
    execute_withdrawal(total_deduction, amount_width_draw_money)
