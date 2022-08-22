import datetime, os
from .models import *
from .forms import *
from .forms import SetPassword as SetPasswordForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa

def designation_check(user):
    return user.accountType == 'Administrator'

def phaseCheck(project):
    phase = ['Obtain PO', 'Confirm PO', 'Delivery', 'Payment']
    check = []
    for p in phase:
        fileIDs = AssignedTask.objects.filter(projectID=project).filter(taskID__phaseName=p).filter(taskID__has_file=True).values_list('id', flat=True)
        fileIDs = list(fileIDs)
        done = AssignedTask.objects.filter(projectID=project).filter(taskID__phaseName=p).filter(is_done=False).exclude(id__in=fileIDs).exists()
        uploaded = AssignedTask.objects.filter(id__in=fileIDs).filter(is_file_uploaded=False).exists()
        if done == False and uploaded == False:
            check.append(p)
    if not check or phase[0] not in check:
        project.projectPhase = phase[0]
        project.projectStatus = 'Ongoing'
        project.save()
    elif check and phase[1] not in check or phase[0] in check and len(check) == 1:
        project.projectPhase = phase[1]
        project.projectStatus = 'Ongoing'
        project.save()
    elif check and phase[2] not in check or phase[0] and phase[1] in check and len(check) == 2:
        project.projectPhase = phase[2]
        project.projectStatus = 'Ongoing'
        project.save()
    elif check and phase[3] not in check or phase[0] and phase[1] and phase[2] in check and len(check) == 3:
        project.projectPhase = phase[3]
        project.projectStatus = 'Ongoing'
        project.save()
    elif phase[0] and phase[1] and phase[2] and phase[3] in check and len(check) == 4:
        project.projectPhase = 'Done'
        project.projectStatus = 'Completed'
        project.save()

#USER
def signup(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account ' + user + ' has been successfully created.')
            messages.info(request, 'Please contact your Administrator to get an account designation.')
            return redirect('login')
    return render(request, 'signup.html', {'form':form})
def signin(request):
    if request.user.is_authenticated:
        messages.warning(request, 'This will log out the current user!')
        messages.info(request, 'Note: To view Admin pages you must use an account with Administrator designation.')
    if request.method == 'POST':
        next_url = request.POST.get('next')
        username = request.POST.get('InputEmail')
        password = request.POST.get('InputPassword')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active == True:
                if user.accountType == '':
                    messages.info(request, 'Please contact your Administrator to get an account designation.')
                else:
                    login(request, user)
                    if next_url != '':
                        return redirect(next_url)
                    else:
                        if user.accountType == 'Administrator':
                            return redirect('adminHome')
                        else:
                            return redirect('home')
            else:
                messages.info(request, 'Please refer to your Administrator for account activation.')
        else:
            messages.error(request, 'Username or password is incorrect!')
    return render(request, 'login.html')
@login_required(login_url='login')
def signout(request):
    logout(request)
    messages.success(request, 'Your account has been logged out.')
    return redirect('login')

#HOME
@login_required(login_url='login')
def home(request):
    ongoingProjects = Project.objects.filter(projectStatus='Ongoing')
    overDeadlines = Project.objects.filter(projectStatus='Ongoing',projectDeadline__lt=now())
    nearDeadlines = Project.objects.filter(projectStatus='Ongoing',projectDeadline__range=[now(),now() + datetime.timedelta(days = 7)])
    context = {
        'page':'home',
        'overDeadlines' : overDeadlines,
        'nearDeadlines' : nearDeadlines,
        'ongoingProjects':ongoingProjects
    }
    return render(request, 'home.html', context)
@login_required(login_url='login')
def userProfile(request):
    return render(request, 'userProfile.html', {'page':'userProfile'})
@login_required(login_url='login')
def userEditProfile(request):
    user = CustomUser.objects.get(username=request.user)
    departments = Department.objects.filter(is_inactive=0)
    context = {
        'page':'userEditProfile',
        'user':user,
        'departments':departments
    }
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.department = Department.objects.get(pk=request.POST.get('departmentEdit'))
        user.contactNumber = request.POST.get('contactNumber')
        user.email = request.POST.get('email')
        user.save()
        return redirect('userProfile')
    return render(request, 'userEditProfile.html', context)
@login_required(login_url='login')
def userPassword(request):
    form = SetPasswordForm(user=request.user)
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully.')
            return HttpResponseRedirect('/userPassword/')
    context = {
        'page':'userPassword',
        'form':form
    }
    return render(request, 'userPassword.html', context)

#CLIENTS
@login_required(login_url='login')
def clients(request):
    client = Client.objects.all()
    context = {
        'page':'clients',
        'client':client
    }
    if request.method == 'POST':
        arrow = request.POST.get('arrow')
        request.session['profile'] = arrow
        return redirect('clientProfile')
    return render(request, 'clients.html', context)
@login_required(login_url='login')
def newClient(request):
    businessStyles = BusinessStyle.objects.filter(is_inactive=0)
    context = {
        'page':'newClient',
        'businessStyles':businessStyles
    }
    if request.method == 'POST':
        companyName = request.POST.get('companyName')
        companyAddress = request.POST.get('companyAddress')
        region = request.POST.get('region')
        province = request.POST.get('province')
        city = request.POST.get('city')
        barangay = request.POST.get('barangay')
        postalCode = request.POST.get('postalCode')
        companyTIN = request.POST.get('companyTIN')
        contactPerson = request.POST.get('contactPerson')
        contactNumber = request.POST.get('contactNumber')
        contactPosition = request.POST.get('contactPosition')
        businessStyle = BusinessStyle.objects.get(pk=request.POST.get('businessStyle'))
        create = Client(postalCode=postalCode,barangay=barangay,city=city,province=province,region=region,companyName=companyName,companyAddress=companyAddress,companyTIN=companyTIN,contactPerson=contactPerson,contactNumber=contactNumber,contactPosition=contactPosition,businessStyle=businessStyle)
        create.save()
        return redirect('clients')
    return render(request, 'newClient.html', context)
@login_required(login_url='login')
def clientProfile(request):
    profile = request.session['profile']
    client = Client.objects.get(companyTIN=profile)
    context = {
        'page':'clientProfile',
        'client':client
    }
    if request.method == 'POST':
        Client.objects.filter(pk=client.id).update(is_inactive=True, date_of_inactivity=now())
        return redirect('clients')
    return render(request, 'clientProfile.html', context)
@login_required(login_url='login')
def editClient(request):
    profile = request.session['profile']
    client = Client.objects.get(companyTIN=profile)
    businessStyles = BusinessStyle.objects.filter(is_inactive=0)
    context = {
        'page':'editClient',
        'client':client,
        'businessStyles':businessStyles
    }
    if request.method == 'POST':
        client.companyName = request.POST.get('companyName')
        client.companyAddress = request.POST.get('companyAddress')
        client.region = request.POST.get('region')
        client.province = request.POST.get('province')
        client.city = request.POST.get('city')
        client.barangay = request.POST.get('barangay')
        client.postalCode = request.POST.get('postalCode')
        client.companyTIN = request.POST.get('companyTIN')
        client.contactPerson = request.POST.get('contactPerson')
        client.contactNumber = request.POST.get('contactNumber')
        client.contactPosition = request.POST.get('contactPosition')
        client.businessStyle = BusinessStyle.objects.get(pk=request.POST.get('businessStyle'))
        client.save()
        request.session['profile'] = client.companyTIN
        return redirect('clientProfile')
    return render(request, 'editClient.html', context)

#PROJECTS
@login_required(login_url='login')
def projects(request):
    project = Project.objects.all()
    obtainPO = Project.objects.filter(projectPhase='Obtain PO')
    confirmPO = Project.objects.filter(projectPhase='Confirm PO')
    delivery = Project.objects.filter(projectPhase='Delivery')
    payment = Project.objects.filter(projectPhase='Payment')
    context = {
        'page':'projects',
        'project':project,
        'obtainPOCount':obtainPO.count(),
        'confirmPOCount':confirmPO.count(),
        'deliveryCount':delivery.count(),
        'paymentCount':payment.count()
    }
    if request.method == 'POST':
        arrow = request.POST.get('arrow')
        request.session['projectID'] = arrow
        return redirect('projectObtain')
    return render(request, 'projects.html', context)
@login_required(login_url='login')
def newProject(request):
    clientProject = Client.objects.filter(is_inactive=0)
    tasks = Task.objects.filter(is_inactive=0).order_by('phaseName', 'id')
    projectTypes = ProjectType.objects.filter(is_inactive=0)
    context = {
        'page':'newProject',
        'clientProject':clientProject,
        'projectTypes':projectTypes,
        'tasks':tasks
    }
    if request.method == 'POST':
        projName = request.POST.get('projName')
        clientProject = Client.objects.get(pk=request.POST.get('ClientNewProj'))
        poDeadline = request.POST.get('poDeadline')
        deliveryTerms = request.POST.get('deliveryTerms')
        paymentTerms = request.POST.get('paymentTerms')
        projectType = request.POST.get('projectType')
        projCreate = Project(projectName=projName,clients=clientProject,poDeadline=poDeadline,deliveryTerms=deliveryTerms,paymentTerms=paymentTerms,projectType=projectType)
        projCreate.save()
        for taskID in request.POST.get('tasksArr').split(','):
            task = Task.objects.get(pk=taskID)
            proj = Project.objects.get(pk=projCreate.pk)
            assignedTask = AssignedTask(taskID=task,projectID=proj)
            assignedTask.save()
        return redirect('projects')
    return render(request, 'newProject.html', context)
@login_required(login_url='login')
def projectObtain(request):
    countTaskTotal = 0
    countTaskDone = 0
    allChecked = False
    projID = request.session['projectID']
    project = Project.objects.get(pk=projID)
    phaseCheck(project)
    tasks = AssignedTask.objects.filter(projectID=project)
    tasksIDs = AssignedTask.objects.filter(projectID=project).values_list('taskID_id', flat=True)
    tasksIDs = list(tasksIDs)
    alltask = Task.objects.filter(is_inactive=0).order_by('phaseName', 'id').exclude(id__in=tasksIDs)
    delivery = project.poDeadline + datetime.timedelta(days = int(project.deliveryTerms))
    payment = project.poDeadline + datetime.timedelta(days = int(project.deliveryTerms)) + datetime.timedelta(days = int(project.paymentTerms))
    project.projectDeadline = payment
    project.save()
    for task in tasks:
        if task.taskID.phaseName == 'Obtain PO':
            countTaskTotal += 1
            if task.is_done == True and task.taskID.has_file == False:
                countTaskDone += 1
            if task.is_file_uploaded == True and task.taskID.has_file == True:
                countTaskDone += 1
    if countTaskTotal == countTaskDone:
        allChecked = True
    context = {
        'page':'projectOverview',
        'project':project,
        'alltask':alltask, 
        'tasks':tasks,
        'allChecked':allChecked,
        'countTaskTotal':countTaskTotal,
        'countTaskDone':countTaskDone,
        'delivery':delivery,
        'payment':payment
    }
    if request.method == 'POST' and 'setDoneTasks' in request.POST:
        if request.POST.get('doneTasks'):
            for taskID in request.POST.get('doneTasks').split(','):
                assignedTask = AssignedTask.objects.get(id=taskID)
                assignedTask.is_done = True
                assignedTask.save()
        if request.POST.get('undoneTasks'):
            for taskID in request.POST.get('undoneTasks').split(','):
                assignedTask = AssignedTask.objects.get(id=taskID)
                assignedTask.is_done = False
                assignedTask.save()
        if request.POST.get('doneTasksFile'):
            x=0
            for taskID in request.POST.get('doneTasksFile').split(','):
                x=x+1
                y=0
                for f in request.FILES.getlist('files'):
                    y=y+1
                    if x == y:
                        assignedTask = AssignedTask.objects.get(id=taskID)
                        assignedTask.is_file_uploaded = True
                        assignedTask.taskFile = f
                        assignedTask.save()
        if request.POST.get('undoneTasksFile'):
            for taskID in request.POST.get('undoneTasksFile').split(','):
                assignedTask = AssignedTask.objects.get(id=taskID)
                assignedTask.is_file_uploaded = False
                assignedTask.taskFile = ""
                assignedTask.save()
        return redirect('projectObtain')
    elif request.method == 'POST' and 'addAssignedTask' in request.POST:
        projID = request.POST.get('projID')
        for taskID in request.POST.get('tasksArr').split(','):
            task = Task.objects.get(pk=taskID)
            proj = Project.objects.get(pk=projID)
            assignedTask = AssignedTask(taskID=task,projectID=proj)
            assignedTask.save()
        return redirect('projectObtain')
    elif request.method == 'POST' and 'assignedTaskDelete' in request.POST:
        instance = AssignedTask.objects.get(pk=request.POST.get('taskID'))
        instance.delete()
        return redirect('projectObtain')
    return render(request, 'projectObtain.html', context)
@login_required(login_url='login')
def projectConfirm(request):
    countTaskTotal = 0
    countTaskDone = 0
    allChecked = False
    projID = request.session['projectID']
    project = Project.objects.get(pk=projID)
    phaseCheck(project)
    tasks = AssignedTask.objects.filter(projectID=project)
    tasksIDs = AssignedTask.objects.filter(projectID=project).values_list('taskID_id', flat=True)
    tasksIDs = list(tasksIDs)
    alltask = Task.objects.filter(is_inactive=0).order_by('phaseName', 'id').exclude(id__in=tasksIDs)
    delivery = project.poDeadline + datetime.timedelta(days = int(project.deliveryTerms))
    payment = project.poDeadline + datetime.timedelta(days = int(project.deliveryTerms)) + datetime.timedelta(days = int(project.paymentTerms))
    for task in tasks:
        if task.taskID.phaseName == 'Confirm PO':
            countTaskTotal += 1
            if task.is_done == True and task.taskID.has_file == False:
                countTaskDone += 1
            if task.is_file_uploaded == True and task.taskID.has_file == True:
                countTaskDone += 1
    if countTaskTotal == countTaskDone:
        allChecked = True
    context = {
        'page':'projectOverview',
        'project':project,
        'tasks':tasks,
        'alltask':alltask,
        'allChecked':allChecked,
        'countTaskTotal':countTaskTotal,
        'countTaskDone':countTaskDone,
        'delivery':delivery,
        'payment':payment
    }
    if request.method == 'POST' and 'setDoneTasks' in request.POST:
        if request.POST.get('doneTasks'):
            for taskID in request.POST.get('doneTasks').split(','):
                assignedTask = AssignedTask.objects.get(id=taskID)
                assignedTask.is_done = True
                assignedTask.save()
        if request.POST.get('undoneTasks'):
            for taskID in request.POST.get('undoneTasks').split(','):
                assignedTask = AssignedTask.objects.get(id=taskID)
                assignedTask.is_done = False
                assignedTask.save()
        if request.POST.get('doneTasksFile'):
            x=0
            for taskID in request.POST.get('doneTasksFile').split(','):
                x=x+1
                y=0
                for f in request.FILES.getlist('files'):
                    y=y+1
                    if x == y:
                        assignedTask = AssignedTask.objects.get(id=taskID)
                        assignedTask.is_file_uploaded = True
                        assignedTask.taskFile = f
                        assignedTask.save()
        if request.POST.get('undoneTasksFile'):
            for taskID in request.POST.get('undoneTasksFile').split(','):
                assignedTask = AssignedTask.objects.get(id=taskID)
                assignedTask.is_file_uploaded = False
                assignedTask.taskFile = ""
                assignedTask.save()
        return redirect('projectConfirm')
    elif request.method == 'POST' and 'addAssignedTask' in request.POST:
        for taskID in request.POST.get('tasksArr').split(','):
            task = Task.objects.get(pk=taskID)
            proj = Project.objects.get(pk=projID)
            assignedTask = AssignedTask(taskID=task,projectID=proj)
            assignedTask.save()
        return redirect('projectConfirm')
    elif request.method == 'POST' and 'assignedTaskDelete' in request.POST:
        instance = AssignedTask.objects.get(pk=request.POST.get('taskID'))
        instance.delete()
        return redirect('projectConfirm')
    return render(request, 'projectConfirm.html', context)
@login_required(login_url='login')
def projectDelivery(request):
    countTaskTotal = 0
    countTaskDone = 0
    allChecked = False
    projID = request.session['projectID']
    project = Project.objects.get(pk=projID)
    phaseCheck(project)
    tasks = AssignedTask.objects.filter(projectID=project)
    tasksIDs = AssignedTask.objects.filter(projectID=project).values_list('taskID_id', flat=True)
    tasksIDs = list(tasksIDs)
    alltask = Task.objects.filter(is_inactive=0).order_by('phaseName', 'id').exclude(id__in=tasksIDs)
    delivery = project.poDeadline + datetime.timedelta(days = int(project.deliveryTerms))
    payment = project.poDeadline + datetime.timedelta(days = int(project.deliveryTerms)) + datetime.timedelta(days = int(project.paymentTerms))
    for task in tasks:
        if task.taskID.phaseName == 'Delivery':
            countTaskTotal += 1
            if task.is_done == True and task.taskID.has_file == False:
                countTaskDone += 1
            if task.is_file_uploaded == True and task.taskID.has_file == True:
                countTaskDone += 1
    if countTaskTotal == countTaskDone:
        allChecked = True
    context = {
        'page':'projectOverview',
        'project':project,
        'tasks':tasks,
        'alltask':alltask,
        'allChecked':allChecked,
        'countTaskTotal':countTaskTotal,
        'countTaskDone':countTaskDone,
        'delivery':delivery,
        'payment':payment
    }
    if request.method == 'POST' and 'setDoneTasks' in request.POST:
        if request.POST.get('doneTasks'):
            for taskID in request.POST.get('doneTasks').split(','):
                assignedTask = AssignedTask.objects.get(id=taskID)
                assignedTask.is_done = True
                assignedTask.save()
        if request.POST.get('undoneTasks'):
            for taskID in request.POST.get('undoneTasks').split(','):
                assignedTask = AssignedTask.objects.get(id=taskID)
                assignedTask.is_done = False
                assignedTask.save()
        if request.POST.get('doneTasksFile'):
            x=0
            for taskID in request.POST.get('doneTasksFile').split(','):
                x=x+1
                y=0
                for f in request.FILES.getlist('files'):
                    y=y+1
                    if x == y:
                        assignedTask = AssignedTask.objects.get(id=taskID)
                        assignedTask.is_file_uploaded = True
                        assignedTask.taskFile = f
                        assignedTask.save()
        if request.POST.get('undoneTasksFile'):
            for taskID in request.POST.get('undoneTasksFile').split(','):
                assignedTask = AssignedTask.objects.get(id=taskID)
                assignedTask.is_file_uploaded = False
                assignedTask.taskFile = ""
                assignedTask.save()
        return redirect('projectDelivery')
    elif request.method == 'POST' and 'addAssignedTask' in request.POST:
        for taskID in request.POST.get('tasksArr').split(','):
            task = Task.objects.get(pk=taskID)
            proj = Project.objects.get(pk=projID)
            assignedTask = AssignedTask(taskID=task,projectID=proj)
            assignedTask.save()
        return redirect('projectDelivery')
    elif request.method == 'POST' and 'assignedTaskDelete' in request.POST:
        instance = AssignedTask.objects.get(pk=request.POST.get('taskID'))
        instance.delete()
        return redirect('projectDelivery')
    return render(request, 'projectDelivery.html', context)
@login_required(login_url='login')
def projectPayment(request):
    countTaskTotal = 0
    countTaskDone = 0
    allChecked = False
    projID = request.session['projectID']
    project = Project.objects.get(pk=projID)
    phaseCheck(project)
    tasks = AssignedTask.objects.filter(projectID=project)
    tasksIDs = AssignedTask.objects.filter(projectID=project).values_list('taskID_id', flat=True)
    tasksIDs = list(tasksIDs)
    alltask = Task.objects.filter(is_inactive=0).order_by('phaseName', 'id').exclude(id__in=tasksIDs)
    delivery = project.poDeadline + datetime.timedelta(days = int(project.deliveryTerms))
    payment = project.poDeadline + datetime.timedelta(days = int(project.deliveryTerms)) + datetime.timedelta(days = int(project.paymentTerms))
    for task in tasks:
        if task.taskID.phaseName == 'Payment':
            countTaskTotal += 1
            if task.is_done == True and task.taskID.has_file == False:
                countTaskDone += 1
            if task.is_file_uploaded == True and task.taskID.has_file == True:
                countTaskDone += 1
    if countTaskTotal == countTaskDone:
        allChecked = True
    context = {
        'page':'projectOverview',
        'project':project,
        'tasks':tasks,
        'alltask':alltask,
        'allChecked':allChecked,
        'countTaskTotal':countTaskTotal,
        'countTaskDone':countTaskDone,
        'delivery':delivery,
        'payment':payment
    }
    if request.method == 'POST' and 'setDoneTasks' in request.POST:
        if request.POST.get('doneTasks'):
            for taskID in request.POST.get('doneTasks').split(','):
                assignedTask = AssignedTask.objects.get(id=taskID)
                assignedTask.is_done = True
                assignedTask.save()
        if request.POST.get('undoneTasks'):
            for taskID in request.POST.get('undoneTasks').split(','):
                assignedTask = AssignedTask.objects.get(id=taskID)
                assignedTask.is_done = False
                assignedTask.save()
        if request.POST.get('doneTasksFile'):
            x=0
            for taskID in request.POST.get('doneTasksFile').split(','):
                x=x+1
                y=0
                for f in request.FILES.getlist('files'):
                    y=y+1
                    if x == y:
                        assignedTask = AssignedTask.objects.get(id=taskID)
                        assignedTask.is_file_uploaded = True
                        assignedTask.taskFile = f
                        assignedTask.save()
        if request.POST.get('undoneTasksFile'):
            for taskID in request.POST.get('undoneTasksFile').split(','):
                assignedTask = AssignedTask.objects.get(id=taskID)
                assignedTask.is_file_uploaded = False
                assignedTask.taskFile = ""
                assignedTask.save()
        return redirect('projectPayment')
    elif request.method == 'POST' and 'addAssignedTask' in request.POST:
        for taskID in request.POST.get('tasksArr').split(','):
            task = Task.objects.get(pk=taskID)
            proj = Project.objects.get(pk=projID)
            assignedTask = AssignedTask(taskID=task,projectID=proj)
            assignedTask.save()
        return redirect('projectPayment')
    elif request.method == 'POST' and 'assignedTaskDelete' in request.POST:
        instance = AssignedTask.objects.get(pk=request.POST.get('taskID'))
        instance.delete()
        return redirect('projectPayment')
    return render(request, 'projectPayment.html', context)

#FORMS
@login_required(login_url='login')
def forms(request):
    formalLetter = FormalLetter.objects.all()
    deliveryReceipt = DeliveryReceipt.objects.all()
    billingInv = BillingInvForm.objects.all()
    salesInv = SalesInvForm.objects.all()
    quotationForm = QuotationForm.objects.all()
    context = {
        'page':'forms',
        'formalLetter':formalLetter,
        'deliveryReceipt':deliveryReceipt,
        'billingInv':billingInv,
        'salesInv':salesInv,
        'quotationForm':quotationForm,
    }
    if request.method == 'POST' and 'formalLetter' in request.POST:
        arrow = request.POST.get('formalLetter')
        request.session['formalLetterFormVerifier'] = arrow
        return redirect('formalLetterFormVerifier')
    elif request.method == 'POST' and 'deliveryReceipt' in request.POST:
        arrow1 = request.POST.get('deliveryReceipt')
        request.session['deliveryReceiptFormVerifier'] = arrow1
        return redirect('deliveryReceiptFormVerifier')
    elif request.method == 'POST' and 'quotationForm' in request.POST:
        arrow2 = request.POST.get('quotationForm')
        request.session['quotationFormVerifier'] = arrow2
        return redirect('quotationFormVerifier')
    elif request.method == 'POST' and 'salesInvForm' in request.POST:
        arrow3 = request.POST.get('salesInvForm')
        request.session['salesInvoiceFormVerifier'] = arrow3
        return redirect('salesInvoiceFormVerifier')
    elif request.method == 'POST' and 'billingInv' in request.POST:
        arrow4 = request.POST.get('billingInv')
        request.session['billingInvoiceFormVerifier'] = arrow4
        return redirect('billingInvoiceFormVerifier')
    return render(request, 'forms.html', context)
@login_required(login_url='login')
def quotationForm(request):
    items = Item.objects.filter(is_inactive=0)
    unit = Unit.objects.filter(is_inactive=0)
    if 'itemQuotationList' in request.session:
        itemList = Item.objects.filter(pk__in=request.session.pop('itemQuotationList'))
    else:
        itemList = []
    context = {
        'page':'quotationForm',
        'items': items,
        'unit': unit,
        'itemList': itemList
    }
    if request.method == 'POST':
        if request.method == 'POST' and 'submit' in request.POST:
            quotationSubj = request.POST.get('quotationSubj')
            dateIssued = request.POST.get('dateIssued')
            companyName = request.POST.get('companyName')
            companyAddress = request.POST.get('companyAddress')
            receiverName = request.POST.get('receiverName')
            position = request.POST.get('position')
            contactNo = request.POST.get('contactNo')
            deliveryTerms = request.POST.get('deliveryTerms')
            paymentTerms = request.POST.get('paymentTerms')
            validityTerms = request.POST.get('validityTerms')   
            warrantyTerms = request.POST.get('warrantyTerms')
            grandTotal = request.POST.get('grandTotal')
            submit = QuotationForm(quotationSubj=quotationSubj,dateIssued=dateIssued,companyName=companyName,companyAddress=companyAddress,receiverName=receiverName,position=position,contactNum=contactNo,deliveryTerms=deliveryTerms,paymentTerms=paymentTerms,validityTerms=validityTerms,warrantyTerms=warrantyTerms,grandTotal=grandTotal)
            submit.save()
            temp = request.POST.getlist('itemName')
            for i, itemName in enumerate(temp):
                item = Item.objects.get(itemName=itemName)
                quantity = request.POST.getlist('qty')
                qty = quantity[i]
                unitID = request.POST.getlist('unit')
                unit = Unit.objects.get(pk=unitID[i])
                amount = request.POST.getlist('amount')
                amt = amount[i]
                quotation = QuotationForm.objects.get(pk=submit.pk)
                assignedItem = AssignedItem(itemID=item,unit=unit,itemQuantity=qty,amount=amt,quotationFormID=quotation)
                assignedItem.save()
        elif request.method == 'POST' and 'addItem' in request.POST:
                request.session['itemQuotationList'] = request.POST.getlist('item')
        return redirect('quotationForm')
    return render(request, 'quotationForm.html', context)
@login_required(login_url='login')
def quotationFormVerifier(request):
    quotationForm = QuotationForm.objects.get(pk=request.session['quotationFormVerifier'])
    assignedItem = AssignedItem.objects.filter(quotationFormID=quotationForm)
    assignedIDs = assignedItem.values_list('itemID__itemID', flat=True)
    assignedIDs = list(assignedIDs)
    unit = Unit.objects.filter(is_inactive=0)
    items = Item.objects.filter(is_inactive=0)
    if 'itemQuotationVerifierList' in request.session:
        itemList = Item.objects.filter(pk__in=request.session.pop('itemQuotationVerifierList')).exclude(itemID__in=assignedIDs)
    else:
        itemList = []
    context = {
        'page':'quotationFormVerifier',
        'quotationForm':quotationForm,
        'status':formStatus,
        'assignedItem':assignedItem,
        'unit': unit,
        'items': items,
        'itemList': itemList
    }
    if request.method == 'POST':
        if request.method == 'POST' and 'submit' in request.POST:
            quotationForm.quotationStatus = request.POST.get('quotationStatus')
            quotationForm.quotationSubj = request.POST.get('quotationSubj')
            quotationForm.dateIssued = request.POST.get('dateIssued')
            quotationForm.companyName = request.POST.get('companyName')
            quotationForm.companyAddress = request.POST.get('companyAddress')
            quotationForm.receiverName = request.POST.get('receiverName')
            quotationForm.position = request.POST.get('position')
            quotationForm.contactNum = request.POST.get('contactNum')
            quotationForm.deliveryTerms = request.POST.get('deliveryTerms')
            quotationForm.paymentTerms = request.POST.get('paymentTerms')
            quotationForm.validityTerms = request.POST.get('validityTerms')   
            quotationForm.warrantyTerms = request.POST.get('warrantyTerms')
            quotationForm.grandTotal = request.POST.get('grandTotal')
            quotationForm.save()
            AssignedItem.objects.filter(quotationFormID=quotationForm).delete()
            temp = request.POST.getlist('itemName')
            for i, itemName in enumerate(temp):
                item = Item.objects.get(itemName=itemName)
                quantity = request.POST.getlist('qty')
                qty = quantity[i]
                unitID = request.POST.getlist('unitEdit')
                unit = Unit.objects.get(pk=unitID[i])
                amount = request.POST.getlist('amount')
                amt = amount[i]
                quotForm = QuotationForm.objects.get(pk=quotationForm.pk)
                assignedItem = AssignedItem(itemID=item,unit=unit,itemQuantity=qty,amount=amt,quotationFormID=quotForm)
                assignedItem.save()
        elif request.method == 'POST' and 'addItem' in request.POST:
            request.session['itemQuotationVerifierList'] = request.POST.getlist('item')
        return redirect('quotationFormVerifier')
    return render(request, 'quotationFormVerifier.html', context)
@login_required(login_url='login')
def quotationFormPDF(request):
    quotationForm = QuotationForm.objects.get(pk=request.session['quotationFormVerifier'])
    assignedItem = AssignedItem.objects.filter(quotationFormID=quotationForm)
    context = {
        'quotationForm':quotationForm,
        'assignedItem':assignedItem
    }
    template_path = 'formTemplates/quotation_form.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="QuotationForm_%s.pdf"' %(quotationForm.quotationFormNumber)
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
@login_required(login_url='login')
def salesInvoiceForm(request):
    clientProject = Client.objects.filter(is_inactive=0)
    items = Item.objects.filter(is_inactive=0)
    unit = Unit.objects.filter(is_inactive=0)
    if 'itemSalesList' in request.session:
        itemList = Item.objects.filter(pk__in=request.session.pop('itemSalesList'))
    else:
        itemList = []
    context = {
        'page':'salesInvoiceForm',
        'clientProject':clientProject,
        'items': items,
        'unit': unit,
        'itemList': itemList
    }
    if request.method == 'POST':
        if request.method == 'POST' and 'submit' in request.POST:
            clients = Client.objects.get(pk=request.POST.get('ClientNewProj'))
            dateIssued = request.POST.get('dateIssued')
            terms = request.POST.get('terms')
            mop = request.POST.get('mop')
            grandTotal = request.POST.get('grandTotal')
            submit = SalesInvForm(clients=clients,dateIssued=dateIssued,terms=terms,mop=mop,grandTotal=grandTotal)
            submit.save()
            temp = request.POST.getlist('itemName')
            for i, itemName in enumerate(temp):
                item = Item.objects.get(itemName=itemName)
                quantity = request.POST.getlist('qty')
                qty = quantity[i]
                unitID = request.POST.getlist('unit')
                unit = Unit.objects.get(pk=unitID[i])
                amount = request.POST.getlist('amount')
                amt = amount[i]
                salesForm = SalesInvForm.objects.get(pk=submit.pk)
                assignedItem = AssignedItem(itemID=item,unit=unit,itemQuantity=qty,amount=amt,salesInvFormID=salesForm)
                assignedItem.save()
        elif request.method == 'POST' and 'addItem' in request.POST:
                request.session['itemSalesList'] = request.POST.getlist('item')
        return redirect('salesInvoiceForm')
    return render(request, 'salesInvoiceForm.html', context)
@login_required(login_url='login')
def salesInvoiceFormVerifier(request):
    clientProject = Client.objects.filter(is_inactive=0)
    salesInvForm = SalesInvForm.objects.get(pk=request.session['salesInvoiceFormVerifier'])
    assignedItem = AssignedItem.objects.filter(salesInvFormID=salesInvForm)
    assignedIDs = assignedItem.values_list('itemID__itemID', flat=True)
    assignedIDs = list(assignedIDs)
    unit = Unit.objects.filter(is_inactive=0)
    items = Item.objects.filter(is_inactive=0)
    if 'itemSalesVerifierList' in request.session:
        itemList = Item.objects.filter(pk__in=request.session.pop('itemSalesVerifierList')).exclude(itemID__in=assignedIDs)
    else:
        itemList = []
    context = {
        'page':'salesInvoiceFormVerifier',
        'salesInvForm':salesInvForm,
        'status':formStatus,
        'clientProject': clientProject,
        'assignedItem':assignedItem,
        'unit': unit,
        'items': items,
        'itemList': itemList
    }
    if request.method == 'POST':
        if request.method == 'POST' and 'submit' in request.POST:
            salesInvForm.salesInvStatus = request.POST.get('salesInvStatus')
            salesInvForm.dateIssued = request.POST.get('dateIssued')
            salesInvForm.clients = Client.objects.get(pk=request.POST.get('ClientNewProj'))
            salesInvForm.terms = request.POST.get('terms')
            salesInvForm.grandTotal = request.POST.get('grandTotal')
            salesInvForm.save()
            AssignedItem.objects.filter(salesInvFormID=salesInvForm).delete()
            temp = request.POST.getlist('itemName')
            for i, itemName in enumerate(temp):
                item = Item.objects.get(itemName=itemName)
                quantity = request.POST.getlist('qty')
                qty = quantity[i]
                unitID = request.POST.getlist('unitEdit')
                unit = Unit.objects.get(pk=unitID[i])
                amount = request.POST.getlist('amount')
                amt = amount[i]
                salesForm = SalesInvForm.objects.get(pk=salesInvForm.pk)
                assignedItem = AssignedItem(itemID=item,unit=unit,itemQuantity=qty,amount=amt,salesInvFormID=salesForm)
                assignedItem.save()
        elif request.method == 'POST' and 'addItem' in request.POST:
            request.session['itemSalesVerifierList'] = request.POST.getlist('item')
        return redirect('salesInvoiceFormVerifier')
    return render(request, 'salesInvoiceFormVerifier.html', context)
@login_required(login_url='login')
def salesInvFormPDF(request):
    salesInvForm = SalesInvForm.objects.get(pk=request.session['salesInvoiceFormVerifier'])
    assignedItem = AssignedItem.objects.filter(salesInvFormID=salesInvForm)
    context = {
        'salesInvForm':salesInvForm,
        'assignedItem':assignedItem
    }
    template_path = 'formTemplates/sales_invoice.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="SalesInvoice_%s.pdf"' %(salesInvForm.salesInvNumber)
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
@login_required(login_url='login')
def deliveryReceiptForm(request):
    clientProject = Client.objects.filter(is_inactive=0)
    items = Item.objects.filter(is_inactive=0)
    unit = Unit.objects.filter(is_inactive=0)
    if 'itemDeliveryList' in request.session:
        itemList = Item.objects.filter(pk__in=request.session.pop('itemDeliveryList'))
    else:
        itemList = []
    context = {
        'page':'deliveryReceiptForm',
        'clientProject':clientProject,
        'items': items,
        'itemList': itemList,
        'unit': unit
    }
    if request.method == 'POST':
        if request.method == 'POST' and 'submit' in request.POST:
            clients = Client.objects.get(pk=request.POST.get('ClientNewProj'))
            dateIssued = request.POST.get('dateIssued')
            terms = request.POST.get('terms')
            submit = DeliveryReceipt(clients=clients,dateIssued=dateIssued,terms=terms)
            submit.save()
            temp = request.POST.getlist('itemName')
            for i, itemName in enumerate(temp):
                item = Item.objects.get(itemName=itemName)
                quantity = request.POST.getlist('qty')
                qty = quantity[i]
                unitID = request.POST.getlist('unit')
                unit = Unit.objects.get(pk=unitID[i])
                amount = request.POST.getlist('amount')
                amt = amount[i]
                deliveryForm = DeliveryReceipt.objects.get(pk=submit.pk)
                assignedItem = AssignedItem(itemID=item,unit=unit,itemQuantity=qty,amount=amt,deliveryReceiptID=deliveryForm)
                assignedItem.save()
        elif request.method == 'POST' and 'addItem' in request.POST:
                request.session['itemDeliveryList'] = request.POST.getlist('item')
        return redirect('deliveryReceiptForm')
    return render(request, 'deliveryReceiptForm.html', context)
@login_required(login_url='login')
def deliveryReceiptFormVerifier(request):
    clientProject = Client.objects.filter(is_inactive=0)
    deliveryReceipt = DeliveryReceipt.objects.get(pk=request.session['deliveryReceiptFormVerifier'])
    assignedItem = AssignedItem.objects.filter(deliveryReceiptID=deliveryReceipt)
    assignedIDs = assignedItem.values_list('itemID__itemID', flat=True)
    assignedIDs = list(assignedIDs)
    unit = Unit.objects.filter(is_inactive=0)
    items = Item.objects.filter(is_inactive=0)
    if 'itemDeliveryVerifierList' in request.session:
        itemList = Item.objects.filter(pk__in=request.session.pop('itemDeliveryVerifierList')).exclude(itemID__in=assignedIDs)
    else:
        itemList = []
    context = {
        'page':'deliveryReceiptFormVerifier',
        'status':formStatus,
        'clientProject': clientProject,
        'deliveryReceipt': deliveryReceipt,
        'assignedItem':assignedItem,
        'unit': unit,
        'items': items,
        'itemList': itemList
    }
    if request.method == 'POST':
        if request.method == 'POST' and 'submit' in request.POST:
            deliveryReceipt.deliveryRecStatus = request.POST.get('deliveryRecStatus')
            deliveryReceipt.dateIssued = request.POST.get('dateIssued')
            deliveryReceipt.clients = Client.objects.get(pk=request.POST.get('ClientNewProj'))
            deliveryReceipt.terms = request.POST.get('terms')
            deliveryReceipt.save()
            AssignedItem.objects.filter(deliveryReceiptID=deliveryReceipt).delete()
            temp = request.POST.getlist('itemName')
            for i, itemName in enumerate(temp):
                item = Item.objects.get(itemName=itemName)
                quantity = request.POST.getlist('qty')
                qty = quantity[i]
                unitID = request.POST.getlist('unitEdit')
                unit = Unit.objects.get(pk=unitID[i])
                amount = request.POST.getlist('amount')
                amt = amount[i]
                deliveryForm = DeliveryReceipt.objects.get(pk=deliveryReceipt.pk)
                assignedItem = AssignedItem(itemID=item,unit=unit,itemQuantity=qty,amount=amt,deliveryReceiptID=deliveryForm)
                assignedItem.save()
        elif request.method == 'POST' and 'addItem' in request.POST:
            request.session['itemDeliveryVerifierList'] = request.POST.getlist('item')
        return redirect('deliveryReceiptFormVerifier')
    return render(request, 'deliveryReceiptFormVerifier.html', context)
@login_required(login_url='login')
def deliveryReceiptFormPDF(request):
    deliveryReceipt = DeliveryReceipt.objects.get(pk=request.session['deliveryReceiptFormVerifier'])
    assignedItem = AssignedItem.objects.filter(deliveryReceiptID=deliveryReceipt)
    context = {
        'deliveryReceipt':deliveryReceipt,
        'assignedItem':assignedItem
    }
    template_path = 'formTemplates/delivery_receipt.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="DeliveryReceipt_%s.pdf"' %(deliveryReceipt.deliveryRecNumber)
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
@login_required(login_url='login')
def billingInvoiceForm(request):
    clientProject = Client.objects.filter(is_inactive=0)
    items = Item.objects.filter(is_inactive=0)
    unit = Unit.objects.all()
    if 'itemBillingList' in request.session:
        itemList = Item.objects.filter(pk__in=request.session.pop('itemBillingList'))
    else:
        itemList = []
    context = {
        'page':'billingInvoiceForm',
        'clientProject':clientProject,
        'items': items,
        'unit':unit,
        'itemList': itemList
    }
    if request.method == 'POST':
        if request.method == 'POST' and 'submit' in request.POST:
            clients = Client.objects.get(pk=request.POST.get('ClientNewProj'))
            dateIssued = request.POST.get('dateIssued')
            terms = request.POST.get('terms')
            jopoNum = request.POST.get('jopoNum')
            grandTotal = request.POST.get('grandTotal')
            submit = BillingInvForm(clients=clients,dateIssued=dateIssued,terms=terms,jopoNum=jopoNum,grandTotal=grandTotal)
            submit.save()
            temp = request.POST.getlist('itemName')
            for i, itemName in enumerate(temp):
                item = Item.objects.get(itemName=itemName)
                quantity = request.POST.getlist('qty')
                qty = quantity[i]
                unitID = request.POST.getlist('unit')
                unit = Unit.objects.get(pk=unitID[i])
                amount = request.POST.getlist('amount')
                amt = amount[i]
                billing = BillingInvForm.objects.get(pk=submit.pk)
                assignedItem = AssignedItem(itemID=item,unit=unit,itemQuantity=qty,amount=amt,billingInvID=billing)
                assignedItem.save()
        elif request.method == 'POST' and 'addItem' in request.POST:
            request.session['itemBillingList'] = request.POST.getlist('item')
        return redirect('billingInvoiceForm')
    return render(request, 'billingInvoiceForm.html', context)
@login_required(login_url='login')
def billingInvoiceFormVerifier(request):
    clientProject = Client.objects.filter(is_inactive=0)
    billingInvoice = BillingInvForm.objects.get(pk=request.session['billingInvoiceFormVerifier'])
    assignedItem = AssignedItem.objects.filter(billingInvID=billingInvoice)
    assignedIDs = assignedItem.values_list('itemID__itemID', flat=True)
    assignedIDs = list(assignedIDs)
    unit = Unit.objects.filter(is_inactive=0)
    items = Item.objects.filter(is_inactive=0)
    if 'itemBillingVerifierList' in request.session:
        itemList = Item.objects.filter(pk__in=request.session.pop('itemBillingVerifierList')).exclude(itemID__in=assignedIDs)
    else:
        itemList = []
    context = {
        'page':'billingInvoiceFormVerifier',
        'status':formStatus,
        'clientProject': clientProject,
        'billingInvoice': billingInvoice,
        'assignedItem':assignedItem,
        'unit': unit,
        'items': items,
        'itemList': itemList
    }
    if request.method == 'POST':
        if request.method == 'POST' and 'submit' in request.POST:
            billingInvoice.billingInvStatus = request.POST.get('billingInvStatus')
            billingInvoice.dateIssued = request.POST.get('dateIssued')
            billingInvoice.clients = Client.objects.get(pk=request.POST.get('ClientNewProj'))
            billingInvoice.terms = request.POST.get('terms')
            billingInvoice.jopoNum = request.POST.get('jopoNum')
            billingInvoice.grandTotal = request.POST.get('grandTotal')
            billingInvoice.save()
            AssignedItem.objects.filter(billingInvID=billingInvoice).delete()
            temp = request.POST.getlist('itemName')
            for i, itemName in enumerate(temp):
                item = Item.objects.get(itemName=itemName)
                quantity = request.POST.getlist('qty')
                qty = quantity[i]
                unitID = request.POST.getlist('unitEdit')
                unit = Unit.objects.get(pk=unitID[i])
                amount = request.POST.getlist('amount')
                amt = amount[i]
                billingForm = BillingInvForm.objects.get(pk=billingInvoice.pk)
                assignedItem = AssignedItem(itemID=item,unit=unit,itemQuantity=qty,amount=amt,billingInvID=billingForm)
                assignedItem.save()
        elif request.method == 'POST' and 'addItem' in request.POST:
            request.session['itemBillingVerifierList'] = request.POST.getlist('item')
        return redirect('billingInvoiceFormVerifier')
    return render(request, 'billingInvoiceFormVerifier.html', context)
@login_required(login_url='login')
def billingInvoiceFormPDF(request):
    billingInvoice = BillingInvForm.objects.get(pk=request.session['billingInvoiceFormVerifier'])
    assignedItem = AssignedItem.objects.filter(billingInvID=billingInvoice)
    context = {
        'billingInvoice':billingInvoice,
        'assignedItem':assignedItem
    }
    template_path = 'formTemplates/billing_invoice.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="BillingInvoice_%s.pdf"' %(billingInvoice.billingInvNumber)
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
@login_required(login_url='login')
def formalLetterForm(request):
    context = {
        'page':'formalLetterForm'
    }
    if request.method == 'POST':
        formalSubj = request.POST.get('formalSubj')
        dateIssued = request.POST.get('dateIssued')
        companyName = request.POST.get('companyName')
        companyAddress = request.POST.get('companyAddress')
        receiverName = request.POST.get('receiverName')
        position = request.POST.get('position')
        body = request.POST.get('body')
        submit = FormalLetter(formalSubj=formalSubj,dateIssued=dateIssued,companyName=companyName,companyAddress=companyAddress,receiverName=receiverName,position=position,body=body)
        submit.save()
        return redirect('forms')
    return render(request, 'formalLetterForm.html', context)
@login_required(login_url='login')
def formalLetterFormVerifier(request):
    formalLetter = FormalLetter.objects.get(pk=request.session['formalLetterFormVerifier'])
    context = {
        'page':'formalLetterFormVerifier',
        'formalLetter':formalLetter,
        'status':formStatus
    }
    if request.method == 'POST':
        formalLetter.formalStatus = request.POST.get('formalStatus')
        formalLetter.formalSubj = request.POST.get('formalSubj')
        formalLetter.dateIssued = request.POST.get('dateIssued')
        formalLetter.companyName = request.POST.get('companyName')
        formalLetter.companyAddress = request.POST.get('companyAddress')
        formalLetter.receiverName = request.POST.get('receiverName')
        formalLetter.position = request.POST.get('position')
        formalLetter.body = request.POST.get('body')
        formalLetter.save()
        del request.session['formalLetterFormVerifier']
        return redirect('forms')
    return render(request, 'formalLetterFormVerifier.html', context)
@login_required(login_url='login')
def formalLetterFormPDF(request):
    formalLetter = FormalLetter.objects.get(pk=request.session['formalLetterFormVerifier'])
    context = {
        'formalLetter':formalLetter
    }
    template_path = 'formTemplates/formal_letter.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="FormalLetter_%s.pdf"' %(formalLetter.formalLetterNumber)
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#DOCUMENTS
@login_required(login_url='login')
def documents(request):
    clients = Client.objects.filter(is_inactive=0)
    files = FileModel.objects.all()
    filesClient = AssignedTask.objects.filter(is_file_uploaded=True)
    categories = Category.objects.filter(is_inactive=0)
    contents = Content.objects.filter(is_inactive=0)
    tags = Tag.objects.filter(is_inactive=0)
    context = {
        'page':'documents',
        'files':files,
        'filesClient':filesClient,
        'categories':categories,
        'contents':contents,
        'clients':clients,
        'tags':tags
    }
    if request.method == 'POST' and 'upload' in request.POST:
        name = ''
        for f in request.FILES.getlist('filePath'):
            name = f.name
        request.POST._mutable = True
        request.POST['fileName'] = name
        form = documentsForm(request.POST, request.FILES)
        client = Client.objects.filter(pk=request.POST.get('clientID')).first()
        if form.is_valid():
            form.instance.clientID = client
            document = form.save(commit=False)
            fileTag = form.cleaned_data['fileTag']
            document.save()
            document.fileTag.set(fileTag)
        else:
            print(form.errors)
            form = documentsForm()
    elif request.method=='POST' and 'fileDelete' in request.POST:
        instance = FileModel.objects.get(pk = request.POST.get('fileID'))
        os.remove(os.path.join(settings.MEDIA_ROOT, str(instance.filePath)))
        instance.delete()
    return render(request, 'documents.html', context)
@login_required(login_url='login')
def documentsClients(request):
    try:
        activeClients = Client.objects.filter(is_inactive=0)
    except activeClients.DoesNotExist:
        activeClients = None
    context = {
        'page':'documentsClients',
        'activeClients':activeClients
    }
    return render(request, 'documentsClients.html', context)
@login_required(login_url='login')
def documentsFolder(request):
    project = Project.objects.filter(pk=request.GET['projid'])
    try:
        projectFiles = AssignedTask.objects.filter(projectID=project[0],is_file_uploaded=True)
    except projectFiles.DoesNotExist:
        projectFiles = None
    context = {
        'page':'documentsFolder',
        'projectFiles':projectFiles,
        'project':project
    }
    return render(request, 'documentsFolder.html', context)
@login_required(login_url='login')
def documentsProjects(request):
    client = request.session['clientDoc']
    client = Client.objects.get(pk=client)
    try:
        clientProjects = Project.objects.filter(is_inactive=0,clients=client)
    except clientProjects.DoesNotExist:
        clientProjects = None
    context = {
        'page':'documentsProjects',
        'clientProjects':clientProjects,
        'client':client
    }
    return render(request, 'documentsProjects.html', context )
@login_required(login_url='login')
def documentsCompanyReqs(request):
    if request.method=='POST' and 'fileDelete' in request.POST:
        instance = FileModel.objects.get(pk = request.POST.get('fileID'))
        instance.delete()
    if request.GET and request.method=='GET':
        request.session['clientDoc'] = request.GET['client']
        client = Client.objects.filter(pk=request.GET['client']).first()
        files = FileModel.objects.filter(clientID=client,fileCategory=1)
    elif request.session['clientDoc']:
        client = Client.objects.filter(pk=request.session['clientDoc']).first()
        files = FileModel.objects.filter(clientID=client,fileCategory=1)
    context = {
        'page':'documentsCompanyReqs',
        'files':files,
        'client':client
    }
    return render(request, 'documentsCompanyReqs.html', context)
@login_required(login_url='login')
def documentsOthers(request):
    if request.method=='POST' and 'fileDelete' in request.POST:
        instance = FileModel.objects.get(pk = request.POST.get('fileID'))
        instance.delete()
    if request.session['clientDoc']:
        client = Client.objects.filter(pk=request.session['clientDoc']).first()
        files = FileModel.objects.filter(clientID=client).exclude(fileCategory=1)
    context = {
        'page':'documentsOthers',
        'files':files,
        'client':client
    }
    return render(request, 'documentsOthers.html', context)

#REPORTS
@login_required(login_url='login')
def reports(request):
    project = Project.objects.all()
    client = Client.objects.all()
    projectType = ProjectType.objects.all()
    if request.method=='POST' and 'phase' in request.POST:
        project = Project.objects.filter(projectPhase=request.POST.get('phase'))
        request.session['phaseReport'] = request.POST.get('phase')
    elif request.method=='POST' and 'type' in request.POST:
        project = Project.objects.filter(projectType=request.POST.get('type'))
        request.session['typeReport'] = request.POST.get('type')
    elif request.method=='POST' and 'companyName' in request.POST:
        project = Project.objects.filter(clients__companyName=request.POST.get('companyName'))
        request.session['companyNameReport'] = request.POST.get('companyName')
    context = {
        'page':'reports',
        'project':project,
        'phase':Task.phase,
        'projectType':projectType,
        'client':client,
    }
    return render(request, 'reports.html', context)
@login_required(login_url='login')
def reportsPDF(request):
    if 'phaseReport' in request.session:
        project = Project.objects.filter(projectPhase=request.session.pop('phaseReport'))
    elif 'typeReport' in request.session:
        project = Project.objects.filter(projectType=request.session.pop('typeReport'))
    elif 'companyNameReport' in request.session:
        project = Project.objects.filter(clients__companyName=request.session.pop('companyNameReport'))
    else:
        project = Project.objects.all()
    template_path = 'formTemplates/reports_projects.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    context = {
        'project':project
    }
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
@login_required(login_url='login')
def reportsClients(request):
    client = Client.objects.all()
    businessType = BusinessStyle.objects.all()
    if request.method=='POST' and 'type' in request.POST:
        client = Client.objects.filter(businessStyle__businessStyleName=request.POST.get('type'))
        request.session['businessTypeReport'] = request.POST.get('type')
    elif request.method=='POST' and 'status' in request.POST:
        client = Client.objects.filter(is_inactive=request.POST.get('status'))
        request.session['statusReport'] = request.POST.get('status')
    context = {
        'page':'reportsClients',
        'client':client,
        'businessType':businessType
    }
    return render(request, 'reportsClients.html', context)
@login_required(login_url='login')
def reportsClientsPDF(request):
    if 'businessTypeReport' in request.session:
        client = Client.objects.filter(businessStyle__businessStyleName=request.session.pop('businessTypeReport'))
    elif 'statusReport' in request.session:
        client = Client.objects.filter(is_inactive=request.session.pop('statusReport'))
    else:
        client = Client.objects.all()
    context = {
        'client':client
    }
    template_path = 'formTemplates/reports_clients.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
@login_required(login_url='login')
def reportsProducts(request):
    item = Item.objects.all()
    context = {
        'page':'reportsProducts',
        'item': item
    }
    return render(request, 'reportsProducts.html', context)
@login_required(login_url='login')
def reportsProductsPDF(request):
    item = Item.objects.all()
    context = {
        'item':item
    }
    template_path = 'formTemplates/reports_products.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
@login_required(login_url='login')
def reportsServices(request):
    return render(request, 'reportsServices.html', {'page':'reportsServices'})
@login_required(login_url='login')
def reportsBillingInvoice(request):
    return render(request, 'reportsBillingInvoice.html', {'page':'reportsBillingInvoice'})
@login_required(login_url='login')
def reportsSalesInvoice(request):
    return render(request, 'reportsSalesInvoice.html', {'page':'reportsSalesInvoice'})
@login_required(login_url='login')
def reportsDeliveryReceipt(request):
    return render(request, 'reportsDeliveryReceipt.html', {'page':'reportsDeliveryReceipt'})

#ADMIN
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminActiveClients(request):
    try:
        activeClients = Client.objects.filter(is_inactive=0)
    except activeClients.DoesNotExist:
        activeClients = None
    context = {
        'page':'adminActiveClients',
        'activeClients':activeClients
    }
    if request.method=='POST':
        instance = Client.objects.get(pk = request.POST.get('id'))
        instance.is_inactive = True
        instance.date_of_inactivity = now()
        instance.save()
    return render(request, 'adminActiveClients.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminActiveProjects(request):
    try:
        activeProjects = Project.objects.filter(is_inactive=0)
    except activeProjects.DoesNotExist:
        activeProjects = None
    context = {
        'page':'adminActiveProjects',
        'activeProjects':activeProjects
    }
    if request.method=='POST':
        instance = Project.objects.get(pk = request.POST.get('id'))
        instance.is_inactive = True
        instance.date_of_inactivity = now()
        instance.save()
    return render(request, 'adminActiveProjects.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminActiveUsers(request):
    request.session['back'] = 'adminActiveUsers'
    try:
        activeUsers = CustomUser.objects.filter(is_active=1)
    except activeUsers.DoesNotExist:
        activeUsers = None
    context = {
        'page':'adminActiveUsers',
        'activeUsers':activeUsers
    }
    if request.method == 'POST':
        if 'pen' in request.POST:
            edit = request.POST.get('pen')
            request.session['user'] = edit
            return redirect('adminEditUser')
        else:
            instance = CustomUser.objects.get(pk = request.POST.get('id'))
            instance.is_active = False
            instance.date_of_inactivity = now()
            instance.save()
    return render(request, 'adminActiveUsers.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminBusinessStyle(request):
    dataList = BusinessStyle.objects.all()
    context = {
        'page':'adminBusinessStyle',
        'dataList':dataList
    }
    if request.method == 'POST' and 'businessStyleAdd' in request.POST:
        form = businessStyleForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            form = businessStyleForm()
    elif request.method=='POST' and 'businessStyleEdit' in request.POST:
        instance = BusinessStyle.objects.get(pk = request.POST.get('businessStyleID'))
        instance.businessStyleName = request.POST.get('businessStyleName')
        instance.save()
    elif request.method=='POST' and 'businessStyleInactive' in request.POST:
        instance = BusinessStyle.objects.get(pk = request.POST.get('businessStyleID'))
        instance.is_inactive = True
        instance.save()
    elif request.method=='POST' and 'businessStyleActive' in request.POST:
        instance = BusinessStyle.objects.get(pk = request.POST.get('businessStyleID'))
        instance.is_inactive = False
        instance.save()
    return render(request, 'adminBusinessStyle.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminCategory(request):
    dataList = Category.objects.all()
    context = {
        'page':'adminCategory',
        'dataList':dataList
    }
    if request.method == 'POST' and 'categoryAdd' in request.POST:
        form = categoryForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            form = categoryForm()
    elif request.method=='POST' and 'categoryEdit' in request.POST:
        instance = Category.objects.get(pk = request.POST.get('categoryID'))
        instance.categoryName = request.POST.get('categoryName')
        instance.save()
    elif request.method=='POST' and 'categoryInactive' in request.POST:
        instance = Category.objects.get(pk = request.POST.get('categoryID'))
        instance.is_inactive = True
        instance.save()
    elif request.method=='POST' and 'categoryActive' in request.POST:
        instance = Category.objects.get(pk = request.POST.get('categoryID'))
        instance.is_inactive = False
        instance.save()
    return render(request, 'adminCategory.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminContent(request):
    dataList = Content.objects.all()
    context = {
        'page':'adminContent',
        'dataList':dataList
    }
    if request.method == 'POST' and 'contentAdd' in request.POST:
        form = contentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            form = contentForm()
    elif request.method=='POST' and 'contentEdit' in request.POST:
        instance = Content.objects.get(pk = request.POST.get('contentID'))
        instance.contentName = request.POST.get('contentName')
        instance.save()
    elif request.method=='POST' and 'contentInactive' in request.POST:
        instance = Content.objects.get(pk = request.POST.get('contentID'))
        instance.is_inactive = True
        instance.save()
    elif request.method=='POST' and 'contentActive' in request.POST:
        instance = Content.objects.get(pk = request.POST.get('contentID'))
        instance.is_inactive = False
        instance.save()
    return render(request, 'adminContent.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminDepartment(request):
    dataList = Department.objects.all()
    context = {
        'page':'adminDepartment',
        'dataList':dataList
    }
    if request.method == 'POST' and 'departmentAdd' in request.POST:
        form = departmentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            form = departmentForm()
    elif request.method=='POST' and 'departmentEdit' in request.POST:
        instance = Department.objects.get(pk = request.POST.get('departmentID'))
        instance.departmentName = request.POST.get('departmentName')
        instance.save()
    elif request.method=='POST' and 'departmentInactive' in request.POST:
        instance = Department.objects.get(pk = request.POST.get('departmentID'))
        instance.is_inactive = True
        instance.save()
    elif request.method=='POST' and 'departmentActive' in request.POST:
        instance = Department.objects.get(pk = request.POST.get('departmentID'))
        instance.is_inactive = False
        instance.save()
    return render(request, 'adminDepartment.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminEditProfile(request):
    user = CustomUser.objects.get(username=request.user)
    departments = Department.objects.filter(is_inactive=0)
    context = {
        'page':'adminEditProfile',
        'user':user,
        'type':CustomUser.type,
        'departments':departments
    }
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.department = Department.objects.get(pk=request.POST.get('departmentEdit'))
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.contactNumber = request.POST.get('contactNumber')
        user.email = request.POST.get('email')
        user.save()
        return redirect(request.session['back'])
    return render(request, 'adminEditProfile.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminEditUser(request):
    user = CustomUser.objects.get(pk=request.session['user'])
    departments = Department.objects.filter(is_inactive=0)
    context = {
        'page':'adminEditUser',
        'user':user,
        'type':CustomUser.type,
        'departments':departments
    }
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.accountType = request.POST.get('accountTypeEdit')
        user.department = Department.objects.get(pk=request.POST.get('departmentEdit'))
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.contactNumber = request.POST.get('contactNumber')
        user.email = request.POST.get('email')
        user.save()
        return redirect(request.session['back'])
    return render(request, 'adminEditUser.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminHome(request):
    activeUsers = CustomUser.objects.filter(is_active=1)
    activeClients = Client.objects.filter(is_inactive=0)
    unverifiedUsers = CustomUser.objects.filter(is_active=1,accountType__exact='')
    context = {
        'page':'adminHome',
        'activeClients':activeClients,
        'unverifiedUsers':unverifiedUsers,
        'activeUsers':activeUsers
    }
    return render(request, 'adminHome.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminInactiveClients(request):
    try:
        inactiveClients = Client.objects.filter(is_inactive=1)
    except inactiveClients.DoesNotExist:
        inactiveClients = None
    context = {
        'page':'adminInactiveClients',
        'inactiveClients':inactiveClients
    }
    if request.method=='POST':
        instance = Client.objects.get(pk = request.POST.get('id'))
        instance.is_inactive = False
        instance.date_of_inactivity = None
        instance.save()
    return render(request, 'adminInactiveClients.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminInactiveProjects(request):
    try:
        inactiveProjects = Project.objects.filter(is_inactive=1)
    except inactiveProjects.DoesNotExist:
        inactiveProjects = None
    context = {
        'page':'adminInactiveProjects',
        'inactiveProjects':inactiveProjects
    }
    if request.method=='POST':
        instance = Project.objects.get(pk = request.POST.get('id'))
        instance.is_inactive = False
        instance.date_of_inactivity = None
        instance.save()
    return render(request, 'adminInactiveProjects.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminInactiveUsers(request):
    request.session['back'] = 'adminInactiveUsers'
    try:
        inactiveUsers = CustomUser.objects.filter(is_active=0)
    except inactiveUsers.DoesNotExist:
        inactiveUsers = None
    context = {
        'page':'adminInactiveUsers',
        'inactiveUsers':inactiveUsers
    }
    if request.method == 'POST':
        if 'pen' in request.POST:
            edit = request.POST.get('pen')
            request.session['user'] = edit
            return redirect('adminEditUser')
        else:
            instance = CustomUser.objects.get(pk = request.POST.get('id'))
            instance.is_active = True
            instance.date_of_inactivity = None
            instance.save()
    return render(request, 'adminInactiveUsers.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminItem(request):
    dataList = Item.objects.all()
    context = {
        'page':'adminItem',
        'dataList':dataList,
        'type':Item.type
    }
    if request.method == 'POST' and 'itemAdd' in request.POST:
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            form = itemForm()
    elif request.method=='POST' and 'itemEdit' in request.POST:
        instance = Item.objects.get(pk = request.POST.get('itemID'))
        instance.itemName = request.POST.get('itemName')
        instance.itemPrice = request.POST.get('itemPrice')
        instance.itemType = request.POST.get('itemType')
        instance.save()
    elif request.method=='POST' and 'itemInactive' in request.POST:
        instance = Item.objects.get(pk = request.POST.get('itemID'))
        instance.is_inactive = True
        instance.save()
    elif request.method=='POST' and 'itemActive' in request.POST:
        instance = Item.objects.get(pk = request.POST.get('itemID'))
        instance.is_inactive = False
        instance.save()
    return render(request, 'adminItem.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminPassword(request):
    form = SetPasswordForm(user=request.user)
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully.')
            return HttpResponseRedirect('/adminPassword/')
    context = {
        'page':'adminPassword',
        'form':form
    }
    return render(request, 'adminPassword.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminProfile(request):
    request.session['back'] = 'adminProfile'
    return render(request, 'adminProfile.html', {'page':'adminProfile'})
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminProjectType(request):
    dataList = ProjectType.objects.all()
    context = {
        'page':'adminProjectType',
        'dataList':dataList
    }
    if request.method == 'POST' and 'projectTypeAdd' in request.POST:
        form = projectTypeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            form = projectTypeForm()
    elif request.method=='POST' and 'projectTypeEdit' in request.POST:
        instance = ProjectType.objects.get(pk = request.POST.get('projectTypeID'))
        instance.projectTypeName = request.POST.get('projectTypeName')
        instance.save()
    elif request.method=='POST' and 'projectTypeInactive' in request.POST:
        instance = ProjectType.objects.get(pk = request.POST.get('projectTypeID'))
        instance.is_inactive = True
        instance.save()
    elif request.method=='POST' and 'projectTypeActive' in request.POST:
        instance = ProjectType.objects.get(pk = request.POST.get('projectTypeID'))
        instance.is_inactive = False
        instance.save()
    return render(request, 'adminProjectType.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminTag(request):
    dataList = Tag.objects.all()
    context = {
        'page':'adminTag',
        'dataList':dataList
    }
    if request.method == 'POST' and 'tagAdd' in request.POST:
        form = tagForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            form = tagForm()
    elif request.method=='POST' and 'tagEdit' in request.POST:
        instance = Tag.objects.get(pk = request.POST.get('tagID'))
        instance.tagName = request.POST.get('tagName')
        instance.save()
    elif request.method=='POST' and 'tagInactive' in request.POST:
        instance = Tag.objects.get(pk = request.POST.get('tagID'))
        instance.is_inactive = True
        instance.save()
    elif request.method=='POST' and 'tagActive' in request.POST:
        instance = Tag.objects.get(pk = request.POST.get('tagID'))
        instance.is_inactive = False
        instance.save()
    return render(request, 'adminTag.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminTask(request):
    dataList = Task.objects.all()
    context = {
        'page':'adminTask',
        'dataList':dataList,
        'phase':Task.phase
    }
    if request.method == 'POST' and 'taskAdd' in request.POST:
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            form = taskForm()
    elif request.method=='POST' and 'taskEdit' in request.POST:
        instance = Task.objects.get(pk = request.POST.get('taskID'))
        instance.taskName = request.POST.get('taskName')
        instance.phaseName = request.POST.get('taskPhase')
        instance.has_file = request.POST.get('taskOption') == 'on'
        instance.save()
    elif request.method=='POST' and 'taskInactive' in request.POST:
        instance = Task.objects.get(pk = request.POST.get('taskID'))
        instance.is_inactive = True
        instance.save()
    elif request.method=='POST' and 'taskActive' in request.POST:
        instance = Task.objects.get(pk = request.POST.get('taskID'))
        instance.is_inactive = False
        instance.save()
    return render(request, 'adminTask.html', context)
@login_required(login_url='login')
@user_passes_test(designation_check, login_url='login')
def adminUnit(request):
    dataList = Unit.objects.all()
    context = {
        'page':'adminUnit',
        'dataList':dataList
    }
    if request.method == 'POST' and 'unitAdd' in request.POST:
        form = unitForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            form = unitForm()
    elif request.method=='POST' and 'unitEdit' in request.POST:
        instance = Unit.objects.get(pk = request.POST.get('unitID'))
        instance.unitName = request.POST.get('unitName')
        instance.save()
    elif request.method=='POST' and 'unitInactive' in request.POST:
        instance = Unit.objects.get(pk = request.POST.get('unitID'))
        instance.is_inactive = True
        instance.save()
    elif request.method=='POST' and 'unitActive' in request.POST:
        instance = Unit.objects.get(pk = request.POST.get('unitID'))
        instance.is_inactive = False
        instance.save()
    return render(request, 'adminUnit.html', context)
