from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout
from .DB import DbConnection
from django.core.mail import send_mail

dbobj=DbConnection(host="localhost",user="root",passwd="",database="crowdfund",port=3306)

def investorsignup(request):
    return render(request,'investorsignup.html')

def investorsignupaction(request):
    username=request.POST['txtusername']
    password=request.POST['txtpassword']
    firstname=request.POST['txtfirstname']
    lastname=request.POST['txtlastname']
    address=request.POST['txtaddress']
    mobile=request.POST['txtmobile']
    email=request.POST['txtemail']
    country=request.POST['txtcountry']
    investortype=request.POST['txtinvestortype']
    role='investor'
    
    investor=Investor.objects.create(username=username,firstname=firstname,lastname=lastname,address=address,mobile=mobile,email=email,country=country,investortype=investortype)
    useraccount=UserAccount.objects.create(username=username,password=password,role=role)
    try:
        investor.save()
        useraccount.save()
        return redirect(login)
    except:
        errmsg='User Registration Failed'
        return render(request,'investorsignup.html',{'errmsg':errmsg})
    
def projectpublish(request):
    return render(request,'projectpublish.html')

def projectpublishaction(request):
    title=request.POST['txttitle']
    description=request.POST['txtdescription']
    hours=request.POST['txthours']
    amount=request.POST['txtamount']
    project=Project.objects.create(title=title,description=description,hours=hours,amount=amount) 
    project.save()

    return redirect(projectpublish)
    
def ownersignupaction(request):
    username=request.POST['txtusername']
    password=request.POST['txtpassword']
    firstname=request.POST['txtfirstname']
    lastname=request.POST['txtlastname']
    address=request.POST['txtaddress']
    mobile=request.POST['txtmobile']
    email=request.POST['txtemail']
    country=request.POST['txtcountry']
    businessprofile=request.POST['txtbusprofile']
    domain=request.POST['txtdomain']
    role='owner'
    owner=Owner.objects.create(username=username,firstname=firstname,lastname=lastname,address=address,mobile=mobile,email=email,country=country,companyprofile=businessprofile,domain=domain)
    useraccount=UserAccount.objects.create(username=username,password=password,role=role)
    try:
        owner.save()
        useraccount.save()
        return redirect(login)
    except:
        errmsg='User Registration Failed'
        return render(request,'investorsignup.html',{'errmsg':errmsg})
        
    
def ownersignup(request):
    return render(request,'ownersignup.html')
   
def home(request):
    role=request.session['role']
    if role=='admin':
        return render(request,'adminhome.html')
    elif role=='investor':
        return render(request,'investorhome.html')
    else:
        return render(request,'ownerhome.html')
    
def login(request):
    return render(request,'login.html')

def loginaction(request):
    username=request.POST["username"]
    password=request.POST["password"]
    record=UserAccount.objects.filter(username=username,password=password,status=1)
    if record.count()>0:
        record=UserAccount.objects.get(username=username,password=password)
        request.session['username'] = record.username
        request.session['role']=record.role
        if record.role=="admin":
            return render(request,'adminhome.html')
        elif record.role=='investor':
            return render(request,'investorhome.html')
        else:
            return render(request,'ownerhome.html')
        
    else:
        return render(request,'login.html',{'errmsg':'Invlid username or password, or your account is not activated'})

def editlogin(request,id):
    login = UserAccount.objects.get(userid=id)
    return render(request,'editlogin.html', {'login':login})

def updatelogin(request, id):
    login = UserAccount.objects.get(userid=id)
    form = UserAccount(request.POST, instance = login)
    if form.is_valid():
        form.save()
        return render(request,'editusers.html')
    else:
        login = UserAccount.objects.get(userid=id)
        return render(request,'editlogin.html', {'login':login})

def deletelogin(request, id):
    login = UserAccount.objects.get(userid=id)
    login.delete()
    logins=UserAccount.objects.all()
    return render(request,'adminhome.html',{'logins':logins})

def editprofile(request):
    username=request.session['username']
    login = UserAccount.objects.get(username=username)
    return render(request,'editprofile.html', {'login':login})

def updateprofile(request):
    username=request.session['username']
    firstname=request.POST['txtfirstname']
    lastname=request.POST['txtlastname']
    address=request.POST['txtaddress']
    panchayath=request.POST['txtpanchayath']
    phc=request.POST['txtphc']
    mobile=request.POST['txtmobile']
    sql="update useraccount set firstname=%s, lastname=%s, address=%s, panchayath=%s, phc=%s, mobile=%s where username=%s"
    val=(firstname,lastname,address,panchayath,phc,mobile,username,)
    try:
        dbobj.executenonquery(sql,val)
        return redirect(home)
    except:
        errmsg='Update Failed'
        username=request.session['username']
        login = UserAccount.objects.get(username=username)
        return render(request,'editprofile.html', {'login':login,'errmsg':errmsg})
        
def custom_logout(request):
    logout(request)
    return redirect('login')

def changepassword(request):
    return render(request,'changepassword.html')

def updatepassword(request):
    password=request.POST['password']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    username=request.session['username']
    sql="select password from useraccount where username=%s"
    val=(username,)
    p=getstring(sql,val)
    if p==password:
        if newpassword==confirmpassword:
            sql="update useraccount set password=%s where username=%s"
            val=(newpassword,username)
            if dbobj.executenonquery(sql,val):
                errmsg='Password changed successfully'
                return render(request,'changepassword.html',{'errmsg':errmsg})
            else:
                errmsg='Unable to change password at this time'
                return render(request,'changepassword.html',{'errmsg':errmsg})
        else:
            errmsg='New Password and Confirm Password must be the same'
            return render(request,'changepassword.html',{'errmsg':errmsg})
    else:
        errmsg='Invalid Current Password'
        return render(request,'changepassword.html',{'errmsg':errmsg})
    

def getstring(sql,val):
    d=dbobj.selectrecords(sql,val)
    print(sql)
    s=""
    for row in d:
        s=row[0]
    print("password:"+str(s))
    return s

def validateinvestor(request):
    investors=Investor.objects.filter(status=0)
    return render(request,'validateinvestor.html',{'investors':investors})

def viewprojects(request):
    viewprojects=Project.objects.filter(status=1)
    return render(request,'projectview.html',{'viewprojects':viewprojects})

def responseview(request):
    r=ProjectResponse.objects.filter(status=1)
    return render(request,'responseview.html',{'r':r})

def validateowner(request):
    owners=Owner.objects.filter(status=0)
    return render(request,'validateowner.html',{'owners':owners})

def approveinvestor(request,username):
    account=UserAccount.objects.get(username=username)
    account.status=1
    account.save()
    sql="update investor set status=1 where username=%s"
    val=(username,)
    if dbobj.executenonquery(sql,val):
        logins=Investor.objects.filter(status=0)
        return render(request,'validateinvestor.html',{'logins':logins})
    else:
        logins=Investor.objects.filter(status=0)
        return render(request,'validateinvestor.html',{'logins':logins})
    
def sendgmail(toemail,msg,subject):
    message = msg
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [toemail,]
    send_mail( subject, message, email_from, recipient_list, fail_silently=False )
   
def approveproject(request,projectid):
    project=Project.objects.get(projectid=projectid)
    project.status=2
    project.save()
    sendgmail("arj333un@gmail.com","ProjectApproved","CrowdFundingPlatform")
    return render(request,'responseview.html')

   
def rejectinvestor(request,username):
    account=UserAccount.objects.get(username=username)
    account.delete()
    
    sql="delete from investor where username=%s"
    val=(username,)
    if dbobj.executenonquery(sql,val):
        investors=UserAccount.objects.filter(status=0)
        return render(request,'validateinvestor.html',{'investors':investors})
    else:
        logins=UserAccount.objects.filter(status=0)
        return render(request,'validateinvestor.html',{'investors':investors})
    
def approveowner(request,username):
    account=UserAccount.objects.get(username=username)
    account.status=1
    account.save()
    sql="update owner set status=1 where username=%s"
    val=(username,)
    if dbobj.executenonquery(sql,val):
        owners=Owner.objects.filter(status=0)
        return render(request,'validateowner.html',{'owners':owners})
    else:
        owners=Investor.objects.filter(status=0)
        return render(request,'validateowner.html',{'owners':owners})

def rejectowner(request,username):
    account=UserAccount.objects.get(username=username)
    account.delete()
    
    sql="delete from owner where username=%s"
    val=(username,)
    if dbobj.executenonquery(sql,val):
        owners=UserAccount.objects.filter(status=0)
        return render(request,'validateowner.html',{'owners':owners})
    else:
        owners=UserAccount.objects.filter(status=0)
        return render(request,'validateowner.html',{'owners':owners})
    
def editusers(request):
    logins=UserAccount.objects.all()
    return render(request,'editusers.html',{'logins':logins})

def respond(request,id):
    project = Project.objects.get(projectid=id)
    return render(request,'respond.html',{'project':project})

def respondaction(request):
    projectid=request.POST['projectid']
    quotedamount=request.POST['quotedamount']
    quotedby=request.session['username']
    status=1
    print(projectid)
    resp=ProjectResponse.objects.create(projectid=projectid,quotedamount=quotedamount,quotedby=quotedby,status=status) 
    resp.save()
    #return render(request,'respond.html',{'project':project})
    return redirect(viewprojects)

def feedback(request):
    return render(request,'feedback.html')

def feedbackaction(request):
    describe=request.POST['describe']
    username=request.session['username']
    print(describe)
    resp=Feedback.objects.create(describe=describe,username=username) 
    resp.save()
    #return render(request,'respond.html',{'project':project})
    return redirect(feedback)

def viewfeedback(request):
    viewfeedback=Feedback.objects.all()
    return render(request,'viewfeedback.html',{'viewfeedback':viewfeedback})

def report(request):
    reports = Project.objects.filter(status=2)
    return render(request,'report.html',{'reports':reports})

def index(request):
    return render(request,'index.html')


# def editlogin(request,id):
#      login = UserAccount.objects.get(userid=id)
#      return render(request,'editlogin.html', {'login':login})