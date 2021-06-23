import unittest
from salaryman import best_schedule

class MyTestCase(unittest.TestCase):
    def test_best_schedule_1(self):
        regular_work = [3, 7, 2, 1, 8, 4, 5] #change
        special_events = [(1, 3, 15), (2, 2, 8), (0, 4, 30), (3, 5, 19), (5, 6, 1)]  #change
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 42 #change
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + most_cash + "."

    def test_best_schedule_2(self):
        regular_work = [3, 7, 2, 1, 8, 4, 5]
        special_events = [(1, 3, 15), (2, 2, 8), (0, 4, 35), (3, 5, 19), (5, 6, 1)]  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 44
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_3(self):
        regular_work = [3, 7, 2, 1, 8, 4, 5]
        special_events = [(1, 3, 15), (2, 2, 8), (0, 4, 30), (3, 5, 19), (5, 6, 14)]  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 44
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_4(self):
        regular_work = [3, 7, 2, 1, 8, 4, 5]
        special_events = [(1, 3, 15), (2, 2, 8), (3, 4, 30), (3, 5, 19), (5, 6, 1)]  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 57
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_5(self):
        regular_work = [3, 7, 18, 1, 8, 4, 5]
        special_events = [(1, 3, 15), (2, 2, 8), (0, 4, 30), (3, 5, 19), (5, 6, 14)]  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 52
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_6(self):
        regular_work = [3, 7, 2, 1, 8, 4, 5]
        special_events = [(1, 3, 15), (2, 2, 8), (0, 4, 30), (3, 5, 19), (5, 5, 14)]  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 49
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_7(self):
        regular_work = [3, 7, 2, 1, 18, 4, 5]
        special_events = [(1, 3, 15), (2, 2, 8), (0, 4, 30), (3, 5, 19), (5, 6, 1)]  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 46
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_8(self):
        regular_work = [3, 7, 2, 1, 8, 4, 5]
        special_events = [(1, 3, 15), (1, 2, 8), (0, 4, 30), (3, 5, 19), (5, 6, 4)]  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 39
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_9(self): # no work no time nothing
        regular_work = []
        special_events = []  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 0
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."


    def test_best_schedule_10(self):
        regular_work = [3, 7, 2, 5, 8, 4, 5]
        special_events = [(1, 3, 15), (1, 2, 14), (0, 4, 30), (3, 5, 19)]  
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 41
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."
    
    # compare competition within same week
    def test_best_schedule_11(self):
        regular_work = [1]
        special_events = [(0, 0, 7), (0,0,10)]  
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 10
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."
    
    def test_best_schedule_12(self):
        regular_work = [11,2]
        special_events = [(0, 0, 7), (0,0,10)]  
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 13
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."
    
    def test_best_schedule_13(self):
        regular_work = [11]
        special_events = [(0, 0, 7), (0,0,10)]  
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 11
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_14(self):
        regular_work = [1,1,1,1,1,1,1]
        special_events = [(2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 2, 5)]  
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 11
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_15(self):
        regular_work = [100,100,100,100,100,100,100]
        special_events = [(2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 2, 4), (2, 2, 5)]  
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 700
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

if __name__ == '__main__':
    unittest.main()
