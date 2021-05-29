times = ('Flamengo','Santos','Palmeiras','Grêmio','Athletico-PR','São Paulo','Internacional','Corinthians',
         'Fortaleza','Goiás','Bahia','Vasco da Gama','Atlético-MG','Fluminense','Botafogo','Ceará-SC','Cruzeiro',
         'CSA','Chapecoense','Avaí')
print('Os Cinco Primeiros: ',times[0:5])
print('Os ultimos 4 Colocados: ',times[-4:])
print(sorted(times))
print('Chapecoense está em: {}'.format(times.index('Chapecoense')+1))