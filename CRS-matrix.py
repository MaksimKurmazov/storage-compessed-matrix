class FiveDimensionsArray:

    def __init__(self, array):
        self.not_null_array = []
        self.not_null_col_array = []
        self.not_null_row_array = []
        self._initiate_array(array)

    def _initiate_array(self, array):
        n = 0
        for i, row in enumerate(array):
            self.not_null_row_array.append(n)
            for j, val in enumerate(row):
                if val != 0:
                    n += 1
                    self.not_null_array.append(val)
                    self.not_null_col_array.append(j)
        self.not_null_row_array.append(n)
        del array

    def get_item(self, row, col):
        res = 0
        n1 = self.not_null_row_array[row]
        n2 = self.not_null_row_array[row + 1]
        while n1 < n2:
            if self.not_null_col_array[n1] == col:
                res = self.not_null_array[n1]
                break
            n1 += 1
        return res

    def set_item(self, row, col, value):
        n1 = self.not_null_row_array[row]
        n2 = self.not_null_row_array[row + 1]
        while n1 < n2:
            if self.not_null_col_array[n1] == col:
                self.not_null_array[n1] = value
                break
            n1 += 1


ARR = [
    [1, 2, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 1],
    [0, 0, 0, 0, 9, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 8, 0, 4, 0, 3],
]

ARR[0][2] = 4

handler = FiveDimensionsArray(ARR)

print(handler.not_null_array)
print(handler.not_null_col_array)
print(handler.not_null_row_array)
print(handler.get_item(0, 1))
print(handler.get_item(2, 1))
handler.set_item(0, 2, 4)
print(handler.not_null_array)

