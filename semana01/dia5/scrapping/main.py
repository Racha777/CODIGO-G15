import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url=requests.get('https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx')


def scrapping_tipocambio():
    if(url.status_code==200):
        print('pagina encontrada')
        #print(url.text)
        html=BeautifulSoup(url.text,'html.parser')
        tabla=html.find_all('table',{'id':'ctl00_cphContent_rgTipoCambio_ctl00'})
        #print(tabla)
        #filaDolar=html.find_all('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__0'})
        #print(filaDolar)
        """
        moneda=filaDolar[0].find('td',{'class':'APLI_fila3'})
        compra=filaDolar[0].find('td',{'class':'APLI_fila2'})
        venta=filaDolar[0].find('td',{'class':'APLI_fila2'}).findNext()
        print(moneda.get_text())
        print(compra.get_text())
        print(venta.get_text())
        cambio_valores=filaDolar[0].find_all('td',{'class':'APLI_fila2'})
        print(cambio_valores[0].get_text())
        print(cambio_valores[1].get_text())
        """

        listaMonedas=[]
        for i in range(7):
            fila=html.find('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__'+str(i)})
            moneda=fila.find('td',{'class':'APLI_fila3'})
            cambio_valores=fila.find_all('td',{'class':'APLI_fila2'})
            compra=cambio_valores[0]
            venta=cambio_valores[1]
            dicMoneda={
                'moneda':moneda.get_text(),
                'compra':compra.get_text(),
                'venta':venta.get_text()
            }
            listaMonedas.append(dicMoneda)
        comlumnas=['moneda','compra','venta']
        tablaMonedas=[moneda.values() for moneda in listaMonedas]
        print(tabulate(tablaMonedas,headers=comlumnas,tablefmt='grid'))
    else:
        print('error '+str(url.status_code))

if __name__=='__main__':
    scrapping_tipocambio()