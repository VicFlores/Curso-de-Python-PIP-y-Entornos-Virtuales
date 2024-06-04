import matplotlib.pyplot as plt


def generate_pie_charts():
    labels = ['Python', 'C++', 'Ruby', 'Java']
    sizes = [215, 130, 245, 210]

    fig1, ax = plt.subplots()

    ax.pie(sizes, labels=labels)

    plt.savefig('pie.png')
    plt.close()
