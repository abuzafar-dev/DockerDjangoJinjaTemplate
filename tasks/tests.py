from django.test import TestCase
from django.urls import reverse

from tasks.models import Task


class TaskViewsTests(TestCase):
    def test_add_task(self):
        response = self.client.post(reverse('task_list'), {'title': 'Kitob o\'qish'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)

    def test_list_page(self):
        Task.objects.create(title='Sport')
        response = self.client.get(reverse('task_list'))
        self.assertContains(response, 'Sport')

    def test_toggle_task(self):
        task = Task.objects.create(title='Dars')
        self.client.post(reverse('task_toggle', args=[task.pk]))
        task.refresh_from_db()
        self.assertTrue(task.is_done)

    def test_delete_task(self):
        task = Task.objects.create(title='Dars')
        self.client.post(reverse('task_delete', args=[task.pk]))
        self.assertFalse(Task.objects.exists())

    def test_empty_title(self):
        self.client.post(reverse('task_list'), {'title': ''})
        self.assertFalse(Task.objects.exists())
