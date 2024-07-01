from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A cannot be both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),

    # A being knight implies he is both
    Implication(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A both knaves sentence
    Implication(AKnight, And(AKnave, BKnave)),

    # A tells lie
    Implication(AKnave, Not(And(AKnave, BKnave))),

    # A cannot be both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),

    # B cannot be both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # both same kind true
    Implication(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),

    # both same kind lie
    Implication(AKnave, Not(Or(And(AKnave, BKnave), And(AKnight, BKnight)))),

    # different kind
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),

    # different kind lie
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))),

    # A cannot be both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),

    # B cannot be both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A cannot be both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),

    # B cannot be both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),

    # C cannot be both
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),

    # A Knight True
    Implication(AKnight, And(
        Or(AKnight, AKnave),
        Not(And(AKnight, AKnave)),
    )),

    # A Knave Lie
    Implication(AKnave, Not(And(
        Or(AKnight, AKnave),
        Not(And(AKnight, AKnave)),
    ))),

    # B Knight truth
    Implication(BKnight, AKnave),
    Implication(BKnight, CKnave),

    # B knave lie
    Implication(BKnave, Not(AKnave)),
    Implication(BKnave, Not(CKnave)),

    # C knight truth
    Implication(CKnight, AKnight),

    # C Knave lie
    Implication(CKnave, Not(AKnight)),

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
