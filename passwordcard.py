#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# passwordcard - A passwordcard generator compatible with passwordcard.org
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

import javarandom

CHARSETS = {
    'original.digits': u"0123456789",
    'original.alphanumeric': u"23456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ",
    'original.alphanumeric_with_symbols': u"23456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ@#$%&*<>?€+{}[]()/\\"
    }

HEADERS = {
    'original': u"■□▲△○●★☂☀☁☹☺♠♣♥♦♫€¥£$!?¡¿⊙◐◩�",
    }

def generate_card(seed, width, height, top_charset, bottom_charset, header):
    """Generate a password card with the given parameters"""
    rng = javarandom.JavaRandom(seed)

    header = list(header)
    top_charset = list(top_charset)
    bottom_charset = list(bottom_charset)

    rng.shuffle(header)

    contents = []

    midheight = 1 + (height/2)

    for i in range(1, midheight):
        line = []
        for j in range(width):
            line.append(top_charset[rng.next_int(len(top_charset))])
        contents.append(u''.join(line))
    for j in range(midheight, height+1):
        line = []
        for j in range(width):
            line.append(bottom_charset[rng.next_int(len(bottom_charset))])
        contents.append(u''.join(line))

    return u''.join(header), contents
