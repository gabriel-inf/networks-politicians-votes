import pandas as pd

data = pd.read_csv('resources/votacoesVotos-2020.csv.gz', compression='gzip', sep=';')

start_year = 2013
years = [x + start_year for x in range(0,8)]


for year in years:
    data = pd.read_csv('resources/votacoesVotos-' + str(year) + '.csv.gz', compression='gzip', sep=';')

    del data['dataHoraVoto']
    del data['uriVotacao']
    del data['deputado_urlFoto']
    del data['deputado_uri']
    del data['deputado_uriPartido']

    data = data[data['voto'] != 'Simbólico']
    if year == 2013:
        data.to_csv('all.csv')
    else:
        data.to_csv('all.csv', mode='a', header=False)