from ycm.completers.completer import Completer

class RhymeCompleter(Completer):
    def SupportedFiletypes(self):
        return ['flow']

    def AsyncCandidateRequestReady(self):
        print('yes!')
        return True

    def CandidateFromStoredRequest(self):
        return ['yes']
