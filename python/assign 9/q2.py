def find_char_in_matrix(matrix,char):
    found=False
    num_rows=len(mstrix)
    num_cols=len(matrix[0]) if num_rows>0 else 0

    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j]==char:
                print(f"character '{char} found at row{i},column{j}")
                found=True
    if not found:
        print(f"character '{char}' not found")

def matrix_input():
    rows=int(input("enter the number of rows:"))
    cols=int(input("enter the number of columns:"))
    matrix=[]
    print("enter matrix elements row by row:")
    for i in range(rows):
        row=input(f"enter the elements for row {i}:").split()
        matrix.append(row)
    return matrix

def main():
    matrix=matrix_input()
    char=input("enter character to search for:")
    find_char_in_matrix(matrix,char)

if __name__ =="__main__":
    main()