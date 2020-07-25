from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from memories.models import MemoryItem
from parameterized import parameterized
from django.urls import reverse


class SigninTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='test',
                                                            email='test@example.com')
        self.user.save()
    
    def tearDown(self):
        self.user.delete()

    @parameterized.expand([
        ('test', 'test', True),
        ('wrong', 'test', False),
        ('test', 'wrong', False),
        ])
    def test_signin(self, username, password, expected):
        user = authenticate(username=username, password=password)
        received = user is not None and user.is_authenticated
        self.assertEqual(received, expected)


class MemoryItemTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='test', 
                                                            email='test@example.com')
        self.user.save()
        self.memory = MemoryItem(owner=self.user,
                                name='test',
                                comment='test comment')
        self.memory.save()
        
    def tearDown(self):
        self.user.delete()

    def test_read_memory(self):
        self.assertEqual(self.memory.owner, self.user)
        self.assertEqual(self.memory.name, 'test')
        self.assertEqual(self.memory.comment, 'test comment')

    def test_update_memory_name(self):
        self.memory.name = 'new test'
        self.memory.save()
        self.assertEqual(self.memory.name, 'new test')

    def test_update_comment(self):
        self.memory.comment = 'new test comment'
        self.memory.save()
        self.assertEqual(self.memory.comment, 'new test comment')


def create_memory(name, comment, owner):
    return MemoryItem.objects.create(name=name, comment=comment, owner=owner)

class MemoriesViewTest(TestCase):
    """
    If no memories, an appropriate message is displayed
    """
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='test',
                                                            email='test@example.com')
        self.user.save()
    
    def tearDown(self):
        self.user.delete()

    def test_no_memories(self):
        response = self.client.get(reverse('memories:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'У вас пока ни одного воспоминания')
        self.assertQuerysetEqual(response.context['memories'], [])

    def test_memories_exist(self):
        create_memory('test name 1', 'comment test 1', self.user)
        create_memory('test name 2', 'comment test 2', self.user)
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('memories:list'))

        self.assertQuerysetEqual(list(response.context['memories']),
                                ['<MemoryItem: test name 1>', '<MemoryItem: test name 2>'])

class CreateMemoryViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='test',
                                                            email='test@example.com')
        self.user.save()
    
    def tearDown(self):
        self.user.delete()

    def test_create_memory(self):
        self.client.login(username='test', password='test')
        self.client.post(reverse('memories:create'), 
                            {'name': 'test', 'comment': 'test comment'})
        data = str(MemoryItem.objects.get(id=1))
        self.assertEqual(data, 'test')
