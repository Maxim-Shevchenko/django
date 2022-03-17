from django.shortcuts import render
from django.shortcuts import redirect
from reviews.forms import ReviewForm
def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            email = data.get('email')
            review = data.get('review')
            rating = data.get('rating')
            with open('data.csv', 'a') as file:
                file.write(f'{name}|{email}|{review}|{rating}\n')
            return redirect('reviews')
    else:
        form = ReviewForm()
        return render(request, 'reviews.html', {'form': form})

