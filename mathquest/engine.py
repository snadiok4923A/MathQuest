"""MathQuest question generation and scoring engine."""
import random

def make_question(level, rng=None):
    rng = rng or random
    level = max(1, min(5, int(level)))
    if level == 1:
        a,b=rng.randint(1,10),rng.randint(1,10); op="+"
    elif level == 2:
        a,b=rng.randint(5,30),rng.randint(1,20); op="-"
        if b>a: a,b=b,a
    elif level == 3:
        a,b=rng.randint(2,12),rng.randint(2,12); op="×"
    elif level == 4:
        b=rng.randint(2,12); answer=rng.randint(2,12); a=b*answer; op="÷"
    else:
        a,b=rng.randint(2,15),rng.randint(2,15); op=rng.choice(["+","-","×"])
        if op=="-" and b>a: a,b=b,a
    answer={"+":a+b,"-":a-b,"×":a*b,"÷":a//b}[op]
    return {"text":f"{a} {op} {b} = ?","answer":answer,"level":level}

def choices_for(answer, rng=None):
    rng=rng or random
    values={answer}
    while len(values)<4:
        offset=rng.choice([-10,-7,-5,-3,-2,-1,1,2,3,5,7,10])
        values.add(max(0,answer+offset))
    result=list(values); rng.shuffle(result)
    return result

def award(score, streak, correct):
    if correct:
        streak += 1
        return score + 10 + min(streak-1,5)*2, streak
    return score, 0

def rank(score):
    if score>=300: return "Genius"
    if score>=150: return "Scholar"
    if score>=60: return "Apprentice"
    return "Beginner"
