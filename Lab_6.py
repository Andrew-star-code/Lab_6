"""
10.	Формируется матрица F следующим образом: скопировать в нее А и если в С количество минимальных чисел в нечетных столбцах,
чем количество максимальных чисел в четных строках, то поменять местами В и С симметрично, иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение: A-1*A – K * F, иначе вычисляется выражение (AТ +GТ-F-1)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно."""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 4 до 100:"))
    while row_q < 4 or row_q > 100:
        row_q = int(input("Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    K = int(input("Введите число К="))

    A = np.random.randint(-10, 10, (row_q, row_q)) # заполняем матрицу А случайными числами
    print("Матрица А\n", A)

    F = A.copy() #копируем элементы матрицы А в матрицу F
    print("Матрица F\n", F, "\n")
    min_num = 11
    min_num_count = 0
    max_num = -11
    max_num_count = 0
    # подсчет минимальных и максимальных чисел
    for i in range(row_q // 2 + row_q % 2, row_q):
        for j in range(row_q // 2 + row_q % 2, row_q):
            if j % 2 == 0:
                if F[i][j] < min_num:
                    min_num = F[i][j]
            if i % 2 == 1:
                if F[i][j] > max_num:
                    max_num = F[i][j]

    for i in range(row_q // 2 + row_q % 2, row_q):
        for j in range(row_q // 2 + row_q % 2, row_q):
            if j % 2 == 0:
                if F[i][j] == min_num:
                    min_num_count += 1
            if i % 2 == 1:
                if F[i][j] == max_num:
                    max_num_count += 1
    print ('Минимальные числа в нечетных слобцах: ', min_num_count, "\nМаксимальные числа четных строках: ", max_num_count, "\n")
    if min_num_count > max_num_count:
        for i in range(row_q // 2):
            for j in range(row_q // 2 + row_q %2, row_q):
                F[i][j], F[i + row_q//2 + row_q % 2][j] = F[i + row_q//2 + row_q % 2][j], F[i][j]
    else:
        for i in range(row_q // 2):
            for j in range(row_q // 2):
                F[i][j], F[i][j + row_q // 2 + row_q % 2] = F[i][j + row_q // 2 + row_q % 2], F[i][j]
    print("Матрица F после изменений\n", F)
    print("\n Определитель A = ", np.linalg.det(A),"\n Сумма диагоналей F = ", np.trace(F),"\n")
    G = np.tril(A, k=0)
    print("Нижняя трeугольная матрица G\n", G,"\n")
    if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:
        print("Нельзя вычислить")
    elif np.linalg.det(A) > np.trace(F):
        print("A^-1*A – K * F\n")
        print(np.linalg.inv(A)*A-K*F)
    else:
        print("(AТ +GТ-F-1)*K\n")
        print((np.transpose(A) + np.transpose(G) - np.linalg.inv(F))*K)


    fig, ax = plt.subplots()  # matplotlib
    ax.set(xlabel='column number', ylabel='value')
    for i in range(row_q):
        for j in range(row_q):
            plt.bar(i, A[i][j])
    plt.show()

    fig, ax = plt.subplots()
    ax.set(xlabel='column number', ylabel='value')
    ax.grid()
    for j in range(row_q):
        ax.plot([i for i in range(row_q)], A[j][::])
    plt.show()

    ax = plt.figure().add_subplot(projection='3d')
    ax.set(xlabel='x', ylabel='y', zlabel='z')
    for i in range(row_q):
        plt.plot([j for j in range(row_q)], A[i][::], i)
    plt.show()

    sns.heatmap(data=F, annot=True)  # seaborn
    plt.xlabel('column number')
    plt.ylabel('row number')
    plt.show()

    sns.boxplot(data=F)
    plt.xlabel('column number')
    plt.ylabel('value')
    plt.show()

    sns.lineplot(data=F)
    plt.xlabel('column number')
    plt.ylabel('value')
    plt.show()

except ValueError:
        print("\nэто не число, перезапустите программу и повторите попытку")