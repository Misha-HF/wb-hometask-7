from sqlalchemy import func, desc
from sqlalchemy.orm import sessionmaker
from create_tables import Group, Student, Teacher, Subject, Grade, engine

def select_1():
    # Створення сесії
    Session = sessionmaker(bind=engine)
    session = Session()

    # Запит на знаходження 5 студентів з найбільшим середнім балом
    #LMS
    top_students = session.query(Student, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()


    # Вивід результатів
    print("Top 5 students with highest average grade:")
    for student, avg_grade in top_students:
        print(f"Student ID: {student.id}, Fullname: {student.fullname}, Average Grade: {avg_grade}")

if __name__ == "__main__":
    select_1()
