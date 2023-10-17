#!/usr/bin/env python3
"""
Script to list students sorted by average score
"""

import pymongo

def top_students(mongo_collection):
    """
    Return all students sorted by average score.

    """
    students = list(mongo_collection.find())

    for student in students:
        total_score = 0
        for topic in student['topics']:
            total_score += topic['score']
        student['averageScore'] = total_score / len(student['topics'])

    sorted_students = sorted(students, key=lambda x: x['averageScore'], reverse=True)

    return sorted_students

if __name__ == "__main__":
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    students_collection = client.my_db.students

    # Sample student data
    j_students = [
        { 'name': "John", 'topics': [{ 'title': "Algo", 'score': 10.3 },{ 'title': "C", 'score': 6.2 }, { 'title': "Python", 'score': 12.1 }]},
        { 'name': "Bob", 'topics': [{ 'title': "Algo", 'score': 5.4 },{ 'title': "C", 'score': 4.9 }, { 'title': "Python", 'score': 7.9 }]},
        { 'name': "Sonia", 'topics': [{ 'title': "Algo", 'score': 14.8 },{ 'title': "C", 'score': 8.8 }, { 'title': "Python", 'score': 15.7 }]},
        { 'name': "Amy", 'topics': [{ 'title': "Algo", 'score': 9.1 },{ 'title': "C", 'score': 14.2 }, { 'title': "Python", 'score': 4.8 }]},
        { 'name': "Julia", 'topics': [{ 'title': "Algo", 'score': 10.5 },{ 'title': "C", 'score': 10.2 }, { 'title': "Python", 'score': 10.1 }]}
    ]
    for j_student in j_students:
        students_collection.insert_one(j_student)

    students = top_students(students_collection)
    for student in students:
        print("[{}] {} => {:.2f}".format(student['_id'], student['name'], student['averageScore']))
