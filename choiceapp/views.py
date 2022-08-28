from django.shortcuts import render, redirect
from choiceapp.models import Customer, Pollques, Solution
from django.http import HttpResponse
from datetime import datetime

import psycopg2

from django.views.generic import View
# importing get_template from loader
from django.template.loader import get_template
# import render_to_pdf from util.py
from .utils import render_to_pdf

# Create your views here.
conn = psycopg2.connect(
    database="poll_choice", user='postgres', password='sneha123'
# database="mydb", user='postgres', password='sneha123', host='127.0.0.1', port= '5432'
)


# Setting auto commit false

conn.autocommit = True


# Creating a cursor object using the cursor() method

cursor1 = conn.cursor()


def index(request):
    data = {}
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    date = now.strftime("%b-%d-%Y")
    data['s_user'] = request.session.get('user')
    data['result'] = Pollques.objects.all()
    if request.method == "GET":
        return render(request, 'index.html', data)
    else:
        answer = request.POST.get('aa')
        user = request.session.get('user')
        que_id = request.POST.get('poll_id')
        feed = "None"
        cursor = conn.cursor()
        cursor.execute("select * from poll_sol where username ='" + user + "' and que_id ='" + que_id + "'")
        tempvar = cursor.fetchall()
        rowcount = len(tempvar)
        print(rowcount)
        print(que_id, answer, user)
        if rowcount == 1:
            data["msg"] = "you already solved this question"
            return render(request, 'index.html', data)
        else:
            savecard = Solution()
            # here fullname , username, password is database field name
            savecard.que_id = que_id
            savecard.ans = answer
            savecard.username = user
            savecard.t_time = current_time
            savecard.t_date = date
            savecard.note = feed
            savecard.save()

            return render(request, 'index.html', data)




def signup(request):
    sign_data = {}
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        name = request.POST.get('fname')
        addr = request.POST.get('add')
        e_mail = request.POST.get('mail')
        mobile = request.POST.get('num')
        user_name = request.POST.get('user')
        pass_word = request.POST.get('pass')
        print(name, addr, e_mail, mobile, user_name, pass_word)

        cursor1.execute("select * from customer where username='" + user_name + "'")
        tempvar = cursor1.fetchall()
        rowcount = len(tempvar)

        cursor2 = conn.cursor()
        cursor2.execute("select * from customer where email='" + e_mail + "'")
        mailvar = cursor2.fetchall()
        rowcount2 = len(mailvar)

        cursor3 = conn.cursor()
        cursor3.execute("select * from customer where mobile='" + mobile + "'")
        mobvar = cursor3.fetchall()
        rowcount3 = len(mobvar)

        if rowcount == 1:
            sign_data['msg'] = 'username allready exist'
            return render(request, 'signup.html', sign_data)
        elif rowcount2 == 1:
            sign_data['emsg'] = 'email allready exist'
            return render(request, 'signup.html', sign_data)
        elif rowcount3 == 1:
            sign_data['pmsg'] = 'mobile allready exist'
            return render(request, 'signup.html', sign_data)
        else:
            savecard = Customer()
            # here fullname , username, password is database field name
            savecard.fullname = name
            savecard.address = addr
            savecard.email = e_mail
            savecard.mobile = mobile
            savecard.username = user_name
            savecard.password = pass_word
            savecard.save()
            print('demo')
            return redirect("login")


def poll(request):
    data = {}
    data['s_user'] = request.session.get('user')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    date = now.strftime("%b-%d-%Y")
    if request.method == "GET":
        return render(request, 'polls.html', data)
    else:
        user_name = request.POST.get('user')
        query = request.POST.get('que')
        ans1 = request.POST.get('cho1')
        ans2 = request.POST.get('cho2')
        ans3 = request.POST.get('cho3')
        ans4 = request.POST.get('cho4')
        print(query, ans1, ans2, ans3, ans4, user_name)

        cursor1.execute("select * from poll_ques where username='" + user_name + "'")
        mobvar = cursor1.fetchall()
        rowcount3 = len(mobvar)
        print(rowcount3)

        if rowcount3 == 5:
            data['msg'] = 'you allready added 5 questions, operation terminated'
            return render(request, 'polls.html', data)
        else:
            savecard = Pollques()
            # here Question , username, cho4 is database field name
            savecard.Question = query
            savecard.cho1 = ans1
            savecard.cho2 = ans2
            savecard.cho3 = ans3
            savecard.cho4 = ans4
            savecard.username = user_name
            savecard.t_time = current_time
            savecard.t_date = date
            savecard.save()
            print('demo')
            data['confir'] = "data added successfully"
            return render(request, 'polls.html', data)


def login(request):

    data = {}

    if request.method == "GET":
        return render(request, 'login.html')
    else:
        if 'log' in request.POST:
            name = request.POST.get('users')
            passwo = request.POST.get('passw')
            cursor = conn.cursor()
            cursor.execute("select * from customer where username='" + name + "' and password ='" + passwo + "'")
            tempvar = cursor.fetchall()
            rowcount = len(tempvar)
            print(rowcount)

            if rowcount == 1:
                request.session['user'] = name
                data['s_user'] = request.session.get('user')
                print(request.session['user'])
                return redirect("home")
            else:
                data['msg'] = 'enter valid username or password'
                return render(request, 'login.html', data)


def profile(request):
    data = {}
    data['s_user'] = request.session.get('user')
    data['result'] = Customer.objects.filter(username=data['s_user'])
    return render(request, 'profile.html', data)


def activity(request):
    data = {}
    data['s_user'] = request.session.get('user')
    data['result'] = Pollques.objects.filter(username=data['s_user'])
    return render(request, 'activity.html', data)


def u_logout(request):
    del request.session['user']
    return redirect('login')


def profilePDF(request):
    data = {}
    data['s_user'] = request.session.get('user')
    if request.method == "GET":
        data['result'] = Customer.objects.filter(username=data['s_user'])
        data['p_result'] = Customer.objects.filter(username=data['s_user'])
        return render(request, 'profileinfo.html', data)
    else:
        name = request.POST.get('p_name')
        add = request.POST.get('p_address')
        mail = request.POST.get('p_mail')
        no = request.POST.get('p_no')
        user = request.POST.get('p_user')
        passwo = request.POST.get('p_pass')
        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": name,
            "address": add,
            "mail": mail,
            "mob": no,
            "user_name": user,
            "u_pass": passwo,

            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")





class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,

            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
# this is end

# this is end








