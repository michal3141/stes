from collections import defaultdict
from statistics import mean
import pandas as pd

# Mapping between possible connections between the decision interval I and decision interval II
d1_to_d2 = {
    1: [1, 3, 8, 9, 23, 47, 48, 49, 50],
    2: [2],
    3: [3, 1, 8, 9, 23, 47, 48, 49, 50],
    4: [4, 7],
    5: [5, 6, 7],
    6: [6, 5, 7],
    7: [7, 4, 5, 6],
    8: [8, 1, 3, 9, 23, 47, 48, 49, 50],
    9: [9, 1, 3, 8, 23, 47, 48, 49, 50],
    10: [10, 16, 17, 20, 22, 26, 35],
    11: [11, 12, 13, 14, 15],
    12: [12, 11, 14, 15],
    13: [13, 11, 14],
    14: [14, 11, 12, 15, 16, 17, 20, 22, 26, 35],
    15: [15, 11, 12, 14],
    16: [16, 10, 14, 17, 20, 22, 26, 35],
    17: [17, 10, 16, 20, 22, 26, 35],
    18: [18, 21, 22, 26, 35],
    19: [19, 28],
    20: [20, 10, 16, 17, 22, 26, 35],
    21: [21, 18],
    22: [22, 10, 16, 17, 20, 26, 35],
    23: [23, 1, 3, 8, 9, 47, 48, 49, 50],
    24: [24, 30, 31, 38, 40],
    25: [25, 45],
    26: [26, 10, 16, 17, 18, 20, 21, 22, 35],
    27: [27, 29, 34, 41, 45],
    28: [28, 19],
    29: [29, 27, 34, 36, 41, 45],
    30: [30, 24, 36, 38, 40],
    31: [31, 24, 38, 39, 40, 42, 44],
    32: [32, 33, 37, 43, 46],
    33: [33, 32, 37, 43, 46],
    34: [34, 27, 29, 41, 45],
    35: [35, 10, 16, 17, 18, 20, 21, 22, 26],
    36: [36, 24, 29, 30, 38, 40],
    37: [37, 32, 33, 43, 46],
    38: [38, 24, 30, 40],
    39: [39, 31, 42, 44],
    40: [40, 24, 30, 38],
    41: [41, 27, 29, 34, 36],
    42: [42, 31, 39, 44],
    43: [43, 32, 33, 37, 46],
    44: [44, 31, 39, 42],
    45: [45, 25, 27, 29, 34],
    46: [46, 32, 33, 37, 43],
    47: [47, 1, 3, 8, 9, 23, 48, 49, 50],
    48: [48, 1, 3, 8, 9, 23, 47, 49, 50],
    49: [49, 1, 3, 8, 9, 23, 47, 48, 50],
    50: [50, 1, 3, 8, 9, 23, 47, 48, 49]
}
# Mapping between possible connections between the decision interval II and decision interval III
d2_to_d3 = {
    1: [1, 8, 19, 28, 31, 34, 39, 46],
    2: [2],
    3: [3, 9, 25, 47, 48, 49, 50],
    4: [4],
    5: [5],
    6: [6],
    7: [7],
    8: [8, 1, 19, 28, 31, 34, 39, 46],
    9: [9, 3, 25, 47, 48, 49, 50],
    10: [10, 11, 12, 13, 14, 15, 16, 17, 20, 22, 23, 26, 35],
    11: [11, 10, 12, 13, 14, 15, 16, 17, 20, 22, 23, 26, 35],
    12: [12, 10, 11, 13, 14, 15, 16, 17, 20, 22, 23, 26, 35],
    13: [13, 10, 11, 12, 14, 15, 16, 17, 20, 22, 23, 26, 35],
    14: [14, 10, 11, 12, 13, 15, 16, 17, 20, 22, 23, 26, 35],
    15: [15, 10, 11, 12, 13, 14, 16, 17, 20, 22, 23, 26, 35],
    16: [16, 10, 11, 12, 13, 14, 15, 17, 20, 22, 23, 26, 35],
    17: [17, 10, 11, 12, 13, 14, 15, 16, 20, 22, 23, 26, 35],
    18: [18, 21, 24, 27, 29, 30, 32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45],
    19: [19, 1, 8, 28, 31, 34, 39, 46],
    20: [20, 10, 11, 12, 13, 14, 15, 16, 17, 22, 23, 26, 35],
    21: [21, 18, 24, 27, 29, 30, 32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45],
    22: [22, 10, 11, 12, 13, 14, 15, 16, 17, 20, 23, 26, 35],
    23: [23, 10, 11, 12, 13, 14, 15, 16, 17, 20, 22, 26, 35],
    24: [24, 18, 21, 27, 29, 30, 32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45],
    25: [25, 3, 9, 47, 48, 49, 50],
    26: [26, 10, 11, 12, 13, 14, 15, 16, 17, 20, 22, 23, 35],
    27: [27, 18, 21, 24, 29, 30, 32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45],
    28: [28, 1, 8, 19, 31, 34, 39, 46],
    29: [29, 18, 21, 24, 27, 30, 32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45],
    30: [30, 18, 21, 24, 27, 29, 32, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45],
    31: [31, 1, 8, 19, 28, 34, 39, 46],
    32: [32, 18, 21, 24, 27, 29, 30, 33, 36, 37, 38, 40, 41, 42, 43, 44, 45],
    33: [33, 18, 21, 24, 27, 29, 30, 32, 36, 37, 38, 40, 41, 42, 43, 44, 45],
    34: [34, 1, 8, 19, 28, 31, 39, 46],
    35: [35, 10, 11, 12, 13, 14, 15, 16, 17, 20, 22, 23, 26],
    36: [36, 18, 21, 24, 27, 29, 30, 32, 33, 37, 38, 40, 41, 42, 43, 44, 45],
    37: [37, 18, 21, 24, 27, 29, 30, 32, 33, 36, 38, 40, 41, 42, 43, 44, 45],
    38: [38, 18, 21, 24, 27, 29, 30, 32, 33, 36, 37, 40, 41, 42, 43, 44, 45],
    39: [39, 1, 8, 19, 28, 31, 34, 46],
    40: [40, 18, 21, 24, 27, 29, 30, 32, 33, 36, 37, 39, 41, 42, 43, 44, 45],
    41: [41, 18, 21, 24, 27, 29, 30, 32, 33, 36, 37, 39, 40, 42, 43, 44, 45],
    42: [42, 18, 21, 24, 27, 29, 30, 32, 33, 36, 37, 39, 40, 41, 43, 44, 45],
    43: [43, 18, 21, 24, 27, 29, 30, 32, 33, 36, 37, 38, 40, 41, 42, 44, 45],
    44: [44, 18, 21, 24, 27, 29, 30, 32, 33, 36, 37, 38, 40, 41, 42, 43, 45],
    45: [45, 18, 21, 24, 27, 29, 30, 32, 33, 36, 37, 38, 40, 41, 42, 43, 44],
    46: [46, 1, 8, 19, 28, 31, 34, 39],
    47: [47, 3, 9, 25, 48, 49, 50],
    48: [48, 3, 9, 25, 47, 49, 50],
    49: [49, 3, 9, 25, 47, 48, 50],
    50: [50, 3, 9, 25, 47, 48, 49]
}

eps = 10e-6

v_cols = ['W%s' % i for i in range(1, 51)]

criteria = [
    'sportowo-rekreacyjne',
    'przemyslowo-gospodarcze',
    'wyburzenia',
    'geologia',
    'gornicze',
    'budowa',
    'przyrodnicze',
    'sakralne',
    'hydrologia',
    'zabytkowe',
    'transportowo-ruchowe'
]

criteria_indices = set([0, 9, 18, 26, 30, 40, 46, 54, 58, 60, 68, 79])
# Stymulanty to: liczba wezlow, prognoza ruchu, dodatkowe natezenie na A4
stimulants = set([70, 71, 72, 74, 76])

scores = {}

def get_origin(i):
    if 1 <= i <= 7:
        return 'Skawina'
    elif 8 <= i <= 17:
        return 'Poludnie'
    elif 18 <= i <= 22:
        return 'Lagiewniki'
    elif 23 <= i <= 28:
        return 'Tuchowska'
    elif 29 <= i <= 36:
        return 'Blacharska'
    elif 37 <= i <= 42:
        return 'Biezanow'
    elif 43 <= i <= 46:
        return 'Niepolomice'
    elif i == 47:
        return 'Lagiewniki'
    elif i == 48:
        return 'Blacharska'
    elif i == 49:
        return 'Biezanow'
    elif i == 50:
        return 'Niepolomice'

def min_max_normalize(row):
    return None

def main():
    cnt = 0
    budynki_mieszkalne = [
        [54, 80, 60, 53, 48, 57, 44, 65, 71, 64, 124, 92, 40, 58, 68, 67, 102, 94, 121, 111, 136, 88, 192, 127, 103, 109, 142, 85, 107, 115, 145, 149, 132, 136, 109, 135, 224, 238, 237, 217, 239, 220, 130, 101, 129, 130, 113, 110, 294, 129],
        [64, 61, 58, 94, 40, 44, 57, 50, 56, 52, 34, 50, 24, 27, 24, 27, 43, 31, 49, 34, 30, 28, 36, 61, 51, 34, 20, 57, 23, 65, 87, 112, 52, 17, 40, 43, 56, 72, 78, 53, 12, 65, 67, 100, 41, 89, 57, 85, 98, 60],
        [90, 35, 28, 35, 30, 30, 19, 89, 28, 21, 19, 21, 19, 22, 32, 30, 30, 20, 22, 29, 25, 29, 31, 26, 28, 34, 25, 29, 26, 25, 32, 20, 22, 89, 27, 21, 26, 26, 21, 26, 25, 22, 22, 26, 26, 22, 28, 28, 28, 28]

    ]
    budynki_mieszkalne_res = {}
    budynki_mieszkalne_origin = defaultdict(list)

    df1 = pd.read_csv('WAP_Dane_D1.csv')
    df2 = pd.read_csv('WAP_Dane_D2.csv')
    df3 = pd.read_csv('WAP_Dane_D3.csv')
    print(df1)
    print(df1.dtypes)
    print(df1['W1'])
    for c in v_cols:
        df1[c] = df1[c].str.replace(',','.').str.replace(' ', '').str.replace('%', '')
        df1[c] = df1[c].astype(float)
        df2[c] = df2[c].str.replace(',','.').str.replace(' ', '').str.replace('%', '') 
        df2[c] = df2[c].astype(float)
        df3[c] = df3[c].str.replace(',','.').str.replace(' ', '').str.replace('%', '') 
        df3[c] = df3[c].astype(float)

    print(df1['W1'])
    print(df2['W1'])
    print(df3['W1'])

    W1 = df1['W1'] + df2['W1'] + df3['W1']
    df = df1[['Podkryterium - Obiekt', 'Waga podkryterium', 'Jednostka w buforze']]
    print(W1)
    print(df)
    for i in range(1, 51):
        #if cnt > 10: break
        for j in d1_to_d2[i]:
            #if cnt > 10: break
            for k in d2_to_d3[j]:
                #if cnt > 10: break
                df[(i, j, k)] = df1['W%d'%i] + df2['W%d'%j] + df3['W%d'%k]
                v = budynki_mieszkalne[0][i-1] + budynki_mieszkalne[1][j-1] + budynki_mieszkalne[2][k-1]
                budynki_mieszkalne_res[(i, j, k)] = v
                budynki_mieszkalne_origin[get_origin(i)].append(v)
                cnt += 1
    #print(budynki_mieszkalne_res)
    #print(budynki_mieszkalne_origin)
    #for k, v in budynki_mieszkalne_origin.items():
    #    print(k)
    #    print(min(v), mean(v), max(v))
    print(cnt)
    print(df)
    criteria_index = 0
    for index, row in df.iterrows():
        if index in criteria_indices:
            if index != 0:
                print('-----------Wyniki:-----------------')
                criterion = criteria[criteria_index]
                score = wmean_num/wmean_denom
                print(criterion)
                print(score)
                scores[criterion] = score
                criteria_index += 1
            wmean_num = 0 * row[3:]
            wmean_denom = 0
        #print(row['Podkryterium - Obiekt'])
        weight = row['Waga podkryterium']
        #print('Waga podkryterium:', weight)
        s = row[3:]
        smin = s.min()
        smax = s.max()
        #print('Original values:')
        #print(s)
        #print('Normalized values:')
        if smax-smin < eps:
            sn = 0*s
        else:
            sn = 5.0*(s-smin)/(smax-smin)
            # For criteria which are stimulants we invert the scores:
            if index in stimulants:
                sn = 5.0 - sn
        #print(sn)
        wmean_num += weight*sn
        wmean_denom += weight
    print('-----------Wyniki:-----------------')
    criterion = criteria[criteria_index]
    score = wmean_num/wmean_denom
    print(criterion)
    print(score)
    scores[criterion] = score

    print(budynki_mieszkalne_res)
    with open('budynki-mieszkalne.csv', 'w') as f:
        f.write('Wezel,Kombinacja,Wyburzenia_Mieszkalne\n')
        for k, v in budynki_mieszkalne_res.items():
            f.write('%s,%s,%s\n' % (get_origin(k[0]), 'W%dW%dW%d' % (k[0], k[1], k[2]), str(v)))

    przestrzenno_spoleczne = (3.0 * scores['sportowo-rekreacyjne'] + 4.0 * scores['przemyslowo-gospodarcze'] + 4.0 * scores['wyburzenia']) / 11.0
    print('Wyniki dla kryterium przestrzenno-społecznego:')
    print(przestrzenno_spoleczne)
    przestrzenno_spoleczne_dict = przestrzenno_spoleczne.to_dict()
    with open('przestrzenno-spoleczne.csv', 'w') as f:
        #f.write('Wezel,Kombinacja,Ocena\n')
        for k, v in przestrzenno_spoleczne_dict.items():
            f.write('%s,%s,%s\n' % (get_origin(k[0]), 'W%dW%dW%d' % (k[0], k[1], k[2]), str(v)))

    ekonomiczne = (5.0 * scores['geologia'] + 5.0 * scores['gornicze'] + 5.0 * scores['budowa']) / 15.0
    print('Wyniki dla kryterium ekonomicznego:')
    print(ekonomiczne)
    ekonomiczne_dict = ekonomiczne.to_dict()
    with open('ekonomiczne.csv', 'w') as f:
        #f.write('Wezel,Kombinacja,Ocena\n')
        for k, v in ekonomiczne_dict.items():
            f.write('%s,%s,%s\n' % (get_origin(k[0]), 'W%dW%dW%d' % (k[0], k[1], k[2]), str(v)))

    srodowiskowe = (5.0 * scores['przyrodnicze'] + 3.0 * scores['sakralne'] + 4.0 * scores['hydrologia'] + 5.0 * scores['zabytkowe']) / 17.0
    print('Wyniki dla kryterium srodowiskowego:')
    print(srodowiskowe)
    srodowiskowe_dict = srodowiskowe.to_dict()
    with open('srodowiskowe.csv', 'w') as f:
        #f.write('Wezel,Kombinacja,Ocena\n')
        for k, v in srodowiskowe_dict.items():
            f.write('%s,%s,%s\n' % (get_origin(k[0]), 'W%dW%dW%d' % (k[0], k[1], k[2]), str(v)))

    transportowe = scores['transportowo-ruchowe']
    print('Wyniki dla kryterium transportowego:')
    print(transportowe)
    transportowe_dict = transportowe.to_dict()
    with open('transportowe.csv', 'w') as f:
        #f.write('Wezel,Kombinacja,Ocena\n')
        for k, v in transportowe_dict.items():
            f.write('%s,%s,%s\n' % (get_origin(k[0]), 'W%dW%dW%d' % (k[0], k[1], k[2]), str(v)))

    sumarycznie = 0.15 * przestrzenno_spoleczne + 0.25 * ekonomiczne + 0.25 * srodowiskowe + 0.35 * transportowe
    print('Wyniki sumarycznie:')
    print(sumarycznie)
    sumarycznie_dict = sumarycznie.to_dict()
    with open('sumarycznie.csv', 'w') as f:
        #f.write('Wezel,Kombinacja,Ocena\n')
        for k, v in sumarycznie_dict.items():
            f.write('%s,%s,%s\n' % (get_origin(k[0]), 'W%dW%dW%d' % (k[0], k[1], k[2]), str(v)))

if __name__ == '__main__':
    main()
