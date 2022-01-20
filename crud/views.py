from django.shortcuts import render,redirect



def home(request):
               if request.user.is_authenticated:
                                  user = request.user
                                  print(user.username)
                                  return redirect('/vehicle/list/'+user.username+'/')
               return render(request,"home.html")