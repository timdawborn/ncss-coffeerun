import unittest

from coffeespecs import Coffee, get_all_tokens


class TestCoffeeValidation(unittest.TestCase):
    def test_minimal_spec(self):
        c = Coffee('')
        self.assertFalse(c.validate())
        self.assertTrue(c.add_spec('type', 'C'))
        self.assertTrue(c.validate())
        self.assertTrue(c.add_spec('size', 'l'))
        self.assertTrue(c.validate())

        # Still valid if we add more.
        self.assertTrue(c.add_spec('milk', 'soy'))


class TestParser(unittest.TestCase):
    def test_get_tokens(self):
        tokens = get_all_tokens()
        self.assertEqual('iced chocolate', tokens[0])

    def test_parse(self):
        c = Coffee('Large Cap')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Cappuccino',
                'size': 'Large',
        })

        c = Coffee('LC')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Cappuccino',
                'size': 'Large',
        })

        c = Coffee('SC')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Cappuccino',
                'size': 'Small',
        })

        c = Coffee('Large Cap 2 Sugars')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Cappuccino',
                'size': 'Large',
                'sugar': '2 Sugars',
        })

        c = Coffee('Small strong cap')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Cappuccino',
                'size': 'Small',
                'strength': 'Extra-shot',
        })

        c = Coffee('Small doubleshot cap')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Cappuccino',
                'size': 'Small',
                'strength': 'Extra-shot',
        })

        c = Coffee('Small Latte')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Latte',
                'size': 'Small',
        })

        c = Coffee('SL')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Latte',
                'size': 'Small',
        })

        c = Coffee('RegL')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Latte',
                'size': 'Regular',
        })

        c = Coffee('LL')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Latte',
                'size': 'Large',
        })

        c = Coffee('CL')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Cappuccino',
                'size': 'Large',
        })

        c = Coffee('CL 2S')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Cappuccino',
                'size': 'Large',
                'sugar': '2 Sugars',
        })

        c = Coffee('Large Iced Latte')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Latte',
                'size': 'Large',
                'iced': 'Iced',
        })

        c = Coffee('Large Flat white')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Flat White',
                'size': 'Large',
        })

        c = Coffee('Large FW 3 Sugars')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Flat White',
                'size': 'Large',
                'sugar': '3 Sugars',
        })

        c = Coffee('Regular Flat White')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Flat White',
                'size': 'Regular',
        })

        c = Coffee('Soy decaf latte with 2 sugars')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Latte',
                'sugar': '2 Sugars',
                'decaf': 'Decaf',
                'milk': 'Soy',
        })

        c = Coffee('yfw')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Flat White',
                'milk': 'Soy',
        })

        c = Coffee('Soy Iced Coffee')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Iced Coffee',
                'milk': 'Soy',
        })

        c = Coffee('Skim Iced Chocolate')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                'type': 'Iced Chocolate',
                'milk': 'Skim',
        })

        c = Coffee('Lactose Free Cap')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                    'type': 'Cappuccino',
                    'milk': 'Lactose Free',
        })

        c = Coffee('lfw')
        self.assertTrue(c.validate())
        self.assertEqual(c.specs, {
                    'type': 'Flat White',
                    'size': 'Large',
        })


class TestPrettyPrint(unittest.TestCase):

    def testPrint(self):
        c = Coffee('Large Cap')
        self.assertEqual('Large Cappuccino', str(c))

        c = Coffee('SC')
        self.assertEqual('Small Cappuccino', str(c))

        c = Coffee('Large Cap 2 Sugars')
        self.assertEqual('Large Cappuccino with 2 Sugars', str(c))

        c = Coffee('Small strong cap')
        self.assertEqual('Small Extra-shot Cappuccino', str(c))

        c = Coffee('Small Latte')
        self.assertEqual('Small Latte', str(c))

        c = Coffee('RegL')
        self.assertEqual('Regular Latte', str(c))

        c = Coffee('LL')
        self.assertEqual('Large Latte', str(c))

        c = Coffee('Large Iced Latte')
        self.assertEqual('Large Iced Latte', str(c))

        c = Coffee('Large Flat white')
        self.assertEqual('Large Flat White', str(c))

        c = Coffee('Large FW 3 Sugars')
        self.assertEqual('Large Flat White with 3 Sugars', str(c))

        c = Coffee('Regular Flat White')
        self.assertEqual('Regular Flat White', str(c))

        c = Coffee('Soy decaf latte with 2 sugars')
        self.assertEqual('Regular Soy Decaf Latte with 2 Sugars', str(c))


if __name__ == '__main__':
    unittest.main()
