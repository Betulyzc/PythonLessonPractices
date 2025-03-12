"""
** BankaHesabi isminde bir sınıf tanımlayınız.
** Üretilen her bir nesne "hesapSahibi" isminde biz özelliğe sahip olmalıdır. BankaHesabi("Sadık Turan")
** Üretilen her bir nesne "bakiye" isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır.
** Üretilen her bir nesne için "paraYatir" metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp bakiye
   üzerine ekleyin ve bakiye miktarını geriye döndürün.
** Üretilen her bir nesne için "paraCek" metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp bakiye
   değerinden çıkarıp geriye döndürün.

    hesap = BankaHesabi("Sadık Turan")
    hesap.hesapSahibi => Sadık Turan
    hesap.bakiye => 0.0
    hesap.paraYatir(1000) => 1000.0
    hesap.paraCek(500) => 500.0
"""

class BankAccount:
    def __init__(self, accountOwner):
        self.accountOwner=accountOwner
        self.balance=0.0
    
    def depositMoney(self,amountDeposit):
        self.balance+=amountDeposit
        return self.balance
    
    def withdrawMoney(self,amountWithdraw):
        self.balance-=amountWithdraw
        return self.balance

    def balanceInquiry(self):
        return self.balance


account=BankAccount("Betül Yazıcı")
print(account.balanceInquiry())

account.depositMoney(1000)
print(account.balanceInquiry())

account.withdrawMoney(500)
print(account.balanceInquiry())

