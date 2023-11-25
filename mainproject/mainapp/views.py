import razorpay
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
import re
from django.contrib.auth import authenticate,login
from . models import *

# Create your views here.

def index(request):
    if request.method == "POST":
        email = request.POST.get("email")
        student_details = Student.objects.filter(email=email).first()
        instructor_details = Instructor.objects.filter(email=email).first()
        if student_details:
            return redirect('student-dashboard')
        elif instructor_details:
            return redirect('instructor-dashboard')
        else:
            messages.error(request, str("Invalid Credentials"))
            return redirect(request.META['HTTP_REFERER'])
    return render(request,"index.html")

def login_check(request):
    login_type = request.GET.get("login_type")
    email = request.GET.get("email")
    password = request.GET.get("password")
    if login_type == "student":
        user = Student.objects.filter(email=email).first()
        if not user:
            return JsonResponse({"message": "Invalid Student Datas", "status": "error"})
        elif user.password != password:
            return JsonResponse({"message": "Invalid Password", "status": "error"})
        else:
            request.session['user_id'] = user.id
            request.session['user_type'] = login_type
            return JsonResponse({"message": "success", "status": "success"})
    elif login_type == "instructor":
        user = Instructor.objects.filter(email=email).first()
        if not user:
            return JsonResponse({"message": "Invalid Instructor Datas", "status": "error"})
        elif user.password != password:
            return JsonResponse({"message": "Invalid Password", "status": "error"})
        else:
            request.session['user_id'] = user.id
            request.session['user_type'] = login_type
            return JsonResponse({"message": "success", "status": "success"})
    else:
        return JsonResponse({"message": "Invalid Datas", "status": "error"})

def register(request):
    if request.method == "POST":
        messages.success(request, str("Successfully Registered"))
        return redirect("/")
    return render(request,"register.html")

def register_data(request):
    if request.method == "POST":
        user_type = request.POST.get("user_type")
        name = request.POST.get("name").strip()
        email = request.POST.get("email").strip()
        password = request.POST.get("password").strip()
        required_fields = []
        if not name:
            required_fields.append("name")
        if not email:
            required_fields.append("email")
        if not password:
            required_fields.append("password")
        if required_fields:
            response = f"{', '.join(required_fields)} are required"
            return JsonResponse({"message": response, "status": "error"})
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return JsonResponse({"message": "not a valid email", "status": "error"})
        if user_type == "student":
            if Student.objects.filter(email=email).exists():
                return JsonResponse({"message": "student with same email exists", "status": "error"})
            data_create = Student.objects.create(
                fullname = name,
                email = email,
                password = password
            )
        else:
            if Instructor.objects.filter(email=email).exists():
                return JsonResponse({"message": "instructor with same email exists", "status": "error"})
            data_create = Instructor.objects.create(
                fullname=name,
                email=email,
                password=password
            )
        return JsonResponse({"message": "success", "status": "success"})


def student_dashboard(request):
    user_id = request.session['user_id']
    data = StudentCourses.objects.filter(student_id_id=user_id)
    context = {
        'data':data
    }
    return render(request,"student_dashboard.html",context)

def buy_course(request):
    user_id = request.session['user_id']
    data__student_course = StudentCourses.objects.filter(student_id_id=user_id)
    course_id = list(data__student_course.values_list('course_id_id', flat=True))
    data = Courses.objects.all().exclude(id__in=course_id)
    context = {
        'data':data
    }
    return render(request,"buy_course.html",context)

def instructor_dashboard(request):
    if request.method == "POST":
        messages.success(request, str("Success"))
        return redirect(request.META['HTTP_REFERER'])
    user_id = request.session['user_id']
    data = Courses.objects.filter(instructor_id_id=user_id)
    context = {
        'data':data
    }
    return render(request,"instructor_dashboard.html",context)

def create_course(request):
    if request.method == "POST":
        user_id = request.session['user_id']
        course_type = request.POST.get("course_type")
        course_name = request.POST.get("course_name").strip()
        contact = request.POST.get("contact").strip()
        amount = request.POST.get("amount").strip()
        if amount == "" or amount == None:
            amount = 0
        required_fields = []
        if not course_name:
            required_fields.append("course name")
        if course_type == "link":
            course_link = request.POST.get("course_link").strip()
            if not course_link:
                required_fields.append("course link")
            if required_fields:
                response = f"{', '.join(required_fields)} are required"
                return JsonResponse({"message": response, "status": "error"})
            data_create = Courses.objects.create(
                instructor_id_id = user_id,
                course_name = course_name,
                course_type = course_type,
                course_link = course_link,
                contact_number= contact,
                amount = amount
            )
        if course_type == "file":
            try:
                course_file = request.FILES["course_file"]
            except:
                course_file = ""
            if not course_file:
                required_fields.append("course file")
            if required_fields:
                response = f"{', '.join(required_fields)} are required"
                return JsonResponse({"message": response, "status": "error"})
            data_create = Courses.objects.create(
                instructor_id_id=user_id,
                course_name=course_name,
                course_type=course_type,
                course_file = course_file,
                contact_number = contact,
                amount = amount
            )
        return JsonResponse({"message": "success", "status": "success"})

def edit_course(request):
    id = request.GET.get("id")
    data = Courses.objects.get(id=id)
    context = {
        'data':data
    }
    return render(request,"edit_course.html",context)


def edit_course_action(request):
    if request.method == "POST":
        course_id = request.POST.get("course_id")
        course_type = request.POST.get("course_type")
        course_name = request.POST.get("course_name").strip()
        contact = request.POST.get("contact").strip()
        amount = request.POST.get("amount").strip()
        if amount == "" or amount == None:
            amount = 0
        required_fields = []
        if not course_name:
            required_fields.append("course name")
        if course_type == "link":
            course_link = request.POST.get("course_link").strip()
            if not course_link:
                required_fields.append("course link")
            if required_fields:
                response = f"{', '.join(required_fields)} are required"
                return JsonResponse({"message": response, "status": "error"})
            data_create = Courses.objects.filter(id=course_id).update(
                course_name=course_name,
                course_type=course_type,
                course_link=course_link,
                contact_number=contact,
                amount = amount
            )
        if course_type == "file":
            try:
                course_file = request.FILES["course_file"]
            except:
                course_file = ""
            if required_fields:
                response = f"{', '.join(required_fields)} are required"
                return JsonResponse({"message": response, "status": "error"})
            data_create = Courses.objects.filter(id=course_id).update(
                course_name=course_name,
                course_type=course_type,
                contact_number=contact,
                amount = amount
            )
            if course_file != "":
                data_save = Courses.objects.get(id=course_id)
                data_save.course_file = course_file
                data_save.save()
        return JsonResponse({"message": "success", "status": "success"})


def view_users(request):
    id = request.GET.get("id")
    data = StudentCourses.objects.filter(course_id_id=id)
    context = {
        'data':data
    }
    return render(request,"view_user.html",context)


def delete_course(request,id):
    data = Courses.objects.get(id=id).delete()
    messages.success(request, str("Success"))
    return redirect(request.META['HTTP_REFERER'])





razorpay_client = razorpay.Client(auth=('rzp_test_Z9UoekuvjmnspV', 'V3dICVUkzpRkxGhgbOChIG1l'))

def pay_course(request,id):
    user_id = request.session['user_id']
    course=Courses.objects.get(id=id)
    amount1 = course.amount
    currency = 'INR'
    amount = int(amount1) * 100  # Rs. 200
    if amount == 0:
        data = StudentCourses()
        data.student_id_id = user_id
        data.course_id_id = course.id
        data.save()
        messages.success(request, str("Success"))
        return redirect('student-dashboard')
    else:
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                           currency=currency,
                                                           payment_capture='0'))
        razorpay_order_id = razorpay_order['id']
        callback_url = 'paymenthandler'
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['user_id'] = user_id
        context['course_name'] = course.course_name
        context['course_id'] = course.id
        context['amount1'] = amount1
        context['razorpay_merchant_key'] = 'rzp_test_Z9UoekuvjmnspV'
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
        return render(request, 'tester.html', context=context)




def paymenthandler(request):
    if request.method == "POST":
        data=StudentCourses()
        data.student_id_id = request.POST.get('user_id','')
        data.course_id_id=request.POST.get('course_id','')
        data.save()
        razorpay_order_id = request.POST.get('order_id')
        payment_id = request.POST.get('payment_id', '')

        signature = request.POST.get('razorpay_signature', '')

        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        amount = int(request.POST.get("amount")) * 100  # Rs. 200
        razorpay_client.payment.capture(payment_id, amount)

        messages.success(request, str("Success"))
        return redirect('student-dashboard')
