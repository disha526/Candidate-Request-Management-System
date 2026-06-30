from datetime import datetime
from CandidateRequest import CandidateRequest

class CandidateRequestBO:
    def __init__(self):
        self.requests = []

    def createCandidateRequest(self, candidateRequestDetail, candidate):
        # Format: id,requestType,requestedDate
        details = candidateRequestDetail.split(',')
        return CandidateRequest(int(details[0]), candidate, int(details[1]), datetime.strptime(details[2], '%d/%m/%Y'))

    def searchCandidateRequestByRequestedDate(self, date_str, request_list):
        target_date = datetime.strptime(date_str, '%d/%m/%Y')
        return [r for r in request_list if r.requestDate == target_date]

    def searchCandidateRequestByEducation(self, education, request_list):
        return [r for r in request_list if r.candidate.education.lower() == education.lower()]

    def updateCandidateRequest(self, request_list, request_id, new_type):
        for r in request_list:
            if r.id == request_id:
                r.requestType = new_type
                return True
        return False

    def deleteCandidateRequest(self, request_list, request_id):
        for i, r in enumerate(request_list):
            if r.id == request_id:
                del request_list[i]
                return True
        return False

    def filterRequestsByDateRange(self, request_list, start_date_str, end_date_str):
        start = datetime.strptime(start_date_str, '%d/%m/%Y')
        end = datetime.strptime(end_date_str, '%d/%m/%Y')
        return [r for r in request_list if start <= r.requestDate <= end]

    def displayDetails(self, request_list):
        if not request_list:
            print("No request found")
        for r in request_list:
            print(f"ID: {r.id}\nCandidate: {r.candidate.name}\nRequest Type: {r.requestType}\nRequested Date: {r.requestDate.strftime('%d/%m/%Y')}")