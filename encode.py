#!/usr/bin/env python3


def split(items):
    total = sum(item[1] for item in items)

    index = 0
    subset_total = 0
    min_difference = total

    for item in items:
        subset_total += item[1]
        difference = abs(total - 2 * subset_total)

        if min_difference > difference:
            min_difference = difference
        else:
            break

        index += 1

    return items[:index], items[index:]


def shannon_fano(items):
    if len(items) == 1:
        return

    first, second = split(items)

    for item in first:
        item[2] += '0'

    for item in second:
        item[2] += '1'

    shannon_fano(first)
    shannon_fano(second)


def main():
    labels = input("Enter symbols splitted by space: ").split(' ')

    items = []
    for label in labels:
        weight = int(input("Enter the weight for '{}' symbol: ".format(label)))
        items.append([label, weight, ''])

    items = sorted(items, key=lambda x: x[1], reverse=True)
    shannon_fano(items)

    for item in items:
        print(item[0], "=>", item[2])


if __name__ == '__main__':
    main()
