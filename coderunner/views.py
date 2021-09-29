from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import random 
import string 
import os
import subprocess
# Create your views here.

auth_key = '8Tj4MPqAI7;_oZU`C5Ni' # Randomly Generated String in Python
allowed_languages = ['Python', 'C','C++']


class RunCode(APIView):        
    def post(self,request):
        data = request.data
        file = string.ascii_lowercase + string.digits
        file = [chr for chr in file]
        random.shuffle(file)
        file  = ''.join(file)[:18]
        while file + '.in' in os.listdir('./code_files/in'):
            file = string.ascii_lowercase + string.digits
            file = [chr for chr in file]
            random.shuffle(file)
            file  = ''.join(file)[:18]


        data = request.data
        language = data['language'] 
        code = data['code']
        input = data['input']
        authkey = data['authkey']
        if auth_key == authkey:
            if language not in allowed_languages:
                return Response({
                    "message" : "Selected Language Not Supported! Allowed Languages are C,C++,Python and Java Only"
                })

            input_file = open(f"code_files/in/{file}.in",'w')
            input_file.writelines(input)
            input_file.close()
            input_file = open(f"code_files/in/{file}.in",'r')
            if language == 'Python':
                main_code = open(f"code_files/code/python/{file}.py",'w') 
                main_code.writelines(code)
                main_code.close()
                # py -> python3
                p = subprocess.Popen(f'py code_files/code/python/{file}.py', shell=True,stdin=input_file,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = p.communicate()
                os.remove(f'./code_files/code/python/{file}.py')

            elif language == 'C':
                main_code = open(f"code_files/code/c/{file}.c",'w') 
                main_code.writelines(code)
                main_code.close()
                p = subprocess.Popen(f'gcc ./code_files/code/c/{file}.c -o ./code_files/code/c/{file} && ./code_files/code/c/{file}', shell=True,stdin=input_file,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = p.communicate()
                # os.remove(f'./code_files/code/c/{file}.c')
                # os.remove(f'./code_files/code/c/{file}')


            elif language == 'C++':
                main_code = open(f"code_files/code/cpp/{file}.cpp",'w') 
                main_code.writelines(code)
                main_code.close()
                p = subprocess.Popen(f'g++ ./code_files/code/cpp/{file}.cpp -o ./code_files/code/cpp/{file} && ./code_files/code/cpp/{file}', shell=True,stdin=input_file,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = p.communicate()
                # os.remove(f'./code_files/code/cpp/{file}.cpp')
                # os.remove(f'./code_files/code/cpp/{file}')

            
            input_file.close()
            os.remove(f'./code_files/in/{file}.in')
            return Response({
                'output' : out.decode('utf-8'),
                'errors' : err.decode('utf-8')

            })

        return Response({
            "message" : "You are Not Authorized"
        })

