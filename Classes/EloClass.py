class EloCalculator(object):
    def __init__(self):
    self.studentElo = 0
    self.studentExpected = 0
    self.studentActual = 0
    self.questionElo = 0
    self.totalQuestionElo = 0
    self.questionExpected = 0
    self.numOfQuestions = 0
    self.studentScore = 0
    self.kFactor = 32

    def expected_score(self):
        self.studentExpected = 1/(1 + 10 ** ((self.studentElo - self.questionElo) / 400))
        self.questionExpected = 1 - self.studentExpected
        
    def actual_score(self):
        self.studentActual = (self.totalQuestionElo + 400 * (self.studentScore - (self.numOfQuestions - self.studentScore)))/self.numOfQuestions

    def update_elo(self):
        self.studentElo = self.studentElo + kFactor * (self.studentActual - self.studentExpected)
    
