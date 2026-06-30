from CandidateBO import CandidateBO
from CandidateRequestBO import CandidateRequestBO

def main():
    crbo = CandidateRequestBO()
    requests = []

    while True:
        print("1.Create request\n2.Search request using requestedDate\n3.Search request using candidate education\n4.Update request\n5.Delete request\n6.Filter requests by date range\n7.Display all requests\n8.Exit")
        try:
            choice = int(input("Enter the choice\n"))
        except ValueError:
            continue
            
        if choice == 1:
            cand_str = input("Enter the candidate details\n")
            req_str = input("Enter request details\n")
            cand = CandidateBO.createCandidate(cand_str)
            req = crbo.createCandidateRequest(req_str, cand)
            requests.append(req)
        elif choice == 7:
            crbo.displayDetails(requests)
        elif choice == 8:
            print("Thank you")
            break
        # Implement remaining logic for cases 2-6 based on your requirements.

if __name__ == "__main__":
    main()