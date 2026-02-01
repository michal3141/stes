import matplotlib.pyplot as plt

origin_to_index = {
    'Skawina': 1,
    'Poludnie': 2,
    'Lagiewniki': 3,
    'Tuchowska': 4,
    'Blacharska': 5,
    'Biezanow': 7,
    'Niepolomice': 8
}

def visualize(criterion):
    x = []
    y = []
    z = []
    i = 0 
    with open('%s.csv' % criterion, 'r') as f:
        for line in f:
            x.append(i)
            arr = line.strip().split(',')
            origin = arr[0]
            y.append(origin_to_index[origin])
            variant = arr[1]
            arr2 = variant.strip().split('W')
            z.append(int(arr2[1]))
            i += 1
    plt.scatter(x, y, c=y)
    plt.xlabel('Pozycja wariantu w rankingu')
    plt.ylabel('Numer węzła początkowego')
    plt.title('WAP węzły %s' % criterion)
    plt.show()

    plt.scatter(x, z, c=y)
    plt.xlabel('Pozycja wariantu w rankingu')
    plt.ylabel('Pierwszy odcinek decyzyjny')
    plt.title('WAP odcinki %s' % criterion)
    plt.show()

def compare_waps():
    variant_to_index = {}
    with open('WAP_Ranking.csv', 'r') as f:
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
    with open('sumarycznie.csv', 'r') as f:
        for line in f:
            arr = line.strip().split(',')
            origin  = arr[0]
            c.append(origin_to_index[origin])
            variant = arr[1]
            x.append(i)
            y.append(variant_to_index[variant])
            i += 1
    plt.scatter(x, y, c=c)
    plt.xlabel('Pozycja wariantu w rankingu WAP')
    plt.ylabel('Pozycja wariantu w rankingu IVIA')
    plt.title('WAP vs IVIA')
    plt.show()
  


def main():
    compare_waps()
    visualize('sumarycznie')
    visualize('przestrzenno-spoleczne')
    visualize('ekonomiczne')
    visualize('srodowiskowe')
    visualize('transportowe')
    visualize('budynki-mieszkalne')
	

if __name__ == '__main__':
    main()
