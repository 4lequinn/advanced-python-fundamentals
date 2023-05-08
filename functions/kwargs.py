def user_info(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} - {value}')


user_info(fistname='Jorge',lastname='Quintui',age=22)

data = {'email':'jorge@gmail.com','career':'Software engineer'}
user_info(**data)