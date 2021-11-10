import django

from .models import Submission


def custom_problem_data(problems: django.db.models.query.QuerySet):
    custom_json_data = []
    for elem in problems:
        problem_data = {
            'id': elem.id,
            'name': elem.name,
            'difficulty': elem.difficulty,
            'country': elem.contributor.country,
            'domain': elem.domain,
            'fitness_function': elem.fitness_function,
            'language': elem.language,
            'dimension': [{
                'dimension': el.dimension,
                'participationD': len(Submission.objects.filter(id=elem.id, dimension=el.dimension))
            } for el in elem.dimensions.all()],
            'participationAll': len(Submission.objects.filter(id=elem.id))
        }
        custom_json_data.append(problem_data.copy())
    return custom_json_data