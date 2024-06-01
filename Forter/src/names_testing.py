import unittest
from count_unique_names import countUniqueNames,change_max_typos
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.billFirstName = "John"
        self.billLastName = "Doe"
        self.shipFirstName = "John"
        self.shipLastName = "Doe"
        self.billNameOnCard = "John Doe"

    def test_nickname(self):
        self.shipFirstName = "Johnny"
        self.assertEqual(countUniqueNames(self.billFirstName, self.billLastName, self.shipFirstName, self.shipLastName, self.billNameOnCard), 1)

    def test_two_different_nicknames(self):
        self.shipFirstName = "Dick" #dick is a nickname of richard
        self.billFirstName = "Rich" #rich is a nickname of richard
        self.billNameOnCard = "Richard Doe"
        self.assertEqual(countUniqueNames(self.billFirstName, self.billLastName, self.shipFirstName, self.shipLastName, self.billNameOnCard), 1)

    def test_1_typo(self):
        self.shipFirstName = "Jon"
        self.assertEqual(countUniqueNames(self.billFirstName, self.billLastName, self.shipFirstName, self.shipLastName,self.billNameOnCard), 1)

    def test_2_typos(self):
        change_max_typos(2)
        self.shipFirstName = "Jon"
        self.shipLastName = "Dor"
        self.assertEqual(countUniqueNames(self.billFirstName, self.billLastName, self.shipFirstName, self.shipLastName,
                                          self.billNameOnCard), 1)
    def test_two_different_names_bill(self):
        self.billFirstName = "Chen"
        self.billLastName = "Li"
        self.assertEqual(countUniqueNames(self.billFirstName, self.billLastName, self.shipFirstName, self.shipLastName, self.billNameOnCard), 2)

    def test_two_different_names_card(self):
        self.billNameOnCard = "Chen Li"
        self.assertEqual(countUniqueNames(self.billFirstName, self.billLastName, self.shipFirstName, self.shipLastName, self.billNameOnCard), 2)

    def test_three_different_names(self):
        self.billFirstName = "Chen"
        self.billLastName = "Li"
        self.billNameOnCard = "Madam Eve"
        self.assertEqual(countUniqueNames(self.billFirstName, self.billLastName, self.shipFirstName, self.shipLastName, self.billNameOnCard), 3)
    def test_two_different_names_ship(self):
        self.shipFirstName = "Chen"
        self.shipLastName = "Li"
        self.assertEqual(countUniqueNames(self.billFirstName, self.billLastName, self.shipFirstName, self.shipLastName, self.billNameOnCard), 2)
    def test_same_name_no_middle_name(self):
        self.assertEqual(countUniqueNames(self.billFirstName, self.billLastName, self.shipFirstName, self.shipLastName, self.billNameOnCard), 1)

    def test_bill_name_reverse(self):
        self.billNameOnCard = "Doe John"
        self.assertEqual(countUniqueNames(self.billFirstName, self.billLastName, self.shipFirstName, self.shipLastName, self.billNameOnCard), 1)
    def test_same_name_with_middle_name_bill(self):
        self.billFirstName = "John mid"
        self.assertEqual(countUniqueNames(self.billFirstName, self.billLastName, self.shipFirstName, self.shipLastName, self.billNameOnCard), 1)

    def test_same_name_with_middle_name_ship(self):
        self.shipFirstName = "John mid"
        self.assertEqual(countUniqueNames(self.billFirstName, self.billLastName, self.shipFirstName, self.shipLastName, self.billNameOnCard), 1)

    def test_same_name_with_middle_name_card(self):
        self.billNameOnCard = "John mid Doe"
        self.assertEqual(countUniqueNames(self.billFirstName, self.billLastName, self.shipFirstName, self.shipLastName, self.billNameOnCard), 1)

if __name__ == '__main__':
    unittest.main()
