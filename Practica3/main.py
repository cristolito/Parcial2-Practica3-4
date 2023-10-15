import flet as ft
from linked_list import LinkedList
from student import Student

def main(page: ft.Page):
    def reset_error():
        error_name.value = ""
        error_grade.value = ""
        error_grade.visible = False
        error_name.visible = False

    def error_inputs(name, grade):
        result = True
        reset_error()
        if name == "":
            error_name.visible = True
            error_name.value = "Ingresa un nombre"
            result = False

        if grade == "":
            error_grade.visible = True
            error_grade.value = "Ingresa una calificación valida"
            result = False

        dot = False
        for char in grade:
            if not char.isdigit():
                if char == '.' and not dot:
                    dot = True
                else:
                    error_grade.visible = True
                    error_grade.value = "Ingresa una calificación valida"
                    result = False

        return result
    
    def handle_end(e):
        current = students.head
        previous = None

        while current:
            student = current.data

            if student.grade < 7.0:
                failed_students.insert(student)

                if previous:
                    previous.next_node = current.next_node
                else:
                    students.head = current.next_node

                current = current.next_node
            else:
                previous = current
                current = current.next_node

        print_students()

    def handle_submit(e):
        name = input_name.value
        grade = input_grade.value
        if error_inputs(name, grade):
            if float(grade) >= 10:
                error_grade.visible = True
                error_grade.value = "Ingresa una calificación entre 0 y 10"
            else:
                reset_error()
                input_name.value = ""
                input_grade.value = ""
                student = Student(name, float(grade))
                students.insert(student)
                print_students()

        page.update()

    def print_students():
        columna1.controls.clear()
        columna2.controls.clear()
        students_list = students.get_list()
        failed_students_list = failed_students.get_list()

        columna1.controls.append(ft.Text(f"Estudiantes Aprobados"))
        columna2.controls.append(ft.Text(f"Estudiantes Reprobados"))

        for student in students_list:
            columna1.controls.append(ft.Text(f"{student.name}: {student.grade}"))
        for student in failed_students_list:
            columna2.controls.append(ft.Text(f"{student.name}: {student.grade}"))

        page.update()

    students = LinkedList()
    failed_students = LinkedList()
    input_name = ft.TextField(label="Nombre", width=400, bgcolor=ft.colors.WHITE10)
    input_grade = ft.TextField(label="Calificación", width=200, bgcolor=ft.colors.WHITE10)
    btn_submit = ft.ElevatedButton("Subir", on_click=handle_submit)
    btn_end = ft.ElevatedButton("Ver reprobados", on_click=handle_end)
    error_name = ft.Text(visible=False)
    error_grade = ft.Text(visible=False)
    columna1 = ft.Column([ft.Text(f"Estudiantes Aprobados")])
    columna2 = ft.Column([ft.Text(f"Estudiantes Reprobados")])
    row_students = ft.Row([columna1, columna2],alignment=ft.MainAxisAlignment.SPACE_AROUND)
    container_students = ft.Container(row_students, alignment=ft.alignment.top_center, border_radius=ft.border_radius.all(5), border=ft.border.all(5, "white"))

    main_container = ft.Container(ft.Column([input_name, error_name, input_grade, error_grade, btn_submit,btn_end], spacing=15), alignment=ft.alignment.top_center)

    page.add(main_container, container_students)

ft.app(main)
