from django.apps import AppConfig


class YoConfig(AppConfig):
    name = 'yo'
    
    def ready(self) :
        # setting up signals 
        print("setting up signals")
        import yo.signals
