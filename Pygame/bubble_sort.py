"""Implements bubble sort"""
def bubble_sort(draw_info, ascending = True):
    """takes information to use bubble sort on list"""
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) -1 -i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                yield j

def main():
    """driver"""
    print("Implements bubble sort.")

if __name__ == "__main__":
    main()
