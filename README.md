Адрес backend'a: https://howtonamaz.pythonanywhere.com/



Шаблоны для фронтенда: https://github.com/Nurdanchik/namaz_templates.git



1. **Login (Вход)**:
   - URL: `/api/v1/login/`
   - Метод: POST
   - Описание: Этот эндпоинт используется для аутентификации пользователей. Пользователь должен предоставить правильные учетные данные для входа в систему.
   - Пример использования: 
     ```http
     POST /api/v1/login/
     Content-Type: application/json
     
     {
         "username": "example_username",
         "password": "example_password"
     }
     ```

2. **Register (Регистрация)**:
   - URL: `/api/v1/register/`
   - Метод: POST
   - Описание: Этот эндпоинт позволяет пользователям зарегистрироваться в системе, предоставив необходимые данные для создания учетной записи.
   - Пример использования: 
     ```http
     POST /api/v1/register/
     Content-Type: application/json
     
     {
         "username": "new_user",
         "email": "user@example.com",
         "password": "password123",
         "password2": "password123",
         "city": "Astana",
         "country": "Kazakhstan",
         "sex": "male"
     }
     ```

3. **User Profile (Профиль пользователя)**:
   - URL: `/api/v1/users/profile/`
   - Метод: GET
   - Описание: Этот эндпоинт используется для получения информации о профиле текущего пользователя. Только аутентифицированные пользователи могут получить доступ к своему профилю.
   - Пример использования: 
     ```http
     GET /api/v1/users/profile/
     Authorization: Bearer <access_token>
     ```

4. **Tutorials (Обучающие материалы)**:
   - URL: `/api/v1/tutorials/`
   - Метод: GET
   - Описание: Этот эндпоинт предоставляет список обучающих материалов доступных в системе.
   - Пример использования: 
     ```http
     GET /api/v1/tutorials/
     ```

5. **Tutorial Info (Информация о материале)**:
   - URL: `/api/v1/tutorials/<int:tutorial_id>/info/`
   - Метод: GET
   - Описание: Этот эндпоинт возвращает информацию о конкретном обучающем материале по его идентификатору.
   - Пример использования: 
     ```http
     GET /api/v1/tutorials/1/info/
     ```

6. **Prayer Timings (Время молитвы)**:
   - URL: `/api/v1/prayer-timings/<str:date>/<str:city_name>/<str:country_name>/`
   - Метод: GET
   - Описание: Этот эндпоинт предоставляет время молитвы для указанной даты, города и страны.
   - Пример использования: 
     ```http
     GET /api/v1/prayer-timings/20-05-2008/Astana/Kazakhstan/
     ```

7. **Communities (Сообщества)**:
   - URL: `/api/v1/communities/`
   - Метод: GET
   - Описание: Этот эндпоинт возвращает список сообществ доступных в системе.
   - Пример использования: 
     ```http
     GET /api/v1/communities/
     ```

8. **Community Info (Информация о сообществе)**:
   - URL: `/api/v1/communities/<int:community_id>/info/`
   - Метод: GET
   - Описание: Этот эндпоинт предоставляет информацию о конкретном сообществе по его идентификатору.
   - Пример использования: 
     ```http
     GET /api/v1/communities/1/info/
     ```

9. **Create Community (Создание сообщества)**:
   - URL: `/api/v1/communities/create/`
   - Метод: POST
   - Описание: Этот эндпоинт позволяет создать новое

 сообщество в системе.
   - Пример использования: 
     ```http
     POST /api/v1/communities/create/
     Content-Type: application/json
     
     {
         "name": "New Community",
         "description": "Description of the new community"
     }
     ```

10. **Create Comment (Создание комментария)**:
    - URL: `/api/v1/communities/<int:community_id>/comments/create/`
    - Метод: POST
    - Описание: Этот эндпоинт позволяет создать новый комментарий в определенном сообществе.
    - Пример использования: 
      ```http
      POST /api/v1/communities/1/comments/create/
      Content-Type: application/json
      
      {
          "text": "This is a new comment."
      }
      ```
   
Это краткое объяснение каждого эндпоинта в вашем API с примерами использования.
