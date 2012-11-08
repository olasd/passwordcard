#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# javarandom - Java-compatible random number generator
#
# Copyright © 2012 Nicolas Dandrimont <nicolas.dandrimont@crans.org>
#
#   This file is part of PasswordCard.
#
#   PasswordCard is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import threading
import time

class JavaRandom(object):
    """A partial implementation of a java-compatible random number generator"""
    def __init__(self, seed = None):
        if seed is None:
            seed = int(time.time() * 1000)

        self.seed = seed
        self.lock = threading.Lock()

    @property
    def seed(self):
        return self._seed

    @seed.setter
    def seed(self, seed):
        self._seed = (seed ^ 0x5DEECE66D) & ((1 << 48) - 1)

    def next(self, bits):
        """Return `bits` random bits as a signed 32 bits integer"""
        with self.lock:
            self._seed = (self._seed * 0x5DEECE66D + 0xB) & ((1 << 48) - 1)

            ret = self._seed >> (48 - bits)

            if ret & (1 << 31):
                ret -= (1 << 32)

            return ret

    def next_int(self, maxint = None):
        """Return an integer evenly distributed between 0 and maxint-1"""
        if maxint is None:
            return self.next(32)
        if maxint <= 0 or maxint > (1 << 31) - 1:
            raise ValueError("maxint needs to be in range 1 - 2^31-1")

        # if maxint is a power of two, just return the right number of bits (MSB of self.next)
        if (maxint & -maxint) == maxint:
            return (maxint * self.next(31)) >> 31

        bits = self.next(31)
        val = bits % maxint

        # We need to emulate the 32-bit int here too
        #     (bits - val + maxint - 1) < 0
        while (bits - val + maxint - 1) & (1 << 31):
            bits = self.next(31)
            val = bits % maxint

        return val

    def shuffle(self, list):
        """Shuffle the list given in the argument, using the algorithm from java.collections"""
        for i in reversed(range(2, len(list)+1)):
            rnd = self.next_int(i)
            list[i-1], list[rnd] = list[rnd], list[i-1]

