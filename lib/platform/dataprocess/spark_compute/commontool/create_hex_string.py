import os
import random


class CreateHexString(object):

    @staticmethod
    def create_by_length(length):
        if length % 2 == 0:
            id_list = map(
                lambda byte: '{:0>2}'.format(hex(ord(byte))[2:]),
                os.urandom(length/2)
            )
        else:
            id_list = map(
                lambda byte: '{:0>2}'.format(hex(ord(byte))[2:]),
                os.urandom(length/2)
            )
            id_list.append(str(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a', 'b', 'c', 'd', 'e', 'f'])))
        return (''.join(id_list)).upper()
