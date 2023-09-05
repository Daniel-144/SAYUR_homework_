# ####### Problem  3 ###############
# Print Chess board (alternate black and white squares)
# print('\u25A0') - will print white Square. You can use "B" to print black squares
Rows = 8
Columns = 8
# for loop for rows
for i in range(Rows):
    # for loop for columns
    for j in range(Columns):
        if (j + i) % 2 == 0:
            # when row and colum are added and the number is even then the block should be white.
            print("\u25A0", end=" ")
        else:
            # when row and colum are added and the number is odd then the block should be black.
            print('\u25A1', end=" ")
    # for next line
    print("")
    """
■ □ ■ □ ■ □ ■ □ 
□ ■ □ ■ □ ■ □ ■
■ □ ■ □ ■ □ ■ □
□ ■ □ ■ □ ■ □ ■
■ □ ■ □ ■ □ ■ □
□ ■ □ ■ □ ■ □ ■
■ □ ■ □ ■ □ ■ □
□ ■ □ ■ □ ■ □ ■
"""