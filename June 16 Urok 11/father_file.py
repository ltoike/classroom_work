from kassa import Kassa
from person import Person
from ticket import Ticket
from train import Train          

test_man = Person("Ilon Mask", 55)
test_man.earn(27000)
test_man.pay(11111)
test_man.show()


kassa = Kassa()
price = kassa.get_price("Алматы", "Ош")
kassa.buy_ticket("Алматы", "Сантьяго", test_man)


if test_man.ticket:
    test_man.ticket.show()

train = Train("Алматы", "Сантьяго")
train.show()

train.board(test_man)
if test_man.ticket is None:
    print("Битти билет")
