import tkinter
from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("GAMD Chapter 13 Calculator")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.state("zoomed")

countyformatted = StringVar()
countyformatted.set("Bibb County")
meansteststatusformatted = StringVar()
maritalfilingstatussinglesingleformatted = IntVar()
maritalfilingstatusmarriedsingleformatted = IntVar()
maritalfilingstatusmarriedsingleformatted.set("1")
maritalfilingstatusmarriedmarriedformatted = IntVar()
householdsizeformatted = IntVar()
householdsizeformatted.set("5")
householdover65formatted = IntVar()
householdover65formatted.set("1")
householdunder18formatted = IntVar()
householdunder18formatted.set("2")
averagemonthlyincomeformatted = DoubleVar()
averagemonthlyincomeformatted.set("18000.00")
maritaladjustmentformatted = DoubleVar()
maritaladjustmentformatted.set("2000.00")
currentmonthlyincomeformatted = DoubleVar()
currentmonthlyincomeformatted.set("0.00")
childsupportreceivedformatted = DoubleVar()
childsupportreceivedformatted.set("1000.00")
housequeryformatted = StringVar()
housequeryformatted.set("Yes")
housevalueformatted = DoubleVar()
housevalueformatted.set("150000.00")
firstmortgagequeryformatted = StringVar()
firstmortgagequeryformatted.set("Yes")
firstmortgagenameformatted = StringVar()
firstmortgagenameformatted.set("Wells Fargo")
firstmortgageamountformatted = DoubleVar()
firstmortgageamountformatted.set("125000.00")
firstmortgagecurrentpaymentformatted = DoubleVar()
firstmortgagecurrentpaymentformatted.set("1500.00")
firstmortgagearrearsformatted = DoubleVar()
firstmortgagearrearsformatted.set("3000.00")
secondmortgagequeryformatted = StringVar()
secondmortgagequeryformatted.set("Yes")
secondmortgagenameformatted = StringVar()
secondmortgagenameformatted.set("RFCU")
secondmortgageamountformatted = DoubleVar()
secondmortgageamountformatted.set("20000.00")
secondmortgagecurrentpaymentformatted = DoubleVar()
secondmortgagecurrentpaymentformatted.set("300.00")
secondmortgagearrearsformatted = DoubleVar()
secondmortgagearrearsformatted.set("600.00")
houseplantreatmentformatted = StringVar()
houseplantreatmentformatted.set("Retain and Pay")
numberofcarsformatted = IntVar()
numberofcarsformatted.set("2")
car1valueformatted = DoubleVar()
car1valueformatted.set("20000.00")
car1plantreatmentformatted = StringVar()
car1plantreatmentformatted.set("Pay")
car1loanqueryformatted = StringVar()
car1loanqueryformatted.set("Yes")
car1loannameformatted = StringVar()
car1loannameformatted.set("RFCU")
car1loanamountformatted = DoubleVar()
car1loanamountformatted.set("25000.00")
car1loancurrentpaymentformatted = DoubleVar()
car1loancurrentpaymentformatted.set("450.00")
car1loanarrearsformatted = DoubleVar()
car1loanarrearsformatted.set("900.00")
car1910statusformatted = StringVar()
car1910statusformatted.set("No")
car2valueformatted = DoubleVar()
car2valueformatted.set("15000.00")
car2plantreatmentformatted = StringVar()
car2plantreatmentformatted.set("")
car2loanqueryformatted = StringVar()
car2loanqueryformatted.set("Yes")
car2loannameformatted = StringVar()
car2loannameformatted.set("Suntrust")
car2loanamountformatted = DoubleVar()
car2loanamountformatted.set("17000.00")
car2loancurrentpaymentformatted = DoubleVar()
car2loancurrentpaymentformatted.set("250.00")
car2loanarrearsformatted = DoubleVar()
car2loanarrearsformatted.set("500.00")
car2910statusformatted = StringVar()
car2910statusformatted.set("No")
secureddebt1nameformatted = StringVar()
secureddebt1nameformatted.set("IRS")
secureddebt2nameformatted = StringVar()
secureddebt2nameformatted.set("Farmers")
secureddebt3nameformatted = StringVar()
secureddebt3nameformatted.set("World Finance")
secureddebt4nameformatted = StringVar()
secureddebt4nameformatted.set("Capital One")
secureddebt1amountformatted = DoubleVar()
secureddebt1amountformatted.set("27000.00")
secureddebt2amountformatted = DoubleVar()
secureddebt2amountformatted.set("1800.00")
secureddebt3amountformatted = DoubleVar()
secureddebt3amountformatted.set("750.00")
secureddebt4amountformatted = DoubleVar()
secureddebt4amountformatted.set("11000.00")
secureddebt1collateralvalueformatted = DoubleVar()
secureddebt1collateralvalueformatted.set("27000.00")
secureddebt2collateralvalueformatted = DoubleVar()
secureddebt2collateralvalueformatted.set("200.00")
secureddebt3collateralvalueformatted = DoubleVar()
secureddebt3collateralvalueformatted.set("100.00")
secureddebt4collateralvalueformatted = DoubleVar()
secureddebt4collateralvalueformatted.set("27000.00")
secureddebt1typeformatted = StringVar()
secureddebt1typeformatted.set("Lien")
secureddebt2typeformatted = StringVar()
secureddebt2typeformatted.set("PMSI")
secureddebt3typeformatted = StringVar()
secureddebt3typeformatted.set("NPPMSI")
secureddebt4typeformatted = StringVar()
secureddebt4typeformatted.set("Judgment")
secureddebt1treatmentformatted = StringVar()
secureddebt1treatmentformatted.set("Retain and Pay")
secureddebt2treatmentformatted = StringVar()
secureddebt2treatmentformatted.set("Cramdown")
secureddebt3treatmentformatted = StringVar()
secureddebt3treatmentformatted.set("Avoid")
secureddebt4treatmentformatted = StringVar()
secureddebt4treatmentformatted.set("Avoid")
priorityclaimstotalformatted = DoubleVar()
priorityclaimstotalformatted.set("3800.00")
generalunsecuredclaimsformatted = DoubleVar()
generalunsecuredclaimsformatted.set("52000.00")
attorneysfeeformatted = DoubleVar()
attorneysfeeformatted.set("3250.00")
chapter7dividendformatted = DoubleVar()
chapter7dividendformatted.set("7000.00")
toydividendformatted = DoubleVar()
toydividendformatted.set("4500.00")
scheduleiline12formatted = DoubleVar()
scheduleiline12formatted.set("18000.00")
schedulejline22cformatted = DoubleVar()
schedulejline22cformatted.set("15000.00")
mtline6formatted = DoubleVar()
mtline6formatted.set("0.00")
mtline7formatted = DoubleVar()
mtline7formatted.set("0.00")
mtline8formatted = DoubleVar()
mtline8formatted.set("0.00")
mtline9formatted = DoubleVar()
mtline9formatted.set("0.00")
mtline12formatted = DoubleVar()
mtline12formatted.set("0.00")
mtline13cformatted = DoubleVar()
mtline13cformatted.set("0.00")
mtline13fformatted = DoubleVar()
mtline13fformatted.set("0.00")
mtline16formatted = DoubleVar()
mtline16formatted.set("3000.00")
mtline17formatted = DoubleVar()
mtline17formatted.set("155.55")
mtline18formatted = DoubleVar()
mtline18formatted.set("52.00")
mtline19formatted = DoubleVar()
mtline19formatted.set("0.00")
mtline20formatted = DoubleVar()
mtline20formatted.set("0.00")
mtline21formatted = DoubleVar()
mtline21formatted.set("800.00")
mtline22formatted = DoubleVar()
mtline22formatted.set("0.00")
mtline23formatted = DoubleVar()
mtline23formatted.set("0.00")
mtline25formatted = DoubleVar()
mtline25formatted.set("525.00")
mtline26formatted = DoubleVar()
mtline26formatted.set("0.00")
mtline27formatted = DoubleVar()
mtline27formatted.set("0.00")
mtline28formatted = DoubleVar()
mtline28formatted.set("0.00")
mtline29formatted = DoubleVar()
mtline29formatted.set("0.00")
mtline30formatted = DoubleVar()
mtline30formatted.set("0.00")
mtline31formatted = DoubleVar()
mtline31formatted.set("200.00")
mtline33aformatted = DoubleVar()
mtline33aformatted.set("0.00")
mtline33bcformatted = DoubleVar()
mtline33bcformatted.set("0.00")
mtline33eformatted = DoubleVar()
mtline33eformatted.set("0.00")
mtline34formatted = DoubleVar()
mtline34formatted.set("0.00")
mtline35formatted = DoubleVar()
mtline35formatted.set("0.00")
mtline36aformatted = DoubleVar()
mtline36aformatted.set("0.00")
mtline36bformatted = DoubleVar()
mtline36bformatted.set("0.00")
mtline41formatted = DoubleVar()
mtline41formatted.set("625.00")
meanstestdeductionsformatted = DoubleVar()
meanstestdeductionsformatted.set("0.00")
monthlydisposableincomeformatted = DoubleVar()
monthlydisposableincomeformatted.set("0.00")
planlongtermdebtarrearspaymentformatted = DoubleVar()
planlongtermdebtarrearspaymentformatted.set("0.00")
plansecurednocramdownformatted = DoubleVar()
plansecurednocramdownformatted.set("0.00")
plansecuredcramdownformatted = DoubleVar()
plansecuredcramdownformatted.set("0.00")
planattorneysfeesformatted = DoubleVar()
planattorneysfeesformatted.set("0.00")
plantrusteefeesformatted = DoubleVar()
plantrusteefeesformatted.set("0.00")
planpriorityclaimsformatted = DoubleVar()
planpriorityclaimsformatted.set("0.00")
plangeneralunsecuredclaimsformatted = DoubleVar()
plangeneralunsecuredclaimsformatted.set("0.00")
plangeneralunsecuredclaimsbasisformatted = StringVar()
plangeneralunsecuredclaimsbasisformatted.set("(None)")
plantotalmonthlycostformatted = DoubleVar()
plantotalmonthlycostformatted.set("0.00")

def yes0():
    houseplantreatmentpay.config(state="normal")
    houseplantreatmentsurrender.config(state="normal")
    houseplantreatmentlabel.config(state="normal")

def no0():
    housevalueentry.config(state="disabled")
    housevalueentry.config(state="disabled")
    housevaluelabel.config(state="disabled")
    firstmortgagequeryformatted.set("")
    firstmortgagequeryentryyes.config(state="disabled")
    firstmortgagequeryentryno.config(state="disabled")
    firstmortgagequerylabel.config(state="disabled")
    firstmortgagenameentry.config(state="disabled")
    firstmortgagenamelabel.config(state="disabled")
    firstmortgageamountlabel.config(state="disabled")
    firstmortgageamountentry.config(state="disabled")
    firstmortgagecurrentpaymententry.config(state="disabled")
    firstmortgagecurrentpaymentlabel.config(state="disabled")
    firstmortgagearrearsentry.config(state="disabled")
    firstmortgagearrearslabel.config(state="disabled")
    secondmortgagequeryformatted.set("")
    secondmortgagequeryentryyes.config(state="disabled")
    secondmortgagequeryentryno.config(state="disabled")
    secondmortgagequerylabel.config(state="disabled")
    secondmortgagenameentry.config(state="disabled")
    secondmortgagenamelabel.config(state="disabled")
    secondmortgageamountlabel.config(state="disabled")
    secondmortgageamountentry.config(state="disabled")
    secondmortgagecurrentpaymententry.config(state="disabled")
    secondmortgagecurrentpaymentlabel.config(state="disabled")
    secondmortgagearrearsentry.config(state="disabled")
    secondmortgagearrearslabel.config(state="disabled")

def yes1():
    firstmortgagenameentry.config(state="normal")
    firstmortgagenamelabel.config(state="normal")
    firstmortgageamountlabel.config(state="normal")
    firstmortgageamountentry.config(state="normal")
    firstmortgagecurrentpaymententry.config(state="normal")
    firstmortgagecurrentpaymentlabel.config(state="normal")
    firstmortgagearrearsentry.config(state="normal")
    firstmortgagearrearslabel.config(state="normal")
    secondmortgagequeryentryyes.config(state="normal")
    secondmortgagequeryentryno.config(state="normal")
    secondmortgagequerylabel.config(state="normal")

def no1():
    firstmortgagenameentry.config(state="disabled")
    firstmortgagenamelabel.config(state="disabled")
    firstmortgageamountlabel.config(state="disabled")
    firstmortgageamountentry.config(state="disabled")
    firstmortgagecurrentpaymententry.config(state="disabled")
    firstmortgagecurrentpaymentlabel.config(state="disabled")
    firstmortgagearrearsentry.config(state="disabled")
    firstmortgagearrearslabel.config(state="disabled")
    secondmortgagequeryformatted.set("")
    secondmortgagequeryentryyes.config(state="disabled")
    secondmortgagequeryentryno.config(state="disabled")
    secondmortgagequerylabel.config(state="disabled")

def yes2():
    secondmortgagenameentry.config(state="normal")
    secondmortgagenamelabel.config(state="normal")
    secondmortgageamountlabel.config(state="normal")
    secondmortgageamountentry.config(state="normal")
    secondmortgagecurrentpaymententry.config(state="normal")
    secondmortgagecurrentpaymentlabel.config(state="normal")
    secondmortgagearrearsentry.config(state="normal")
    secondmortgagearrearslabel.config(state="normal")

def no2():
    secondmortgagenameentry.config(state="disabled")
    secondmortgagenamelabel.config(state="disabled")
    secondmortgageamountlabel.config(state="disabled")
    secondmortgageamountentry.config(state="disabled")
    secondmortgagecurrentpaymententry.config(state="disabled")
    secondmortgagecurrentpaymentlabel.config(state="disabled")
    secondmortgagearrearsentry.config(state="disabled")
    secondmortgagearrearslabel.config(state="disabled")

def yes3():
    car1loannameentry.config(state="normal")
    car1loannamelabel.config(state="normal")
    car1loanamountlabel.config(state="normal")
    car1loanamountentry.config(state="normal")
    car1loancurrentpaymententry.config(state="normal")
    car1loancurrentpaymentlabel.config(state="normal")
    car1loanarrearsentry.config(state="normal")
    car1loanarrearslabel.config(state="normal")
    car1910querylabel.config(state="normal")
    car1910queryno.config(state="normal")
    car1910queryyes.config(state="normal")

def no3():
    car1loannameentry.config(state="disabled")
    car1loannamelabel.config(state="disabled")
    car1loanamountlabel.config(state="disabled")
    car1loanamountentry.config(state="disabled")
    car1loancurrentpaymententry.config(state="disabled")
    car1loancurrentpaymentlabel.config(state="disabled")
    car1loanarrearsentry.config(state="disabled")
    car1loanarrearslabel.config(state="disabled")
    car1910querylabel.config(state="disabled")
    car1910queryno.config(state="disabled")
    car1910queryyes.config(state="disabled")

def yes4():
    car2loannameentry.config(state="normal")
    car2loannamelabel.config(state="normal")
    car2loanamountlabel.config(state="normal")
    car2loanamountentry.config(state="normal")
    car2loancurrentpaymententry.config(state="normal")
    car2loancurrentpaymentlabel.config(state="normal")
    car2loanarrearsentry.config(state="normal")
    car2loanarrearslabel.config(state="normal")
    car2910querylabel.config(state="normal")
    car2910queryyes.config(state="normal")
    car2910queryno.config(state="normal")

def no4():
    car2loannameentry.config(state="disabled")
    car2loannamelabel.config(state="disabled")
    car2loanamountlabel.config(state="disabled")
    car2loanamountentry.config(state="disabled")
    car2loancurrentpaymententry.config(state="disabled")
    car2loancurrentpaymentlabel.config(state="disabled")
    car2loanarrearsentry.config(state="disabled")
    car2loanarrearslabel.config(state="disabled")
    car2910querylabel.config(state="disabled")
    car2910queryyes.config(state="disabled")
    car2910queryno.config(state="disabled")

def car0():
    return

def car1():
    car1plantreatmentlabel.config(state="normal")
    car1plantreatmentpay.config(state="normal")
    car1plantreatmentsurrender.config(state="normal")

def car2():
    car1plantreatmentlabel.config(state="normal")
    car1plantreatmentpay.config(state="normal")
    car1plantreatmentsurrender.config(state="normal")
    car2plantreatmentlabel.config(state="normal")
    car2plantreatmentpay.config(state="normal")
    car2plantreatmentsurrender.config(state="normal")

def lock0():
    shortmeanstestbutton.config(state="disabled")
    countyentry.config(state="disabled")
    countylabel.config(state="disabled")
    householdsizeentry.config(state="disabled")
    householdsizelabel.config(state="disabled")
    filingstatuslabel.config(state="disabled")
    filingstatusmarriedcheckbutton.config(state="disabled")
    filingstatusmarriedsinglecheckbutton.config(state="disabled")
    filingstatussinglesinglecheckbutton.config(state="disabled")
    householdover65label.config(state="disabled")
    householdover65entry.config(state="disabled")
    householdunder18label.config(state="disabled")
    householdunder18entry.config(state="disabled")
    averagemonthlyincomeentry.config(state="disabled")
    averagemonthlyincomelabel.config(state="disabled")
    maritaladjustmentlabel.config(state="disabled")
    maritaladjustmententry.config(state="disabled")
    currentmonthlyincomelabel.config(state="disabled")
    currentmonthlyincomeentry.config(state="disabled")
    childsupportreceivedentry.config(state="disabled")
    childsupportreceivedlabel.config(state="disabled")

def unlock0():
    housequeryentryyes.config(state="normal")
    housequeryentryno.config(state="normal")
    housequerylabel.config(state="normal")
    numberofcarslabel.config(state="normal")
    numberofcarsentry0.config(state="normal")
    numberofcarsentry1.config(state="normal")
    numberofcarsentry2.config(state="normal")
    priorityclaimstotalentry.config(state="normal")
    priorityclaimstotallabel.config(state="normal")
    generalunsecuredentry.config(state="normal")
    generalunsecuredlabel.config(state="normal")
    attorneysfeeentry.config(state="normal")
    attorneysfeelabel.config(state="normal")
    scheduleiline12entry.config(state="normal")
    scheduleiline12label.config(state="normal")
    schedulejline22centry.config(state="normal")
    schedulejline22clabel.config(state="normal")

def unlock1():
    meanstestfoodclothingandotheritemslabel.config(state="normal")
    meanstestoutofpockethealthcarelabel.config(state="normal")
    meanstesthousingandutilitiesinsuranceandoperatinglabel.config(state="normal")
    meanstesthousingandutilitiesmortgageorrentlabel.config(state="normal")
    meanstestvehicleoperationexpenselabel.config(state="normal")
    meanstestvehicleownershiporleaselabel1.config(state="normal")
    meanstestvehicleownershiporleaselabel2.config(state="normal")
    meanstesttaxeslabel.config(state="normal")
    meanstesttaxesentry.config(state="normal")
    meanstestinvoluntarydeductionslabel.config(state="normal")
    meanstestinvoluntarydeductionsentry.config(state="normal")
    meanstestlifeinsuranceentry.config(state="normal")
    meanstestlifeinsurancelabel.config(state="normal")
    meanstestcourtorderedpaymentsentry.config(state="normal")
    meanstestcourtorderedpaymentslabel.config(state="normal")
    meanstesteducationentry.config(state="normal")
    meanstesteducationlabel.config(state="normal")
    meanstestchildcareentry.config(state="normal")
    meanstestchildcarelabel.config(state="normal")
    meanstestadditionalhealthcareexpensesentry.config(state="normal")
    meanstestadditionalhealthcareexpenseslabel.config(state="normal")
    meanstestoptionalphoneservicelabel.config(state="normal")
    meanstestoptionalphoneserviceentry.config(state="normal")
    meanstesthealthinsuranceentry.config(state="normal")
    meanstesthealthinsurancelabel.config(state="normal")
    meanstestcontinuingcontributionstocareentry.config(state="normal")
    meanstestcontinuingcontributionstocarelabel.config(state="normal")
    meanstestprotectionagainstfamilyvioilenceentry.config(state="normal")
    meanstestprotectionagainstfamilyviolencelabel.config(state="normal")
    meanstestadditionalhomeenergyentry.config(state="normal")
    meanstestadditionalhomeenergylabel.config(state="normal")
    meanstestdependenteducationalentry.config(state="normal")
    meanstestdependenteducationallabel.config(state="normal")
    meanstestadditionalfoodandclothingentry.config(state="normal")
    meanstestadditionalfoodandclothinglabel.config(state="normal")
    meanstestcharitablecontributionslabel.config(state="normal")
    meanstestcharitablecontributionsentry.config(state="normal")
    meanstestsecureddebtmortgageslabel.config(state="normal")
    meanstestsecureddebtcarslabel.config(state="normal")
    meanstestothersecureddebtslabel.config(state="normal")
    meanstestsecuredarrearslabel.config(state="normal")
    meanstestpriorityclaimslabel.config(state="normal")
    meanstestprojectedadminexpenselabel.config(state="normal")
    meanstestchildsupportdeductionlabel.config(state="normal")
    meanstestretirementdeductionentry.config(state="normal")
    meanstestretirementdeductionlabel.config(state="normal")
    othersecureddebtamountlabel.config(state="normal")
    secureddebt1amountentry.config(state="normal")
    secureddebt2amountentry.config(state="normal")
    secureddebt3amountentry.config(state="normal")
    secureddebt4amountentry.config(state="normal")
    othersecureddebtcollaterallabel.config(state="normal")
    secureddebt1collateralentry.config(state="normal")
    secureddebt2collateralentry.config(state="normal")
    secureddebt3collateralentry.config(state="normal")
    secureddebt4collateralentry.config(state="normal")
    othersecureddebtnamelabel.config(state="normal")
    secureddebt1nameentry.config(state="normal")
    secureddebt2nameentry.config(state="normal")
    secureddebt3nameentry.config(state="normal")
    secureddebt4nameentry.config(state="normal")
    othersecureddebttypelabel.config(state="normal")
    secureddebt1typeentryjudgment.config(state="normal")
    secureddebt2typeentryjudgment.config(state="normal")
    secureddebt3typeentryjudgment.config(state="normal")
    secureddebt4typeentryjudgment.config(state="normal")
    secureddebt1typeentrypmsi.config(state="normal")
    secureddebt2typeentrypmsi.config(state="normal")
    secureddebt3typeentrypmsi.config(state="normal")
    secureddebt4typeentrypmsi.config(state="normal")
    secureddebt1typeentrynppmsi.config(state="normal")
    secureddebt2typeentrynppmsi.config(state="normal")
    secureddebt3typeentrynppmsi.config(state="normal")
    secureddebt4typeentrynppmsi.config(state="normal")
    secureddebt1typeentrylien.config(state="normal")
    secureddebt2typeentrylien.config(state="normal")
    secureddebt3typeentrylien.config(state="normal")
    secureddebt4typeentrylien.config(state="normal")
    othersecureddebttreatmentlabel.config(state="normal")
    secureddebt1treatmentavoidentry.config(state="normal")
    secureddebt1treatmentcdentry.config(state="normal")
    secureddebt1treatmentrpentry.config(state="normal")
    secureddebt1treatmentsurrenderentry.config(state="normal")
    secureddebt2treatmentavoidentry.config(state="normal")
    secureddebt2treatmentcdentry.config(state="normal")
    secureddebt2treatmentrpentry.config(state="normal")
    secureddebt2treatmentsurrenderentry.config(state="normal")
    secureddebt3treatmentavoidentry.config(state="normal")
    secureddebt3treatmentcdentry.config(state="normal")
    secureddebt3treatmentrpentry.config(state="normal")
    secureddebt3treatmentsurrenderentry.config(state="normal")
    secureddebt4treatmentavoidentry.config(state="normal")
    secureddebt4treatmentcdentry.config(state="normal")
    secureddebt4treatmentrpentry.config(state="normal")
    secureddebt4treatmentsurrenderentry.config(state="normal")
    chapter7dividendentry.config(state="normal")
    chapter7dividendlabel.config(state="normal")
    toydividendentry.config(state="normal")
    toydividendlabel.config(state="normal")

def married():
    if maritalfilingstatusmarriedsingleformatted.get() == 1:
        maritaladjustmentlabel.config(state="normal")
        maritaladjustmententry.config(state="normal")
    if maritalfilingstatusmarriedsingleformatted.get() == 0:
        maritaladjustmentlabel.config(state="disabled")
        maritaladjustmententry.config(state="disabled")
        a = averagemonthlyincomeformatted.get()
        currentmonthlyincomeformatted.set(a)

def houseretainandpay():
    housevalueentry.config(state="normal")
    housevaluelabel.config(state="normal")
    firstmortgagequeryentryyes.config(state="normal")
    firstmortgagequeryentryno.config(state="normal")
    firstmortgagequerylabel.config(state="normal")

def car1retainandpay():
    car1valueentry.config(state="normal")
    car1valuelabel.config(state="normal")
    car1loanquerylabel.config(state="normal")
    car1loanqueryentryyes.config(state="normal")
    car1loanqueryentryno.config(state="normal")

def car1surrender():
    car1valueentry.config(state="disabled")
    car1valuelabel.config(state="disabled")
    car1loanquerylabel.config(state="disabled")
    car1loanqueryentryyes.config(state="disabled")
    car1loanqueryentryno.config(state="disabled")

def car2retainandpay():
    car2valueentry.config(state="normal")
    car2valuelabel.config(state="normal")
    car2loanquerylabel.config(state="normal")
    car2loanqueryentryyes.config(state="normal")
    car2loanqueryentryno.config(state="normal")

def car2surrender():
    car2valueentry.config(state="disabled")
    car2valuelabel.config(state="disabled")
    car2loanquerylabel.config(state="disabled")
    car2loanqueryentryyes.config(state="disabled")
    car2loanqueryentryno.config(state="disabled")

def form122c2():
    global meanstestdeductionsformatted
    meanstestdeductions = float(0)
    householdsizeget = int(householdsizeformatted.get())
    mtline6 = float(0)
    mtline7 = float(0)

    natstan0 = [0.00, 723.00, 1292.00, 1473.00, 1740.00]
    if householdsizeget <= 4:
        mtline6 = natstan0[householdsizeget]
        mtline6 = round(mtline6, 2)
    elif householdsizeget > 4:
        mtline6 = 1740.00 + ((householdsizeget - 4) * 341)
        mtline6 = round(mtline6, 2)

    mtline6formatted.set(mtline6)

    meanstestdeductions += mtline6

    householdover65 = float(householdover65formatted.get())
    mtline7 = (householdover65 * 142.00) + ((float(householdsizeget) - householdover65) * 68.00)

    mtline7formatted.set(mtline7)

    meanstestdeductions += mtline7

    countyget = countyformatted.get()

    r0 = requests.get('https://www.justice.gov/ust/eo/bapcpa/20210515/bci_data/housing_charts/irs_housing_charts_GA.htm')
    r1 = r0.text
    soup = BeautifulSoup(r1, 'html.parser')
    housingoperating0 = soup.find("td", class_="hctablecellleft", string=countyget)
    housingoperating1 = housingoperating0.find_next_siblings("td")
    housingoperating1person = float(str(housingoperating1[1].string.extract()).replace("$", "").replace(",", ""))
    housingoperating2people = float(str(housingoperating1[3].string.extract()).replace("$", "").replace(",", ""))
    housingoperating3people = float(str(housingoperating1[5].string.extract()).replace("$", "").replace(",", ""))
    housingoperating4people = float(str(housingoperating1[7].string.extract()).replace("$", "").replace(",", ""))
    housingoperating5people = float(str(housingoperating1[9].string.extract()).replace("$", "").replace(",", ""))
    if householdsizeget == 1:
        mtline8 = housingoperating1person
        mtline8formatted.set(mtline8)
    elif householdsizeget == 2:
        mtline8 = housingoperating2people
        mtline8formatted.set(mtline8)
    elif householdsizeget == 3:
        mtline8 = housingoperating3people
        mtline8formatted.set(mtline8)
    elif householdsizeget == 4:
        mtline8 = housingoperating4people
        mtline8formatted.set(mtline8)
    elif householdsizeget >= 5:
        mtline8 = housingoperating5people
        mtline8formatted.set(mtline8)

    housingmortgageandrent1person = float(str(housingoperating1[2].string.extract()).replace("$", "").replace(",", ""))
    housingmortgageandrent2people = float(str(housingoperating1[4].string.extract()).replace("$", "").replace(",", ""))
    housingmortgageandrent3people = float(str(housingoperating1[6].string.extract()).replace("$", "").replace(",", ""))
    housingmortgageandrent4people = float(str(housingoperating1[8].string.extract()).replace("$", "").replace(",", ""))
    housingmortgageandrent5people = float(str(housingoperating1[10].string.extract()).replace("$", "").replace(",", ""))
    claimedmortgage1person = housingmortgageandrent1person - firstmortgagecurrentpaymentformatted.get() - secondmortgagecurrentpaymentformatted.get()
    claimedmortgage2people = housingmortgageandrent2people - firstmortgagecurrentpaymentformatted.get() - secondmortgagecurrentpaymentformatted.get()
    claimedmortgage3people = housingmortgageandrent3people - firstmortgagecurrentpaymentformatted.get() - secondmortgagecurrentpaymentformatted.get()
    claimedmortgage4people = housingmortgageandrent4people - firstmortgagecurrentpaymentformatted.get() - secondmortgagecurrentpaymentformatted.get()
    claimedmortgage5people = housingmortgageandrent5people - firstmortgagecurrentpaymentformatted.get() - secondmortgagecurrentpaymentformatted.get()
    if householdsizeget == 1:
        if claimedmortgage1person < 0:
            claimedmortgage1person = 0
        mtline9 = float(claimedmortgage1person)
        mtline9formatted.set(mtline9)
        meanstestdeductions += (claimedmortgage1person + housingoperating1person)
    elif householdsizeget == 2:
        if claimedmortgage2people < 0:
            claimedmortgage2people = 0
        mtline9 = float(claimedmortgage2people)

        mtline9formatted.set(mtline9)
        meanstestdeductions += (claimedmortgage2people + housingoperating2people)
    elif householdsizeget == 3:
        if claimedmortgage3people < 0:
            claimedmortgage3people = 0
        mtline9 = float(claimedmortgage3people)
        mtline9formatted.set(mtline9)
        meanstestdeductions += (claimedmortgage3people + housingoperating3people)
    elif householdsizeget == 4:
        if claimedmortgage4people < 0:
            claimedmortgage4people = 0
        mtline9 = float(claimedmortgage4people)
        mtline9formatted.set(mtline9)
        meanstestdeductions += (claimedmortgage4people + housingoperating4people)
    elif householdsizeget >= 5:
        if claimedmortgage5people < 0:
            claimedmortgage5people = 0
        mtline9 = float(claimedmortgage5people)
        mtline9formatted.set(mtline9)
        meanstestdeductions += (claimedmortgage5people + housingoperating5people)

    if numberofcarsformatted.get() == 0:
        mtline12 = 217.00
        mtline12formatted.set(mtline12)
        meanstestdeductions += 217.00
    elif numberofcarsformatted.get() == 1:
        if countyget in ["Butts County", "Jasper County", "Lamar County", "Morgan County", "Walton County"]:
            mtline12 = 251.00
            mtline12formatted.set(mtline12)
            meanstestdeductions += 251.00
        else:
            mtline12 = 224.00
            mtline12formatted.set(mtline12)
            meanstestdeductions += 224.00
    elif numberofcarsformatted.get() == 2:
        if countyget in ["Butts County", "Jasper County", "Lamar County", "Morgan County", "Walton County"]:
            mtline12 = 502.00
            mtline12formatted.set(mtline12)
            meanstestdeductions += 502.00
        else:
            mtline12 = 448.00
            mtline12formatted.set(mtline12)
            meanstestdeductions += 448.00

    if numberofcarsformatted.get() == 1:
        claimedcar1 = float(533.00) - float(car1loanamountformatted.get()) / 60.00
        claimedcar1 = round(claimedcar1, 2)
        if claimedcar1 < 0:
            claimedcar1 = 0
        mtline13c = claimedcar1
        mtline13cformatted.set(mtline13c)
        meanstestdeductions += mtline13c
    if numberofcarsformatted.get() == 2:
        claimedcar1 = float(533.00) - float(car1loanamountformatted.get()) / 60.00
        claimedcar1 = round(claimedcar1, 2)
        if claimedcar1 < 0:
            claimedcar1 = 0
        mtline13c = claimedcar1
        mtline13cformatted.set(mtline13c)
        claimedcar2 = float(533.00) - float(car2loanamountformatted.get()) / 60.00
        claimedcar2 = round(claimedcar2, 2)
        if claimedcar2 < 0:
            claimedcar2 = 0
        mtline13f = claimedcar2
        mtline13fformatted.set(mtline13f)
        meanstestdeductions += ((float(mtline13c) + float(mtline13f)))

        mtline16 = float(mtline16formatted.get())
        meanstestdeductions += mtline16

        mtline17 = float(mtline17formatted.get())
        meanstestdeductions += mtline17

        mtline18 = float(mtline18formatted.get())
        meanstestdeductions += mtline18

        mtline19 = float(mtline19formatted.get())
        meanstestdeductions += mtline19

        mtline20 = float(mtline20formatted.get())
        meanstestdeductions += mtline20

        mtline21 = float(mtline21formatted.get())
        meanstestdeductions += mtline21

        mtline22 = float(mtline22formatted.get())
        meanstestdeductions += mtline22

        mtline23 = float(mtline23formatted.get())
        meanstestdeductions += mtline23

        mtline25 = float(mtline25formatted.get())
        meanstestdeductions += mtline25

        mtline26 = float(mtline26formatted.get())
        meanstestdeductions += mtline26

        mtline27 = float(mtline27formatted.get())
        meanstestdeductions += mtline27

        mtline28 = float(mtline28formatted.get())
        meanstestdeductions += mtline28

        mtline29 = float(mtline29formatted.get())
        if mtline29 > (170.83 * float(householdunder18formatted.get())):
            mtline29 = (170.83 * float(householdunder18formatted.get()))
            mtline29formatted.set(mtline29)
        meanstestdeductions += mtline29

        mtline30 = float(mtline30formatted.get())
        if mtline30 > round((float(mtline6formatted.get()) * 0.05), 2):
            mtline30 = round((float(mtline6formatted.get()) * 0.05), 2)
            mtline30formatted.set(mtline30)
        meanstestdeductions += mtline30

        mtline31 = float(mtline31formatted.get())
        meanstestdeductions += mtline31

        mtline33a = float(firstmortgagecurrentpaymentformatted.get()) + float(secondmortgagecurrentpaymentformatted.get())
        mtline33aformatted.set(mtline33a)
        mtline33bc = (float(car1loanamountformatted.get()) / 60.00) + (float(car2loanamountformatted.get()) / 60.00)
        mtline33bc = round(mtline33bc, 2)
        mtline33bcformatted.set(mtline33bc)
        mtline33e = ((float(secureddebt1amountformatted.get()) + float(secureddebt2amountformatted.get()) + float(secureddebt3amountformatted.get()) + float(secureddebt4amountformatted.get())) / 60.00)
        mtline33e = round(mtline33e, 2)
        mtline33eformatted.set(mtline33e)
        meanstestdeductions += (float(mtline33aformatted.get()) + float(mtline33bcformatted.get()) + float(mtline33eformatted.get()))

        mtline34 = round((float(firstmortgagearrearsformatted.get()) + float(secondmortgagearrearsformatted.get()) + float(car1loanarrearsformatted.get()) + float(car2loanarrearsformatted.get())) / 60.00, 2)
        mtline34formatted.set(mtline34)
        meanstestdeductions += float(mtline34formatted.get())

        mtline35 = round((priorityclaimstotalformatted.get() / 60.00), 2)
        mtline35formatted.set(mtline35)
        meanstestdeductions += mtline35formatted.get()

        mtline36a = (scheduleiline12formatted.get() - schedulejline22cformatted.get())
        mtline36aformatted.set(mtline36a)

        mtline36b = (mtline36a * 0.06)
        mtline36b = round(mtline36b, 2)
        mtline36bformatted.set(mtline36b)
        meanstestdeductions += mtline36bformatted.get()

        meanstestdeductions += childsupportreceivedformatted.get()

        meanstestdeductions += float(mtline41formatted.get())

        meanstestdeductions = round(meanstestdeductions, 2)

        meanstestdeductionsformatted.set(meanstestdeductions)

        mdi = (float(currentmonthlyincomeformatted.get()) - float(meanstestdeductionsformatted.get()))
        mdi = round(mdi, 2)

        monthlydisposableincomeformatted.set(mdi)


        cmirestatedentry.config(state="readonly")
        cmirestatedlabel.config(state="normal")
        minuslabel.config(state="normal")
        totalmeanstestdeductionsentry.config(state="readonly")
        totalmeanstestdeductionslabel.config(state="normal")
        equallabel.config(state="normal")
        monthlydisposableincomeentry.config(state="readonly")
        monthlydisposableincomelabel.config(state="normal")
        plancostcalcbutton.config(state="normal")

        return

def form122c1():
    currentmonthlyincomeentry.config(state="normal")
    currentmonthlyincomelabel.config(state="normal")

    averagemonthyincome = float(0)
    medianincome = float(0)
    abovemedian = str("")
    householdsizeget = int(0)

    if maritalfilingstatussinglesingleformatted.get() == 1 or maritalfilingstatusmarriedmarriedformatted.get() == 1:
        a = averagemonthlyincomeformatted.get()
        currentmonthlyincomeformatted.set(a)
    if maritalfilingstatusmarriedsingleformatted.get() == 1:
        a = averagemonthlyincomeformatted.get()
        b = maritaladjustmentformatted.get()
        c = float(a) - float(b)
        currentmonthlyincomeformatted.set(c)

    georgia = [float(0), float(53105), float(68295), float(76391), float(92286)]
    householdsizeget = int(householdsizeformatted.get())

    if householdsizeget <= 4:
        medianincome = georgia[householdsizeget]
    elif householdsizeget > 4:
        medianincome = georgia[4] + (9000 * (householdsizeget - 4))

    if medianincome is None:
        meansteststatuslabel.config(background="cyan")
    elif medianincome == 0:
        abovemedian = "No"
        meansteststatuslabel.config(background="green", text="BELOW MEDIAN")
    elif medianincome <= (float(currentmonthlyincomeformatted.get()) * float(12)):
        abovemedian = "Yes"
        meansteststatuslabel.config(background="red", text="ABOVE MEDIAN", width=26)
        longmeanstestbutton.config(state="normal")
        unlock1()
        lock0()
    elif medianincome > (float(currentmonthlyincomeformatted.get()) * float(12)):
        abovemedian = "No"
        meansteststatuslabel.config(background="green", text="BELOW MEDIAN")
    return

def plancostcalc():
    return

contentlevel0 = ttk.Frame(root, borderwidth=10)
contentlevel0.grid(sticky=tkinter.NW, column=0, row=0)
contentlevel0.columnconfigure(0, weight=10)
contentlevel0.rowconfigure(0, weight=10)

# contentlevel1 = ttk.LabelFrame(contentlevel0, borderwidth10)

countyentry = ttk.Combobox(contentlevel0, values=("Baker County", "Baldwin County", "Ben Hill County", "Berrien County",
                                                  "Bibb County", "Bleckley County", "Brooks County", "Butts County",
                                                  "Calhoun County", "Chattahoochee County", "Clarke County", "Clay County",
                                                  "Clinch County", "Colquitt County", "Cook County", "Crawford County",
                                                  "Crisp County", "Decatur County", "Dooly County", "Dougherty County",
                                                  "Early County", "Echols County", "Elbert County", "Franklin County",
                                                  "Grady County", "Greene County", "Hancock County", "Harris County",
                                                  "Hart County", "Houston County", "Irwin County", "Jasper County", "Jones County",
                                                  "Lamar County", "Lanier County", "Lee County", "Lowndes County", "Macon County",
                                                  "Madison County", "Marion County", "Miller County", "Mitchell County",
                                                  "Monroe County", "Morgan County", "Muscogee County", "Oconee County",
                                                  "Oglethorpe", "Peach County", "Pulaski County", "Putnam County", "Quitman County",
                                                  "Randolph County", "Schley County", "Seminole County", "Stewart County",
                                                  "Sumter County", "Talbot County", "Taylor County", "Terrell County",
                                                  "Thomas County", "Tift County", "Turner County", "Twiggs County", "Upson County",
                                                  "Walton County", "Washington County", "Webster County", "Wilcox County",
                                                  "Wilkinson County", "Worth County"), textvariable=countyformatted)
countylabel = ttk.Label(contentlevel0, text="County Name", justify="center")
countylabel.grid(column=0, row=1, pady=5, padx=10)
countyentry.grid(column=0, row=2, pady=5, padx=10)
countyentry.focus()

filingstatuslabel = ttk.Label(contentlevel0, text="Marital/Filing Status", justify="center", state="normal")
filingstatuslabel.grid(column=1, row=1, pady=5, columnspan=3)
filingstatussinglesinglecheckbutton = ttk.Checkbutton(contentlevel0, text="Single/Single", onvalue=1, offvalue=0, variable=maritalfilingstatussinglesingleformatted, state="normal")
filingstatussinglesinglecheckbutton.grid(column=1, row=2, padx=10)
filingstatusmarriedsinglecheckbutton = ttk.Checkbutton(contentlevel0, text="Married/Single", onvalue=1, offvalue=0, variable=maritalfilingstatusmarriedsingleformatted, command=lambda: married(), state="normal")
filingstatusmarriedsinglecheckbutton.grid(column=2, row=2, padx=10)
filingstatusmarriedcheckbutton = ttk.Checkbutton(contentlevel0, text="Married/Married", onvalue=1, offvalue=0, variable=maritalfilingstatusmarriedmarriedformatted, state="normal")
filingstatusmarriedcheckbutton.grid(column=3, row=2, padx=10)

householdsizeentry = ttk.Entry(contentlevel0, textvariable=householdsizeformatted)
householdsizelabel = ttk.Label(contentlevel0, text="Household Size", justify="center")
householdsizelabel.grid(column=0, row=3, pady=5, padx=10)
householdsizeentry.grid(column=0, row=4, pady=5, padx=10)

householdover65entry = ttk.Entry(contentlevel0, textvariable=householdover65formatted)
householdover65label = ttk.Label(contentlevel0, text="Houshold Over 65", justify="center")
householdover65label.grid(column=1, row=3, pady=5, padx=10)
householdover65entry.grid(column=1, row=4, pady=5, padx=10)

householdunder18entry = ttk.Entry(contentlevel0, textvariable=householdunder18formatted)
householdunder18label = ttk.Label(contentlevel0, text="Household Under 18", justify="center")
householdunder18label.grid(column=2, row=3, pady=5, padx=10)
householdunder18entry.grid(column=2, row=4, pady=5, padx=10)

averagemonthlyincomeentry = ttk.Entry(contentlevel0, textvariable=averagemonthlyincomeformatted)
averagemonthlyincomelabel = ttk.Label(contentlevel0, text="Avg. Monthly Income", justify="center")
averagemonthlyincomelabel.grid(column=0, row=5, pady=5, padx=10)
averagemonthlyincomeentry.grid(column=0, row=6, pady=5, padx=10)

maritaladjustmententry = ttk.Entry(contentlevel0, textvariable=maritaladjustmentformatted, state="disabled")
maritaladjustmentlabel = ttk.Label(contentlevel0, text="Marital Adjustment", justify="center", state="disabled")
maritaladjustmentlabel.grid(column=1, row=5, pady=5, padx=10)
maritaladjustmententry.grid(column=1, row=6, pady=5, padx=10)

currentmonthlyincomeentry = ttk.Entry(contentlevel0, textvariable=currentmonthlyincomeformatted, state="disabled")
currentmonthlyincomelabel =ttk.Label(contentlevel0, text="CMI", justify="center", state="disabled")
currentmonthlyincomelabel.grid(column=2, row=5, pady=5, padx=10)
currentmonthlyincomeentry.grid(column=2, row=6, pady=5, padx=10)

childsupportreceivedentry = ttk.Entry(contentlevel0, textvariable=childsupportreceivedformatted)
childsupportreceivedlabel = ttk.Label(contentlevel0, text="CS Portion of CMI", justify="center")
childsupportreceivedlabel.grid(column=3, row=5, pady=5, padx=10)
childsupportreceivedentry.grid(column=3, row=6, pady=5, padx=10)

meansteststatuslabel = ttk.Label(contentlevel0, background="cyan", anchor="center", text="No Means Test Data Entered")
meansteststatuslabel.grid(column=3, row=4, pady=10, padx=10)

shortmeanstestbutton = ttk.Button(contentlevel0, text="1. Run Short Means Test", command=lambda: [form122c1(), unlock0()])
shortmeanstestbutton.grid(column=0, row=7, pady=5, padx=10)

horizontalseparator0 = ttk.Separator(contentlevel0, orient='horizontal')
horizontalseparator0.grid(sticky=EW, row=8, columnspan=25, pady=10)

housequeryentryyes = ttk.Radiobutton(contentlevel0, text="Yes", variable=housequeryformatted, value="Yes", state="disabled", command=yes0)
housequeryentryno = ttk.Radiobutton(contentlevel0, text="No", variable=housequeryformatted, value="No", state="disabled", command=no0)
housequerylabel = ttk.Label(contentlevel0, state="disabled", text="House?")
housequerylabel.grid(column=0, row=9, pady=5)
housequeryentryyes.grid(sticky="W", column=0, row=10)
housequeryentryno.grid(sticky="W", column=0, row=11)

housevalueentry = ttk.Entry(contentlevel0, textvariable=housevalueformatted, state="disabled")
housevaluelabel = ttk.Label(contentlevel0, text="Value of house", state="disabled")
housevaluelabel.grid(column=1, row=9, pady=5)
housevalueentry.grid(column=1, row=10)

houseplantreatmentpay = ttk.Radiobutton(contentlevel0, text="Retain & Pay", variable=houseplantreatmentformatted, value="Pay", command=lambda: houseretainandpay(), state="disabled")
houseplantreatmentsurrender = ttk.Radiobutton(contentlevel0, text="Surrender", variable=houseplantreatmentformatted, value="Surrender", state="disabled")
houseplantreatmentlabel = ttk.Label(contentlevel0, text="Plan Treatment", state="disabled")
houseplantreatmentlabel.grid(column=1, row=13, pady=5)
houseplantreatmentpay.grid(sticky="W", column=1, row=14)
houseplantreatmentsurrender.grid(sticky="W", column=1, row=15)

firstmortgagequeryentryyes = ttk.Radiobutton(contentlevel0, text="Yes", variable=firstmortgagequeryformatted, value="Yes", command=yes1, state="disabled")
firstmortgagequeryentryno = ttk.Radiobutton(contentlevel0, text="No", variable=firstmortgagequeryformatted, value="No", command=no1, state="disabled")
firstmortgagequerylabel = ttk.Label(contentlevel0, text="First mortgage?", state="disabled")
firstmortgagequerylabel.grid(column=2, row=9, pady=5)
firstmortgagequeryentryyes.grid(sticky="W", column=2, row=10)
firstmortgagequeryentryno.grid(sticky="W", column=2, row=11)

firstmortgagenameentry = ttk.Entry(contentlevel0, textvariable=firstmortgagenameformatted, state="disabled")
firstmortgagenamelabel = ttk.Label(contentlevel0, text="First Mortgage Creditor", state="disabled")
firstmortgagenamelabel.grid(column=3, row=9, pady=5)
firstmortgagenameentry.grid(column=3, row=10)

firstmortgageamountentry = ttk.Entry(contentlevel0, textvariable=firstmortgageamountformatted, state="disabled")
firstmortgageamountlabel = ttk.Label(contentlevel0, text="Amount Owed", state="disabled")
firstmortgageamountlabel.grid(column=3, row=11, pady=5)
firstmortgageamountentry.grid(column=3, row=12)

firstmortgagecurrentpaymententry = ttk.Entry(contentlevel0, textvariable=firstmortgagecurrentpaymentformatted, state="disabled")
firstmortgagecurrentpaymentlabel = ttk.Label(contentlevel0, text="Monthly Payment", state="disabled")
firstmortgagecurrentpaymentlabel.grid(column=3, row=13, pady=5)
firstmortgagecurrentpaymententry.grid(column=3, row=14)

firstmortgagearrearsentry = ttk.Entry(contentlevel0, textvariable=firstmortgagearrearsformatted, state="disabled")
firstmortgagearrearslabel = ttk.Label(contentlevel0, text="Arrears", state="disabled")
firstmortgagearrearslabel.grid(column=3, row=15, pady=5)
firstmortgagearrearsentry.grid(column=3, row=16)

secondmortgagequeryentryyes = ttk.Radiobutton(contentlevel0, text="Yes", variable=secondmortgagequeryformatted, value="Yes", command=yes2, state="disabled")
secondmortgagequeryentryno = ttk.Radiobutton(contentlevel0, text="No", variable=secondmortgagequeryformatted, value="No", command=no2, state="disabled")
secondmortgagequerylabel = ttk.Label(contentlevel0, text="Second mortgage?", state="disabled")
secondmortgagequerylabel.grid(column=2, row=17, pady=5)
secondmortgagequeryentryyes.grid(sticky="W", column=2, row=18)
secondmortgagequeryentryno.grid(sticky="W", column=2, row=19)

secondmortgagenameentry = ttk.Entry(contentlevel0, textvariable=secondmortgagenameformatted, state="disabled")
secondmortgagenamelabel = ttk.Label(contentlevel0, text="Second Mortgage Creditor", state="disabled")
secondmortgagenamelabel.grid(column=3, row=17, pady=5)
secondmortgagenameentry.grid(column=3, row=18)

secondmortgageamountentry = ttk.Entry(contentlevel0, textvariable=secondmortgageamountformatted, state="disabled")
secondmortgageamountlabel = ttk.Label(contentlevel0, text="Amount Owed", state="disabled")
secondmortgageamountlabel.grid(column=3, row=19, pady=5)
secondmortgageamountentry.grid(column=3, row=20)

secondmortgagecurrentpaymententry = ttk.Entry(contentlevel0, textvariable=secondmortgagecurrentpaymentformatted, state="disabled")
secondmortgagecurrentpaymentlabel = ttk.Label(contentlevel0, text="Monthly Payment", state="disabled")
secondmortgagecurrentpaymentlabel.grid(column=3, row=21, pady=5)
secondmortgagecurrentpaymententry.grid(column=3, row=22)

secondmortgagearrearsentry = ttk.Entry(contentlevel0, textvariable=secondmortgagearrearsformatted, state="disabled")
secondmortgagearrearslabel = ttk.Label(contentlevel0, text="Arrears", state="disabled")
secondmortgagearrearslabel.grid(column=3, row=23, pady=5)
secondmortgagearrearsentry.grid(column=3, row=24)

numberofcarsentry0 = ttk.Radiobutton(contentlevel0, text="0", state="disabled", variable=numberofcarsformatted, value="0", command=car0)
numberofcarsentry1 = ttk.Radiobutton(contentlevel0, text="1", state="disabled", variable=numberofcarsformatted, value="1", command=car1)
numberofcarsentry2 = ttk.Radiobutton(contentlevel0, text="2", state="disabled", variable=numberofcarsformatted, value="2", command=car2)
numberofcarslabel = ttk.Label(contentlevel0, state="disabled", text="Total number of cars")
numberofcarslabel.grid(column=0, row=25, pady=5)
numberofcarsentry0.grid(sticky="W", column=0, row=26)
numberofcarsentry1.grid(sticky="W", column=0, row=27)
numberofcarsentry2.grid(sticky="W", column=0, row=28)

car1valueentry = ttk.Entry(contentlevel0, textvariable=car1valueformatted, state="disabled")
car1valuelabel = ttk.Label(contentlevel0, text="Value of Car #1", state="disabled")
car1valuelabel.grid(column=1, row=25, pady=5)
car1valueentry.grid(column=1, row=26)

car1plantreatmentpay = ttk.Radiobutton(contentlevel0, text="Retain & Pay", variable=car1plantreatmentformatted, value="Pay", command=lambda: car1retainandpay(), state="disabled")
car1plantreatmentsurrender = ttk.Radiobutton(contentlevel0, text="Surrender", variable=car1plantreatmentformatted, value="Surrender", command=lambda: car1surrender(), state="disabled")
car1plantreatmentlabel = ttk.Label(contentlevel0, text="Plan Treatment", state="disabled")
car1plantreatmentlabel.grid(column=1, row=28, pady=5)
car1plantreatmentpay.grid(sticky="W", column=1, row=29)
car1plantreatmentsurrender.grid(sticky="W", column=1, row=30)

car1loanqueryentryyes = ttk.Radiobutton(contentlevel0, text="Yes", variable=car1loanqueryformatted, value="Yes", command=yes3, state="disabled")
car1loanqueryentryno = ttk.Radiobutton(contentlevel0, text="No", variable=car1loanqueryformatted, value="No", command=no3, state="disabled")
car1loanquerylabel = ttk.Label(contentlevel0, text="Loan on Car #1?", state="disabled")
car1loanquerylabel.grid(column=2, row=25, pady=5)
car1loanqueryentryyes.grid(sticky="W", column=2, row=26)
car1loanqueryentryno.grid(sticky="W", column=2, row=27)

car1910queryyes = ttk.Radiobutton(contentlevel0, text="Yes", variable=car1910statusformatted, state="disabled", value="Yes")
car1910queryno = ttk.Radiobutton(contentlevel0, text="No", variable=car1910statusformatted, state="disabled", value="No")
car1910querylabel = ttk.Label(contentlevel0, text="910 claim?", state="disabled")
car1910querylabel.grid(column=2, row=28, pady=5)
car1910queryyes.grid(sticky="W", column=2, row=29)
car1910queryno.grid(sticky="W", column=2, row=30)

car1loannameentry = ttk.Entry(contentlevel0, textvariable=car1loannameformatted, state="disabled")
car1loannamelabel = ttk.Label(contentlevel0, text="Car #1 Creditor", state="disabled")
car1loannamelabel.grid(column=3, row=25, pady=5)
car1loannameentry.grid(column=3, row=26)

car1loanamountentry = ttk.Entry(contentlevel0, textvariable=car1loanamountformatted, state="disabled")
car1loanamountlabel = ttk.Label(contentlevel0, text="Amount Owed", state="disabled")
car1loanamountlabel.grid(column=3, row=27, pady=5)
car1loanamountentry.grid(column=3, row=28)

car1loancurrentpaymententry = ttk.Entry(contentlevel0, textvariable=car1loancurrentpaymentformatted, state="disabled")
car1loancurrentpaymentlabel = ttk.Label(contentlevel0, text="Monthly Payment", state="disabled")
car1loancurrentpaymentlabel.grid(column=3, row=29, pady=5)
car1loancurrentpaymententry.grid(column=3, row=30)

car1loanarrearsentry = ttk.Entry(contentlevel0, textvariable=car1loanarrearsformatted, state="disabled")
car1loanarrearslabel = ttk.Label(contentlevel0, text="Arrears", state="disabled")
car1loanarrearslabel.grid(column=3, row=31, pady=5)
car1loanarrearsentry.grid(column=3, row=32)

car2valueentry = ttk.Entry(contentlevel0, textvariable=car2valueformatted, state="disabled")
car2valuelabel = ttk.Label(contentlevel0, text="Value of Car #2", state="disabled")
car2valuelabel.grid(column=1, row=34, pady=5)
car2valueentry.grid(column=1, row=35)

car2plantreatmentpay = ttk.Radiobutton(contentlevel0, text="Retain & Pay", variable=car2plantreatmentformatted, value="Pay", command=lambda: car2retainandpay(), state="disabled")
car2plantreatmentsurrender = ttk.Radiobutton(contentlevel0, text="Surrender", variable=car2plantreatmentformatted, value="Surrender", command=lambda: car2surrender(), state="disabled")
car2plantreatmentlabel = ttk.Label(contentlevel0, text="Plan Treatment", state="disabled")
car2plantreatmentlabel.grid(column=1, row=37, pady=5)
car2plantreatmentpay.grid(sticky="W", column=1, row=38)
car2plantreatmentsurrender.grid(sticky="W", column=1, row=39)

car2loanqueryentryyes = ttk.Radiobutton(contentlevel0, text="Yes", variable=car2loanqueryformatted, value="Yes", command=yes4, state="disabled")
car2loanqueryentryno = ttk.Radiobutton(contentlevel0, text="No", variable=car2loanqueryformatted, value="No", command=no4, state="disabled")
car2loanquerylabel = ttk.Label(contentlevel0, text="Loan on Car #2?", state="disabled")
car2loanquerylabel.grid(column=2, row=34, pady=5)
car2loanqueryentryyes.grid(sticky="W", column=2, row=35)
car2loanqueryentryno.grid(sticky="W", column=2, row=36)

car2910queryyes = ttk.Radiobutton(contentlevel0, text="Yes", variable=car2910statusformatted, state="disabled", value="Yes")
car2910queryno = ttk.Radiobutton(contentlevel0, text="No", variable=car2910statusformatted, state="disabled", value="No")
car2910querylabel = ttk.Label(contentlevel0, text="910 claim?", state="disabled")
car2910querylabel.grid(column=2, row=37, pady=5)
car2910queryyes.grid(sticky="W", column=2, row=38)
car2910queryno.grid(sticky="W", column=2, row=39)

car2loannameentry = ttk.Entry(contentlevel0, textvariable=car2loannameformatted, state="disabled")
car2loannamelabel = ttk.Label(contentlevel0, text="Car #2 Creditor", state="disabled")
car2loannamelabel.grid(column=3, row=34, pady=5)
car2loannameentry.grid(column=3, row=35)

car2loanamountentry = ttk.Entry(contentlevel0, textvariable=car2loanamountformatted, state="disabled")
car2loanamountlabel = ttk.Label(contentlevel0, text="Amount Owed", state="disabled")
car2loanamountlabel.grid(column=3, row=36, pady=5)
car2loanamountentry.grid(column=3, row=37)

car2loancurrentpaymententry = ttk.Entry(contentlevel0, textvariable=car2loancurrentpaymentformatted, state="disabled")
car2loancurrentpaymentlabel = ttk.Label(contentlevel0, text="Monthly Payment", state="disabled")
car2loancurrentpaymentlabel.grid(column=3, row=38, pady=5)
car2loancurrentpaymententry.grid(column=3, row=39)

car2loanarrearsentry = ttk.Entry(contentlevel0, textvariable=car2loanarrearsformatted, state="disabled")
car2loanarrearslabel = ttk.Label(contentlevel0, text="Arrears", state="disabled")
car2loanarrearslabel.grid(column=3, row=40, pady=5)
car2loanarrearsentry.grid(column=3, row=41)

planlongtermdebtscurrentdata = ttk.Label(contentlevel0, textvariable=firstmortgagecurrentpaymentformatted, state="disabled")
planlongtermdebtscurrentlabel = ttk.Label(contentlevel0, text="Long-Term Debts (3.1)", state="disabled")
planlongtermdebtscurrentlabel.grid(column=5, row=1, pady=5)
planlongtermdebtscurrentdata.grid(column=5, row=2)

planlongtermdebtsarrearsdata = ttk.Label(contentlevel0, textvariable=planlongtermdebtarrearspaymentformatted, state="disabled")
planlongtermdebtsarrearslabel = ttk.Label(contentlevel0, text="Long-Term Debt Arrears (3.2)", state="disabled")
planlongtermdebtsarrearslabel.grid(column=5, row=3, pady=5)
planlongtermdebtsarrearsdata.grid(column=5, row=4)

plansecurednocramdowndata = ttk.Label(contentlevel0, textvariable=plansecurednocramdownformatted, state="disabled")
plansecurednocramdownlabel = ttk.Label(contentlevel0, text="Secured Claims, No CD (3.3)", state="disabled")
plansecurednocramdownlabel.grid(column=5, row=5, pady=5)
plansecurednocramdowndata.grid(column=5, row=6)

plancostcalcbutton = ttk.Button(contentlevel0, text="3. Run Plan Cost Calc", command=lambda: plancostcalc(), state="disabled")
plancostcalcbutton.grid(column=5, row=7, pady=10, padx=10)

plansecuredcramdowndata = ttk.Label(contentlevel0, textvariable=plansecuredcramdownformatted, state="disabled")
plansecuredcramdownlabel = ttk.Label(contentlevel0, text="Secured Claims, CD (3.5)", state="disabled")
plansecuredcramdownlabel.grid(column=6, row=1, pady=5)
plansecuredcramdowndata.grid(column=6, row=2)

planattorneysfeesdata = ttk.Label(contentlevel0, textvariable=planattorneysfeesformatted, state="disabled")
planattorneysfeeslabel = ttk.Label(contentlevel0, text="Attorney's Fees (4.1)", state="disabled")
planattorneysfeeslabel.grid(column=6, row=3, pady=5)
planattorneysfeesdata.grid(column=6, row=4)

plantrusteefeesdata = ttk.Label(contentlevel0, textvariable=plantrusteefeesformatted, state="disabled")
plantrusteefeeslabel = ttk.Label(contentlevel0, text="Trustee Fees (4.1)", state="disabled")
plantrusteefeeslabel.grid(column=6, row=5, pady=5)
plantrusteefeesdata.grid(column=6, row=6)

planpriorityclaimsdata = ttk.Label(contentlevel0, textvariable=planpriorityclaimsformatted, state="disabled")
planpriorityclaimslabel = ttk.Label(contentlevel0, text="Priority Claims (4.4)", state="disabled")
planpriorityclaimslabel.grid(column=7, row=1, pady=5)
planpriorityclaimsdata.grid(column=7, row=2)

plangeneralunsecuredclaimsdata = ttk.Label(contentlevel0, textvariable=plangeneralunsecuredclaimsformatted, state="disabled")
plangeneralunsecuredclaimslabel = ttk.Label(contentlevel0, text="Gen. Unsecured (5.2)", state="disabled")
plangeneralunsecuredclaimslabel.grid(column=7, row=3, pady=5)
plangeneralunsecuredclaimsdata.grid(column=7, row=4)

plangeneralunsecuredclaimsbasisdata = ttk.Label(contentlevel0, textvariable=plangeneralunsecuredclaimsbasisformatted, state="disabled")
plangeneralunsecuredclaimsbasislabel = ttk.Label(contentlevel0, text="Basis (5.1)", state="disabled")
plangeneralunsecuredclaimsbasislabel.grid(column=8, row=3, pady=5)
plangeneralunsecuredclaimsbasisdata.grid(column=8, row=4)

plantotalmonthlycostdata = ttk.Label(contentlevel0, textvariable=plantotalmonthlycostformatted, state="disabled")
plantotalmonthlycostlabel = ttk.Label(contentlevel0, text="TOTAL", state="disabled")
plantotalmonthlycostlabel.grid(column=7, row=5, pady=5)
plantotalmonthlycostdata.grid(column=7, row=6)

othersecureddebtnamelabel = ttk.Label(contentlevel0, text="Sec. Creditor Name", state="disabled")
othersecureddebtnamelabel.grid(column=5, row=9, pady=5, padx=10)

secureddebt1nameentry = ttk.Entry(contentlevel0, textvariable=secureddebt1nameformatted, state="disabled")
secureddebt1nameentry.grid(column=5, row=10, padx=10)
secureddebt2nameentry = ttk.Entry(contentlevel0, textvariable=secureddebt2nameformatted, state="disabled")
secureddebt2nameentry.grid(column=5, row=11, padx=10)
secureddebt3nameentry = ttk.Entry(contentlevel0, textvariable=secureddebt3nameformatted, state="disabled")
secureddebt3nameentry.grid(column=5, row=12, padx=10)
secureddebt4nameentry = ttk.Entry(contentlevel0, textvariable=secureddebt4nameformatted, state="disabled")
secureddebt4nameentry.grid(column=5, row=13, padx=10)

othersecureddebtamountlabel = ttk.Label(contentlevel0, text="Total Owed", state="disabled")
othersecureddebtamountlabel.grid(column=6, row=9, pady=5, padx=10)

secureddebt1amountentry = ttk.Entry(contentlevel0, textvariable=secureddebt1amountformatted, state="disabled")
secureddebt1amountentry.grid(column=6, row=10, padx=10)
secureddebt2amountentry = ttk.Entry(contentlevel0, textvariable=secureddebt2amountformatted, state="disabled")
secureddebt2amountentry.grid(column=6, row=11, padx=10)
secureddebt3amountentry = ttk.Entry(contentlevel0, textvariable=secureddebt3amountformatted, state="disabled")
secureddebt3amountentry.grid(column=6, row=12, padx=10)
secureddebt4amountentry = ttk.Entry(contentlevel0, textvariable=secureddebt4amountformatted, state="disabled")
secureddebt4amountentry.grid(column=6, row=13, padx=10)

othersecureddebtcollaterallabel = ttk.Label(contentlevel0, text="Value of Collateral", state="disabled")
othersecureddebtcollaterallabel.grid(column=7, row=9, pady=5)

secureddebt1collateralentry = ttk.Entry(contentlevel0, textvariable=secureddebt1collateralvalueformatted, state="disabled")
secureddebt1collateralentry.grid(column=7, row=10)
secureddebt2collateralentry = ttk.Entry(contentlevel0, textvariable=secureddebt2collateralvalueformatted, state="disabled")
secureddebt2collateralentry.grid(column=7, row=11)
secureddebt3collateralentry = ttk.Entry(contentlevel0, textvariable=secureddebt3collateralvalueformatted, state="disabled")
secureddebt3collateralentry.grid(column=7, row=12)
secureddebt4collateralentry = ttk.Entry(contentlevel0, textvariable=secureddebt4collateralvalueformatted, state="disabled")
secureddebt4collateralentry.grid(column=7, row=13)

othersecureddebttypelabel = ttk.Label(contentlevel0, text="Type", justify="center", state="disabled")
othersecureddebttypelabel.grid(column=8, row=9, pady=5, columnspan=4)

secureddebt1typeentryjudgment = ttk.Radiobutton(contentlevel0, text="Judgment", value="Judgment", variable=secureddebt1typeformatted, state="disabled")
secureddebt1typeentryjudgment.grid(column=8, row=10, padx=10)
secureddebt2typeentryjudgment = ttk.Radiobutton(contentlevel0, text="Judgment", value="Judgment", variable=secureddebt2typeformatted, state="disabled")
secureddebt2typeentryjudgment.grid(column=8, row=11, padx=10)
secureddebt3typeentryjudgment = ttk.Radiobutton(contentlevel0, text="Judgment", value="Judgment", variable=secureddebt3typeformatted, state="disabled")
secureddebt3typeentryjudgment.grid(column=8, row=12, padx=10)
secureddebt4typeentryjudgment = ttk.Radiobutton(contentlevel0, text="Judgment", value="Judgment", variable=secureddebt4typeformatted, state="disabled")
secureddebt4typeentryjudgment.grid(column=8, row=13, padx=10)

secureddebt1typeentrypmsi = ttk.Radiobutton(contentlevel0, text="PMSI", value="PMSI", variable=secureddebt1typeformatted, state="disabled")
secureddebt1typeentrypmsi.grid(column=9, row=10, padx=10)
secureddebt2typeentrypmsi = ttk.Radiobutton(contentlevel0, text="PMSI", value="PMSI", variable=secureddebt2typeformatted, state="disabled")
secureddebt2typeentrypmsi.grid(column=9, row=11, padx=10)
secureddebt3typeentrypmsi = ttk.Radiobutton(contentlevel0, text="PMSI", value="PMSI", variable=secureddebt3typeformatted, state="disabled")
secureddebt3typeentrypmsi.grid(column=9, row=12, padx=10)
secureddebt4typeentrypmsi = ttk.Radiobutton(contentlevel0, text="PMSI", value="PMSI", variable=secureddebt4typeformatted, state="disabled")
secureddebt4typeentrypmsi.grid(column=9, row=13, padx=10)

secureddebt1typeentrynppmsi = ttk.Radiobutton(contentlevel0, text="NPPMSI", value="NPPMSI", variable=secureddebt1typeformatted, state="disabled")
secureddebt1typeentrynppmsi.grid(column=10, row=10, padx=10)
secureddebt2typeentrynppmsi = ttk.Radiobutton(contentlevel0, text="NPPMSI", value="NPPMSI", variable=secureddebt2typeformatted, state="disabled")
secureddebt2typeentrynppmsi.grid(column=10, row=11, padx=10)
secureddebt3typeentrynppmsi = ttk.Radiobutton(contentlevel0, text="NPPMSI", value="NPPMSI", variable=secureddebt3typeformatted, state="disabled")
secureddebt3typeentrynppmsi.grid(column=10, row=12, padx=10)
secureddebt4typeentrynppmsi = ttk.Radiobutton(contentlevel0, text="NPPMSI", value="NPPMSI", variable=secureddebt4typeformatted, state="disabled")
secureddebt4typeentrynppmsi.grid(column=10, row=13, padx=10)

secureddebt1typeentrylien = ttk.Radiobutton(contentlevel0, text="Lien", value="Lien", variable=secureddebt1typeformatted, state="disabled")
secureddebt1typeentrylien.grid(column=11, row=10, padx=10)
secureddebt2typeentrylien = ttk.Radiobutton(contentlevel0, text="Lien", value="Lien", variable=secureddebt2typeformatted, state="disabled")
secureddebt2typeentrylien.grid(column=11, row=11, padx=10)
secureddebt3typeentrylien = ttk.Radiobutton(contentlevel0, text="Lien", value="Lien", variable=secureddebt3typeformatted, state="disabled")
secureddebt3typeentrylien.grid(column=11, row=12, padx=10)
secureddebt4typeentrylien = ttk.Radiobutton(contentlevel0, text="Lien", value="Lien", variable=secureddebt4typeformatted, state="disabled")
secureddebt4typeentrylien.grid(column=11, row=13, padx=10)

verticalseparator3 = ttk.Separator(contentlevel0, orient='vertical')
verticalseparator3.grid(column=12, row=9, sticky=tkinter.NS, rowspan=5, padx=10)

othersecureddebttreatmentlabel = ttk.Label(contentlevel0, text="Treatment", justify="center", state="disabled")
othersecureddebttreatmentlabel.grid(column=13, row=9, pady=5, columnspan=4)

secureddebt1treatmentrpentry = ttk.Radiobutton(contentlevel0, text="R & P", value="Retain and Pay", variable=secureddebt1treatmentformatted, state="disabled")
secureddebt1treatmentrpentry.grid(column=13, row=10, padx=10)
secureddebt2treatmentrpentry = ttk.Radiobutton(contentlevel0, text="R & P", value="Retain and Pay", variable=secureddebt2treatmentformatted, state="disabled")
secureddebt2treatmentrpentry.grid(column=13, row=11, padx=10)
secureddebt3treatmentrpentry = ttk.Radiobutton(contentlevel0, text="R & P", value="Retain and Pay", variable=secureddebt3treatmentformatted, state="disabled")
secureddebt3treatmentrpentry.grid(column=13, row=12, padx=10)
secureddebt4treatmentrpentry = ttk.Radiobutton(contentlevel0, text="R & P", value="Retain and Pay", variable=secureddebt4treatmentformatted, state="disabled")
secureddebt4treatmentrpentry.grid(column=13, row=13, padx=10)

secureddebt1treatmentcdentry = ttk.Radiobutton(contentlevel0, text="Cram", value="Cramdown", variable=secureddebt1treatmentformatted, state="disabled")
secureddebt1treatmentcdentry.grid(column=14, row=10, padx=10)
secureddebt2treatmentcdentry = ttk.Radiobutton(contentlevel0, text="Cram", value="Cramdown", variable=secureddebt2treatmentformatted, state="disabled")
secureddebt2treatmentcdentry.grid(column=14, row=11, padx=10)
secureddebt3treatmentcdentry = ttk.Radiobutton(contentlevel0, text="Cram", value="Cramdown", variable=secureddebt3treatmentformatted, state="disabled")
secureddebt3treatmentcdentry.grid(column=14, row=12, padx=10)
secureddebt4treatmentcdentry = ttk.Radiobutton(contentlevel0, text="Cram", value="Cramdown", variable=secureddebt4treatmentformatted, state="disabled")
secureddebt4treatmentcdentry.grid(column=14, row=13, padx=10)

secureddebt1treatmentsurrenderentry = ttk.Radiobutton(contentlevel0, text="Surrender", value="Surrender", variable=secureddebt1treatmentformatted, state="disabled")
secureddebt1treatmentsurrenderentry.grid(column=15, row=10, padx=10)
secureddebt2treatmentsurrenderentry = ttk.Radiobutton(contentlevel0, text="Surrender", value="Surrender", variable=secureddebt2treatmentformatted, state="disabled")
secureddebt2treatmentsurrenderentry.grid(column=15, row=11, padx=10)
secureddebt3treatmentsurrenderentry = ttk.Radiobutton(contentlevel0, text="Surrender", value="Surrender", variable=secureddebt3treatmentformatted, state="disabled")
secureddebt3treatmentsurrenderentry.grid(column=15, row=12, padx=10)
secureddebt4treatmentsurrenderentry = ttk.Radiobutton(contentlevel0, text="Surrender", value="Surrender", variable=secureddebt4treatmentformatted, state="disabled")
secureddebt4treatmentsurrenderentry.grid(column=15, row=13, padx=10)

secureddebt1treatmentavoidentry = ttk.Radiobutton(contentlevel0, text="Avoid", value="Avoid", variable=secureddebt1treatmentformatted, state="disabled")
secureddebt1treatmentavoidentry.grid(column=16, row=10, padx=10)
secureddebt2treatmentavoidentry = ttk.Radiobutton(contentlevel0, text="Avoid", value="Avoid", variable=secureddebt2treatmentformatted, state="disabled")
secureddebt2treatmentavoidentry.grid(column=16, row=11, padx=10)
secureddebt3treatmentavoidentry = ttk.Radiobutton(contentlevel0, text="Avoid", value="Avoid", variable=secureddebt3treatmentformatted, state="disabled")
secureddebt3treatmentavoidentry.grid(column=16, row=12, padx=10)
secureddebt4treatmentavoidentry = ttk.Radiobutton(contentlevel0, text="Avoid", value="Avoid", variable=secureddebt4treatmentformatted, state="disabled")
secureddebt4treatmentavoidentry.grid(column=16, row=13, padx=10)

priorityclaimstotalentry = ttk.Entry(contentlevel0, textvariable=priorityclaimstotalformatted, state="disabled")
priorityclaimstotallabel = ttk.Label(contentlevel0, text="Priority Claims", state="disabled")
priorityclaimstotallabel.grid(column=5, row=14, pady=5)
priorityclaimstotalentry.grid(column=5, row=15)

generalunsecuredentry = ttk.Entry(contentlevel0, textvariable=generalunsecuredclaimsformatted, state="disabled")
generalunsecuredlabel = ttk.Label(contentlevel0, text="Gen. Unsec. Claims", state="disabled")
generalunsecuredlabel.grid(column=6, row=14, pady=5)
generalunsecuredentry.grid(column=6, row=15)

attorneysfeeentry = ttk.Entry(contentlevel0, textvariable=attorneysfeeformatted, state="disabled")
attorneysfeelabel = ttk.Label(contentlevel0, text="Attorney's Fee", state="disabled")
attorneysfeelabel.grid(column=7, row=14, pady=5)
attorneysfeeentry.grid(column=7, row=15)

chapter7dividendentry = ttk.Entry(contentlevel0, textvariable=chapter7dividendformatted, state="disabled")
chapter7dividendlabel = ttk.Label(contentlevel0, text="Ch. 7 Dividend", state="disabled")
chapter7dividendlabel.grid(column=5, row=16, pady=5)
chapter7dividendentry.grid(column=5, row=17)

toydividendentry = ttk.Entry(contentlevel0, textvariable=toydividendformatted, state="disabled")
toydividendlabel = ttk.Label(contentlevel0, text="Toy Dividend", state="disabled")
toydividendlabel.grid(column=5, row=18, pady=5)
toydividendentry.grid(column=5, row=19)

scheduleiline12entry = ttk.Entry(contentlevel0, textvariable=scheduleiline12formatted, state="disabled")
scheduleiline12label = ttk.Label(contentlevel0, text="Schedule I - Line 12", state="disabled")
scheduleiline12label.grid(column=7, row=16, pady=5)
scheduleiline12entry.grid(column=7, row=17)

schedulejline22centry = ttk.Entry(contentlevel0, textvariable=schedulejline22cformatted, state="disabled")
schedulejline22clabel = ttk.Label(contentlevel0, text="Schedule J - Line 22c", state="disabled")
schedulejline22clabel.grid(column=7, row=18, pady=5)
schedulejline22centry.grid(column=7, row=19)

meanstestprojectedplanpaymententry = ttk.Entry(contentlevel0, textvariable=mtline36aformatted, state="disabled")
meanstestprojectedplanpaymentlabel = ttk.Label(contentlevel0, text="Projected Plan Payment", state="disabled")
meanstestprojectedplanpaymentlabel.grid(column=7, row=20, pady=5)
meanstestprojectedplanpaymententry.grid(column=7, row=21)

verticalseparator1 = ttk.Separator(contentlevel0, orient='vertical')
verticalseparator1.grid(column=4, row=0, sticky=tkinter.NS, rowspan=120, padx=20)

verticalseparator2 = ttk.Separator(contentlevel0, orient='vertical')
verticalseparator2.grid(column=17, row=0, sticky=tkinter.NS, rowspan=120, padx=20)

meanstestfoodclothingandotheritemsentry = ttk.Entry(contentlevel0, textvariable=mtline6formatted, state="disabled")
meanstestfoodclothingandotheritemslabel = ttk.Label(contentlevel0, text="Food, Clothing, etc.", state="disabled")
meanstestfoodclothingandotheritemslabel.grid(column=18, row=9, pady=5)
meanstestfoodclothingandotheritemsentry.grid(column=18, row=10)

meanstestoutofpockethealthcareentry = ttk.Entry(contentlevel0, textvariable=mtline7formatted, state="disabled")
meanstestoutofpockethealthcarelabel = ttk.Label(contentlevel0, text="OOP Healthcare", state="disabled")
meanstestoutofpockethealthcarelabel.grid(column=18, row=11, pady=5)
meanstestoutofpockethealthcareentry.grid(column=18, row=12)

meanstesthousingandutilitiesinsuranceandoperatingentry = ttk.Entry(contentlevel0, textvariable=mtline8formatted, state="disabled")
meanstesthousingandutilitiesinsuranceandoperatinglabel = ttk.Label(contentlevel0, text="Housing: Ins. and Op.", state="disabled")
meanstesthousingandutilitiesinsuranceandoperatinglabel.grid(column=18, row=13, pady=5)
meanstesthousingandutilitiesinsuranceandoperatingentry.grid(column=18, row=14)

meanstesthousingandutilitiesmortgageorrententry = ttk.Entry(contentlevel0, textvariable=mtline9formatted, state="disabled")
meanstesthousingandutilitiesmortgageorrentlabel = ttk.Label(contentlevel0, text="Housing: Mort. or Rent", state="disabled")
meanstesthousingandutilitiesmortgageorrentlabel.grid(column=18, row=15, pady=5)
meanstesthousingandutilitiesmortgageorrententry.grid(column=18, row=16)

meanstestvehicleoperationexpenseentry = ttk.Entry(contentlevel0, textvariable=mtline12formatted, state="disabled")
meanstestvehicleoperationexpenselabel = ttk.Label(contentlevel0, text="Vehicle Op. / Public Trans.", state="disabled")
meanstestvehicleoperationexpenselabel.grid(column=18, row=17, pady=5)
meanstestvehicleoperationexpenseentry.grid(column=18, row=18)

meanstestvehicleownershiporleaseentry1 = ttk.Entry(contentlevel0, textvariable=mtline13cformatted, state="disabled")
meanstestvehicleownershiporleaselabel1 = ttk.Label(contentlevel0, text="Veh. 1 Ownership", state="disabled")
meanstestvehicleownershiporleaselabel1.grid(column=18, row=19, pady=5)
meanstestvehicleownershiporleaseentry1.grid(column=18, row=20)

meanstestvehicleownershiporleaseentry2 = ttk.Entry(contentlevel0, textvariable=mtline13fformatted, state="disabled")
meanstestvehicleownershiporleaselabel2 = ttk.Label(contentlevel0, text="Veh. 2 Ownership", state="disabled")
meanstestvehicleownershiporleaselabel2.grid(column=18, row=21, pady=5)
meanstestvehicleownershiporleaseentry2.grid(column=18, row=22)

meanstesttaxesentry = ttk.Entry(contentlevel0, textvariable=mtline16formatted, state="disabled")
meanstesttaxeslabel = ttk.Label(contentlevel0, text="Taxes", state="disabled")
meanstesttaxeslabel.grid(column=18, row=23, pady=5)
meanstesttaxesentry.grid(column=18, row=24)

meanstestinvoluntarydeductionsentry = ttk.Entry(contentlevel0, textvariable=mtline17formatted, state="disabled")
meanstestinvoluntarydeductionslabel = ttk.Label(contentlevel0, text="Invol. Deductions", state="disabled")
meanstestinvoluntarydeductionslabel.grid(column=18, row=25, pady=5)
meanstestinvoluntarydeductionsentry.grid(column=18, row=26)

meanstestlifeinsuranceentry = ttk.Entry(contentlevel0, textvariable=mtline18formatted, state="disabled")
meanstestlifeinsurancelabel = ttk.Label(contentlevel0, text="Life Insurance", state="disabled")
meanstestlifeinsurancelabel.grid(column=18, row=27, pady=5)
meanstestlifeinsuranceentry.grid(column=18, row=28)

meanstestcourtorderedpaymentsentry = ttk.Entry(contentlevel0, textvariable=mtline19formatted, state="disabled")
meanstestcourtorderedpaymentslabel = ttk.Label(contentlevel0, text="Court Payments", state="disabled")
meanstestcourtorderedpaymentslabel.grid(column=18, row=29, pady=5)
meanstestcourtorderedpaymentsentry.grid(column=18, row=30)

meanstesteducationentry = ttk.Entry(contentlevel0, textvariable=mtline20formatted, state="disabled")
meanstesteducationlabel = ttk.Label(contentlevel0, text="Education", state="disabled")
meanstesteducationlabel.grid(column=18, row=31, pady=5)
meanstesteducationentry.grid(column=18, row=32)

meanstestchildcareentry = ttk.Entry(contentlevel0, textvariable=mtline21formatted, state="disabled")
meanstestchildcarelabel = ttk.Label(contentlevel0, text="Childcare", state="disabled")
meanstestchildcarelabel.grid(column=18, row=33, pady=5)
meanstestchildcareentry.grid(column=18, row=34)

meanstestadditionalhealthcareexpensesentry = ttk.Entry(contentlevel0, textvariable=mtline22formatted, state="disabled")
meanstestadditionalhealthcareexpenseslabel = ttk.Label(contentlevel0, text="Add'l Healthcare Exp.", state="disabled")
meanstestadditionalhealthcareexpenseslabel.grid(column=18, row=35, pady=5)
meanstestadditionalhealthcareexpensesentry.grid(column=18, row=36)

meanstestoptionalphoneserviceentry = ttk.Entry(contentlevel0, textvariable=mtline23formatted, state="disabled")
meanstestoptionalphoneservicelabel = ttk.Label(contentlevel0, text="Opt. Phone Serv.", state="disabled")
meanstestoptionalphoneservicelabel.grid(column=18, row=37, pady=5)
meanstestoptionalphoneserviceentry.grid(column=18, row=38)

meanstesthealthinsuranceentry = ttk.Entry(contentlevel0, textvariable=mtline25formatted, state="disabled")
meanstesthealthinsurancelabel = ttk.Label(contentlevel0, text="Health, Disability, HSA", state="disabled")
meanstesthealthinsurancelabel.grid(column=19, row=9, pady=5)
meanstesthealthinsuranceentry.grid(column=19, row=10)

meanstestcontinuingcontributionstocareentry = ttk.Entry(contentlevel0, textvariable=mtline26formatted, state="disabled")
meanstestcontinuingcontributionstocarelabel = ttk.Label(contentlevel0, text="Cont. Contrib. to Care", state="disabled")
meanstestcontinuingcontributionstocarelabel.grid(column=19, row=11, pady=5)
meanstestcontinuingcontributionstocareentry.grid(column=19, row=12)

meanstestprotectionagainstfamilyvioilenceentry = ttk.Entry(contentlevel0, textvariable=mtline27formatted, state="disabled")
meanstestprotectionagainstfamilyviolencelabel = ttk.Label(contentlevel0, text="Protection Against FV", state="disabled")
meanstestprotectionagainstfamilyviolencelabel.grid(column=19, row=13, pady=5)
meanstestprotectionagainstfamilyvioilenceentry.grid(column=19, row=14)

meanstestadditionalhomeenergyentry = ttk.Entry(contentlevel0, textvariable=mtline28formatted, state="disabled")
meanstestadditionalhomeenergylabel = ttk.Label(contentlevel0, text="Add'l Home Energy Costs", state="disabled")
meanstestadditionalhomeenergylabel.grid(column=19, row=15, pady=5)
meanstestadditionalhomeenergyentry.grid(column=19, row=16)

meanstestdependenteducationalentry = ttk.Entry(contentlevel0, textvariable=mtline29formatted, state="disabled")
meanstestdependenteducationallabel = ttk.Label(contentlevel0, text="Dependent Ed. Exp.", state="disabled")
meanstestdependenteducationallabel.grid(column=19, row=17, pady=5)
meanstestdependenteducationalentry.grid(column=19, row=18)

meanstestadditionalfoodandclothingentry = ttk.Entry(contentlevel0, textvariable=mtline30formatted, state="disabled")
meanstestadditionalfoodandclothinglabel = ttk.Label(contentlevel0, text="Add'l Food and Clothing", state="disabled")
meanstestadditionalfoodandclothinglabel.grid(column=19, row=19, pady=5)
meanstestadditionalfoodandclothingentry.grid(column=19, row=20)

meanstestcharitablecontributionsentry = ttk.Entry(contentlevel0, textvariable=mtline31formatted, state="disabled")
meanstestcharitablecontributionslabel = ttk.Label(contentlevel0, text="Charitable Contrib.", state="disabled")
meanstestcharitablecontributionslabel.grid(column=19, row=21, pady=5)
meanstestcharitablecontributionsentry.grid(column=19, row=22)

meanstestsecureddebtmortgagesentry = ttk.Entry(contentlevel0, textvariable=mtline33aformatted, state="disabled")
meanstestsecureddebtmortgageslabel = ttk.Label(contentlevel0, text="Sec. Debt: Mortgages", state="disabled")
meanstestsecureddebtmortgageslabel.grid(column=19, row=23, pady=5)
meanstestsecureddebtmortgagesentry.grid(column=19, row=24)

meanstestsecureddebtcarsentry = ttk.Entry(contentlevel0, textvariable=mtline33bcformatted, state="disabled")
meanstestsecureddebtcarslabel = ttk.Label(contentlevel0, text="Sec. Debt: Cars", state="disabled")
meanstestsecureddebtcarslabel.grid(column=19, row=25, pady=5)
meanstestsecureddebtcarsentry.grid(column=19, row=26)

meanstestothersecureddebtsentry = ttk.Entry(contentlevel0, textvariable=mtline33eformatted, state="disabled")
meanstestothersecureddebtslabel = ttk.Label(contentlevel0, text="Sec. Debt: Other", state="disabled")
meanstestothersecureddebtslabel.grid(column=19, row=27, pady=5)
meanstestothersecureddebtsentry.grid(column=19, row=28)

meanstestsecuredarrearsentry = ttk.Entry(contentlevel0, textvariable=mtline34formatted, state="disabled")
meanstestsecuredarrearslabel = ttk.Label(contentlevel0, text="Sec. Debt Arrears", state="disabled")
meanstestsecuredarrearslabel.grid(column=19, row=29, pady=5)
meanstestsecuredarrearsentry.grid(column=19, row=30)

meanstestpriorityclaimsentry = ttk.Entry(contentlevel0, textvariable=mtline35formatted, state="disabled")
meanstestpriorityclaimslabel = ttk.Label(contentlevel0, text="Priority Payments", state="disabled")
meanstestpriorityclaimslabel.grid(column=19, row=31, pady=5)
meanstestpriorityclaimsentry.grid(column=19, row=32)

meanstestprojectedadminexpenseentry = ttk.Entry(contentlevel0, textvariable=mtline36bformatted, state="disabled")
meanstestprojectedadminexpenselabel = ttk.Label(contentlevel0, text="Proj. Admin. Expense", state="disabled")
meanstestprojectedadminexpenselabel.grid(column=19, row=33, pady=5)
meanstestprojectedadminexpenseentry.grid(column=19, row=34)

meanstestchildsupportdeductionentry = ttk.Entry(contentlevel0, textvariable=childsupportreceivedformatted, state="disabled")
meanstestchildsupportdeductionlabel = ttk.Label(contentlevel0, text="CS Deduction", state="disabled")
meanstestchildsupportdeductionlabel.grid(column=19, row=35, pady=5)
meanstestchildsupportdeductionentry.grid(column=19, row=36)

meanstestretirementdeductionentry = ttk.Entry(contentlevel0, textvariable=mtline41formatted, state="disabled")
meanstestretirementdeductionlabel = ttk.Label(contentlevel0, text="Ret. Deduction", state="disabled")
meanstestretirementdeductionlabel.grid(column=19, row=37, pady=5)
meanstestretirementdeductionentry.grid(column=19, row=38)

longmeanstestbutton = ttk.Button(contentlevel0, text="2. Run Long Means Test", command=lambda: form122c2(), state="disabled")
longmeanstestbutton.grid(column=18, row=40, pady=5, padx=10)

cmirestatedentry = ttk.Entry(contentlevel0, textvariable=currentmonthlyincomeformatted, state="disabled")
cmirestatedlabel = ttk.Label(contentlevel0, text="CMI", state="disabled")
cmirestatedlabel.grid(column=19, row=39, pady=5)
cmirestatedentry.grid(column=19, row=40)

minuslabel = ttk.Label(contentlevel0, text="-", state="disabled")
minuslabel.grid(column=20, row=40, pady=5, padx=5)

totalmeanstestdeductionsentry = ttk.Entry(contentlevel0, textvariable=meanstestdeductionsformatted, state="disabled")
totalmeanstestdeductionslabel = ttk.Label(contentlevel0, text="Total Deductions", state="disabled")
totalmeanstestdeductionslabel.grid(column=21, row=39, pady=5)
totalmeanstestdeductionsentry.grid(column=21, row=40)

equallabel = ttk.Label(contentlevel0, text="=", state="disabled")
equallabel.grid(column=22, row=40, pady=5)

monthlydisposableincomeentry = ttk.Entry(contentlevel0, textvariable=monthlydisposableincomeformatted, state="disabled")
monthlydisposableincomelabel = ttk.Label(contentlevel0, text="MDI", state="disabled")
monthlydisposableincomelabel.grid(column=23, row=39, pady=5)
monthlydisposableincomeentry.grid(column=23, row=40)

root.mainloop()