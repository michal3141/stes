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
    plt.scatter(x, y)
    plt.xlabel('Pozycja wariantu w rankingu')
    plt.ylabel('Numer węzła początkowego')
    plt.title('WAP węzły %s' % criterion)
    plt.show()

    plt.scatter(x, z)
    plt.xlabel('Pozycja wariantu w rankingu')
    plt.ylabel('Pierwszy odcinek decyzyjny')
    plt.title('WAP odcinki %s' % criterion)
    plt.show()

def main():
    visualize('sumarycznie')
    visualize('przestrzenno-spoleczne')
    visualize('ekonomiczne')
    visualize('srodowiskowe')
    visualize('transportowe')
	

if __name__ == '__main__':
    main()
