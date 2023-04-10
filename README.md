# Little Lemon Project

This repository is a project made in **Backed Developer Professional Certificate**

Github: <https://github.com/CrstnAraujo/coursera-littlelemon>

## API Endpoints

To review my project, you should visit the following endpoints:  

Home of the Little Lemon Restaurant. Returns an HTML response:  

```txt
/restaurant/
```

Returns the available menu as JSON:  

```txt
/restaurant/menu/
```

Returns a single item from the menu (adding a valid pk at the end of the path):  

```txt
/restaurant/menu/1
```

Returns an authentication token by sending valid credentials:  

```txt
/restaurant/api-token-auth/
```

Returns a list of bookings:  

```txt
/restaurant/user/tables/
```

Returns a user list. CRUD operations can be performed:

```txt
/restaurant/user/user/
```

## Djoser Enpoints

To access Djoser's endpoints:

```txt
http://127.0.0.1:8000/auth/users/
http://127.0.0.1:8000/auth/users/me/
http://127.0.0.1:8000/auth/token/login/
```
