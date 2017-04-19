import unittest
from money import money

class UselessTest(unittest.TestCase):

    def test_passa_sempre(self):
        self.assertTrue(True, msg='se fallisce son problemi')
    
    def test_ordina_ore(self):
        date = [
            {
                'data' : '18/04/2017',
                'ora' : '00:01',
                'prog' : 1,
            },
            {
                'data' : '19/04/2017',
                'ora' : '00:01',
                'prog' : 2,
            },
            {
                'data' : '17/04/2017',
                'ora' : '',
                'prog' : 3,
            },
            {
                'data' : '',
                'ora' : '00:01',
                'prog' : 4,
            },
        ]
        res = money.ordina(date)
        self.assertEqual(res[0]['prog'], 2)
        self.assertEqual(res[1]['prog'], 1)
        self.assertEqual(res[2]['prog'], 3)
        self.assertEqual(res[3]['prog'], 4)

def main():
    unittest.main()

if __name__ == '__main__':
    main()