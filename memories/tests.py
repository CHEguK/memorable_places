''' memories/test.py '''
from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase
from django.urls import reverse

from parameterized import parameterized
from memories.models import MemoryItem


class SigninTest(TestCase):
    ''' Signin Test '''
    def setUp(self):
        ''' Set up actions '''
        self.user = get_user_model().objects.create_user(username='test', password='test',
                                                         email='test@example.com')
        self.user.save()

    def tearDown(self):
        ''' Teardown actions '''
        self.user.delete()

    @parameterized.expand([
        ('test', 'test', True),
        ('wrong', 'test', False),
        ('test', 'wrong', False),
        ])
    def test_signin(self, username, password, expected):
        ''' Test sigin '''
        user = authenticate(username=username, password=password)
        received = user is not None and user.is_authenticated
        self.assertEqual(received, expected)


class MemoryItemTest(TestCase):
    ''' Test MemoryItem View '''
    def setUp(self):
        ''' Set up actions '''
        self.user = get_user_model().objects.create_user(username='test', password='test',
                                                         email='test@example.com')
        self.user.save()
        self.memory = MemoryItem(owner=self.user,
                                 name='test',
                                 comment='test comment')
        self.memory.save()

    def tearDown(self):
        ''' Tear down actions'''
        self.user.delete()

    def test_read_memory(self):
        ''' Test read memory '''
        self.assertEqual(self.memory.owner, self.user)
        self.assertEqual(self.memory.name, 'test')
        self.assertEqual(self.memory.comment, 'test comment')

    def test_update_memory_name(self):
        ''' Test update memory name '''
        self.memory.name = 'new test'
        self.memory.save()
        self.assertEqual(self.memory.name, 'new test')

    def test_update_comment(self):
        ''' Test update comment '''
        self.memory.comment = 'new test comment'
        self.memory.save()
        self.assertEqual(self.memory.comment, 'new test comment')


def create_memory(name, comment, owner):
    ''' Create memory in database '''
    return MemoryItem.objects.create(name=name, comment=comment,  # pylint: disable=no-member
                                     owner=owner)


class MemoriesViewTest(TestCase):
    """
    Test MemoriesView
    If no memories, an appropriate message is displayed
    """
    def setUp(self):
        ''' Set up actions '''
        self.user = get_user_model().objects.create_user(username='test', password='test',
                                                         email='test@example.com')
        self.user.save()

    def tearDown(self):
        ''' Teardown actions '''
        self.user.delete()

    def test_no_memories(self):
        ''' Test no memories '''
        response = self.client.get(reverse('memories:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'У вас пока ни одного воспоминания')
        self.assertQuerysetEqual(response.context['memories'], [])

    def test_memories_exist(self):
        ''' Test memories exist '''
        create_memory('test name 1', 'comment test 1', self.user)
        create_memory('test name 2', 'comment test 2', self.user)
        self.client.login(username='test', password='test')
        response = self.client.get(reverse('memories:list'))

        self.assertQuerysetEqual(list(response.context['memories']),
                                 ['<MemoryItem: test name 1>', '<MemoryItem: test name 2>'])


class CreateMemoryViewTest(TestCase):
    ''' Test CreateMemoryView'''
    def setUp(self):
        ''' Set up actions '''
        self.user = get_user_model().objects.create_user(username='test', password='test',
                                                         email='test@example.com')
        self.user.save()

    def tearDown(self):
        ''' Teardown actions '''
        self.user.delete()

    def test_create_memory(self):
        ''' Test create memory '''
        self.client.login(username='test', password='test')
        self.client.post(reverse('memories:create'),
                         {'name': 'test', 'comment': 'test comment'})
        data = str(MemoryItem.objects.get(id=1))  # pylint: disable=no-member
        self.assertEqual(data, 'test')
