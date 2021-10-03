from statsmodels.tsa.stattools import adfuller

# aplicando o teste Dickey-Fuller aumentado
test_series = adfuller(df['bidi4'])

print('ADF Statics: %f' % test_series[0])
print('p-value: %f' % test_series[1])
print('Critical values: ')
for key, value in test_series[4].items():
    print('\t%s: %.3f' % (key, value))
print(f'Confidence: {confidence:.2%}')
