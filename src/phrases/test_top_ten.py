import unittest
import subprocess
import os
from phrases import top_ten

class TestTopTen(unittest.TestCase):

    def setUp(self):
        self.input_list = ["a b c", "A B C", "a B c", "$a %B !C"]

    def test_top_ten_files(self):
        self.test_results = list()
        for index,item in enumerate(self.input_list):
            with open(str(index) + '.txt', 'w') as text_file:
                text_file.write(item)  
            self.test_results.append(subprocess.check_output("phrases %s.txt" % index , shell=True))
            if len(self.test_results) > 2:
                self.assertEqual(self.test_results[index], self.test_results[1])
            os.remove(str(index) + '.txt')
            
        

if __name__ == '__main__':
    unittest.main()

# test_file = "pg2009.txt"
# test_args = "{0} {1}".format("phrases",test_file)

# test = subprocess.check_output(test_args, shell=True)
# test2 = subprocess.check_output(test_args, shell=True)


# if test2 == test:
#     print("{}".format("TRUE"))
