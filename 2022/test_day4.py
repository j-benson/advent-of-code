from day4 import AssignmentPair

def test_assignment_pair():
  ap = AssignmentPair('2-4,6-8')
  assert ap.assignments[0].set == { 2, 3, 4 }
  assert ap.assignments[1].set == { 6, 7, 8 }
  assert len(ap.assignments[0]) == 3
  assert len(ap.assignments[1]) == 3
  assert ap.has_full_assignment_overlap() == False

  ap = AssignmentPair('2-8,3-7')
  assert ap.has_full_assignment_overlap() == True

  ap = AssignmentPair('6-6,4-6')
  assert ap.assignments[0].set == { 6 }
  assert ap.has_full_assignment_overlap() == True
