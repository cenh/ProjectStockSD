from .scrapers.dikuspider import DikuAnsatteSpider
from django.core.exceptions import MultipleObjectsReturned
from models import Supervisor

'''
Usage:
python2 manage.py shell

from project_stock.fillmockdata import main

main()
'''

def main():
    spider = DikuAnsatteSpider()
    spider.start()

    for i in spider.items:
        if i['status'] in ['Lektor', 'Professor'] or i['status'].lower().contains('phd') or i['status'].lower().contains('postdoc'):
            try:
                email = Supervisor.objects.get(email=i['email'])
            except MultipleObjectsReturned:
                pass
            except Supervisor.DoesNotExist:
                members = [attr for attr in dir(Supervisor()) if not
                           callable(attr) and not
                           attr.startswith("__") and not
                           attr.startswith("_")]

                try:
                    sup = Supervisor()
                    name = i['name'].split()
                    setattr(sup, 'first_name', ' '.join(name[0:-1]))
                    setattr(sup, 'last_name', name[-1])
                    for key, value in i.items():
                        if key in members:
                            if value:
                                setattr(sup, key, value)
                    sup.save()
                except IndexError:
                    continue


if __name__ == '__main__':
    main()
