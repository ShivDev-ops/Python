class score:
    class test:
        def __init__(self, m_no, s_no):
            self.s_no = s_no
            self.m_no = m_no
            
        
        def total(self):
            return (self.m_no + self.s_no)/2

    class attendace:
        def __init__(self, att):
            self.attendence = att
    
        def att_score(self):
            return self.attendence/2 
    
    def __init__(self, test, attendance):
        self.test_score = test.total()/2
        self.attendance_score = attendance.att_score()
        self.final_score = self.test_score + self.attendance_score
    
    def final(self):
        return f"final score = {self.final_score}\n test score = {self.test_score}\n attendance score = {self.attendance_score}"
    
aman_marks = score.test(90, 80)
aman_att = score.attendace(90)
aman = score(aman_marks, aman_att)
print(aman.final())