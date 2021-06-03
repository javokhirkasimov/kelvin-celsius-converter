from django.shortcuts import render

def home(request):
    return render(request,'kelvin.html')

def celsius(request):
    return render(request,'celsius.html')



def result(request):
    """ Kelvin Number to Celsius Number"""
    if 'convert-kelvin' in request.GET and request.GET['num'] != '':
        num=request.GET['num']
        if ',' in num:
            num = num.replace(',', '.')
            num = float(num)
        cel=-273.15
        for i in range(int(num)):
            cel+=1
        context = {'output': round(cel,2),'value':'°C'}
        return render(request, 'result.html', context)
    else:
        return render(request,'result.html',{'output': 'Error!\n','value':'Make Sure You Entered Correct Value'})

def result2(request):
    """ Celsius Number to Kelvin Number"""
    if 'convert-celsius' in request.GET and request.GET['num'] != '':
        num = request.GET['num']
        if ',' in num:
            num = num.replace(',', '.')
            num = float(num)
        cel = int(num)+273.15
        context = {'output': round(cel, 2),'value': 'K'}
        return render(request, 'result2.html', context)
    else:
        return render(request,'result2.html',{'output': 'Error!\n','value':'Make Sure You Entered Correct Value'})


