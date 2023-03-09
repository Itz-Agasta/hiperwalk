import numpy as np
from sys import path as sys_path
sys_path.append('../')
sys_path.append('../../')
from qwalk.coined import segment as hpseg
import unittest

class TestCoinedSegment(unittest.TestCase):

    def test_persistent_shift_state_transfer(self):
        num_vert = 10
        seg = hpseg.Segment(num_vert)

        init_cond = seg.state([(1, 0, 0)])
        S = seg.persistent_shift_operator()
        final_state = seg.simulate_walk(S, init_cond, num_vert - 1)
        final_state = final_state[0]

        self.assertTrue(
            final_state[-1] == 1 and np.all(final_state[:-1] == 0)
        )
