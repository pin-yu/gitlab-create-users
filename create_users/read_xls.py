import xlrd
import student


def get_students_from_ilms_member_xls(xls_path):
    data = xlrd.open_workbook(xls_path)
    table = data.sheets()[0]

    students = []

    # ignore the first two header rows
    for i in range(2, table.nrows):
        student_id = table.row_values(i)[0]
        student_name = table.row_values(i)[1]
        student_email = table.row_values(i)[2]

        students.append(
            student.Student(
                student_id,
                student_name,
                student_email))

    return students
