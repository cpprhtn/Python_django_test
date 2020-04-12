from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['textarea']
    get = text.split()
    word_dic = {}

    for something in get:
        if something in word_dic:
            word_dic[something]+=1

        else:
            word_dic[something]=1

    return render(request, 'result.html', {'full':text, 'total':len(text), 'ok':len(word_dic.items())})
