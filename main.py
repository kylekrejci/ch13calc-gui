import tkinter
from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("GAMD Chapter 13 Calculator")

# Define input fields. Populate with dummy data.

countyformatted = StringVar()
countyformatted.set("Bibb County")
comittmentperiodformatted = DoubleVar()
comittmentperiodformatted.set("0")
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
car2plantreatmentformatted.set("Pay")
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
presumptiveplanpaymentformatted = DoubleVar()
presumptiveplanpaymentformatted.set("0.00")
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
planlongtermdebtpaymentformatted = DoubleVar()
planlongtermdebtpaymentformatted.set(float(firstmortgagecurrentpaymentformatted.get()) + float(secondmortgagecurrentpaymentformatted.get()))
planlongtermdebtarrearspaymentformatted = DoubleVar()
planlongtermdebtarrearspaymentformatted.set("0.00")
plansecurednocramdowntotalformatted = DoubleVar()
plansecurednocramdowntotalformatted.set("0.00")
plansecurednocramdowncar1formatted = DoubleVar()
plansecurednocramdowncar1formatted.set("0.00")
plansecurednocramdowncar2formatted = DoubleVar()
plansecurednocramdowncar2formatted.set("0.00")
plansecurednocramdownclaim1formatted = DoubleVar()
plansecurednocramdownclaim1formatted.set("0.00")
plansecurednocramdownclaim2formatted = DoubleVar()
plansecurednocramdownclaim2formatted.set("0.00")
plansecurednocramdownclaim3formatted = DoubleVar()
plansecurednocramdownclaim3formatted.set("0.00")
plansecurednocramdownclaim4formatted = DoubleVar()
plansecurednocramdownclaim4formatted.set("0.00")
plansecuredcramdowntotalformatted = DoubleVar()
plansecuredcramdowntotalformatted.set("0.00")
plansecuredcramdowncar1formatted = DoubleVar()
plansecuredcramdowncar1formatted.set("0.00")
plansecuredcramdowncar2formatted = DoubleVar()
plansecuredcramdowncar2formatted.set("0.00")
plansecuredcramdownclaim1formatted = DoubleVar()
plansecuredcramdownclaim1formatted.set("0.00")
plansecuredcramdownclaim2formatted = DoubleVar()
plansecuredcramdownclaim2formatted.set("0.00")
plansecuredcramdownclaim3formatted = DoubleVar()
plansecuredcramdownclaim3formatted.set("0.00")
plansecuredcramdownclaim4formatted = DoubleVar()
plansecuredcramdownclaim4formatted.set("0.00")
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
plangeneralunsecuredclaimsdividendformatted = DoubleVar()
plangeneralunsecuredclaimsdividendformatted.set("0.00")
plangeneralunsecuredclaimspercentageformatted = DoubleVar()
plangeneralunsecuredclaimspercentageformatted.set("0.0")
plantotalmonthlycostformatted = DoubleVar()
plantotalmonthlycostformatted.set("0.00")

# Helper functions.

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
    applicablecomittmentperiod60m.config(state="normal")
    applicablecomittmentperioddefined.config(state="normal")
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

def unlock2():
    planlongtermdebtscurrentdata.config(state="normal")
    planlongtermdebtscurrentlabel.config(state="normal")
    planlongtermdebtsarrearsdata.config(state="normal")
    planlongtermdebtsarrearslabel.config(state="normal")
    plansecurednocramdowndata0.config(state="normal")
    plansecurednocramdowndata1.config(state="normal")
    plansecurednocramdowndata2.config(state="normal")
    plansecurednocramdowndata3.config(state="normal")
    plansecurednocramdowndata4.config(state="normal")
    plansecurednocramdowndata5.config(state="normal")
    plansecurednocramdowndata6.config(state="normal")
    plansecurednocramdownlabel0.config(state="normal")
    plansecurednocramdownlabel1.config(state="normal")
    plansecurednocramdownlabel2.config(state="normal")
    plansecurednocramdownlabel3.config(state="normal")
    plansecurednocramdownlabel4.config(state="normal")
    plansecurednocramdownlabel5.config(state="normal")
    plansecurednocramdownlabel6.config(state="normal")
    plansecuredcramdowndata0.config(state="normal")
    plansecuredcramdowndata1.config(state="normal")
    plansecuredcramdowndata2.config(state="normal")
    plansecuredcramdowndata3.config(state="normal")
    plansecuredcramdowndata4.config(state="normal")
    plansecuredcramdowndata5.config(state="normal")
    plansecuredcramdowndata6.config(state="normal")
    plansecuredcramdownlabel0.config(state="normal")
    plansecuredcramdownlabel1.config(state="normal")
    plansecuredcramdownlabel2.config(state="normal")
    plansecuredcramdownlabel3.config(state="normal")
    plansecuredcramdownlabel4.config(state="normal")
    plansecuredcramdownlabel5.config(state="normal")
    plansecuredcramdownlabel6.config(state="normal")
    planattorneysfeesdata.config(state="normal")
    planattorneysfeeslabel.config(state="normal")
    planpriorityclaimsdata.config(state="normal")
    planpriorityclaimslabel.config(state="normal")
    plangeneralunsecuredclaimspercentagedata.config(state="normal")
    plangeneralunsecuredclaimspercentagelabel.config(state="normal")
    plangeneralunsecuredclaimsbasisdata.config(state="normal")
    plangeneralunsecuredclaimsbasislabel.config(state="normal")
    plangeneralunsecuredclaimsdividenddata.config(state="normal")
    plangeneralunsecuredclaimsdividendlabel.config(state="normal")
    plangeneralunsecuredclaimsdata.config(state="normal")
    plangeneralunsecuredclaimslabel.config(state="normal")
    plantrusteefeesdata.config(state="normal")
    plantrusteefeeslabel.config(state="normal")
    plantotalmonthlycostdata.config(state="normal")
    plantotalmonthlycostlabel.config(state="normal")
    presumptivemonthlyplanpaymentlabel.config(state="normal")

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

# Long-form means test function

def form122c2():
    global meanstestdeductionsformatted
    meanstestdeductions = float(0)
    householdsizeget = int(householdsizeformatted.get())
    mtline6 = float(0)
    mtline7 = float(0)

    natstan0 = [0.00, 785.00, 1410.00, 1610.00, 1900.00]
    if householdsizeget <= 4:
        mtline6 = natstan0[householdsizeget]
        mtline6 = round(mtline6, 2)
    elif householdsizeget > 4:
        mtline6 = 1740.00 + ((householdsizeget - 4) * 344)
        mtline6 = round(mtline6, 2)

    mtline6formatted.set(mtline6)

    meanstestdeductions += mtline6

    householdover65 = float(householdover65formatted.get())
    mtline7 = (householdover65 * 153.00) + ((float(householdsizeget) - householdover65) * 75.00)

    mtline7formatted.set(mtline7)

    meanstestdeductions += mtline7

    countyget = countyformatted.get()

    r0 = requests.get('https://www.justice.gov/ust/eo/bapcpa/20220515/bci_data/housing_charts/irs_housing_charts_GA.htm')
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
        mtline12 = 242.00
        mtline12formatted.set(mtline12)
        meanstestdeductions += 242.00
    elif numberofcarsformatted.get() == 1:
        if countyget in ["Butts County", "Jasper County", "Lamar County", "Morgan County", "Walton County"]:
            mtline12 = 320.00
            mtline12formatted.set(mtline12)
            meanstestdeductions += 320.00
        else:
            mtline12 = 267.00
            mtline12formatted.set(mtline12)
            meanstestdeductions += 267.00
    elif numberofcarsformatted.get() == 2:
        if countyget in ["Butts County", "Jasper County", "Lamar County", "Morgan County", "Walton County"]:
            mtline12 = 640.00
            mtline12formatted.set(mtline12)
            meanstestdeductions += 640.00
        else:
            mtline12 = 534.00
            mtline12formatted.set(mtline12)
            meanstestdeductions += 534.00

    if numberofcarsformatted.get() == 1:
        claimedcar1 = float(588.00) - float(car1loanamountformatted.get()) / 60.00
        claimedcar1 = round(claimedcar1, 2)
        if claimedcar1 < 0:
            claimedcar1 = 0
        mtline13c = claimedcar1
        mtline13cformatted.set(mtline13c)
        meanstestdeductions += mtline13c
    if numberofcarsformatted.get() == 2:
        claimedcar1 = float(588.00) - float(car1loanamountformatted.get()) / 60.00
        claimedcar1 = round(claimedcar1, 2)
        if claimedcar1 < 0:
            claimedcar1 = 0
        mtline13c = claimedcar1
        mtline13cformatted.set(mtline13c)
        claimedcar2 = float(588.00) - float(car2loanamountformatted.get()) / 60.00
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
        if mtline29 > (189.58 * float(householdunder18formatted.get())):
            mtline29 = (189.58 * float(householdunder18formatted.get()))
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

        if mdi <= 0:
            abovemedian = "No"
            meansteststatuslabel.config(background="green", text="BELOW MEDIAN")
            comittmentperiodformatted.set("36")

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

# Short-form means test function

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
        comittmentperiodformatted.set("36")
        applicablecomittmentperioddefined.config(state="normal")
    elif medianincome <= (float(currentmonthlyincomeformatted.get()) * float(12)):
        abovemedian = "Yes"
        meansteststatuslabel.config(background="red", text="ABOVE MEDIAN", width=26)
        longmeanstestbutton.config(state="normal")
        comittmentperiodformatted.set("58")
        unlock1()
        lock0()
    elif medianincome > (float(currentmonthlyincomeformatted.get()) * float(12)):
        abovemedian = "No"
        meansteststatuslabel.config(background="green", text="BELOW MEDIAN")
    return

# Monthly plan cost function

def plancostcalc():
    commitmentperiod = float(comittmentperiodformatted.get())
    totalcramdownamount = 0.0
    totalnoncramdownamount = 0.0
    totalpriorityunsecured = 0.0
    totalgeneralunsecured = float(generalunsecuredclaimsformatted.get())
    attorneysfee = 100.00
    car1planpayment = 0.0
    car2planpayment = 0.0
    secureddebt1planpayment = 0.0
    secureddebt2planpayment = 0.0
    secureddebt3planpayment = 0.0
    secureddebt4planpayment = 0.0
    mdi = 0.00
    ch7 = 0.00
    toy = 0.00

    presumptiveplanpayment = float(scheduleiline12formatted.get()) - float(schedulejline22cformatted.get())
    presumptiveplanpaymentformatted.set(presumptiveplanpayment)

    ltdarrearscost = (float(firstmortgagearrearsformatted.get()) + float(secondmortgagearrearsformatted.get())) / 60.0
    planlongtermdebtarrearspaymentformatted.set(ltdarrearscost)

    if car1plantreatmentformatted.get() == "Pay":
        if car1910statusformatted.get() == "No":
            car1planpayment = (0.0525 * float(car1loanamountformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
            car1planpayment = round(car1planpayment, 2)
            totalnoncramdownamount += car1planpayment
            plansecurednocramdowncar1formatted.set(car1planpayment)
        elif car1910statusformatted.get() == "Yes":
            car1planpayment = (0.0525 * float(car1valueformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
            car1planpayment = round(car1planpayment, 2)
            totalcramdownamount += car1planpayment
            plansecuredcramdowncar1formatted.set(car1planpayment)

    if car2plantreatmentformatted.get() == "Pay":
        if car2910statusformatted.get() == "No":
            car2planpayment = (0.0525 * float(car2loanamountformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
            car2planpayment = round(car2planpayment, 2)
            totalnoncramdownamount += car2planpayment
            plansecurednocramdowncar2formatted.set(car2planpayment)
        elif car2910statusformatted.get() == "Yes":
            car2planpayment = (0.0525 * float(car2valueformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
            car2planpayment = round(car2planpayment, 2)
            totalcramdownamount += car2planpayment
            plansecuredcramdowncar2formatted.set(car2planpayment)

    if float(secureddebt1amountformatted.get()) != 0.00:
        if secureddebt1typeformatted.get() == "Judgment":
            totalgeneralunsecured += float(secureddebt1amountformatted.get())
        elif secureddebt1typeformatted.get() == "NPPMSI":
            totalgeneralunsecured += float(secureddebt1amountformatted.get())
        elif secureddebt1typeformatted.get() == "PMSI":
            if secureddebt1treatmentformatted.get() == "Retain and Pay":
                secureddebt1planpayment = (0.0525 * float(secureddebt1amountformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
                secureddebt1planpayment = round(secureddebt1planpayment, 2)
                totalnoncramdownamount += secureddebt1planpayment
                plansecurednocramdownclaim1formatted.set(secureddebt1planpayment)
            elif secureddebt1treatmentformatted.get() == "Cramdown":
                secureddebt1planpayment = (0.0525 * float(secureddebt1collateralvalueformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
                secureddebt1planpayment = round(secureddebt1planpayment, 2)
                totalcramdownamount += secureddebt1planpayment
                plansecuredcramdownclaim1formatted.set(secureddebt1planpayment)
        elif secureddebt1typeformatted.get() == "Lien":
            secureddebt1planpayment = (0.06 * float(secureddebt1amountformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
            totalnoncramdownamount += secureddebt1planpayment
            secureddebt1planpayment = round(secureddebt1planpayment, 2)
            plansecurednocramdownclaim1formatted.set(secureddebt1planpayment)

    if float(secureddebt2amountformatted.get()) != 0.00:
        if secureddebt2typeformatted.get() == "Judgment":
            totalgeneralunsecured += float(secureddebt2amountformatted.get())
        elif secureddebt2typeformatted.get() == "NPPMSI":
            totalgeneralunsecured += float(secureddebt2amountformatted.get())
        elif secureddebt2typeformatted.get() == "PMSI":
            if secureddebt2treatmentformatted.get() == "Retain and Pay":
                secureddebt2planpayment = (0.0525 * float(secureddebt2amountformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
                secureddebt2planpayment = round(secureddebt2planpayment, 2)
                totalnoncramdownamount += secureddebt2planpayment
                plansecurednocramdownclaim2formatted.set(secureddebt2planpayment)
            elif secureddebt2treatmentformatted.get() == "Cramdown":
                secureddebt2planpayment = (0.0525 * float(secureddebt2collateralvalueformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
                secureddebt2planpayment = round(secureddebt2planpayment, 2)
                totalcramdownamount += secureddebt2planpayment
                plansecuredcramdownclaim2formatted.set(secureddebt2planpayment)
        elif secureddebt2typeformatted.get() == "Lien":
            secureddebt2planpayment = (0.06 * float(secureddebt2amountformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
            totalnoncramdownamount += secureddebt2planpayment
            secureddebt2planpayment = round(secureddebt2planpayment, 2)
            plansecurednocramdownclaim2formatted.set(secureddebt2planpayment)

    if float(secureddebt3amountformatted.get()) != 0.00:
        if secureddebt3typeformatted.get() == "Judgment":
            totalgeneralunsecured += float(secureddebt3amountformatted.get())
        elif secureddebt3typeformatted.get() == "NPPMSI":
            totalgeneralunsecured += float(secureddebt3amountformatted.get())
        elif secureddebt3typeformatted.get() == "PMSI":
            if secureddebt3treatmentformatted.get() == "Retain and Pay":
                secureddebt3planpayment = (0.0525 * float(secureddebt3amountformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
                secureddebt3planpayment = round(secureddebt3planpayment, 2)
                totalnoncramdownamount += secureddebt3planpayment
                plansecurednocramdownclaim3formatted.set(secureddebt3planpayment)
            elif secureddebt3treatmentformatted.get() == "Cramdown":
                secureddebt3planpayment = (0.0525 * float(secureddebt3collateralvalueformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
                secureddebt3planpayment = round(secureddebt3planpayment, 2)
                totalcramdownamount += secureddebt3planpayment
                plansecuredcramdownclaim3formatted.set(secureddebt3planpayment)
        elif secureddebt3typeformatted.get() == "Lien":
            secureddebt3planpayment = (0.06 * float(secureddebt3amountformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
            totalnoncramdownamount += secureddebt3planpayment
            secureddebt3planpayment = round(secureddebt3planpayment, 2)
            plansecurednocramdownclaim3formatted.set(secureddebt3planpayment)

    if float(secureddebt4amountformatted.get()) != 0.00:
        if secureddebt4typeformatted.get() == "Judgment":
            totalgeneralunsecured += float(secureddebt4amountformatted.get())
        elif secureddebt4typeformatted.get() == "NPPMSI":
            totalgeneralunsecured += float(secureddebt4amountformatted.get())
        elif secureddebt4typeformatted.get() == "PMSI":
            if secureddebt4treatmentformatted.get() == "Retain and Pay":
                secureddebt4planpayment = (0.0525 * float(secureddebt4amountformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
                secureddebt4planpayment = round(secureddebt4planpayment, 2)
                totalnoncramdownamount += secureddebt4planpayment
                plansecurednocramdownclaim4formatted.set(secureddebt4planpayment)
            elif secureddebt4treatmentformatted.get() == "Cramdown":
                secureddebt4planpayment = (0.0525 * float(secureddebt4collateralvalueformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
                secureddebt4planpayment = round(secureddebt4planpayment, 2)
                totalcramdownamount += secureddebt4planpayment
                plansecuredcramdownclaim4formatted.set(secureddebt4planpayment)
        elif secureddebt4typeformatted.get() == "Lien":
            secureddebt4planpayment = (0.06 * float(secureddebt4amountformatted.get())) / (12.0 * (1.0 - (1.0 + (0.0525 / 12.0)) ** (-1.0 * float(commitmentperiod))))
            totalnoncramdownamount += secureddebt4planpayment
            secureddebt4planpayment = round(secureddebt4planpayment, 2)
            plansecurednocramdownclaim4formatted.set(secureddebt4planpayment)

    totalnoncramdownamount = round(totalnoncramdownamount, 2)
    totalcramdownamount = round(totalcramdownamount, 2)

    plansecurednocramdowntotalformatted.set(totalnoncramdownamount)
    plansecuredcramdowntotalformatted.set(totalcramdownamount)

    planattorneysfeesformatted.set(attorneysfee)

    totalpriorityunsecured = float(priorityclaimstotalformatted.get()) / float(commitmentperiod)
    totalpriorityunsecured = round(totalpriorityunsecured, 2)
    planpriorityclaimsformatted.set(totalpriorityunsecured)

    dummypaymentcalc = float(planlongtermdebtpaymentformatted.get()) + ltdarrearscost + totalnoncramdownamount + totalcramdownamount + attorneysfee + totalpriorityunsecured
    dummypaymentcalc = dummypaymentcalc * 1.06
    dummypaymentcalc = round(dummypaymentcalc, 2)

    if monthlydisposableincomeformatted.get() != "0.00":
        mdi = float(monthlydisposableincomeformatted.get()) * 60.0
    if chapter7dividendformatted.get() != "0.00":
        ch7 = float(chapter7dividendformatted.get())
    if toydividendformatted.get() != "0.00":
        toy = float(toydividendformatted.get())

    planparamamount = max(mdi, ch7, toy)
    planparambasis = "N/A"
    if planparamamount == mdi:
        planparambasis = "5.1(a)"
    elif planparamamount == ch7:
        planparambasis = "5.1(b)"
    elif planparamamount == toy:
        planparambasis = "5.1(c)"
    
    plangeneralunsecuredclaimsbasisformatted.set(planparambasis)

    planunsecuredividendamount = 0.0
    planunsecuredividendbasis = "N/A"
    planpaymentbudget0 = 0.0
    planpaymentbudget1 = 0.0
    planpaymentbudget2 = 0.0
    planpaymentbudget3 = 0.0

    if planparambasis == "N/A":
        planpaymentbudget0 = float(scheduleiline12entry) - float(schedulejline22cformatted)
        planpaymentbudget1 = planpaymentbudget0 - dummypaymentcalc
        if planpaymentbudget1 > 0:
            planpaymentbudget2 = planpaymentbudget1 * float(commitmentperiod)
            planpaymentbudget3 = planpaymentbudget2 / float(generalunsecuredclaimsformatted.get())
            planpaymentbudget3 = round(planpaymentbudget3, 2)
            planpaymentbudget3 = planpaymentbudget3 * 100
            if planpaymentbudget3 > 1:
                planpaymentbudget3 = 100
        elif planpaymentbudget1 <= 0:
            planpaymentbudget3 = 0.0
    elif planparambasis != "N/A":
        planpaymentbudget3 = float(planparamamount) / float(totalgeneralunsecured)
        planpaymentbudget3 = round(planpaymentbudget3, 2)
        planpaymentbudget3 = planpaymentbudget3 * 100
        if planpaymentbudget3 > 1:
            planpaymentbudget3 = 100

    plangeneralunsecuredclaimspercentageformatted.set(planpaymentbudget3)

    totalgeneralunsecuredpaidunderplan = (planpaymentbudget3 / 100) * totalgeneralunsecured

    plangeneralunsecuredclaimsdividendformatted.set(totalgeneralunsecuredpaidunderplan)

    totalgeneralunsecuredpaidunderplanmonthly = totalgeneralunsecuredpaidunderplan / commitmentperiod

    plangeneralunsecuredclaimsformatted.set(round(totalgeneralunsecuredpaidunderplanmonthly, 2))

    completemonthlytotal0 = float(planlongtermdebtpaymentformatted.get()) + ltdarrearscost + totalnoncramdownamount + \
                           totalcramdownamount + attorneysfee + totalpriorityunsecured + totalgeneralunsecuredpaidunderplanmonthly
    completemonthlytotal1 = completemonthlytotal0 * 0.06
    completemonthlytotal2 = completemonthlytotal0 * 1.06

    plantrusteefeesformatted.set(round(completemonthlytotal1, 2))

    plantotalmonthlycostformatted.set(round(completemonthlytotal2, 2))

    unlock2()
    return

# Layout

panel = ttk.Notebook(root)
panel.grid(sticky=NW, column=0, row=0)

shortmeanstestpage = ttk.Frame(root, borderwidth=10)
shortmeanstestpage.grid(column=0, row=0)
panel.add(shortmeanstestpage, text="1 - Basic Data & Short Means Test")

debtentrypage = ttk.Frame(root, borderwidth=10)
debtentrypage.grid(column=0, row=0)
panel.add(debtentrypage, text="2 - Claim & Data Entry")

house = ttk.Frame(debtentrypage, borderwidth=10)
house.grid(column=0, row=0)

cars = ttk.Frame(debtentrypage, borderwidth=10)
cars.grid(column=2, row=0)

otherdebts = ttk.Frame(debtentrypage, borderwidth=10)
otherdebts.grid(column=0, row=2, columnspan=3)

unsecdebts = ttk.Frame(debtentrypage, borderwidth=10)
unsecdebts.grid(column=0, row=4)

longmeanstestpage = ttk.Frame(root, borderwidth=10)
longmeanstestpage.grid(sticky=NW, column=0, row=0)
panel.add(longmeanstestpage, text="3 - Long Means Test (If Applicable)")

plancalcpage = ttk.Frame(root, borderwidth=10)
plancalcpage.grid(column=0, row=0)
panel.add(plancalcpage, text="4 - Plan Calculator")


countyentry = ttk.Combobox(shortmeanstestpage, values=("Baker County", "Baldwin County", "Ben Hill County", "Berrien County",
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
                                                  "Oglethorpe County", "Peach County", "Pulaski County", "Putnam County", "Quitman County",
                                                  "Randolph County", "Schley County", "Seminole County", "Stewart County",
                                                  "Sumter County", "Talbot County", "Taylor County", "Terrell County",
                                                  "Thomas County", "Tift County", "Turner County", "Twiggs County", "Upson County",
                                                  "Walton County", "Washington County", "Webster County", "Wilcox County",
                                                  "Wilkinson County", "Worth County"), textvariable=countyformatted)
countylabel = ttk.Label(shortmeanstestpage, text="County Name", justify="center")
countylabel.grid(column=0, row=1, pady=5, padx=10)
countyentry.grid(column=0, row=2, pady=5, padx=10)
countyentry.focus()

filingstatuslabel = ttk.Label(shortmeanstestpage, text="Marital/Filing Status", justify="center", state="normal")
filingstatuslabel.grid(column=1, row=1, pady=5, columnspan=3)
filingstatussinglesinglecheckbutton = ttk.Checkbutton(shortmeanstestpage, text="Single/Single", onvalue=1, offvalue=0, variable=maritalfilingstatussinglesingleformatted, state="normal")
filingstatussinglesinglecheckbutton.grid(column=1, row=2, padx=10)
filingstatusmarriedsinglecheckbutton = ttk.Checkbutton(shortmeanstestpage, text="Married/Single", onvalue=1, offvalue=0, variable=maritalfilingstatusmarriedsingleformatted, command=lambda: married(), state="normal")
filingstatusmarriedsinglecheckbutton.grid(column=2, row=2, padx=10)
filingstatusmarriedcheckbutton = ttk.Checkbutton(shortmeanstestpage, text="Married/Married", onvalue=1, offvalue=0, variable=maritalfilingstatusmarriedmarriedformatted, state="normal")
filingstatusmarriedcheckbutton.grid(column=3, row=2, padx=10)

householdsizeentry = ttk.Entry(shortmeanstestpage, textvariable=householdsizeformatted)
householdsizelabel = ttk.Label(shortmeanstestpage, text="Household Size", justify="center")
householdsizelabel.grid(column=0, row=3, pady=5, padx=10)
householdsizeentry.grid(column=0, row=4, pady=5, padx=10)

householdover65entry = ttk.Entry(shortmeanstestpage, textvariable=householdover65formatted)
householdover65label = ttk.Label(shortmeanstestpage, text="Houshold Over 65", justify="center")
householdover65label.grid(column=1, row=3, pady=5, padx=10)
householdover65entry.grid(column=1, row=4, pady=5, padx=10)

householdunder18entry = ttk.Entry(shortmeanstestpage, textvariable=householdunder18formatted)
householdunder18label = ttk.Label(shortmeanstestpage, text="Household Under 18", justify="center")
householdunder18label.grid(column=2, row=3, pady=5, padx=10)
householdunder18entry.grid(column=2, row=4, pady=5, padx=10)

averagemonthlyincomeentry = ttk.Entry(shortmeanstestpage, textvariable=averagemonthlyincomeformatted)
averagemonthlyincomelabel = ttk.Label(shortmeanstestpage, text="Avg. Monthly Income", justify="center")
averagemonthlyincomelabel.grid(column=0, row=5, pady=5, padx=10)
averagemonthlyincomeentry.grid(column=0, row=6, pady=5, padx=10)

maritaladjustmententry = ttk.Entry(shortmeanstestpage, textvariable=maritaladjustmentformatted, state="disabled")
maritaladjustmentlabel = ttk.Label(shortmeanstestpage, text="Marital Adjustment", justify="center", state="disabled")
maritaladjustmentlabel.grid(column=1, row=5, pady=5, padx=10)
maritaladjustmententry.grid(column=1, row=6, pady=5, padx=10)

currentmonthlyincomeentry = ttk.Entry(shortmeanstestpage, textvariable=currentmonthlyincomeformatted, state="disabled")
currentmonthlyincomelabel =ttk.Label(shortmeanstestpage, text="CMI", state="disabled")
currentmonthlyincomelabel.grid(column=2, row=5, pady=5, padx=10)
currentmonthlyincomeentry.grid(column=2, row=6, pady=5, padx=10)

childsupportreceivedentry = ttk.Entry(shortmeanstestpage, textvariable=childsupportreceivedformatted)
childsupportreceivedlabel = ttk.Label(shortmeanstestpage, text="CS Portion of CMI", justify="center")
childsupportreceivedlabel.grid(column=3, row=5, pady=5, padx=10)
childsupportreceivedentry.grid(column=3, row=6, pady=5, padx=10)

shortmeanstestbutton = ttk.Button(shortmeanstestpage, text="Run Short Means Test", command=lambda: [form122c1(), unlock0()])
shortmeanstestbutton.grid(column=0, row=7, pady=10, padx=10)

blankline0 = ttk.Label(shortmeanstestpage, text="", state="disabled")
blankline0.grid(column=0, row=8, pady=5)

applicablecomittmentperiod36m = ttk.Radiobutton(shortmeanstestpage, text="36 months", variable=comittmentperiodformatted, value="36", state="disabled")
applicablecomittmentperiod60m = ttk.Radiobutton(shortmeanstestpage, text="60 months", variable=comittmentperiodformatted, value="58", state="disabled")
applicablecomittmentperioddefined = ttk.Entry(shortmeanstestpage, textvariable=comittmentperiodformatted, state="disabled")
applicablecomittmentperiodlabel = ttk.Label(shortmeanstestpage, text="Applicable Commitment Period", state="normal")
applicablecomittmentperiodlabel.grid(column=0, row=9, columnspan=3, pady=5)
applicablecomittmentperiod36m.grid(column=0, row=10, pady=5)
applicablecomittmentperiod60m.grid(column=1, row=10, pady=5)
applicablecomittmentperioddefined.grid(column=2, row=10, pady=5)

meanstestresultlabel = ttk.Label(shortmeanstestpage, text="Means Test Result")
meansteststatuslabel = ttk.Label(shortmeanstestpage, background="cyan", anchor="center", text="No Means Test Data Entered")
meanstestresultlabel.grid(column=1, row=11, pady=5)
meansteststatuslabel.grid(column=1, row=12, pady=5)

housequeryentryyes = ttk.Radiobutton(house, text="Yes", variable=housequeryformatted, value="Yes", state="disabled", command=yes0)
housequeryentryno = ttk.Radiobutton(house, text="No", variable=housequeryformatted, value="No", state="disabled", command=no0)
housequerylabel = ttk.Label(house, state="disabled", text="House?")
housequerylabel.grid(column=0, row=0, pady=5)
housequeryentryyes.grid(sticky="W", column=0, row=1)
housequeryentryno.grid(sticky="W", column=0, row=2)

housevalueentry = ttk.Entry(house, textvariable=housevalueformatted, state="disabled")
housevaluelabel = ttk.Label(house, text="Value of house", state="disabled")
housevaluelabel.grid(column=1, row=0, pady=5)
housevalueentry.grid(column=1, row=1)

houseplantreatmentpay = ttk.Radiobutton(house, text="Retain & Pay", variable=houseplantreatmentformatted, value="Pay", command=lambda: houseretainandpay(), state="disabled")
houseplantreatmentsurrender = ttk.Radiobutton(house, text="Surrender", variable=houseplantreatmentformatted, value="Surrender", state="disabled")
houseplantreatmentlabel = ttk.Label(house, text="Plan Treatment", state="disabled")
houseplantreatmentlabel.grid(column=1, row=2, pady=5)
houseplantreatmentpay.grid(sticky="W", column=1, row=3)
houseplantreatmentsurrender.grid(sticky="W", column=1, row=4)

firstmortgagequeryentryyes = ttk.Radiobutton(house, text="Yes", variable=firstmortgagequeryformatted, value="Yes", command=yes1, state="disabled")
firstmortgagequeryentryno = ttk.Radiobutton(house, text="No", variable=firstmortgagequeryformatted, value="No", command=no1, state="disabled")
firstmortgagequerylabel = ttk.Label(house, text="First mortgage?", state="disabled")
firstmortgagequerylabel.grid(column=2, row=0, pady=5)
firstmortgagequeryentryyes.grid(sticky="W", column=2, row=1)
firstmortgagequeryentryno.grid(sticky="W", column=2, row=2)

firstmortgagenameentry = ttk.Entry(house, textvariable=firstmortgagenameformatted, state="disabled")
firstmortgagenamelabel = ttk.Label(house, text="First Mortgage Creditor", state="disabled")
firstmortgagenamelabel.grid(column=3, row=0, pady=5)
firstmortgagenameentry.grid(column=3, row=1)

firstmortgageamountentry = ttk.Entry(house, textvariable=firstmortgageamountformatted, state="disabled")
firstmortgageamountlabel = ttk.Label(house, text="Amount Owed", state="disabled")
firstmortgageamountlabel.grid(column=3, row=2, pady=5)
firstmortgageamountentry.grid(column=3, row=3)

firstmortgagecurrentpaymententry = ttk.Entry(house, textvariable=firstmortgagecurrentpaymentformatted, state="disabled")
firstmortgagecurrentpaymentlabel = ttk.Label(house, text="Monthly Payment", state="disabled")
firstmortgagecurrentpaymentlabel.grid(column=3, row=4, pady=5)
firstmortgagecurrentpaymententry.grid(column=3, row=5)

firstmortgagearrearsentry = ttk.Entry(house, textvariable=firstmortgagearrearsformatted, state="disabled")
firstmortgagearrearslabel = ttk.Label(house, text="Arrears", state="disabled")
firstmortgagearrearslabel.grid(column=3, row=6, pady=5)
firstmortgagearrearsentry.grid(column=3, row=7)

secondmortgagequeryentryyes = ttk.Radiobutton(house, text="Yes", variable=secondmortgagequeryformatted, value="Yes", command=yes2, state="disabled")
secondmortgagequeryentryno = ttk.Radiobutton(house, text="No", variable=secondmortgagequeryformatted, value="No", command=no2, state="disabled")
secondmortgagequerylabel = ttk.Label(house, text="Second mortgage?", state="disabled")
secondmortgagequerylabel.grid(column=2, row=8, pady=5)
secondmortgagequeryentryyes.grid(sticky="W", column=2, row=9)
secondmortgagequeryentryno.grid(sticky="W", column=2, row=10)

secondmortgagenameentry = ttk.Entry(house, textvariable=secondmortgagenameformatted, state="disabled")
secondmortgagenamelabel = ttk.Label(house, text="Second Mortgage Creditor", state="disabled")
secondmortgagenamelabel.grid(column=3, row=8, pady=5)
secondmortgagenameentry.grid(column=3, row=9)

secondmortgageamountentry = ttk.Entry(house, textvariable=secondmortgageamountformatted, state="disabled")
secondmortgageamountlabel = ttk.Label(house, text="Amount Owed", state="disabled")
secondmortgageamountlabel.grid(column=3, row=10, pady=5)
secondmortgageamountentry.grid(column=3, row=11)

secondmortgagecurrentpaymententry = ttk.Entry(house, textvariable=secondmortgagecurrentpaymentformatted, state="disabled")
secondmortgagecurrentpaymentlabel = ttk.Label(house, text="Monthly Payment", state="disabled")
secondmortgagecurrentpaymentlabel.grid(column=3, row=12, pady=5)
secondmortgagecurrentpaymententry.grid(column=3, row=13)

secondmortgagearrearsentry = ttk.Entry(house, textvariable=secondmortgagearrearsformatted, state="disabled")
secondmortgagearrearslabel = ttk.Label(house, text="Arrears", state="disabled")
secondmortgagearrearslabel.grid(column=3, row=14, pady=5)
secondmortgagearrearsentry.grid(column=3, row=15)

numberofcarsentry0 = ttk.Radiobutton(cars, text="0", state="disabled", variable=numberofcarsformatted, value="0", command=car0)
numberofcarsentry1 = ttk.Radiobutton(cars, text="1", state="disabled", variable=numberofcarsformatted, value="1", command=car1)
numberofcarsentry2 = ttk.Radiobutton(cars, text="2", state="disabled", variable=numberofcarsformatted, value="2", command=car2)
numberofcarslabel = ttk.Label(cars, state="disabled", text="Number of Cars")
numberofcarslabel.grid(column=0, row=0, pady=5)
numberofcarsentry0.grid(sticky="W", column=0, row=1)
numberofcarsentry1.grid(sticky="W", column=0, row=2)
numberofcarsentry2.grid(sticky="W", column=0, row=3)

car1valueentry = ttk.Entry(cars, textvariable=car1valueformatted, state="disabled")
car1valuelabel = ttk.Label(cars, text="Value of Car #1", state="disabled")
car1valuelabel.grid(column=1, row=0, pady=5)
car1valueentry.grid(column=1, row=1)

car1plantreatmentpay = ttk.Radiobutton(cars, text="Retain & Pay", variable=car1plantreatmentformatted, value="Pay", command=lambda: car1retainandpay(), state="disabled")
car1plantreatmentsurrender = ttk.Radiobutton(cars, text="Surrender", variable=car1plantreatmentformatted, value="Surrender", command=lambda: car1surrender(), state="disabled")
car1plantreatmentlabel = ttk.Label(cars, text="Plan Treatment", state="disabled")
car1plantreatmentlabel.grid(column=1, row=3, pady=5)
car1plantreatmentpay.grid(sticky="W", column=1, row=4)
car1plantreatmentsurrender.grid(sticky="W", column=1, row=5)

car1loanqueryentryyes = ttk.Radiobutton(cars, text="Yes", variable=car1loanqueryformatted, value="Yes", command=yes3, state="disabled")
car1loanqueryentryno = ttk.Radiobutton(cars, text="No", variable=car1loanqueryformatted, value="No", command=no3, state="disabled")
car1loanquerylabel = ttk.Label(cars, text="Loan on Car #1?", state="disabled")
car1loanquerylabel.grid(column=2, row=0, pady=5)
car1loanqueryentryyes.grid(sticky="W", column=2, row=1)
car1loanqueryentryno.grid(sticky="W", column=2, row=2)

car1910queryyes = ttk.Radiobutton(cars, text="Yes", variable=car1910statusformatted, state="disabled", value="Yes")
car1910queryno = ttk.Radiobutton(cars, text="No", variable=car1910statusformatted, state="disabled", value="No")
car1910querylabel = ttk.Label(cars, text="910 claim?", state="disabled")
car1910querylabel.grid(column=2, row=3, pady=5)
car1910queryyes.grid(sticky="W", column=2, row=4)
car1910queryno.grid(sticky="W", column=2, row=5)

car1loannameentry = ttk.Entry(cars, textvariable=car1loannameformatted, state="disabled")
car1loannamelabel = ttk.Label(cars, text="Car #1 Creditor", state="disabled")
car1loannamelabel.grid(column=3, row=0, pady=5)
car1loannameentry.grid(column=3, row=1)

car1loanamountentry = ttk.Entry(cars, textvariable=car1loanamountformatted, state="disabled")
car1loanamountlabel = ttk.Label(cars, text="Amount Owed", state="disabled")
car1loanamountlabel.grid(column=3, row=2, pady=5)
car1loanamountentry.grid(column=3, row=3)

car1loancurrentpaymententry = ttk.Entry(cars, textvariable=car1loancurrentpaymentformatted, state="disabled")
car1loancurrentpaymentlabel = ttk.Label(cars, text="Monthly Payment", state="disabled")
car1loancurrentpaymentlabel.grid(column=3, row=4, pady=5)
car1loancurrentpaymententry.grid(column=3, row=5)

car1loanarrearsentry = ttk.Entry(cars, textvariable=car1loanarrearsformatted, state="disabled")
car1loanarrearslabel = ttk.Label(cars, text="Arrears", state="disabled")
car1loanarrearslabel.grid(column=3, row=6, pady=5)
car1loanarrearsentry.grid(column=3, row=7)

car2valueentry = ttk.Entry(cars, textvariable=car2valueformatted, state="disabled")
car2valuelabel = ttk.Label(cars, text="Value of Car #2", state="disabled")
car2valuelabel.grid(column=1, row=8, pady=5)
car2valueentry.grid(column=1, row=9)

car2plantreatmentpay = ttk.Radiobutton(cars, text="Retain & Pay", variable=car2plantreatmentformatted, value="Pay", command=lambda: car2retainandpay(), state="disabled")
car2plantreatmentsurrender = ttk.Radiobutton(cars, text="Surrender", variable=car2plantreatmentformatted, value="Surrender", command=lambda: car2surrender(), state="disabled")
car2plantreatmentlabel = ttk.Label(cars, text="Plan Treatment", state="disabled")
car2plantreatmentlabel.grid(column=1, row=11, pady=5)
car2plantreatmentpay.grid(sticky="W", column=1, row=12)
car2plantreatmentsurrender.grid(sticky="W", column=1, row=13)

car2loanqueryentryyes = ttk.Radiobutton(cars, text="Yes", variable=car2loanqueryformatted, value="Yes", command=yes4, state="disabled")
car2loanqueryentryno = ttk.Radiobutton(cars, text="No", variable=car2loanqueryformatted, value="No", command=no4, state="disabled")
car2loanquerylabel = ttk.Label(cars, text="Loan on Car #2?", state="disabled")
car2loanquerylabel.grid(column=2, row=8, pady=5)
car2loanqueryentryyes.grid(sticky="W", column=2, row=9)
car2loanqueryentryno.grid(sticky="W", column=2, row=10)

car2910queryyes = ttk.Radiobutton(cars, text="Yes", variable=car2910statusformatted, state="disabled", value="Yes")
car2910queryno = ttk.Radiobutton(cars, text="No", variable=car2910statusformatted, state="disabled", value="No")
car2910querylabel = ttk.Label(cars, text="910 claim?", state="disabled")
car2910querylabel.grid(column=2, row=11, pady=5)
car2910queryyes.grid(sticky="W", column=2, row=12)
car2910queryno.grid(sticky="W", column=2, row=13)

car2loannameentry = ttk.Entry(cars, textvariable=car2loannameformatted, state="disabled")
car2loannamelabel = ttk.Label(cars, text="Car #2 Creditor", state="disabled")
car2loannamelabel.grid(column=3, row=8, pady=5)
car2loannameentry.grid(column=3, row=9)

car2loanamountentry = ttk.Entry(cars, textvariable=car2loanamountformatted, state="disabled")
car2loanamountlabel = ttk.Label(cars, text="Amount Owed", state="disabled")
car2loanamountlabel.grid(column=3, row=10, pady=5)
car2loanamountentry.grid(column=3, row=11)

car2loancurrentpaymententry = ttk.Entry(cars, textvariable=car2loancurrentpaymentformatted, state="disabled")
car2loancurrentpaymentlabel = ttk.Label(cars, text="Monthly Payment", state="disabled")
car2loancurrentpaymentlabel.grid(column=3, row=12, pady=5)
car2loancurrentpaymententry.grid(column=3, row=13)

car2loanarrearsentry = ttk.Entry(cars, textvariable=car2loanarrearsformatted, state="disabled")
car2loanarrearslabel = ttk.Label(cars, text="Arrears", state="disabled")
car2loanarrearslabel.grid(column=3, row=14, pady=5)
car2loanarrearsentry.grid(column=3, row=15)

verticalseparator1 = ttk.Separator(debtentrypage, orient='vertical')
verticalseparator1.grid(column=1, row=0, sticky=NS, rowspan=1, padx=10)

horizontalseparator1 = ttk.Separator(debtentrypage, orient='horizontal')
horizontalseparator1.grid(column=0, row=1, sticky=EW, columnspan=16, pady=10)

horizontalseparator2 = ttk.Separator(debtentrypage, orient='horizontal')
horizontalseparator2.grid(column=0, row=3, sticky=EW, columnspan=16, pady=10)

othersecureddebtnamelabel = ttk.Label(otherdebts, text="Sec. Creditor Name", state="disabled")
othersecureddebtnamelabel.grid(column=0, row=0, pady=5, padx=10)

secureddebt1nameentry = ttk.Entry(otherdebts, textvariable=secureddebt1nameformatted, state="disabled")
secureddebt1nameentry.grid(column=0, row=1, padx=10)
secureddebt2nameentry = ttk.Entry(otherdebts, textvariable=secureddebt2nameformatted, state="disabled")
secureddebt2nameentry.grid(column=0, row=2, padx=10)
secureddebt3nameentry = ttk.Entry(otherdebts, textvariable=secureddebt3nameformatted, state="disabled")
secureddebt3nameentry.grid(column=0, row=3, padx=10)
secureddebt4nameentry = ttk.Entry(otherdebts, textvariable=secureddebt4nameformatted, state="disabled")
secureddebt4nameentry.grid(column=0, row=4, padx=10)

othersecureddebtamountlabel = ttk.Label(otherdebts, text="Total Owed", state="disabled")
othersecureddebtamountlabel.grid(column=1, row=0, pady=5, padx=10)

secureddebt1amountentry = ttk.Entry(otherdebts, textvariable=secureddebt1amountformatted, state="disabled")
secureddebt1amountentry.grid(column=1, row=1, padx=10)
secureddebt2amountentry = ttk.Entry(otherdebts, textvariable=secureddebt2amountformatted, state="disabled")
secureddebt2amountentry.grid(column=1, row=2, padx=10)
secureddebt3amountentry = ttk.Entry(otherdebts, textvariable=secureddebt3amountformatted, state="disabled")
secureddebt3amountentry.grid(column=1, row=3, padx=10)
secureddebt4amountentry = ttk.Entry(otherdebts, textvariable=secureddebt4amountformatted, state="disabled")
secureddebt4amountentry.grid(column=1, row=4, padx=10)

othersecureddebtcollaterallabel = ttk.Label(otherdebts, text="Value of Collateral", state="disabled")
othersecureddebtcollaterallabel.grid(column=2, row=0, pady=5)

secureddebt1collateralentry = ttk.Entry(otherdebts, textvariable=secureddebt1collateralvalueformatted, state="disabled")
secureddebt1collateralentry.grid(column=2, row=1)
secureddebt2collateralentry = ttk.Entry(otherdebts, textvariable=secureddebt2collateralvalueformatted, state="disabled")
secureddebt2collateralentry.grid(column=2, row=2)
secureddebt3collateralentry = ttk.Entry(otherdebts, textvariable=secureddebt3collateralvalueformatted, state="disabled")
secureddebt3collateralentry.grid(column=2, row=3)
secureddebt4collateralentry = ttk.Entry(otherdebts, textvariable=secureddebt4collateralvalueformatted, state="disabled")
secureddebt4collateralentry.grid(column=2, row=4)

othersecureddebttypelabel = ttk.Label(otherdebts, text="Type", justify="center", state="disabled")
othersecureddebttypelabel.grid(column=3, row=0, pady=5, columnspan=4)

secureddebt1typeentryjudgment = ttk.Radiobutton(otherdebts, text="Judgment", value="Judgment", variable=secureddebt1typeformatted, state="disabled")
secureddebt1typeentryjudgment.grid(column=3, row=1, padx=10)
secureddebt2typeentryjudgment = ttk.Radiobutton(otherdebts, text="Judgment", value="Judgment", variable=secureddebt2typeformatted, state="disabled")
secureddebt2typeentryjudgment.grid(column=3, row=2, padx=10)
secureddebt3typeentryjudgment = ttk.Radiobutton(otherdebts, text="Judgment", value="Judgment", variable=secureddebt3typeformatted, state="disabled")
secureddebt3typeentryjudgment.grid(column=3, row=3, padx=10)
secureddebt4typeentryjudgment = ttk.Radiobutton(otherdebts, text="Judgment", value="Judgment", variable=secureddebt4typeformatted, state="disabled")
secureddebt4typeentryjudgment.grid(column=3, row=4, padx=10)

secureddebt1typeentrypmsi = ttk.Radiobutton(otherdebts, text="PMSI", value="PMSI", variable=secureddebt1typeformatted, state="disabled")
secureddebt1typeentrypmsi.grid(column=4, row=1, padx=10)
secureddebt2typeentrypmsi = ttk.Radiobutton(otherdebts, text="PMSI", value="PMSI", variable=secureddebt2typeformatted, state="disabled")
secureddebt2typeentrypmsi.grid(column=4, row=2, padx=10)
secureddebt3typeentrypmsi = ttk.Radiobutton(otherdebts, text="PMSI", value="PMSI", variable=secureddebt3typeformatted, state="disabled")
secureddebt3typeentrypmsi.grid(column=4, row=3, padx=10)
secureddebt4typeentrypmsi = ttk.Radiobutton(otherdebts, text="PMSI", value="PMSI", variable=secureddebt4typeformatted, state="disabled")
secureddebt4typeentrypmsi.grid(column=4, row=4, padx=10)

secureddebt1typeentrynppmsi = ttk.Radiobutton(otherdebts, text="NPPMSI", value="NPPMSI", variable=secureddebt1typeformatted, state="disabled")
secureddebt1typeentrynppmsi.grid(column=5, row=1, padx=10)
secureddebt2typeentrynppmsi = ttk.Radiobutton(otherdebts, text="NPPMSI", value="NPPMSI", variable=secureddebt2typeformatted, state="disabled")
secureddebt2typeentrynppmsi.grid(column=5, row=2, padx=10)
secureddebt3typeentrynppmsi = ttk.Radiobutton(otherdebts, text="NPPMSI", value="NPPMSI", variable=secureddebt3typeformatted, state="disabled")
secureddebt3typeentrynppmsi.grid(column=5, row=3, padx=10)
secureddebt4typeentrynppmsi = ttk.Radiobutton(otherdebts, text="NPPMSI", value="NPPMSI", variable=secureddebt4typeformatted, state="disabled")
secureddebt4typeentrynppmsi.grid(column=5, row=4, padx=10)

secureddebt1typeentrylien = ttk.Radiobutton(otherdebts, text="Lien", value="Lien", variable=secureddebt1typeformatted, state="disabled")
secureddebt1typeentrylien.grid(column=6, row=1, padx=10)
secureddebt2typeentrylien = ttk.Radiobutton(otherdebts, text="Lien", value="Lien", variable=secureddebt2typeformatted, state="disabled")
secureddebt2typeentrylien.grid(column=6, row=2, padx=10)
secureddebt3typeentrylien = ttk.Radiobutton(otherdebts, text="Lien", value="Lien", variable=secureddebt3typeformatted, state="disabled")
secureddebt3typeentrylien.grid(column=6, row=3, padx=10)
secureddebt4typeentrylien = ttk.Radiobutton(otherdebts, text="Lien", value="Lien", variable=secureddebt4typeformatted, state="disabled")
secureddebt4typeentrylien.grid(column=6, row=4, padx=10)

verticalseparator3 = ttk.Separator(otherdebts, orient='vertical')
verticalseparator3.grid(column=7, row=0, sticky=tkinter.NS, rowspan=5, padx=10)

othersecureddebttreatmentlabel = ttk.Label(otherdebts, text="Treatment", justify="center", state="disabled")
othersecureddebttreatmentlabel.grid(column=8, row=0, pady=5, columnspan=4)

secureddebt1treatmentrpentry = ttk.Radiobutton(otherdebts, text="R & P", value="Retain and Pay", variable=secureddebt1treatmentformatted, state="disabled")
secureddebt1treatmentrpentry.grid(column=8, row=1, padx=10)
secureddebt2treatmentrpentry = ttk.Radiobutton(otherdebts, text="R & P", value="Retain and Pay", variable=secureddebt2treatmentformatted, state="disabled")
secureddebt2treatmentrpentry.grid(column=8, row=2, padx=10)
secureddebt3treatmentrpentry = ttk.Radiobutton(otherdebts, text="R & P", value="Retain and Pay", variable=secureddebt3treatmentformatted, state="disabled")
secureddebt3treatmentrpentry.grid(column=8, row=3, padx=10)
secureddebt4treatmentrpentry = ttk.Radiobutton(otherdebts, text="R & P", value="Retain and Pay", variable=secureddebt4treatmentformatted, state="disabled")
secureddebt4treatmentrpentry.grid(column=8, row=4, padx=10)

secureddebt1treatmentcdentry = ttk.Radiobutton(otherdebts, text="Cram", value="Cramdown", variable=secureddebt1treatmentformatted, state="disabled")
secureddebt1treatmentcdentry.grid(column=9, row=1, padx=10)
secureddebt2treatmentcdentry = ttk.Radiobutton(otherdebts, text="Cram", value="Cramdown", variable=secureddebt2treatmentformatted, state="disabled")
secureddebt2treatmentcdentry.grid(column=9, row=2, padx=10)
secureddebt3treatmentcdentry = ttk.Radiobutton(otherdebts, text="Cram", value="Cramdown", variable=secureddebt3treatmentformatted, state="disabled")
secureddebt3treatmentcdentry.grid(column=9, row=3, padx=10)
secureddebt4treatmentcdentry = ttk.Radiobutton(otherdebts, text="Cram", value="Cramdown", variable=secureddebt4treatmentformatted, state="disabled")
secureddebt4treatmentcdentry.grid(column=9, row=4, padx=10)

secureddebt1treatmentsurrenderentry = ttk.Radiobutton(otherdebts, text="Surrender", value="Surrender", variable=secureddebt1treatmentformatted, state="disabled")
secureddebt1treatmentsurrenderentry.grid(column=10, row=1, padx=10)
secureddebt2treatmentsurrenderentry = ttk.Radiobutton(otherdebts, text="Surrender", value="Surrender", variable=secureddebt2treatmentformatted, state="disabled")
secureddebt2treatmentsurrenderentry.grid(column=10, row=2, padx=10)
secureddebt3treatmentsurrenderentry = ttk.Radiobutton(otherdebts, text="Surrender", value="Surrender", variable=secureddebt3treatmentformatted, state="disabled")
secureddebt3treatmentsurrenderentry.grid(column=10, row=3, padx=10)
secureddebt4treatmentsurrenderentry = ttk.Radiobutton(otherdebts, text="Surrender", value="Surrender", variable=secureddebt4treatmentformatted, state="disabled")
secureddebt4treatmentsurrenderentry.grid(column=10, row=4, padx=10)

secureddebt1treatmentavoidentry = ttk.Radiobutton(otherdebts, text="Avoid", value="Avoid", variable=secureddebt1treatmentformatted, state="disabled")
secureddebt1treatmentavoidentry.grid(column=11, row=1, padx=10)
secureddebt2treatmentavoidentry = ttk.Radiobutton(otherdebts, text="Avoid", value="Avoid", variable=secureddebt2treatmentformatted, state="disabled")
secureddebt2treatmentavoidentry.grid(column=11, row=2, padx=10)
secureddebt3treatmentavoidentry = ttk.Radiobutton(otherdebts, text="Avoid", value="Avoid", variable=secureddebt3treatmentformatted, state="disabled")
secureddebt3treatmentavoidentry.grid(column=11, row=3, padx=10)
secureddebt4treatmentavoidentry = ttk.Radiobutton(otherdebts, text="Avoid", value="Avoid", variable=secureddebt4treatmentformatted, state="disabled")
secureddebt4treatmentavoidentry.grid(column=11, row=4, padx=10)

priorityclaimstotalentry = ttk.Entry(unsecdebts, textvariable=priorityclaimstotalformatted, state="disabled")
priorityclaimstotallabel = ttk.Label(unsecdebts, text="Priority Claims", state="disabled")
priorityclaimstotallabel.grid(column=0, row=0, pady=5, padx=10)
priorityclaimstotalentry.grid(column=0, row=1, padx=10)

generalunsecuredentry = ttk.Entry(unsecdebts, textvariable=generalunsecuredclaimsformatted, state="disabled")
generalunsecuredlabel = ttk.Label(unsecdebts, text="Gen. Unsec. Claims", state="disabled")
generalunsecuredlabel.grid(column=0, row=2, pady=5, padx=10)
generalunsecuredentry.grid(column=0, row=3, padx=10)

attorneysfeeentry = ttk.Entry(unsecdebts, textvariable=attorneysfeeformatted, state="disabled")
attorneysfeelabel = ttk.Label(unsecdebts, text="Attorney's Fee", state="disabled")
attorneysfeelabel.grid(column=0, row=4, pady=5, padx=10)
attorneysfeeentry.grid(column=0, row=5, padx=10)

chapter7dividendentry = ttk.Entry(unsecdebts, textvariable=chapter7dividendformatted, state="disabled")
chapter7dividendlabel = ttk.Label(unsecdebts, text="Ch. 7 Dividend", state="disabled")
chapter7dividendlabel.grid(column=1, row=0, pady=5, padx=10)
chapter7dividendentry.grid(column=1, row=1, padx=10)

toydividendentry = ttk.Entry(unsecdebts, textvariable=toydividendformatted, state="disabled")
toydividendlabel = ttk.Label(unsecdebts, text="Toy Dividend", state="disabled")
toydividendlabel.grid(column=1, row=2, pady=5, padx=10)
toydividendentry.grid(column=1, row=3, padx=10)

scheduleiline12entry = ttk.Entry(unsecdebts, textvariable=scheduleiline12formatted, state="disabled")
scheduleiline12label = ttk.Label(unsecdebts, text="Schedule I - Line 12", state="disabled")
scheduleiline12label.grid(column=2, row=0, pady=5, padx=10)
scheduleiline12entry.grid(column=2, row=1, padx=10)

schedulejline22centry = ttk.Entry(unsecdebts, textvariable=schedulejline22cformatted, state="disabled")
schedulejline22clabel = ttk.Label(unsecdebts, text="Schedule J - Line 22c", state="disabled")
schedulejline22clabel.grid(column=2, row=2, pady=5)
schedulejline22centry.grid(column=2, row=3)

presumptivemonthlyplanpaymententry = ttk.Entry(unsecdebts, textvariable=presumptiveplanpaymentformatted, state="disabled")
presumptivemonthlyplanpaymentlabel = ttk.Label(unsecdebts, text="Presumptive Plan Payment", state="disabled")
presumptivemonthlyplanpaymentlabel.grid(column=2, row=4, pady=5)
presumptivemonthlyplanpaymententry.grid(column=2, row=5)

meanstestprojectedplanpaymententry = ttk.Entry(longmeanstestpage, textvariable=mtline36aformatted, state="disabled")
meanstestprojectedplanpaymentlabel = ttk.Label(longmeanstestpage, text="Projected Plan Payment", state="disabled")
meanstestprojectedplanpaymentlabel.grid(column=3, row=24, pady=5, padx=10)
meanstestprojectedplanpaymententry.grid(column=3, row=25)

meanstestfoodclothingandotheritemsentry = ttk.Entry(longmeanstestpage, textvariable=mtline6formatted, state="disabled")
meanstestfoodclothingandotheritemslabel = ttk.Label(longmeanstestpage, text="Food, Clothing, etc.", state="disabled")
meanstestfoodclothingandotheritemslabel.grid(column=0, row=0, pady=5, padx=10)
meanstestfoodclothingandotheritemsentry.grid(column=0, row=1)

meanstestoutofpockethealthcareentry = ttk.Entry(longmeanstestpage, textvariable=mtline7formatted, state="disabled")
meanstestoutofpockethealthcarelabel = ttk.Label(longmeanstestpage, text="OOP Healthcare", state="disabled")
meanstestoutofpockethealthcarelabel.grid(column=0, row=2, pady=5, padx=10)
meanstestoutofpockethealthcareentry.grid(column=0, row=3)

meanstesthousingandutilitiesinsuranceandoperatingentry = ttk.Entry(longmeanstestpage, textvariable=mtline8formatted, state="disabled")
meanstesthousingandutilitiesinsuranceandoperatinglabel = ttk.Label(longmeanstestpage, text="Housing: Ins. and Op.", state="disabled")
meanstesthousingandutilitiesinsuranceandoperatinglabel.grid(column=0, row=4, pady=5, padx=10)
meanstesthousingandutilitiesinsuranceandoperatingentry.grid(column=0, row=5)

meanstesthousingandutilitiesmortgageorrententry = ttk.Entry(longmeanstestpage, textvariable=mtline9formatted, state="disabled")
meanstesthousingandutilitiesmortgageorrentlabel = ttk.Label(longmeanstestpage, text="Housing: Mort. or Rent", state="disabled")
meanstesthousingandutilitiesmortgageorrentlabel.grid(column=0, row=6, pady=5, padx=10)
meanstesthousingandutilitiesmortgageorrententry.grid(column=0, row=7)

meanstestvehicleoperationexpenseentry = ttk.Entry(longmeanstestpage, textvariable=mtline12formatted, state="disabled")
meanstestvehicleoperationexpenselabel = ttk.Label(longmeanstestpage, text="Vehicle Op. / Public Trans.", state="disabled")
meanstestvehicleoperationexpenselabel.grid(column=0, row=8, pady=5, padx=10)
meanstestvehicleoperationexpenseentry.grid(column=0, row=9)

meanstestvehicleownershiporleaseentry1 = ttk.Entry(longmeanstestpage, textvariable=mtline13cformatted, state="disabled")
meanstestvehicleownershiporleaselabel1 = ttk.Label(longmeanstestpage, text="Veh. 1 Ownership", state="disabled")
meanstestvehicleownershiporleaselabel1.grid(column=0, row=10, pady=5, padx=10)
meanstestvehicleownershiporleaseentry1.grid(column=0, row=11)

meanstestvehicleownershiporleaseentry2 = ttk.Entry(longmeanstestpage, textvariable=mtline13fformatted, state="disabled")
meanstestvehicleownershiporleaselabel2 = ttk.Label(longmeanstestpage, text="Veh. 2 Ownership", state="disabled")
meanstestvehicleownershiporleaselabel2.grid(column=0, row=12, pady=5, padx=10)
meanstestvehicleownershiporleaseentry2.grid(column=0, row=13)

meanstesttaxesentry = ttk.Entry(longmeanstestpage, textvariable=mtline16formatted, state="disabled")
meanstesttaxeslabel = ttk.Label(longmeanstestpage, text="Taxes", state="disabled")
meanstesttaxeslabel.grid(column=0, row=14, pady=5, padx=10)
meanstesttaxesentry.grid(column=0, row=15)

meanstestinvoluntarydeductionsentry = ttk.Entry(longmeanstestpage, textvariable=mtline17formatted, state="disabled")
meanstestinvoluntarydeductionslabel = ttk.Label(longmeanstestpage, text="Invol. Deductions", state="disabled")
meanstestinvoluntarydeductionslabel.grid(column=0, row=16, pady=5, padx=10)
meanstestinvoluntarydeductionsentry.grid(column=0, row=17)

meanstestlifeinsuranceentry = ttk.Entry(longmeanstestpage, textvariable=mtline18formatted, state="disabled")
meanstestlifeinsurancelabel = ttk.Label(longmeanstestpage, text="Life Insurance", state="disabled")
meanstestlifeinsurancelabel.grid(column=0, row=18, pady=5, padx=10)
meanstestlifeinsuranceentry.grid(column=0, row=19)

meanstestcourtorderedpaymentsentry = ttk.Entry(longmeanstestpage, textvariable=mtline19formatted, state="disabled")
meanstestcourtorderedpaymentslabel = ttk.Label(longmeanstestpage, text="Court Payments", state="disabled")
meanstestcourtorderedpaymentslabel.grid(column=0, row=20, pady=5, padx=10)
meanstestcourtorderedpaymentsentry.grid(column=0, row=21)

meanstesteducationentry = ttk.Entry(longmeanstestpage, textvariable=mtline20formatted, state="disabled")
meanstesteducationlabel = ttk.Label(longmeanstestpage, text="Education", state="disabled")
meanstesteducationlabel.grid(column=0, row=22, pady=5, padx=10)
meanstesteducationentry.grid(column=0, row=23)

meanstestchildcareentry = ttk.Entry(longmeanstestpage, textvariable=mtline21formatted, state="disabled")
meanstestchildcarelabel = ttk.Label(longmeanstestpage, text="Childcare", state="disabled")
meanstestchildcarelabel.grid(column=0, row=24, pady=5, padx=10)
meanstestchildcareentry.grid(column=0, row=25)

meanstestadditionalhealthcareexpensesentry = ttk.Entry(longmeanstestpage, textvariable=mtline22formatted, state="disabled")
meanstestadditionalhealthcareexpenseslabel = ttk.Label(longmeanstestpage, text="Add'l Healthcare Exp.", state="disabled")
meanstestadditionalhealthcareexpenseslabel.grid(column=0, row=26, pady=5, padx=10)
meanstestadditionalhealthcareexpensesentry.grid(column=0, row=27)

meanstestoptionalphoneserviceentry = ttk.Entry(longmeanstestpage, textvariable=mtline23formatted, state="disabled")
meanstestoptionalphoneservicelabel = ttk.Label(longmeanstestpage, text="Opt. Phone Serv.", state="disabled")
meanstestoptionalphoneservicelabel.grid(column=0, row=28, pady=5, padx=10)
meanstestoptionalphoneserviceentry.grid(column=0, row=29)

meanstesthealthinsuranceentry = ttk.Entry(longmeanstestpage, textvariable=mtline25formatted, state="disabled")
meanstesthealthinsurancelabel = ttk.Label(longmeanstestpage, text="Health, Disability, HSA", state="disabled")
meanstesthealthinsurancelabel.grid(column=1, row=0, pady=5, padx=10)
meanstesthealthinsuranceentry.grid(column=1, row=1)

meanstestcontinuingcontributionstocareentry = ttk.Entry(longmeanstestpage, textvariable=mtline26formatted, state="disabled")
meanstestcontinuingcontributionstocarelabel = ttk.Label(longmeanstestpage, text="Cont. Contrib. to Care", state="disabled")
meanstestcontinuingcontributionstocarelabel.grid(column=1, row=2, pady=5, padx=10)
meanstestcontinuingcontributionstocareentry.grid(column=1, row=3)

meanstestprotectionagainstfamilyvioilenceentry = ttk.Entry(longmeanstestpage, textvariable=mtline27formatted, state="disabled")
meanstestprotectionagainstfamilyviolencelabel = ttk.Label(longmeanstestpage, text="Protection Against FV", state="disabled")
meanstestprotectionagainstfamilyviolencelabel.grid(column=1, row=4, pady=5, padx=10)
meanstestprotectionagainstfamilyvioilenceentry.grid(column=1, row=5)

meanstestadditionalhomeenergyentry = ttk.Entry(longmeanstestpage, textvariable=mtline28formatted, state="disabled")
meanstestadditionalhomeenergylabel = ttk.Label(longmeanstestpage, text="Add'l Home Energy Costs", state="disabled")
meanstestadditionalhomeenergylabel.grid(column=1, row=6, pady=5, padx=10)
meanstestadditionalhomeenergyentry.grid(column=1, row=7)

meanstestdependenteducationalentry = ttk.Entry(longmeanstestpage, textvariable=mtline29formatted, state="disabled")
meanstestdependenteducationallabel = ttk.Label(longmeanstestpage, text="Dependent Ed. Exp.", state="disabled")
meanstestdependenteducationallabel.grid(column=1, row=8, pady=5, padx=10)
meanstestdependenteducationalentry.grid(column=1, row=9)

meanstestadditionalfoodandclothingentry = ttk.Entry(longmeanstestpage, textvariable=mtline30formatted, state="disabled")
meanstestadditionalfoodandclothinglabel = ttk.Label(longmeanstestpage, text="Add'l Food and Clothing", state="disabled")
meanstestadditionalfoodandclothinglabel.grid(column=1, row=10, pady=5, padx=10)
meanstestadditionalfoodandclothingentry.grid(column=1, row=11)

meanstestcharitablecontributionsentry = ttk.Entry(longmeanstestpage, textvariable=mtline31formatted, state="disabled")
meanstestcharitablecontributionslabel = ttk.Label(longmeanstestpage, text="Charitable Contrib.", state="disabled")
meanstestcharitablecontributionslabel.grid(column=1, row=12, pady=5, padx=10)
meanstestcharitablecontributionsentry.grid(column=1, row=13)

meanstestsecureddebtmortgagesentry = ttk.Entry(longmeanstestpage, textvariable=mtline33aformatted, state="disabled")
meanstestsecureddebtmortgageslabel = ttk.Label(longmeanstestpage, text="Sec. Debt: Mortgages", state="disabled")
meanstestsecureddebtmortgageslabel.grid(column=1, row=14, pady=5, padx=10)
meanstestsecureddebtmortgagesentry.grid(column=1, row=15)

meanstestsecureddebtcarsentry = ttk.Entry(longmeanstestpage, textvariable=mtline33bcformatted, state="disabled")
meanstestsecureddebtcarslabel = ttk.Label(longmeanstestpage, text="Sec. Debt: Cars", state="disabled")
meanstestsecureddebtcarslabel.grid(column=1, row=16, pady=5, padx=10)
meanstestsecureddebtcarsentry.grid(column=1, row=17)

meanstestothersecureddebtsentry = ttk.Entry(longmeanstestpage, textvariable=mtline33eformatted, state="disabled")
meanstestothersecureddebtslabel = ttk.Label(longmeanstestpage, text="Sec. Debt: Other", state="disabled")
meanstestothersecureddebtslabel.grid(column=1, row=18, pady=5, padx=10)
meanstestothersecureddebtsentry.grid(column=1, row=19)

meanstestsecuredarrearsentry = ttk.Entry(longmeanstestpage, textvariable=mtline34formatted, state="disabled")
meanstestsecuredarrearslabel = ttk.Label(longmeanstestpage, text="Sec. Debt Arrears", state="disabled")
meanstestsecuredarrearslabel.grid(column=1, row=20, pady=5, padx=10)
meanstestsecuredarrearsentry.grid(column=1, row=21)

meanstestpriorityclaimsentry = ttk.Entry(longmeanstestpage, textvariable=mtline35formatted, state="disabled")
meanstestpriorityclaimslabel = ttk.Label(longmeanstestpage, text="Priority Payments", state="disabled")
meanstestpriorityclaimslabel.grid(column=1, row=22, pady=5, padx=10)
meanstestpriorityclaimsentry.grid(column=1, row=23)

meanstestprojectedadminexpenseentry = ttk.Entry(longmeanstestpage, textvariable=mtline36bformatted, state="disabled")
meanstestprojectedadminexpenselabel = ttk.Label(longmeanstestpage, text="Proj. Admin. Expense", state="disabled")
meanstestprojectedadminexpenselabel.grid(column=1, row=24, pady=5, padx=10)
meanstestprojectedadminexpenseentry.grid(column=1, row=25)

meanstestchildsupportdeductionentry = ttk.Entry(longmeanstestpage, textvariable=childsupportreceivedformatted, state="disabled")
meanstestchildsupportdeductionlabel = ttk.Label(longmeanstestpage, text="CS Deduction", state="disabled")
meanstestchildsupportdeductionlabel.grid(column=1, row=26, pady=5, padx=10)
meanstestchildsupportdeductionentry.grid(column=1, row=27)

meanstestretirementdeductionentry = ttk.Entry(longmeanstestpage, textvariable=mtline41formatted, state="disabled")
meanstestretirementdeductionlabel = ttk.Label(longmeanstestpage, text="Ret. Deduction", state="disabled")
meanstestretirementdeductionlabel.grid(column=1, row=28, pady=5, padx=10)
meanstestretirementdeductionentry.grid(column=1, row=29)

longmeanstestbutton = ttk.Button(longmeanstestpage, text="Run Long Means Test", command=lambda: form122c2(), state="disabled")
longmeanstestbutton.grid(column=4, row=1, pady=5, padx=10)

cmirestatedentry = ttk.Entry(longmeanstestpage, textvariable=currentmonthlyincomeformatted, state="disabled")
cmirestatedlabel = ttk.Label(longmeanstestpage, text="CMI", state="disabled")
cmirestatedlabel.grid(column=5, row=0, pady=5, padx=10)
cmirestatedentry.grid(column=5, row=1)

minuslabel = ttk.Label(longmeanstestpage, text="-", state="disabled")
minuslabel.grid(column=6, row=1, pady=5, padx=10)

totalmeanstestdeductionsentry = ttk.Entry(longmeanstestpage, textvariable=meanstestdeductionsformatted, state="disabled")
totalmeanstestdeductionslabel = ttk.Label(longmeanstestpage, text="Total Deductions", state="disabled")
totalmeanstestdeductionslabel.grid(column=7, row=0, pady=5, padx=10)
totalmeanstestdeductionsentry.grid(column=7, row=1)

equallabel = ttk.Label(longmeanstestpage, text="=", state="disabled")
equallabel.grid(column=8, row=1, pady=5, padx=10)

monthlydisposableincomeentry = ttk.Entry(longmeanstestpage, textvariable=monthlydisposableincomeformatted, state="disabled")
monthlydisposableincomelabel = ttk.Label(longmeanstestpage, text="MDI", state="disabled")
monthlydisposableincomelabel.grid(column=9, row=0, pady=5, padx=10)
monthlydisposableincomeentry.grid(column=9, row=1)

planlongtermdebtscurrentdata = ttk.Label(plancalcpage, textvariable=planlongtermdebtpaymentformatted, state="disabled")
planlongtermdebtscurrentlabel = ttk.Label(plancalcpage, text="Long-Term Debts (3.1)", state="disabled")
planlongtermdebtscurrentlabel.grid(column=0, row=0, pady=5)
planlongtermdebtscurrentdata.grid(column=0, row=1)

planlongtermdebtsarrearsdata = ttk.Label(plancalcpage, textvariable=planlongtermdebtarrearspaymentformatted, state="disabled")
planlongtermdebtsarrearslabel = ttk.Label(plancalcpage, text="Long-Term Debt Arrears (3.2)", state="disabled")
planlongtermdebtsarrearslabel.grid(column=0, row=2, pady=5)
planlongtermdebtsarrearsdata.grid(column=0, row=3)

plansecurednocramdowndata0 = ttk.Label(plancalcpage, textvariable=plansecurednocramdowntotalformatted, state="disabled")
plansecurednocramdownlabel0 = ttk.Label(plancalcpage, text="Secured Claims, No CD (3.3)", state="disabled")
plansecurednocramdownlabel0.grid(column=0, row=4, pady=5, padx=5)
plansecurednocramdowndata0.grid(column=0, row=5)

plansecurednocramdowndata1 = ttk.Label(plancalcpage, textvariable=plansecurednocramdowncar1formatted, state="disabled")
plansecurednocramdownlabel1 = ttk.Label(plancalcpage, text="Car #1", state="disabled")
plansecurednocramdownlabel1.grid(column=1, row=4, pady=5, padx=5)
plansecurednocramdowndata1.grid(column=1, row=5)

plansecurednocramdowndata2 = ttk.Label(plancalcpage, textvariable=plansecurednocramdowncar2formatted, state="disabled")
plansecurednocramdownlabel2 = ttk.Label(plancalcpage, text="Car #2", state="disabled")
plansecurednocramdownlabel2.grid(column=2, row=4, pady=5, padx=5)
plansecurednocramdowndata2.grid(column=2, row=5)

plansecurednocramdowndata3 = ttk.Label(plancalcpage, textvariable=plansecurednocramdownclaim1formatted, state="disabled")
plansecurednocramdownlabel3 = ttk.Label(plancalcpage, text="Sec. Claim #1", state="disabled")
plansecurednocramdownlabel3.grid(column=3, row=4, pady=5, padx=5)
plansecurednocramdowndata3.grid(column=3, row=5)

plansecurednocramdowndata4 = ttk.Label(plancalcpage, textvariable=plansecurednocramdownclaim2formatted, state="disabled")
plansecurednocramdownlabel4 = ttk.Label(plancalcpage, text="Sec. Claim #2", state="disabled")
plansecurednocramdownlabel4.grid(column=4, row=4, pady=5, padx=5)
plansecurednocramdowndata4.grid(column=4, row=5)

plansecurednocramdowndata5 = ttk.Label(plancalcpage, textvariable=plansecurednocramdownclaim3formatted, state="disabled")
plansecurednocramdownlabel5 = ttk.Label(plancalcpage, text="Sec. Claim #3", state="disabled")
plansecurednocramdownlabel5.grid(column=5, row=4, pady=5, padx=5)
plansecurednocramdowndata5.grid(column=5, row=5)

plansecurednocramdowndata6 = ttk.Label(plancalcpage, textvariable=plansecurednocramdownclaim4formatted, state="disabled")
plansecurednocramdownlabel6 = ttk.Label(plancalcpage, text="Sec. Claim #4", state="disabled")
plansecurednocramdownlabel6.grid(column=6, row=4, pady=5, padx=5)
plansecurednocramdowndata6.grid(column=6, row=5)

plansecuredcramdowndata0 = ttk.Label(plancalcpage, textvariable=plansecuredcramdowntotalformatted, state="disabled")
plansecuredcramdownlabel0 = ttk.Label(plancalcpage, text="Sec. Claims Total, CD (3.5)", state="disabled")
plansecuredcramdownlabel0.grid(column=0, row=6, pady=5, padx=5)
plansecuredcramdowndata0.grid(column=0, row=7)

plansecuredcramdowndata1 = ttk.Label(plancalcpage, textvariable=plansecuredcramdowncar1formatted, state="disabled")
plansecuredcramdownlabel1 = ttk.Label(plancalcpage, text="Car #1", state="disabled")
plansecuredcramdownlabel1.grid(column=1, row=6, pady=5, padx=5)
plansecuredcramdowndata1.grid(column=1, row=7)

plansecuredcramdowndata2 = ttk.Label(plancalcpage, textvariable=plansecuredcramdowncar2formatted, state="disabled")
plansecuredcramdownlabel2 = ttk.Label(plancalcpage, text="Car #2", state="disabled")
plansecuredcramdownlabel2.grid(column=2, row=6, pady=5, padx=5)
plansecuredcramdowndata2.grid(column=2, row=7)

plansecuredcramdowndata3 = ttk.Label(plancalcpage, textvariable=plansecuredcramdownclaim1formatted, state="disabled")
plansecuredcramdownlabel3 = ttk.Label(plancalcpage, text="Sec. Claim #1", state="disabled")
plansecuredcramdownlabel3.grid(column=3, row=6, pady=5, padx=5)
plansecuredcramdowndata3.grid(column=3, row=7)

plansecuredcramdowndata4 = ttk.Label(plancalcpage, textvariable=plansecuredcramdownclaim2formatted, state="disabled")
plansecuredcramdownlabel4 = ttk.Label(plancalcpage, text="Sec. Claim #2", state="disabled")
plansecuredcramdownlabel4.grid(column=4, row=6, pady=5, padx=5)
plansecuredcramdowndata4.grid(column=4, row=7)

plansecuredcramdowndata5 = ttk.Label(plancalcpage, textvariable=plansecuredcramdownclaim3formatted, state="disabled")
plansecuredcramdownlabel5 = ttk.Label(plancalcpage, text="Sec. Claim #3", state="disabled")
plansecuredcramdownlabel5.grid(column=5, row=6, pady=5, padx=5)
plansecuredcramdowndata5.grid(column=5, row=7)

plansecuredcramdowndata6 = ttk.Label(plancalcpage, textvariable=plansecuredcramdownclaim4formatted, state="disabled")
plansecuredcramdownlabel6 = ttk.Label(plancalcpage, text="Sec. Claim #4", state="disabled")
plansecuredcramdownlabel6.grid(column=6, row=6, pady=5, padx=5)
plansecuredcramdowndata6.grid(column=6, row=7)

planattorneysfeesdata = ttk.Label(plancalcpage, textvariable=planattorneysfeesformatted, state="disabled")
planattorneysfeeslabel = ttk.Label(plancalcpage, text="Attorney's Fees (4.1)", state="disabled")
planattorneysfeeslabel.grid(column=0, row=8, pady=5)
planattorneysfeesdata.grid(column=0, row=9)

planpriorityclaimsdata = ttk.Label(plancalcpage, textvariable=planpriorityclaimsformatted, state="disabled")
planpriorityclaimslabel = ttk.Label(plancalcpage, text="Priority Claims (4.4)", state="disabled")
planpriorityclaimslabel.grid(column=0, row=10, pady=5)
planpriorityclaimsdata.grid(column=0, row=11)

plangeneralunsecuredclaimsdata = ttk.Label(plancalcpage, textvariable=plangeneralunsecuredclaimsformatted, state="disabled")
plangeneralunsecuredclaimslabel = ttk.Label(plancalcpage, text="Gen. Unsecured (5.2)", state="disabled")
plangeneralunsecuredclaimslabel.grid(column=0, row=12, pady=5)
plangeneralunsecuredclaimsdata.grid(column=0, row=13)

plangeneralunsecuredclaimsdividenddata = ttk.Label(plancalcpage, textvariable=plangeneralunsecuredclaimsdividendformatted, state="disabled")
plangeneralunsecuredclaimsdividendlabel = ttk.Label(plancalcpage, text="Total Div.", state="disabled")
plangeneralunsecuredclaimsdividendlabel.grid(column=1, row=12, pady=5)
plangeneralunsecuredclaimsdividenddata.grid(column=1, row=13)

plangeneralunsecuredclaimsbasisdata = ttk.Label(plancalcpage, textvariable=plangeneralunsecuredclaimsbasisformatted, state="disabled")
plangeneralunsecuredclaimsbasislabel = ttk.Label(plancalcpage, text="Basis", state="disabled")
plangeneralunsecuredclaimsbasislabel.grid(column=2, row=12, pady=5)
plangeneralunsecuredclaimsbasisdata.grid(column=2, row=13)

plangeneralunsecuredclaimspercentagedata = ttk.Label(plancalcpage, textvariable=plangeneralunsecuredclaimspercentageformatted, state="disabled")
plangeneralunsecuredclaimspercentagelabel = ttk.Label(plancalcpage, text="Percentage", state="disabled")
plangeneralunsecuredclaimspercentagelabel.grid(column=3, row=12, pady=5)
plangeneralunsecuredclaimspercentagedata.grid(column=3, row=13)

plantrusteefeesdata = ttk.Label(plancalcpage, textvariable=plantrusteefeesformatted, state="disabled")
plantrusteefeeslabel = ttk.Label(plancalcpage, text="Trustee Fees (4.1)", state="disabled")
plantrusteefeeslabel.grid(column=0, row=14, pady=5)
plantrusteefeesdata.grid(column=0, row=15)

blankline1 = ttk.Label(plancalcpage, text="", state="disabled")
blankline1.grid(column=0, row=16, pady=5)

plantotalmonthlycostdata = ttk.Label(plancalcpage, textvariable=plantotalmonthlycostformatted, state="disabled")
plantotalmonthlycostlabel = ttk.Label(plancalcpage, text="TOTAL", state="disabled")
plantotalmonthlycostlabel.grid(column=0, row=17, pady=5)
plantotalmonthlycostdata.grid(column=0, row=18)

plancostcalcbutton = ttk.Button(plancalcpage, text="Run Plan Cost Calc", command=lambda: plancostcalc(), state="disabled")
plancostcalcbutton.grid(column=0, row=19, pady=10, padx=10)

root.mainloop()