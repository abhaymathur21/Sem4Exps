class Account {
    String cust_name, acc_no;

    public Account(String name, String acc) {
        cust_name = name;
        acc_no = acc;
    }

}

class SavingsAccount extends Account {
    double min_balance, saving_bal;

    public SavingsAccount(String name, String acc, double min, double bal) {
        super(name, acc);
        min_balance = min;
        saving_bal = bal;
    }
}

class AccountDetails extends SavingsAccount {

    public AccountDetails(String name, String acc, double min, double bal) {
        super(name, acc, min, bal);
    }

    public void deposit(double amt) {
        saving_bal += amt;
        System.out.println("Deposit: " + amt);
        System.out.println("New Balance: " + saving_bal);
    }

    public void withdraw(double amt) {
        if (saving_bal - amt < min_balance)
            System.out.println("Insufficient Balance!");
        else {
            saving_bal -= amt;
            System.out.println("Withdraw: " + amt);
            System.out.println("New Balance: " + saving_bal);
        }

    }
}

public class Bank {
    public static void main(String[] args) {
        AccountDetails acc = new AccountDetails("Abhay", "60017210016", 500, 1000);
        System.out.println("Balance: " + acc.saving_bal);
        acc.deposit(200);
        acc.withdraw(500);
        acc.withdraw(400);
    }
}
