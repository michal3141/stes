import matplotlib.pyplot as plt
import os

origin_to_index = {
    'Skawina': 1,
    'Poludnie': 2,
    'Lagiewniki': 3,
    'Tuchowska': 4,
    'Blacharska': 5,
    'Biezanow': 7,
    'Niepolomice': 8
}

index_to_origin = [None, 'Skawina', 'Południe', 'Łagiewniki', 'Tuchowska', 'Blacharska', 'Wieliczka', 'Bieżanów', 'Niepołomice']

legend = [index_to_origin[e] for e in [1, 2, 3, 4, 5, 7, 8]]

def visualize(criterion):
    x = []
    y = []
    z = []
    i = 0 
    with open(os.path.join('results', '%s.csv') % criterion, 'r') as f:
        for line in f:
            x.append(i)
            arr = line.strip().split(',')
            origin = arr[0]
            y.append(origin_to_index[origin])
            variant = arr[1]
            arr2 = variant.strip().split('W')
            z.append(int(arr2[1]))
            i += 1

    result = plt.scatter(x, y, c=y, cmap='gist_rainbow')
    plt.xlabel('Pozycja Wariantu w Rankingu WAP')
    plt.ylabel('Numer Węzła Początkowego')
    plt.title('WAP Węzły %s' % criterion)
    plt.legend(handles=result.legend_elements()[0],
        labels=legend,
        title='Węzły Początkowe'
    )
    plt.show()

    result = plt.scatter(x, z, c=y, cmap='gist_rainbow')
    plt.xlabel('Pozycja Wariantu w Rankingu WAP')
    plt.ylabel('Pierwszy Odcinek Decyzyjny')
    plt.title('WAP Odcinki %s' % criterion)
    plt.legend(handles=result.legend_elements()[0],
        labels=legend,
        title='Węzły Początkowe'
    )
    plt.show()

def compare_waps():
    variant_to_index = {}
    with open(os.path.join('data', 'WAP_Ranking.csv'), 'r') as f:
        f.readline()
        for line in f:
            arr = line.strip().split(',')
            index = int(arr[0])
            variant = '%s%s%s' % (arr[3], arr[4], arr[5])
            variant_to_index[variant] = index
    i = 1
    x = []
    y = []
    c = []
    with open(os.path.join('results', 'sumarycznie.csv'), 'r') as f:
        for line in f:
            arr = line.strip().split(',')
            origin  = arr[0]
            c.append(origin_to_index[origin])
            variant = arr[1]
            x.append(i)
            y.append(variant_to_index[variant])
            i += 1
    result = plt.scatter(x, y, c=c, cmap='gist_rainbow')
    plt.xlabel('Pozycja Wariantu w Rankingu WAP - Analiza Własna')
    plt.ylabel('Pozycja Wariantu w Rankingu WAP - Analiza IVIA')
    plt.title('Pozycja Wariantu WAP')
    plt.legend(handles=result.legend_elements()[0],
        labels=legend,
        title='Węzły Początkowe'
    )
    plt.show()
  
def collisions():
    x = []
    y = []
    z = []
    with open(os.path.join('results', 'budynki-mieszkalne.csv'), 'r') as f:
        for line in f:
            arr = line.strip().split(',')
            origin = arr[0]
            y.append(origin_to_index[origin])
            variant = arr[1]
            arr2 = variant.strip().split('W')
            z.append(int(arr2[1]))
            buildings = int(arr[2])
            x.append(buildings)

    result = plt.scatter(x, y, c=y, cmap='gist_rainbow')
    plt.xlabel('Liczba Wyburzeń Budynków Mieszkalnych')
    plt.ylabel('Numer Węzła Początkowego')
    plt.title('Liczba Wyburzeń Węzły')
    plt.legend(handles=result.legend_elements()[0],
        labels=legend,
        title='Węzły Początkowe'
    )
    plt.show()

    result = plt.scatter(x, z, c=y, cmap='gist_rainbow')
    plt.xlabel('Liczba Wyburzeń Budynków Mieszkalnych')
    plt.ylabel('Pierwszy Odcinek Decyzyjny')
    plt.title('Liczba Wyburzeń Odcinki')
    plt.legend(handles=result.legend_elements()[0],
        labels=legend,
        title='Węzły Początkowe'
    )
    plt.show()

def main():
    collisions()
    compare_waps()
    visualize('sumarycznie')
    visualize('przestrzenno-spoleczne')
    visualize('ekonomiczne')
    visualize('srodowiskowe')
    visualize('transportowe')
    visualize('budynki-mieszkalne')
	

if __name__ == '__main__':
    main()
