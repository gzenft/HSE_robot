import keyring

sender = "gzenft@edu.hse.ru"
query = "Blockchain"
num_page = 2
password = keyring.get_password("HSE_PWD", sender)
receiver = "gzenft@edu.hse.ru"
