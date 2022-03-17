from django.shortcuts import render
def reviews(request):
    name_1 = "Вася"
    email_1 = "vasya@example.com"
    review_1 = "Все понравилось, обязательно приду еще!"
    return render(request, 'reviews.html',{'name_1': name_1, 'email_1': email_1, 'review_1': review_1})
# Create your views here.
