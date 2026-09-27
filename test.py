class Student:
def init(self, name, stu_id, scores):
self.name = name
self.stu_id = stu_id
self.scores = scores
def get_avg(self):
return sum(self.scores)/len(self.scores)
def is_passed(self):
return all(s>=60 for s in self.scores)

if name == "main":
s1 = Student("张三", "2025001", [78, 82, 90])
print(f"{s1.name} 平均分{s1.get_avg():.1f}, 是否全过{s1.is_passed()}")
