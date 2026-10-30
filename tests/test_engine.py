import random, unittest
from mathquest.engine import make_question, choices_for, award, rank

class MathQuestTests(unittest.TestCase):
    def test_generated_answer_is_correct(self):
        rng=random.Random(12)
        for level in range(1,6):
            q=make_question(level,rng)
            self.assertIsInstance(q["answer"],int)
            self.assertEqual(q["level"],level)
    def test_choices_include_answer(self):
        opts=choices_for(42,random.Random(3))
        self.assertEqual(len(opts),4)
        self.assertIn(42,opts)
    def test_correct_awards_points_and_streak(self):
        score,streak=award(0,0,True)
        self.assertEqual((score,streak),(10,1))
        self.assertEqual(award(score,streak,True),(22,2))
    def test_wrong_resets_streak(self):
        self.assertEqual(award(20,3,False),(20,0))
    def test_ranks(self):
        self.assertEqual(rank(0),"Beginner")
        self.assertEqual(rank(80),"Apprentice")
        self.assertEqual(rank(180),"Scholar")
        self.assertEqual(rank(350),"Genius")

if __name__=="__main__": unittest.main()
