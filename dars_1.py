import sqlite3

#1.Ma'lumotlar bazasiga ulanish (File bo'lmasa avtomatik yaratiladi)
#2.'test.db' - bu sizning ma'lumotlar bazasi file ning nomi

conn = sqlite3.connect('test.db')

#2.kursor yaratish (Buyruqlarni bajaruvchi vosita)
cur = conn.cursor()

# #3. Jadval yaratish(Agar mavjud bo'lmasa)
# cur.execute('''
# CREATE TABLE IF NOT EXISTS USERS (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL UNIQUE,
# age INTEGER,
# jinsi TEXT
# )''')
# print("✔ 'users' jadvali tayyor!" )
#
# #4.Malumotlarni qo'shish
# cur.execute("INSERT OR IGNORE INTO users (name,age,jinsi) VALUES (?,?,?)",("abror",13,'erkak'))
# cur.execute("INSERT OR IGNORE INTO users (name,age,jinsi) VALUES (?,?,?)",("sevinch",9,'ayol'))
# cur.execute("INSERT OR IGNORE INTO users (name,age,jinsi) VALUES (?,?,?)",("soliha",3,'ayol'))
# cur.execute("INSERT OR IGNORE INTO users (name,age,jinsi) VALUES (?,?,?)",("oqila",1,'ayol'))
# cur.execute("INSERT OR IGNORE INTO users (name,age,jinsi) VALUES (?,?,?)",("muslimaxon",9,'ayol'))
# conn.commit()
# print("✔ Ma'lumotlar qo'shildi!")
#
# #.5 Malumotlarni o'qish(SELECT)
# cur.execute('SELECT * FROM users')
# rows = cur.fetchall()
#
# print("\n🎞Jadvaldagi barcha foydalanuvchilar!")
# for row in rows:
#     print(f"\nID: {row[0]},Ism: {row[1].title()}, Yoshi:{row[2]},Jinsi: {row[3]}")

#===========2-dars uchun qo'shimchalr=======
# print("\n" + "=" * 50)
# print("2-dars: FITRLASH VA TARTIBLSH")
# print("=" * 50)
#
# ##1.WHERE - Faqat ayol jinsidagilarni ko'rish
#
# print("Faqat ayollar ro'yxati:")
# cur.execute("SELECT * FROM users WHERE jinsi = 'ayol'")
# for row in cur.fetchall():
#     print(f" -  {row[1]}, {row[2]} yosh")



##2. WHERE yooshi > 5 bo'lganlar
# print("\nYoshi 5 dan katta bollar: ")
# cur.execute("SELECT name, age FROM users WHERE age > 5")
# for row in cur.fetchall():
#     print(f" - {row[0]}: {row[1]} yosh.")


##3. ORDER BY Yoshi bo'yicha kamayish tartibida (kattadan kichikka)
# print("\nYoshi bo'yicha kamayish tartibida (kattadan kichikka)")
# cur.execute("SELECT name, age FROM users ORDER BY age DESC")
# for row in cur.fetchall():
#     print(f"  -{row[0]} {row[1]} yosh.")




##4. LIMIT - eng katta 2 ta yoshdagini ko'rish
# print("\nEng katta 2 ta yoshdagi bollar: ")
# cur.execute("SELECT name, age FROM users ORDER BY age DESC LIMIT 2")
# for row in cur.fetchall():
#     print(f" - {row[0]} {row[1]} yosh.")


#
# ##5. UPDATE - ma'lumotlarni yangilash
# cur.execute("UPDATE users SET age = 14 WHERE name = 'abror'")
# conn.commit()
# print("\nAbrorning yoshi 14 ga yangilandi!")
#
#
#
# ## 6. Yangilangan ma'lumotlarni tekshirish
# cur.execute("SELECT * FROM users WHERE name = 'abror'")
# abror = cur.fetchone()
# print(f" - Tekshiruv: {abror[1]} endi {abror[2]} yoshda.")
#
#


# #7. DELETE - ma'lumotlarni o'chirish
# cur.execute("DELETE FROM users WHERE name = 'muslimaxon'")
# conn.commit()
# print("🎁 2-chi dars yakunlandi!")

print("\n🎞Jadvaldagi barcha foydalanuvchilar!")
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(f"\nID: {row[0]},Ism: {row[1].title()}, Yoshi:{row[2]},Jinsi: {row[3]}")

conn.commit()
# 6.Ulanishni yopish
conn.close()
print("\nUlanish yopildi...")