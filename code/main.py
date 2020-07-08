# 1. перебор паролей
# 2. перебор логином
# 3. запрос
# 4. логика перебора

import logic
import generators
import queries

logic.try_many_logins_logic(
    login_generator=generators.simple_logins,
    password_generator=generators.brute_force,
    query=queries.request_local
)
