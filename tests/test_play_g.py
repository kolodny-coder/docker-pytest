import unittest
from scripts import play_g

class TestPlay_g(unittest.TestCase):

    def test_attren_human_sin(self):
        with self.subTest('happy, path'):
            result = play_g.attren_human_skin(400)
            self.assertEqual(400, result)
        # with self.subTest('sad path raise ValueError'):
        #     with self.assertRaises(ValueError):
        #         play_g.attren_human_skin(150)

    def test_arduino(self):
        self.assertTrue(play_g.arduino())

    def test_automative(self):
        result = play_g.automative()
        self.assertEqual(result.status_code, 200)

    def test_applicator_mesaurment(self):
        result = play_g.applicator_mesaurment(5)
        self.assertEqual(result, 5000)

    def test_power_meter(self):
        result = play_g.power_meter(10, 5000)
        self.assertEqual(result, 2500000)






if __name__ == '__main__':
    unittest.main()