import random
import string

MSG_USERNAME_IS_EMPTY = "Не указан логин"
MSG_USERNAME_VALID_LETTERS = (
    "Имя пользователя может содержать только буквенно-цифровые символы в "
    "нижнем регистре, символ подчеркивания (_), дефис (-), точку (.) или символ @."
)
MSG_USERNAME_ONLY_LOWERCASE_LETTERS = "Допустимы только строчные буквы"
MSG_USERNAME_ALREADY_EXISTS = "Данный логин уже используется. Выберите другой."
MSG_FIELD_IS_EMPTY = "Заполните поле"
MSG_PASSWORD_USE_SPEC_SYMBOL = (
    "Пароль должен содержать не менее 1 символов, не являющихся буквами и цифрами, "
    "например таких как *, - или #."
)
MSG_PASSWORD_USE_CAPITAL_LETTER = (
    "Пароль должен содержать не менее 1 прописных(ой) букв(ы)."
)
MSG_PASSWORD_USE_LOWERCASE_LETTER = (
    "Пароль должен содержать не менее 1 строчных(ой) букв(ы)."
)
MSG_PASSWORD_MIN_LENGTH = "Пароль не должен состоять из менее чем 8 символов(а)."
MSG_EMAIL_INVALID_FORMAT = "Некорректный формат адреса электронной почты"
MSG_EMAIL_ALREADY_EXISTS = "Этот адрес электронной почты уже зарегистрирован"
MSG_SEND_EMAIL_FAILED = "Отправить вам письмо не удалось!"


def random_str(chars=string.ascii_lowercase + string.digits, n=1000):
    return "".join(random.choice(chars) for _ in range(n))


SUCCESSFULLY_INPUT_DATA = {
    "username": random_str(n=7),
    "password": "A6532f3*",
    "email": "test@qa.com",
    "email2": "test@qa.com",
    "firstname": "Иван",
    "lastname": "Иванов",
    "city": "Казань",
    "country": "Россия",
}


def run_test(app, **kwargs):
    app.open_page()
    input_data = SUCCESSFULLY_INPUT_DATA.copy()

    for field, value in kwargs.items():
        input_data[field] = value

    app.registration.register(**input_data)


class TestRegistration:
    def test_reg_username_is_empty(self, app):
        """
        Check of situation with empty username
        """
        run_test(app, username="")
        assert MSG_USERNAME_IS_EMPTY in app.driver.page_source

    def test_reg_username_big_length(self, app):
        """
        Check of situation with big length of username
        """
        email = random_str(n=7) + "@mail.ru"
        run_test(app, username=random_str(n=10000), email=email, email2=email)
        assert MSG_SEND_EMAIL_FAILED in app.driver.page_source

    def test_reg_username_length_eq_1(self, app):
        """
        Check of situation with length=1 symbol of username
        """
        email = random_str(n=7) + "@mail.ru"
        run_test(app, username=random_str(n=1), email=email, email2=email)
        assert MSG_SEND_EMAIL_FAILED in app.driver.page_source

    def test_reg_username_first_digit(self, app):
        """
        Check of situation with username begins with digit
        """
        username = "1" + random_str(n=7)
        email = random_str(n=7) + "@mail.ru"
        run_test(app, username=username, email=email, email2=email)
        assert MSG_SEND_EMAIL_FAILED in app.driver.page_source

    def test_reg_username_exists(self, app):
        """
        Check of situation when the same username already exists
        """
        run_test(app, username="super_qa_2021")
        assert MSG_USERNAME_ALREADY_EXISTS in app.driver.page_source

    def test_reg_valid_username(self, app):
        """
        Check of situation with not supported symbols in username
        """
        run_test(app, username="*player34")
        assert MSG_USERNAME_VALID_LETTERS in app.driver.page_source

    def test_reg_username_only_lowercase_letters(self, app):
        """
        Check of situation with not supported capital letters in username
        """
        run_test(app, username="Adams")
        assert MSG_USERNAME_ONLY_LOWERCASE_LETTERS in app.driver.page_source

    def test_reg_username_use_spec_symbols(self, app):
        """
        Check of situation with supported special symbols in username
        """
        run_test(app, username="@-_.")
        assert MSG_USERNAME_VALID_LETTERS not in app.driver.page_source

    def test_reg_username_not_use_russian_letters(self, app):
        """
        Check of situation with not supported russian letters in username
        """
        run_test(app, username="юзер")
        assert MSG_USERNAME_VALID_LETTERS in app.driver.page_source

    def test_reg_username_not_use_space(self, app):
        """
        Check of situation with used space symbol in username
        """
        run_test(app, username="user ivan")
        assert MSG_USERNAME_VALID_LETTERS in app.driver.page_source

    def test_reg_password_is_empty(self, app):
        """
        Check of situation with empty password
        """
        run_test(app, password="")
        assert MSG_FIELD_IS_EMPTY in app.driver.page_source

    def test_reg_password_length_boundary_value_eq_7(self, app):
        """
        Check of situation with password length equals 7
        """
        run_test(app, password="Abc123*")
        assert MSG_PASSWORD_MIN_LENGTH in app.driver.page_source

    def test_reg_password_length_boundary_value_eq_8(self, app):
        """
        Check of situation with password length equals 8
        """
        run_test(app, password="Abc123**")
        assert MSG_PASSWORD_MIN_LENGTH not in app.driver.page_source

    def test_reg_password_length_eq_30(self, app):
        """
        Check of situation with boundary value of length equals 30 of password
        """
        username = random_str(n=8)
        password = (
            random_str(
                chars=string.ascii_uppercase + string.ascii_lowercase + string.digits,
                n=31,
            )
            + "*"
        )
        email = random_str(n=8) + "@qa.com"
        run_test(app, username=username, password=password, email=email, email2=email)
        assert MSG_SEND_EMAIL_FAILED in app.driver.page_source

    def test_reg_password_length_eq_31(self, app):
        """
        Check of situation with boundary value of length equals 31 of password
        """
        username = random_str(n=8)
        password = (
            random_str(
                chars=string.ascii_uppercase + string.ascii_lowercase + string.digits,
                n=31,
            )
            + "*"
        )
        email = random_str(n=8) + "@qa.com"
        run_test(app, username=username, password=password, email=email, email2=email)
        assert MSG_SEND_EMAIL_FAILED not in app.driver.page_source

    def test_reg_password_use_lowercase_letter(self, app):
        """
        Check of situation with not used lowercase letters in password
        """
        run_test(app, password="6532A3**")
        assert MSG_PASSWORD_USE_LOWERCASE_LETTER in app.driver.page_source

    def test_reg_password_use_capital_letter(self, app):
        """
        Check of situation with not used capital letters in password
        """
        run_test(app, password="6532f3**")
        assert MSG_PASSWORD_USE_CAPITAL_LETTER in app.driver.page_source

    def test_reg_password_use_special_symbol(self, app):
        """
        Check of situation with not used supported spacial symbols in password
        """
        run_test(app, password="A6532f36")
        assert MSG_PASSWORD_USE_SPEC_SYMBOL in app.driver.page_source

    def test_reg_email_already_exists(self, app):
        """
        Check of situation when the same email already registered
        """
        run_test(app, username=random_str(n=8))
        assert MSG_EMAIL_ALREADY_EXISTS in app.driver.page_source

    def test_reg_emails_different(self, app):
        """
        Check of situation when the values of email in according fields are different
        """
        run_test(app, email2="test2@qa.com")
        assert MSG_EMAIL_INVALID_FORMAT in app.driver.page_source

    def test_reg_valid_email_without_at(self, app):
        """
        Check of situation when we not use symbol "@" in email
        """
        run_test(app, email="test_mail.ru")
        assert MSG_EMAIL_INVALID_FORMAT in app.driver.page_source

    def test_reg_valid_email_without_dot(self, app):
        """
        Check of situation when we not use symbol "." in email
        """
        run_test(app, email="test@qacom")
        assert MSG_EMAIL_INVALID_FORMAT in app.driver.page_source

    def test_reg_valid_email_with_dot_before_at(self, app):
        """
        Check of situation when we use symbol "." before symbol "@" in email
        """
        run_test(app, email="tes.t@qacom")
        assert MSG_EMAIL_INVALID_FORMAT in app.driver.page_source

    def test_reg_valid_email_skip_nickname(self, app):
        """
        Check of situation when we not use name in email
        """
        run_test(app, email="@qa.com")
        assert MSG_EMAIL_INVALID_FORMAT in app.driver.page_source

    def test_reg_valid_email_skip_domain_part(self, app):
        """
        Check of situation when we not use domain in email
        """
        run_test(app, email="test@")
        assert MSG_EMAIL_INVALID_FORMAT in app.driver.page_source

    def test_reg_valid_email_skip_domain_1level(self, app):
        """
        Check of situation when we skip first level domain in email
        """
        run_test(app, email="test@qa.")
        assert MSG_EMAIL_INVALID_FORMAT in app.driver.page_source

    def test_reg_valid_email_skip_domain_2level(self, app):
        """
        Check of situation when we skip second level domain in email
        """
        run_test(app, email="test@.com")
        assert MSG_EMAIL_INVALID_FORMAT in app.driver.page_source

    def test_reg_first_email_is_empty(self, app):
        """
        Check of situation when email is empty
        """
        run_test(app, email="")
        assert MSG_FIELD_IS_EMPTY in app.driver.page_source

    def test_reg_second_email_is_empty(self, app):
        """
        Check of situation when email is empty
        """
        run_test(app, email2="")
        assert MSG_FIELD_IS_EMPTY in app.driver.page_source

    def test_reg_email_skip_nickname_and_domain(self, app):
        """
        Check of situation when we skips nickname and domain in email
        """
        run_test(app, email="@.", email2="@.")
        assert MSG_EMAIL_INVALID_FORMAT in app.driver.page_source

    def test_reg_email_nickname_length_eq_64(self, app):
        """
        Check of situation when we use big nickname in email
        """
        email = random_str(n=64) + "@qa.com"
        run_test(app, email=email, email2=email)
        assert MSG_EMAIL_INVALID_FORMAT not in app.driver.page_source

    def test_reg_email_nickname_length_eq_65(self, app):
        """
        Check of situation when we use big nickname in email
        """
        email = random_str(n=65) + "@qa.com"
        run_test(app, email=email, email2=email)
        assert MSG_EMAIL_INVALID_FORMAT in app.driver.page_source

    def test_reg_firstname_is_empty(self, app):
        """
        Check of situation when firstname is empty
        """
        run_test(app, firstname="")
        assert MSG_FIELD_IS_EMPTY in app.driver.page_source

    def test_reg_firstname_big_length(self, app):
        """
        Check of situation when firstname has a big length
        """
        username = random_str(n=8)
        email = random_str(n=8) + "@mail.ru"
        run_test(
            app,
            username=username,
            email=email,
            email2=email,
            firstname=random_str(n=1000),
        )
        assert MSG_SEND_EMAIL_FAILED in app.driver.page_source

    def test_reg_lastname_is_empty(self, app):
        """
        Check of situation when lastname is empty
        """
        run_test(app, lastname="")
        assert MSG_FIELD_IS_EMPTY in app.driver.page_source

    def test_reg_lastname_big_length(self, app):
        """
        Check of situation when lastname has a big length
        """
        username = random_str(n=8)
        email = random_str(n=8) + "@mail.ru"
        lastname = random_str(n=1000)
        run_test(app, username=username, email=email, email2=email, lastname=lastname)
        assert MSG_SEND_EMAIL_FAILED in app.driver.page_source

    def test_reg_password_use_space_symbol(self, app):
        """
        Check of situation with space symbol in password
        """
        username = random_str(n=8)
        email = random_str(n=8) + "@mail.ru"
        run_test(
            app, username=username, email=email, email2=email, password="A653 2f36"
        )
        assert MSG_SEND_EMAIL_FAILED in app.driver.page_source

    def test_reg_email_with_russian_letters_in_eng_domain(self, app):
        """
        Check of situation when we use big nickname in email
        """
        run_test(app, email="иванов@qa.com", email2="иванов@qa.com")
        assert MSG_EMAIL_INVALID_FORMAT in app.driver.page_source

    def test_reg_email_in_russian_domain(self, app):
        """
        Check of situation when we use email in russian domain
        """
        run_test(app, email="иванов@ёпочта.рф", email2="иванов@ёпочта.рф")
        assert MSG_EMAIL_INVALID_FORMAT in app.driver.page_source

    def test_reg_email_in_domain_more_than_2level(self, app):
        """
        Check of situation when we use email in domain third level or more
        """
        email = random_str(n=5) + "@projects.mail.ru"
        run_test(app, email=email, email2=email)
        assert MSG_EMAIL_INVALID_FORMAT not in app.driver.page_source

    def test_reg_email_with_2at(self, app):
        """
        Check of situation when we use email with 2 or more symbol "@"
        """
        email = "test@project@mail.ru"
        run_test(app, email=email, email2=email)
        assert MSG_EMAIL_INVALID_FORMAT in app.driver.page_source
