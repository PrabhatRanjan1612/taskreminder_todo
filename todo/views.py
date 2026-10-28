from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib import messages
from todo.models import user , Taskadd

# Create your views here.
def intro(request):
    return render(request,"todo/welcome.html")


def login(request):
    if request.method == 'POST':
        user_name = request.POST['user']
        user_pass = request.POST['password']
        try:
            currUser = user.objects.get(username=user_name)
            if user_name == currUser.username and user_pass == currUser.password:
                # session
                request.session['user_id'] = currUser.id
                request.session['user_name'] = currUser.username

                return render(request , "todo/Task.html")
            else:
                messages.error(request ,"Invalid Password!")
        except user.DoesNotExist:
            messages.error(request ,"User Not Found!")

        return render(request , "todo/login.html")
    else:
        return render(request , "todo/login.html")


def register(request):
    if request.method == "POST":
        Name = request.POST['name']
        UserName = request.POST['user']
        UserPass = request.POST['password']

        try:
            user_valid = user.objects.get(username=UserName)
            messages.error(request , 'User-name already registered!')
        except:
            if Name.isalpha() == True:      
                Newuser = user(name=Name , username=UserName , password=UserPass)
                Newuser.save()
                messages.success(request , 'Sucessfully Registered')
            else:
                messages.error(request , 'Only alphabets allowed in Name!')
        
        return render(request , "todo/register.html")
    else:
        return render(request , "todo/register.html")


def forget(request):
    if request.method == "POST":
        UserName = request.POST['old_user']
        Userpass = request.POST['new_pass']

        try:
            CurrUser = user.objects.get(username=UserName)
            CurrUser.password = Userpass
            CurrUser.save()
            messages.success(request , 'Password Successfully Updated.')
        except:
            messages.error(request , 'User Not Found!')
        
        return render(request , "todo/forget.html")
    else:    
        return render(request , "todo/forget.html")
    

def addtask(request):
    if request.method == "POST":
        Curr_title = request.POST['title']
        curr_desc = request.POST['descri']
        curr_date = request.POST['date']
        
        message = ""
        try:
            user_id = request.session.get('user_id')
            curr_user = user.objects.get(id = user_id)

            task_curr = Taskadd(title=Curr_title , description=curr_desc , due_date=curr_date , user_task=curr_user)
            task_curr.save()
            message = "Task successfully added!"
        except:
            message = "Something went Worng !"
        return render(request , "todo/Task.html" ,{
            "msg":message
        })
    else:
        return render(request , "todo/Task.html")
    

def alltask(request):
    try:
        user_id = request.session.get('user_id')
        curr_user = user.objects.get(id=user_id)
        all_task = Taskadd.objects.filter(user_task=curr_user)
        return render(request , "todo/ViewTask.html" ,{
            "tasks":all_task
        })
    except:
        return render(request , "todo/ViewTask.html")


def Task_update(request , task_id):
    try:
        userid = request.session.get("user_id")
        curr_user = user.objects.get(id=userid)

        task = Taskadd.objects.get(id=task_id)   
        task.completed = True
        task.save()

        all_task = Taskadd.objects.filter(user_task=curr_user)
        return render(request , "todo/ViewTask.html",{
            "tasks":all_task,
            "msg":"Task updated successfully. congratulations you complete your Task."
        })
    except:
        userid = request.session.get("user_id")
        if userid:
            curr_user = user.objects.get(id=userid)
            all_task = Taskadd.objects.filter(user_task=curr_user)
        else:
            all_task = []

        return render(request, "todo/ViewTask.html", {
            "tasks": all_task,
            "msg": "Task update failed. Something went wrong!"
        })


def Task_trash(request , task_id):
    try:
        userid = request.session.get("user_id")
        curr_user = user.objects.get(id=userid)

        task = Taskadd.objects.get(id=task_id)   
        task.delete()

        all_task = Taskadd.objects.filter(user_task=curr_user)
        return render(request , "todo/ViewTask.html",{
            "tasks":all_task,
            "msg":"Task Deleted successfully."
        })
    except:
        userid = request.session.get("user_id")
        if userid:
            curr_user = user.objects.get(id=userid)
            all_task = Taskadd.objects.filter(user_task=curr_user)
        else:
            all_task = []

        return render(request, "todo/ViewTask.html", {
            "tasks": all_task,
            "msg": "Task Deletions failed. Something went wrong!"
        })


def details_task(request , task_id):
    try:
        Task = Taskadd.objects.get(id=task_id)
        return render(request , "todo/taskDetails.html" , {
            "task":Task
        })
    except:
        Task=[]
        return render(request , "todo/taskDetails.html" , {
            "task":Task
        })


def updateTaskDetails(request , task_id):
    if request.method == "POST":
        Curr_title = request.POST['title']
        curr_desc = request.POST['descri']
        curr_date = request.POST['date']

        message = ""
        try:
            task = Taskadd.objects.get(id=task_id)
            task.title = Curr_title
            task.description = curr_desc
            task.due_date = curr_date
            task.save()
            message = "Task successfully update!"
        except:
            message = "Task update failed. Something went wrong!"
        return render(request , "todo/taskupdate.html",{
            "msg":message,
            "task":task
        })
    else:
        try:
            curr_task = Taskadd.objects.get(id=task_id)
        except:
            curr_task=[]
        return render(request , "todo/taskupdate.html" ,{
            "task":curr_task
        })


def log_out(request):
    request.session.flush()
    return render(request , "todo/login.html")

def aboutApp(request):
    return render(request , "todo/about.html")




