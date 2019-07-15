import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Employee
from .serializers import EmployeeSerializer


class GetAllEmployeesTest(TestCase):

    def setUp(self):
        Employee.objects.create(name='Arnaldo Pereira', email='arnaldo@luizalabs.com', department='Architecture')
        Employee.objects.create(name='Renato Pedigoni', email='renato@luizalabs.com', department='E-commerce')
        Employee.objects.create(name='Thiago Catoto', email='catoto@luizalabs.com', department='Mobile')

    def test_get_all_employees(self):
        response = self.client.get('/api/employees/?format=json')
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewEmployeeTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            'name': 'Luis Refatti',
            'email': 'luis@luizalabs.com',
            'department': 'Backend'
        }
        self.invalid_payload = {
            'name': '',
            'email': '',
            'department': ''
        }

    def test_create_valid_employee(self):
        response = self.client.post(('/api/employees/'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_employee(self):
        response = self.client.post('/api/employees/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteEmployeeTest(TestCase):

    def setUp(self):
        Employee.objects.create(
            name='Arnaldo Pereira', email='arnaldo@luizalabs.com', department='Architecture')

    def test_delete_employee(self):
        response = self.client.delete(('/api/employees/1'))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
