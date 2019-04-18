# Peaks and Valleys
# [1,3,2,5,2]
# zip = [(1,3,2), (3,2,5), (2,5,2)]
# enum = [(0,(1,3,2)), (1,(3,2,5)), (2,(2,5,2))]
# peaks = [1,3]
# for i, (x,y,z) in enum:
#     if x < y > z:
#         peaks.append(i+1)


def peaks(data):
    """
    Finds the peaks in the data
    >>> [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    [6, 14]
    """
    return [i for i in range(1, len(data) -1) if data[i-1] < data[i] > data[i+1]]
    # return [i + 1 for i, (x, y, z) in enumerate(zip(data[:], data[1:], data[2:])) if x < y > z]


def valleys(data):
    """
    Finds tha valleys in the data
    >>> [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    [9, 17]
    """
    return [i for i in range(1, len(data) -1) if data[i-1] > data[i] < data[i+1]]
    # return [i + 1 for i, (x, y, z) in enumerate(zip(data[:], data[1:], data[2:])) if x > y < z]


def peaks_valleys(data):
    """
    Creates a sorted list of peaks and valleys out of data
    >>> [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    [6, 9, 14, 17]
    """
    return sorted(peaks(data) + valleys(data))


def draw(data):
    """
    Draws a mountain out of the data
    """
    mountain = []
    counter = max(data)
    while counter > 0:
        row = ['X' if i >= counter else ' ' for i in data]
        mountain.append(''.join(row))
        counter -= 1
    return '\n'.join(mountain)


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print(peaks(data))
    print(valleys(data))
    print(peaks_valleys(data))
    print(draw(data))


if __name__ == '__main__':
    main()
