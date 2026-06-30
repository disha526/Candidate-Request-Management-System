from Candidate import Candidate

class CandidateBO:
    @staticmethod
    def createCandidate(candidateDetail):
        # Format: name,email,dob,mobile,address,education
        details = candidateDetail.split(',')
        return Candidate(details[0], details[1], details[2], details[3], details[4], details[5])