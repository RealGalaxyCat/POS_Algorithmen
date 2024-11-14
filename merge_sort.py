import random
import time


def merge_sort(liste: list) -> list:
    """
    Sortiert eine Liste von Elementen mit dem Merge-Sort-Algorithmus.

    Args:
        liste (list): Liste welche sortiert werden soll
    """

    if len(liste) <= 1:
        return liste

    # Liste in zwei Hälften teilen
    mid = len(liste) // 2  # Finde die Mitte der Liste
    left_half = liste[:mid]  # Linke Hälfte
    right_half = liste[mid:]  # Rechte Hälfte

    # Beide Hälften sortieren
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge_two_lists(sorted_left, sorted_right)



def merge_two_lists(left: list, right: list) -> list:
    """
    Fügt zwei sortierte Listen zu einer einzigen sortierten Liste zusammen.

    Args:
        left (list): erste Liste
        right (list): zweite Liste
    """

    sorted_list = []
    left_index = 0  # Startindex für die linke Liste
    right_index = 0  # Startindex für die rechte Liste

    # Solange es in beiden Listen Elemente gibt
    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:
            # Das Element der linken Liste ist kleiner oder gleich
            sorted_list.append(left[left_index])
            left_index += 1
        else:

            # Das Element der rechten Liste ist kleiner
            sorted_list.append(right[right_index])
            right_index += 1

    # Füge übriggebliebene Elemente hinzu (eine Liste wird leer sein)
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])

    return sorted_list




if __name__ == "__main__":
    unsorted_list = [random.randint(0, 1000) for _ in range(1_000_000)]
    print("Unsortierte Liste:", unsorted_list)

    time_start = time.time()
    sorted_list = merge_sort(unsorted_list)
    time_end = time.time()

    print("Sortierte Liste:", sorted_list)
    print(f"Das Sortieren hat {time_end - time_start:.3f} sekunden gedauert.")



