times=('São Paulo', 'Atlétio - MG', 'Flamengo', 'Inter', 'Grêmio', 'Palmeiras', 'Fluminense',
       'Santos', 'Corinthians','Ceará', 'Athlético','Goianiense','Bragantino','Fortaleza',
       'Sport','Bahia','Vasco','Goiás','Botafogo','Coritiba')
print(f'Os 5 primeiros colocados são: {times[0:6]}')
print('-='*40)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-='*40)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('-='*40)
print(f'O Grêmio está na {times.index("Grêmio")+1}ª posição.') #usei aspa dupla pq não pode ter aspa normal dentro da aspa normal