import requests
from bs4 import BeautifulSoup


#El script busca los sueldos de todos los profesores  de la FCFM en transparencia y los acomoda de menor a mayor

lb = []
ls = []
ld = []


def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



if __name__ == "__main__":

    for i in range(0,10):
        b = str(i+1)
        url = "http://transparencia.uanl.mx/remuneraciones_mensuales/bxd.php?pag_act="+(b)+"&id_area_form=2305&mya_det=082020"
        getreq = requests.get(url)
        texto = getreq.text
        soup = BeautifulSoup(texto, "lxml")
        x = 0
        for nombre in soup.findAll('tr'):
            x += 1
            if x > 5:
                lb.append(nombre.text)

    for profesor in lb:
        c = profesor.replace("Ver Detalle", "").replace("\n", "")
        ld.append(c)

    for d in ld:
        h = d.split("$")
        h[1] = h[1].replace(" ", "").replace(",", "")
        h[1] = float(h[1])
        ls.append(h)

    bubbleSort(ls)

    for f in ls:
        print (f)
