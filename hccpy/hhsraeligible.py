import csv
from pkg_resources import resource_filename as rscfn
        
class RAEligible:

    def __init__(self):
        self.cpts = {}

    def load(self, fn=""):
        if fn == "":
            fn = "data/CY2022_CPTHCPCS_HHS_20230411.csv"
            fn = rscfn(__name__, fn)
        with open(fn, "r", encoding="ISO-8859-1") as fp:
            reader = csv.reader(fp)
            for row in reader:
                if len(row) == 4 and row[3]=="yes":
                    self.cpts[row[0]] = 1

    def is_eligible(self, 
                    pr_lst=[], 
                    billtype="", 
                    claimtype="professional"):
        y = False
        if claimtype == "professional":
            y = self.is_eligible_p(pr_lst)
        elif claimtype == "outpatient":
            if (billtype[:3] in {"131", "137", "711", "717", "731", "737", 
                                 "761", "767", "771", "777", "871", "877"}):
                y = self.is_eligible_p(pr_lst)
        elif claimtype == "inpatient":
            if billtype[:3] in {"111", "117"}:
                y = True
        return y

    def is_eligible_p(self, pr_lst):
        if any((pr in self.cpts) for pr in pr_lst):
            return True
        else:
            return False


