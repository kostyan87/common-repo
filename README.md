# Тестовый репозиторий для пробы пулл-реквестов

Что можно попробовать?

- Сделать форк, что-то закоммитить и отправить пулл-реквест
- Написать в Issues (вкладка под названием репозитория). Напишите, например, о трудностях, возникающих при работе с Git и GitHub. Пожелания тоже рассматриваются

Старайтесь оформлять названия коммитов и описания подобающим образом — так вы проявите вежливость и уважение по отношению к другим.


</br></br>

## Давайте подскажу как настроить эти SSH и GPG ключи

Пока не начали, в обоих случаях используйте свои типа e-mail-ы `12345678+YourUserName@users.noreply.github.com`

### SSH

Зачем это?</br>
Чтобы не вводить каждый раз логин и пароль.

Тээкс.... Открываем `Терминал` или `Git Bash` и начинаем печатать

Генерация ключа. Заходим [сюда](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent), читаем и делаем по инструкции. 


### GPG

Зачем это?</br>
Чтобы в аккаунте на коммитах появился зеленый значек `Verified`

Открываем `Терминал` или `Git Bash` и начинаем печатать

1. Генерация ключа
```bash
gpg --full-generate-key
```
2. А что было дальше узнаете [тут](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-gpg-key)

3. После генерации надо добавить их в свой аккаунт, об этом [тут](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-gpg-key-to-your-github-account)

4. Нужно настроить, чтобы все коммиты по умолчанию подписались GPG ключом. Как? Об этом [тут](https://codex.so/gpg-verification)

4. В WSL у вас могут возникнуть проблемы с `GPG` ключами, коммиты не подписываются, и в принципе не делаются, выдает ошибку такого типа:

```
error: gpg failed to sign the data fatal: 
failed to write commit object
```

решение проблемы [тут](https://stackoverflow.com/questions/39494631/gpg-failed-to-sign-the-data-fatal-failed-to-write-commit-object-git-2-10-0/55993078#55993078)
