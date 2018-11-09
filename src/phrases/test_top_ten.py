import unittest
import subprocess
import os
from phrases import top_ten


class TestTopTen(unittest.TestCase):

    def setUp(self):
        self.pass_list = ["a b c", "A B C", "a B c", "$a %B !C"]
        self.fail_list = ["a b c", "D E F", "G i j", "$H &E !Y"]

        for index, item in enumerate(self.pass_list):
            with open(str(index) + '_pass.txt', 'w') as text_file:
                text_file.write(item)
        for index, item in enumerate(self.fail_list):
            with open(str(index) + '_fail.txt', 'w') as text_file:
                text_file.write(item)

    def test_top_ten_files(self):
        test_results = list()
        for index, item in enumerate(self.pass_list):
            test_results.append(subprocess.check_output(
                "phrases %s_pass.txt" % index, shell=True))
            if len(test_results) > 2:
                self.assertEqual(
                    test_results[index], test_results[1])

    def test_top_ten_stdin(self):
        test_results = list()
        for index, item in enumerate(self.pass_list):
            test_results.append(subprocess.check_output(
                "cat %s_pass.txt | phrases" % index, shell=True))
            if len(test_results) > 2:
                self.assertEqual(
                    test_results[index], test_results[1])

    def test_fail_top_ten_files(self):
        test_results = list()
        for index, item in enumerate(self.fail_list):
            test_results.append(subprocess.check_output(
                "phrases %s_fail.txt" % index, shell=True))
            if len(test_results) > 2:
                self.assertNotEqual(
                    test_results[index], test_results[1])

    def test_fail_top_ten_stdin(self):
        test_results = list()
        for index, item in enumerate(self.fail_list):
            test_results.append(subprocess.check_output(
                "cat %s_fail.txt | phrases" % index, shell=True))
            if len(test_results) > 2:
                self.assertNotEqual(
                    test_results[index], test_results[1])

    def tearDown(self):
        for index, item in enumerate(self.pass_list):
            os.remove(str(index) + '_pass.txt')
        for index, item in enumerate(self.fail_list):
            os.remove(str(index) + '_fail.txt')


if __name__ == '__main__':
    unittest.main()
