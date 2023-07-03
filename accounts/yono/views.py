from django.shortcuts import render,HttpResponse,redirect
from.models import bankModel

# Create your views here.
def display(request):
    return render(request,'display.html')


def bank(request):
    accno=''
    name=''
    bal=''
    result=""
    if request.GET:
        try:

            accno=request.GET['accountno']
            name=request.GET['name']
            bal=int(request.GET['balance'])
            if bal<500 :
                result="Account not Open"
            else:
                wa=bankModel()
                wa.accountno=accno
                wa.name=name
                wa.balance=bal
                wa.save()
                result=" Account Open Successfully "
                print('save')
        except:
            result="Account Already Exist "
    return render(request,'bank.html',{'an':accno,'n':name,'b':bal,'re':result})


def details(request):
    accountno=''
    name=''
    balance=''
    result=''
    if request.GET:
       try:
            accountno=request.GET['accountno']
            accounts = bankModel.objects.filter(accountno=accountno)
            if len(accounts)<=0:
                   result="Please Enter correct Account No"
            else:
                accounts=accounts[0]
                name=accounts.name
                balance=accounts.balance
                print(accounts)
       except:
           result="Please Enter an Account No."
           
    return render(request,'bankdtl.html',{'accountno':accountno,'balance':balance,'name':name,'result':result}) 


def deposite(request):
    accountno=''
    deposite=''
    result=''
    name=''
    balance=''

    if request.GET:
       try:
           accountno=request.GET['accountno']
           deposite=int(request.GET['deposite'])
           account=bankModel.objects.filter(accountno=accountno)
           print(account)
           if len(account)<=0:
                result="Failed"
           else:
                account=account[0]
                account.balance += deposite
                name=account.name
                balance=account.balance
                account.save()
                
                result='Amount Deposited'
       except:
               result= "Please Enter An Account No."          
       
    return render(request,'deposite.html',{'accountno':accountno,'deposite':deposite,'re':result,'name':name,'balance':balance}) 

       
    
    
def withdraw(request):
    accountno=''
    withdraw=''
    balance=''
    result=''
    name=''
    if request.GET:
        accountno=request.GET['accountno']
        withdraw=int(request.GET['withdraw'])
        account=bankModel.objects.filter(accountno=accountno)
        if len(account)<=0:
            result="Account not exist"
        else:
            account=account[0]
            account.balance -= withdraw
            account.save()
            balance=account.balance
            name=account.name
            result='Amount Dedacted'
    return render(request,'withdraw.html',{'accountno':accountno,'withdraw':withdraw,"re":result,'balance':balance,'name':name})    



    

    









