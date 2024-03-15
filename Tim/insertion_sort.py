def insertion_sort(draw_info, ascending = True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i], lst[i-1] = lst[i-1], lst[i]

            yield i-1

def main():
    print("Implements insertion sort.")

if __name__ == "__main__":
    main()
