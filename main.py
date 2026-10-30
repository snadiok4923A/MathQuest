"""MathQuest: a quick-fire arithmetic adventure."""
import json, random
from pathlib import Path
from mathquest.engine import make_question, choices_for, award, rank

SAVE=Path(__file__).with_name("mathquest_save.json")

def load_best():
    try: return int(json.loads(SAVE.read_text(encoding="utf-8")).get("best",0))
    except (OSError,ValueError,TypeError): return 0

def save_best(best):
    SAVE.write_text(json.dumps({"best":best},indent=2),encoding="utf-8")

def main():
    best=load_best()
    print("\\n"+"="*46+"\\n       M A T H Q U E S T\\n  THE QUICK-FIRE NUMBER ADVENTURE\\n"+"="*46)
    name=input("Enter your player name: ").strip() or "Player"
    while True:
        print(f"\\nWelcome, {name}!  Personal best: {best}")
        print("1. Start 10-question challenge")
        print("2. How to play")
        print("3. Quit")
        menu=input("Choose: ").strip()
        if menu=="2":
            print("\\nAnswer each maths question. Correct answers earn 10+ combo points.")
            print("A correct streak increases your bonus. Questions get harder every two rounds.")
            print("Choose 1-4. Type Q during a question to end the run.")
            continue
        if menu=="3": break
        if menu!="1": continue
        score=streak=0
        for turn in range(1,11):
            level=min(5,(turn-1)//2+1)
            q=make_question(level)
            options=choices_for(q["answer"])
            print(f"\\nROUND {turn}/10  |  LEVEL {level}  |  SCORE {score}  |  COMBO x{streak}")
            print("Solve:",q["text"])
            for i,value in enumerate(options,1): print(f"  {i}. {value}")
            response=input("Your answer (1-4 or Q): ").strip().lower()
            if response=="q": break
            correct=response in ("1","2","3","4") and options[int(response)-1]==q["answer"]
            score,streak=award(score,streak,correct)
            if correct: print("✓ Correct! Nice calculation.")
            else: print(f"✗ Correct answer: {q['answer']}. Keep practicing!")
        print(f"\\nCHALLENGE COMPLETE — {name}")
        print(f"Score: {score}  |  Rank: {rank(score)}")
        if score>best:
            best=score; save_best(best); print("NEW PERSONAL BEST!")
        input("Press Enter to return to menu...")
    print("Thanks for playing MathQuest. Keep learning!")

if __name__=="__main__": main()
