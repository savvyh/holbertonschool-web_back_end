export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.city === city)
    .map((student) => ({
      ...student,
      grade: (newGrades.find((grade) => grade.studentId === student.id) || { grade: 'N/A' }).grade,
    }));
}
