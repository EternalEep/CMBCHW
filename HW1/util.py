# created by WeiwenYi on 2020/04/13
import time

class Timer(object):
    ''' Timer for recording time distribution. '''

    def __init__(self):
        self.prev_t = time.time()
        self.clear()

    def set(self):
        self.prev_t = time.time()

    def cnt(self, mode):
        self.time_table[mode] = time.time()-self.prev_t
        self.set()

    def show(self):
        msg = self.time_table
        self.clear()
        return msg

    def clear(self):
        self.time_table = {}

    def time_str_ms(self, t):
        return '{:2f} ms'.format(t * 1000)

class MagicList(object):
    """
    Magic Method of List
    """

    def __init__(self, lens = 1):
        self.arrays = [0] * lens

    # Call print()
    def __str__(self):
        return "Our arrays :" + str(self.arrays)

    # Getting the value
    def __getitem__(self, item):
        return "You get index {} of arrays whose value is : {}". format(item, self.arrays[item])

    # Setting the value
    def __setitem__(self, key, value):
        print("You set value {} for index {} of arrays.".format(value, key))
        self.arrays[key] = value

    def __len__(self):
        print('You get length of list : {}'.format(len(self.arrays)))
        return len(self.arrays)

    def __delitem__(self, key):
        print('You delete list of index {} whose value is : {}'.format(key, self.arrays[key]))
        del self.arrays[key]

if __name__ == "__main__":

    ListMath = MagicList(5)

    ListMath[0] = 1
    ListMath[3] = 4
    ListMath[4] = 5
    del ListMath[3]
    ListMath[1] = 2
    ListMath[2] = 3
    del ListMath[0]

    del ListMath[0]
    len(ListMath)
    print(ListMath)



