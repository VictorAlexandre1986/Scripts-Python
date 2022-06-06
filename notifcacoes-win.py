from win10toast import ToastNotifier

toaster = ToastNotifier()

toaster.show_toast('Notificacao',
                   'Ola Victor',
                   threaded=True,
                   icon_path=None,
                   duration=3
                   )