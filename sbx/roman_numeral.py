from __future__ import annotations
from typing import Any

from dotenv import load_dotenv
import pytest

load_dotenv('.env')


def to_roman(num: int) -> str:

    print(f"\nnum = {num}")
    rev_num = str(num)[-1::-1]
    up_to_1000 = rev_num[0:3]
    out = []
    for year_unit, year_num in enumerate(up_to_1000):
        out.append(_to_roman(int(year_num), year_unit))
    mellenium = ''
    if len(rev_num) == 4:
        mellenium = 'M' * (int(num) // 1000)
    final = mellenium + ''.join(out[-1::-1])
    print(f"final={final}")
    return final


def _to_roman(num: int, unit_place: int = 0):

    rn_ranges = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M']]
    yr_ranges = [[1, 5, 10], [10, 50, 100], [100, 500, 1000]]
    print(f"\nnum = {num}")
    print(str(num)[-1::-1])
    roman_numerals = rn_ranges[unit_place]
    print(f"roman_numerals = {roman_numerals}")
    years = yr_ranges[unit_place]
    print(f"years = {years}")

    out = ""
    if num >= years[2]:
        print(f"num >= years[2]")
        rem = num % years[2]
        print(f"rem = {rem}")
        floor_div = num // years[2]
        print(f"floor_div = {floor_div}")
        return _to_roman(floor_div, unit_place + 1) + _to_roman(
            rem, unit_place)

    if num < years[2]:
        print(f"num = {num}")
        print(f"num < years[2] = {years}")
        lkup = {
            0: '',
            1: roman_numerals[0],
            2: roman_numerals[0] * 2,
            3: roman_numerals[0] * 3,
            4: roman_numerals[0] + roman_numerals[1],
            5: roman_numerals[1],
            6: roman_numerals[1] + roman_numerals[0],
            7: roman_numerals[1] + roman_numerals[0] * 2,
            8: roman_numerals[1] + roman_numerals[0] * 3,
            9: roman_numerals[0] + roman_numerals[2],
        }
        print(f'lkup[num] = {lkup[num]}')
        out += lkup[num]
    return out


def to_roman_old(num: int, unit_place: int = 0) -> str:
    rn_ranges = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M']]
    yr_ranges = [[1, 5, 10], [10, 50, 100], [100, 500, 1000]]

    print(f"\nnum = {num}, unit_place = {unit_place}")
    roman_numerals = rn_ranges[unit_place]
    print(f"roman_numerals = {roman_numerals}")
    years = yr_ranges[unit_place]
    print(f"years = {years}")

    out = ""
    if num >= years[2]:
        print(f"num >= years[2]")
        rem = num % years[2]
        print(f"rem = {rem}")
        floor_div = num // years[2]
        print(f"floor_div = {floor_div}")
        return _to_roman(floor_div, unit_place + 1) + _to_roman(
            rem, unit_place)

    if num < years[2]:
        print(f"num = {num}")
        print(f"num < years[2] = {years}")
        lkup = {
            0: '',
            1: roman_numerals[0],
            2: roman_numerals[0] * 2,
            3: roman_numerals[0] * 3,
            4: roman_numerals[0] + roman_numerals[1],
            5: roman_numerals[1],
            6: roman_numerals[1] + roman_numerals[0],
            7: roman_numerals[1] + roman_numerals[0] * 2,
            8: roman_numerals[1] + roman_numerals[0] * 3,
            9: roman_numerals[0] + roman_numerals[2],
        }
        print(f'lkup[num] = {lkup[num]}')
        out += lkup[num]
    return out




cases = [(1, 'I'),
         (2, 'II'),
         (3, 'III'),
         (4, 'IV'),
         (5, 'V'),
         (6, 'VI'),
         (7, 'VII'),
         (8, 'VIII'),
         (9, 'IX'),
         (10, 'X'),
         (11, 'XI'),
         (12, 'XII'),
         (13, 'XIII'),
         (14, 'XIV'),
         (15, 'XV'),
         (16, 'XVI'),
         (17, 'XVII'),
         (18, 'XVIII'),
         (19, 'XIX'),
         (20, 'XX'),
         (21, 'XXI'),
         (90, 'XC'),
         (99, 'XCIX'),
         (1997, 'MCMXCVII'),
         (1998, 'MCMXCVIII'),
         (1999, 'MCMXCIX'),
         (2000, 'MM'),
         (2001, 'MMI'),
         ] # yapf: disable=true
@pytest.mark.parametrize("num,rn", cases)
def test_foo(num, rn):
    assert to_roman(num) == rn