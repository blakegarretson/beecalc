"""
Bee Calc: Cross-platform notebook calculator with robust unit support

    Copyright (C) 2023  Blake T. Garretson

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
from collections import namedtuple
import re

def beeParser(text):
    return


class BeeNotepad:

    def __init__(self):
        self.data = [] # [(inputstr, output), ...]

    def append(self, text):
        out = beeParser(text)
        if out:
            self.data.append((text,out))

####

if __name__ == '__main__':
    pad = BeeNotepad()
    pad._parse("3+4")