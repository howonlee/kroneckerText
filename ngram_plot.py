import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = range(1,9)
    y= [51156,576283,1490023,2136218,2422978,2526507,2565709,2584265]
    plt.loglog(x, y)
    plt.show()
