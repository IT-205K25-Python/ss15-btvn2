atm_vault_balance = 50000000
user_account_balance = 10000000


def display_balance():
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VNĐ")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VNĐ")


def deposit_money(amount):
    global atm_vault_balance
    global user_account_balance
    
    atm_vault_balance += amount
    user_account_balance += amount
    
    print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,}")
    return True


def check_withdrawal_rules(amount):
    fee = 1100
    total_deduction = amount + fee
    
    if(amount % 50000 != 0):
        return total_deduction, "INVALID_MULTIPLE"
    if(total_deduction > user_account_balance):
        return total_deduction, "INSUFFICIENT_FUNDS"
    if(amount > atm_vault_balance):
        return total_deduction, "ATM_OUT_OF_CASH"
    return total_deduction, "OK"

def execute_withdrawal(total_deduction, amount_to_dispense):
    global user_account_balance
    global atm_vault_balance

    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense
    print("Giao dịch đang xử lý ...")
    print("Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,}")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,}")

def main():
    while True:
        print('''
============= SMART ATM =============
1. Xem số dư
2. Nạp tiền
3. Rút tiền
4. Kết thúc giao dịch
=====================================
Vui lòng chọn giao dịch (1-4):
              ''')

        choice = input("Nhập lựa chọn của người dùng: ")

        match choice:
            case '1':
                display_balance()
            case '2':
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
            case '3':               
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

            case '4':
                print("Cảm ơn quý khách đã sử dụng dịch vụ!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng nhập lại")

if __name__ == "__main__":
    main()
