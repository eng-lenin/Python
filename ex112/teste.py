from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado
preço = dado.leiadinheiro('Digite o preço: R$ ')
taxa = dado.leiadinheiro('Digite a taxa [%]: ')
moeda.resumo(preço, taxa)