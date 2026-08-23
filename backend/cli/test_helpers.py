import unittest
import backend.cli.helpers as helpers

class TestHelpers(unittest.TestCase):

    def test_get_weapons_happy(self):
        """Test get_weapons helper functions happy path"""
        test_unit = {
            "name": "Assault Intercessor Squad",
            "models": [
                {
                    "name": "Intercessor Sergeant",  
                    "r_weapon": "plasma_pistol",
                },
                {
                    "name": "Assault Intercessor",  
                    "r_weapon": "heavy_bolt_pistol",
                },
            ]
        }

        result = helpers.get_weapons(test_unit)
        self.assertEqual(result["plasma_pistol"]["count"], 1)
        self.assertEqual(result["heavy_bolt_pistol"]["count"], 1)

    def test_get_weapons_none(self):
        """Test get_weapons helper functions passes when there is none weapons"""
        test_unit = {
            "name": "Assault Intercessor Squad",
            "models": [
                {
                    "name": "Intercessor Sergeant",  
                    "r_weapon": "none",
                },
                {
                    "name": "Assault Intercessor",  
                    "r_weapon": None,
                },
                {
                    "name": "Assault Intercessor",  
                    "r_weapon": "plasma_pistol",
                },
            ]
        }

        result = helpers.get_weapons(test_unit)

        self.assertNotIn("none", result)
        self.assertNotIn(None, result)
        self.assertEqual(len(result),1)

    def test_calc_wound_value(self):
        """Test calc_wound_value returns the correct value based on 40k rules """

        guardman = {"name": "Guardsman", "T": 3}
        space_marine = {"name": "Space Marine", "T": 4}
        rhino_tank = {"name": "Rhino Tank", "T": 9}

        test_cases = [
                    # High Strength vs Low Toughness (S8 vs T4 -> 2+)
                    ({"name": "Plasma Gun", "stats": {"S": 8}}, space_marine, 2),
                    
                    # Equal Strength vs Toughness (S4 vs T4 -> 4+)
                    ({"name": "Bolt Rifle", "stats": {"S": 4}}, space_marine, 4),
                    
                    # Low Strength vs High Toughness (S3 vs T4 -> 5+)
                    ({"name": "Lasgun", "stats": {"S": 3}}, space_marine, 5),
                    
                    # Half Strength vs Toughness (S4 vs T9 -> 6+)
                    ({"name": "Bolt Rifle", "stats": {"S": 4}}, rhino_tank, 6),
                    
                    # S5 vs T3 (S > T -> 3+)
                    ({"name": "Heavy Bolter", "stats": {"S": 5}}, guardman, 3),
                ]

        for weapon, defender, expected in test_cases:
            test_label = f"{weapon['name']} (S{weapon["stats"]['S']}) vs {defender['name']} (T{defender['T']})"

            with self.subTest(msg=test_label):
                result = helpers.calc_wound_value(weapon,defender)
                self.assertEqual(result,expected,f"Failed for {test_label}. Expected {expected}+ but got {result}+")

    def test_calc_save_value(self):
        terminator = {"name": "Terminator", "SV": 2}
        plasma_gun = {"name": "Plasma Gun", "stats": {"AP": 2}}

        result = helpers.calc_save_value(plasma_gun, terminator)

        self.assertEqual(result, 4)

if __name__ == "__main__":    
    unittest.main()