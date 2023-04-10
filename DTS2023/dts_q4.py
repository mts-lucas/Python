sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

faturamentoTotal = sp + rj + mg + es + outros


def percentualFat(total, individual):
    return round(((individual * 100) / total), 2)


print(
    f'percentual de SP no faturamento: {percentualFat(faturamentoTotal, sp)}%')
print(
    f'percentual de RJ no faturamento: {percentualFat(faturamentoTotal, rj)}%')
print(
    f'percentual de MG no faturamento: {percentualFat(faturamentoTotal, mg)}%')
print(
    f'percentual de ES no faturamento: {percentualFat(faturamentoTotal, es)}%')
print(
    f'perc. de outros estados: {percentualFat(faturamentoTotal, outros)}%')
