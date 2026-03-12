# def test_add_dog(cursor_con):
#
#     cursor, conn = cursor_con
#     cursor.execute('''INSERT INTO public.dogs ("name", breed) VALUES ('Nora', 'Cane Corso') returning id''')
#     dog_id = cursor.fetchone()[0]
#
#     cursor.execute(f'''select "name" from public.dogs where id = {dog_id}''')
#     name_ar = cursor.fetchone()[0]
#
#     assert 'Nora' == name_ar
#     conn.commit()

def test_join_hw21(cursor):
    cursor = cursor
    cursor.execute('''select "name", category_name from public.products join public.categories on public.products.category = public.categories.category_id''')
    rows = cursor.fetchall()

    print('\n')

    for row in rows:
        print(row)

