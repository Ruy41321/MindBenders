import testlib
import random, os
from ddt import file_data, ddt, data, unpack

# change this variable to True to disable timeout and enable print
DEBUG=True
DEBUG=False

WARP = 2   # test VM
WARP = 1   # your PC

import pngmatrix   # preload

@ddt
class Test(testlib.TestCase):
    def do_test(self, id_file, expected_list, timeout):
        """Test implementation
        - file_txt:		text file containing the input matrix
        - file_png:	    png image you must write the picture inside
        - spacing:      spacing between rectangles and for the border
        - expected_png:	expected result - file png
        - expected:     expected result - image dimensions
        - timeout:      variable timeout depending on test
        """
        file_input_png                  = 'images/image' + id_file + '.png'
        file_input_rectangles           = 'rectangles/rectangles' + id_file + '.txt'
        file_input_expected_rectangles  = 'expected/image' + id_file + '.txt'
        file_output_rectangles          = 'test_output/rectangles' + id_file + '.txt'
        if not os.path.isdir("test_output/"):
            os.mkdir("test_output/")

        TIMEOUT = timeout * WARP   # warp factor 
        if DEBUG:
                import program01 as program
                result = program.ex(file_input_png, file_input_rectangles, file_output_rectangles)
        else:
            with    self.ignored_function('pprint.pprint'), \
                    self.ignore_print(), \
                    self.forbidden_function('builtins.input'), \
                    self.forbidden_function('builtins.eval'), \
                    self.check_open( { file_input_png: 'rb', file_input_rectangles: 'rt',
                        file_output_rectangles: 'wta', 'meminfo': 'rb'} ), \
                    self.check_imports(allowed=['program01', '_io', 'pngmatrix', 'encodings.utf_8', 'unicodedata']), \
                    self.timeout(TIMEOUT), \
                    self.timer(TIMEOUT):
                import program01 as program
                result = program.ex(file_input_png, file_input_rectangles, file_output_rectangles)
        self.assertEqual(type(result), list,
                         ('The output type should be: list\n'
                          '[Il tipo di dato in output deve essere: list]'))
        self.assertEqual(result, expected_list,
                         ('The return value is incorrect\n'
                          '[Il valore di ritorno è errato]'))
        self.check_text_file(file_output_rectangles, file_input_expected_rectangles)
        os.remove(file_output_rectangles)
        return 1

    @data(  # id_file   expected_list                                                                       timeout
            ('0',       [True, False, True, False, True, True, False, False, True, True],                 0.5),
            ('1',       [True, True, False, False, True, True, False, True, True, False],                    0.5),
            ('2',       [True, True, True, True, False, True, True, True, True, True],                       0.5),
            ('3',       [True, True, False, True, True, True, True, True, True, True, False, True, True, \
                         True, True, True, True, True, True, True, True, True, True, True, True, False, \
                         True, True, True, True, True, True, True, True, False, True, False, False, True, \
                         True, True, True, True, False, True, True, True, True, True, True, True, True, \
                         True, False, True, True, True, True, True, True, True, True, True, True, True, \
                         True, True, True, True, True, True, False, True, True, True, True, False, False, \
                         True, False, True, False, True, True, True, True, True, False, True, True, True, \
                         True, True, True, True, True, True, True, True, True],                             0.5),
            ('4',       [False, True, False, True, True, True, False, False, True, True, False, False, \
                        False, True, True, True, True, True, False, False],                                 0.5),
            ('5',       [True, False], 0.5),
            ('6',       [False, False, True], 0.5),
            ('7',       [False, True], 0.5),
            # ('8',       
            ('9',       [True, False, False, True, True, False, True, True, False, True, True, True, True, False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, True], 0.5),
            ('10',      [False, False, True, True, False, True, True, True, False, False], 0.5)
            )
    @unpack
    def test_lists(self, id_file, expected_list, timeout):
        return self.do_test(id_file, expected_list, timeout)

    ######################### SECRET TESTS START HERE! #########################

    # @data(  # test-id    spacing   exp_dimensions   timeout
    #         ( 'mat-1-3',    3,      ( 574,  84),     0.5),
    #         ( 'mat-2-32',  32,      ( 402, 186),     0.5),
    #         ( 'mat-16-14', 14,      ( 296, 892),     0.5),
    #         ( 'mat-7-2',    2,      ( 644, 544),     0.5),
    #         ( 'mat-wide',   9,      (1236, 153),     0.5),
    #         ( 'mat-3-8',    8,      (5266, 308),     0.5),
    #         )
    # @unpack
    # def test_secrets(self, id_file, spacing, expected, timeout):
    #     return self.do_test(id_file, spacing, expected, timeout, 'secrets')

if __name__ == '__main__':
    Test.main()

