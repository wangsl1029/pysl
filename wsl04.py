from wsl03celery import add

res = add.delay(4, 4)
print(res.ready())
print(res.get())