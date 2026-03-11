


def test_add_dog(cursor):


    cursor.execute('''INSERT INTO public.dogs ("name", breed) VALUES ('Nora', 'Cane Corso') returning id''')
    dog_id = cursor.fetchone()[0]

    cursor.execute(f'''select "name" from public.dogs where id = {dog_id}''')
    name_ar = cursor.fetchone()[0]

    assert 'Nora' == name_ar
