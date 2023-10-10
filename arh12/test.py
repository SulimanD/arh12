import okno

### тест 1. проверка пароля для пользователя под логином Anton
def test1_password():
     assert okno.list['Anton'] == 458

### тест 2. проверка пароля для пользователя под логином Pavel
def test2_password():
     assert okno.list['Pavel'] == 474