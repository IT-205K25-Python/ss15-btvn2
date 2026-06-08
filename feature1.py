atm_vault_balance = 50000000
user_account_balance = 10000000

def display_balance():
    '''
    Display current account balance and ATM cash balance.

    Args:
        - None

    Returns:
        - None
    '''
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VNĐ")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VNĐ")

display_balance()

