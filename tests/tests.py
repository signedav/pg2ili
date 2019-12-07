import nose2
import unittest

from pg2ili import PG2ILI

SQL1 = "test1.sql"
ILI1 = "res1.ili"
SQL2 = "test2.sql"
ILI2 = "res2.ili"
SQL3 = "test3.sql"
ILI3 = "res3.ili"
SQL4 = "test4.sql"
ILI4 = "res4.ili"

class TestPG2ILI(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('\nINFO: Set up...\n')

    def test_sql1(self):
        print('INFO: Validating pg2ili single table...')
        pg2ili = PG2ILI(SQL1)
        ili_string = pg2ili.convert()
        self.assertTrue(self.compare_ili_to_str(ILI1, ili_string), "Test 1 failed!")

    def test_sql2(self):
        print('INFO: Validating pg2ili two tables...')
        pg2ili = PG2ILI(SQL2)
        ili_string = pg2ili.convert()
        self.assertTrue(self.compare_ili_to_str(ILI2, ili_string), "Test 2 failed!")

    def test_sql3(self):
        print('INFO: Validating pg2ili complete...')
        pg2ili = PG2ILI(SQL3)
        ili_string = pg2ili.convert()
        self.assertTrue(self.compare_ili_to_str(ILI3, ili_string), "Test 3 failed!")

    def test_sql4(self):
        print('INFO: Validating pg2ili UNIQUE constraints...')
        pg2ili = PG2ILI(SQL4)
        ili_string = pg2ili.convert()
        self.assertTrue(self.compare_ili_to_str(ILI4, ili_string), "Test 4 failed!")

    def compare_ili_to_str(self, ili_file, ili_string):
        file_contents = ""
        with open(ili_file) as f:
            file_contents = f.read()

        file_lines = file_contents.split("\n")
        str_lines = ili_string.split("\n")

        if len(file_lines) != len(str_lines):
            print("Number of lines in ili string ({}) differs from number of lines in ili file ({})".format(
                len(str_lines),
                len(file_lines)))
            return False

        for i, file_line in enumerate(file_lines):
            if file_line.strip() != str_lines[i].strip():
                print("ERROR: Different line ({})!".format(i))
                print("file_line:", len(file_line))
                print("str_line:", len(str_lines[i]))
                return False

        return True

    @classmethod
    def tearDownClass(self):
        print('INFO: Tear down...')

if __name__ == '__main__':
    nose2.main()
