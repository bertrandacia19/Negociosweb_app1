from django.shortcuts import render
from django.http import HttpResponse



pagos = [
    {
        'monto': '14000',
        'tasa': '12',
        'plazo' : '2',
        'cuotas': '659',
        'totalPagar' : '15816'
    }
]

def plantilla(request):

    
    if request.method == 'POST':
        monto = int(request.POST.get('monto'))
        tasa = int(request.POST.get('tasa'))
        plazo = int(request.POST.get('plazo'))

        r = tasa / 100 / 12
        n = plazo * 12

        c = (monto*r)/(1-(1+r)**-n)

        tp = monto + monto * r * n

        ctx = {
            'pagos' : pagos
        }

        pagos.append({
            'monto': monto,
            'tasa': tasa,
            'plazo' : plazo,
            'cuotas': c,
            'totalPagar' : tp,
        })

        return render(request, 'app/plantilla.html', ctx)
    else:
         
          ctx = {
               'cuota' : pagos
          }
          
          return render(request, 'app/plantilla.html', ctx)