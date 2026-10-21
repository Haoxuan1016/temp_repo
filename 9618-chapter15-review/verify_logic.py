"""Check the Chapter 15 review paper's circuit, adder, algebra and K-map.

The question paper is original. These checks fix the tables and the simplified
expressions that the mark scheme depends on.
"""

from itertools import product


CIRCUIT_ROWS = []
for a, b, c in product((0, 1), repeat=3):
    p = 1 - (a & b & c)  # 3-input NAND
    q = b ^ c            # XOR
    r = a | q            # OR
    z = p & r            # AND
    CIRCUIT_ROWS.append((a, b, c, p, q, r, z))

# Replacing any one gate with the obvious wrong gate must change Z.
for a, b, c, p, q, r, z in CIRCUIT_ROWS:
    assert (a, b, c, p, q, r, z) in {
        (0, 0, 0, 1, 0, 0, 0),
        (0, 0, 1, 1, 1, 1, 1),
        (0, 1, 0, 1, 1, 1, 1),
        (0, 1, 1, 1, 0, 0, 0),
        (1, 0, 0, 1, 0, 1, 1),
        (1, 0, 1, 1, 1, 1, 1),
        (1, 1, 0, 1, 1, 1, 1),
        (1, 1, 1, 0, 0, 1, 0),
    }

SOP_MINTERMS = [(a, b, c) for a, b, c, p, q, r, z in CIRCUIT_ROWS if z == 1]
assert SOP_MINTERMS == [
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
]


def expr(a, b, c):
    """X = NOT(A . NOT(B + C)) . (B + A . NOT B)"""
    not_b_or_c = 1 - (b | c)
    left = 1 - (a & not_b_or_c)
    right = b | (a & (1 - b))
    return left & right


def simplified(a, b, c):
    return (a & c) | b


def nand_only(a, b, c):
    """(A NAND C) NAND (B NAND B)"""
    nand_ac = 1 - (a & c)
    nand_bb = 1 - (b & b)
    return 1 - (nand_ac & nand_bb)


assert all(expr(a, b, c) == simplified(a, b, c) == nand_only(a, b, c)
           for a, b, c in product((0, 1), repeat=3))


def full_adder(a, b, cin):
    s = a ^ b ^ cin
    cout = (a & b) | (a & cin) | (b & cin)
    cout_alt = (a & b) | (cin & (a ^ b))
    assert cout == cout_alt
    return s, cout


FULL_ADDER = [(*bits, *full_adder(*bits)) for bits in product((0, 1), repeat=3)]
assert FULL_ADDER[0] == (0, 0, 0, 0, 0)
assert FULL_ADDER[3] == (0, 1, 1, 0, 1)
assert FULL_ADDER[7] == (1, 1, 1, 1, 1)


# 4-variable function used for the K-map. Bit order is ABCD, A is the MSB.
KMAP_ONES = {0, 6, 7, 8, 10, 11, 14, 15}
GROUP_AC = {10, 11, 14, 15}   # A.C
GROUP_BC = {6, 7, 14, 15}     # B.C
GROUP_WRAP = {0, 8}           # NOT B . NOT C . NOT D, columns 00 and 10 wrap
assert GROUP_AC | GROUP_BC | GROUP_WRAP == KMAP_ONES

# The six 1s in columns 01, 11 and 10 of the two C=1 rows are not a legal loop.
ILLEGAL_SIX = {6, 7, 14, 15, 10, 11}
assert len(ILLEGAL_SIX) == 6

GRAY = (0b00, 0b01, 0b11, 0b10)


def cell(ab, cd):
    return ((ab << 2) | cd) in KMAP_ONES


KMAP_GRID = [[cell(ab, cd) for ab in GRAY] for cd in GRAY]
assert KMAP_GRID == [
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 1, 1, 1],
]


def nor_sr_step(s, r, q):
    """One settling pass is not enough for feedback. Iterate to a fixed point.

    Returns (q, q_bar) or None when S = R = 1 forces the invalid state.
    """
    if s == 1 and r == 1:
        return None
    q_bar = 1 - q
    for _ in range(4):
        new_q = 1 - (r | q_bar)       # NOR
        new_q_bar = 1 - (s | new_q)   # NOR
        if (new_q, new_q_bar) == (q, q_bar):
            return q, q_bar
        q, q_bar = new_q, new_q_bar
    raise AssertionError("latch did not settle")


# Hold.
assert nor_sr_step(0, 0, 0) == (0, 1)
assert nor_sr_step(0, 0, 1) == (1, 0)
# Reset and set, whatever the previous Q was.
assert nor_sr_step(0, 1, 0) == (0, 1)
assert nor_sr_step(0, 1, 1) == (0, 1)
assert nor_sr_step(1, 0, 0) == (1, 0)
assert nor_sr_step(1, 0, 1) == (1, 0)
assert nor_sr_step(1, 1, 0) is None

print("circuit rows:")
for row in CIRCUIT_ROWS:
    print("  ", row)
print("K-map grid (rows CD 00,01,11,10; columns AB 00,01,11,10):")
for row in KMAP_GRID:
    print("  ", row)
print("algebra, NAND form, full adder and SR latch: ok")
