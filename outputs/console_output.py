from objects.OutputData import OutputData


def console_output(data: OutputData):
    print("Розподіл студентів по дисциплінам:")
    for j in range(len(data.x[0])):
        for i in range(len(data.x)):
            if data.x[i][j] == 1:
                print(f"Студент {j + 1}: Дисципліна {i + 1}")
                break
    print("Значення ЦФ:")
    print(data.s)