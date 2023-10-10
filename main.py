def peak_length(array):
    n = len(array)
    peaks = []
    max_len_peak = 0
    max_peak = []
    peak = 0

    i = 0
    while i < n:
        left_peak = []
        while i < n - 1 and array[i] < array[i + 1]:
            left_peak.append(array[i])
            i += 1

        right_peak = []

        while i < n - 1 and array[i] > array[i + 1]:
            right_peak.append(array[i])
            i += 1
            right_peak.append(array[i])

        if left_peak and right_peak:
            all_side_peak = left_peak + right_peak
            peaks.append(all_side_peak)
            if len(all_side_peak) > max_len_peak:
                max_len_peak = len(all_side_peak)
                max_peak = all_side_peak
        i += 1
        return max_len_peak


print(peak_length([2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0]))
