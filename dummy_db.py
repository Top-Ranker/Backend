import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'topranker.settings')
django.setup()

from top.models import Problem, Dimension, User
from topranker import settings

DJANGO_SETTINGS_MODULE = settings
data_list = []
type = ['Maximization', 'Minimization']
difficulty = ['Easy', 'Medium', 'Hard']
domain = ['Multi Model', 'Constraint', 'Multi Dimensional', 'None']
dimensions = [200, 120, 100, 50, 25, 20, 2, 1]
user = User.objects.get(username="admin")
for i in range(25):
    problem = Problem.objects.create()
    problem.name = f"Problem Name {i}"
    problem.type = type[i % 2]
    problem.difficulty = difficulty[i % 3]
    print(User.objects.get(username="admin"))
    problem.contributer = user
    problem.domain = domain[i % 4]
    problem.language = "Python"
    problem.visibility = True
    problem.fitness_function = """inp = int(input())
                                    print(inp)"""
    problem.dimensions.add(*Dimension.objects.filter(dimension__in=[25, 50, 100]))
    problem.description = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
                            molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
                            numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
                            optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis
                            obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam
                            nihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit,
                            tenetur error, harum nesciunt ipsum debitis quas aliquid. Reprehenderit,
                            quia. Quo neque error repudiandae fuga? Ipsa laudantium molestias eos
                            sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdam
                            recusandae alias error harum maxime adipisci amet laborum. Perspiciatis
                            minima nesciunt dolorem! Officiis iure rerum voluptates a cumque velit
                            quibusdam sed amet tempora.
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
                            molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
                            numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
                            optio, eaque rerum! Provident similique accusantium nemo autem. Veritatis
                            obcaecati tenetur iure eius earum ut molestias architecto voluptate aliquam
                            nihil, eveniet aliquid culpa officia aut! Impedit sit sunt quaerat, odit,
                            tenetur error, harum nesciunt ipsum debitis quas aliquid. Reprehenderit,
                            quia. Quo neque error repudiandae fuga? Ipsa laudantium molestias eos
                            sapiente officiis modi at sunt excepturi expedita sint? Sed quibusdam
                            recusandae alias error harum maxime adipisci amet laborum. Perspiciatis
                            minima nesciunt dolorem! Officiis iure rerum voluptates a cumque velit
                            quibusdam sed amet tempora."""
    problem.save()
