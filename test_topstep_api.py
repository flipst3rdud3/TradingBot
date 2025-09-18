from topstep_api import get_active_accounts

if __name__ == "__main__":
    accounts = get_active_accounts()
    print("Accounts response:", accounts)
