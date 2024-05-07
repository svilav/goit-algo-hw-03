import matplotlib.pyplot as plt
import numpy as np


def koch_snowflake(order, scale=10):
    def koch_curve(points, order):
        if order == 0:
            return points
        else:
            result = []
            for i in range(len(points) - 1):
                p1 = points[i]
                p2 = points[i + 1]
                dist = (p2 - p1) / 3
                p3 = p1 + dist
                p4 = p3 + dist * np.exp(np.pi / 3 * 1j)  # Rotate 60 degrees
                result.extend([p1, p3, p4, p2 - dist])
            result.append(points[-1])
            return koch_curve(result, order - 1)

    # Initial triangle
    p1 = 0 + 0j
    p2 = scale + 0j
    p3 = scale / 2 + scale * np.sin(np.pi / 3) * 1j

    # Generate points
    bottom = koch_curve([p1, p2], order)
    right = koch_curve([p2, p3], order)
    left = koch_curve([p3, p1], order)

    snowflake = np.concatenate([bottom, right, left])
    return snowflake


def plot_snowflake(order):
    snowflake = koch_snowflake(order)
    plt.figure(figsize=(8, 8))
    plt.plot(snowflake.real, snowflake.imag, 'b-')
    plt.axis('equal')
    plt.axis('off')
    plt.title(f"Koch Snowflake - Order {order}")
    plt.savefig(f"koch_snowflake_order_{order}.png")
    plt.show()


def main():
    order = int(input("Enter the recursion level (order) of the Koch Snowflake: "))
    plot_snowflake(order)


if __name__ == "__main__":
    main()