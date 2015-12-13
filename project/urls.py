from .counter import views as counter

urlpatterns = [
    (r'/', counter.CounterHandler),
]
