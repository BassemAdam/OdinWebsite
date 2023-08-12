from django.shortcuts import render,redirect

from item.models import Item,Category

from .forms import SignUpForm


# Create your views here.
def index(request):
    items = Item.objects.filter(is_Finished=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', 
                  {'items': items, 'categories': categories}
                  )

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    form=None
    if  request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid:
            form.save()

            return redirect('/login/')
        else:
            form = SignUpForm()
    

    return render(request, 'core/signup.html', {'form': form})