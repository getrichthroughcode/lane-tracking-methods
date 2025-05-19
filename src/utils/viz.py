import matplotlib.pyplot as plt
from cannyLaneDetector import *
from mpl_toolkits.mplot3d import Axes3D
utils = helperFunction()

def visuGaussianKernel():
    sigma = 1.7
    size = 5
    kernel = utils.createGaussianKernel(sigma)
    # Step 2: Prepare the 3D plot
    x = np.linspace(-size // 2, size // 2, size)
    y = np.linspace(-size // 2, size // 2, size)
    x, y = np.meshgrid(x, y)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Step 3: Plot the surface
    surf = ax.plot_surface(x, y, kernel, cmap='viridis', edgecolor='k')
    # Axis limits and labels
    ax.set_xlim(-size, size)
    ax.set_ylim(-size, size)

    ax.set_title("3D Gaussian Kernel Surface")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Intensity")
    fig.colorbar(surf, shrink=0.6)

    plt.tight_layout()
    plt.show()




visuGaussianKernel()    
