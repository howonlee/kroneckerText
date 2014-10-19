import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = range(1,5)
    y = [56057, 455267, 907494, 1096987]
    plt.loglog(x, y)
    plt.show()
